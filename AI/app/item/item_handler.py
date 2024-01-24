import json
import re

from LearnPython.AI.app.item.item_prompt_templates import (item_title_prompt, item_regenerate_prompt,
                                                           item_translate_prompt,
                                                           item_follow_up_prompt, item_create_prompt)
from LearnPython.AI.app.item.resource_item_pydantic import ResourceItem
from LearnPython.AI.app.util import get_LLMChain, get_output_parser


def item_prompt(event):
    item: dict = create_item(event)
    response = json.dumps(item)
    return {
        'statusCode': 200,
        'body': response
    }


def create_item(params):
    """
      Load and run create item chain
    """
    # Set up a parser + inject instructions into the prompt template.
    parser = get_output_parser(ResourceItem)
    prompt_template = map_prompt(parser, params)
    chain = get_LLMChain(prompt_template)
    result = chain.generate(input_list=[params])
    print(result)

    token_usage = result.llm_output['token_usage']
    output = result.generations[0][0].text
    try:
        item = parser.parse(output).dict()
    except Exception as ex:
        print(ex)
        match = re.search(r'"content": "(.*?)",', output, re.DOTALL)
        item = {'content': match.group(1)} if match else {'content': output}
    id = str(result.run[0].run_id)

    return {'prompt_uuid': id} | item | token_usage


def map_prompt(parser, params):
    action_type = params.get('action_type')
    source = params.get('source')

    if action_type == 'merge':
        return item_title_prompt(parser)
    elif action_type == 'regenerate':
        return item_regenerate_prompt(parser)
    elif action_type == 'translate':
        return item_translate_prompt(parser)
    elif source != "":
        return item_follow_up_prompt(parser)
    else:
        return item_create_prompt(parser)
