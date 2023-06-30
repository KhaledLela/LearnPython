import json
import os
from dotenv import load_dotenv
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from prompt_templates import item_create_prompt, item_regenerate_prompt, item_title_prompt, item_translate_prompt, \
    item_follow_up_prompt
from resource_item_pydantic import ResourceItem

# Load environment variables from .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')


def lambda_handler():
    action_type = 'prompt'
    prompt = 'More please'
    source = """
{\"name\":\"Easter Island, also known as Rapa Nui, is a remote island located in the southeastern Pacific Ocean. It is famous for its giant stone statues called mai and its mysterious history.\"}"
    """

    # source =''
    source_language = 'English'
    output_language = 'Arabic'

    params = {
        'action_type': action_type,
        'prompt': prompt,
        'source': source,
        'source_language': source_language,
        'output_language': output_language
    }
    item: dict = create_item(params)

    response = json.dumps(item)
    return {
        'statusCode': 200,
        'body': response
    }


def create_item(params):
    """
      Load and run create item chain
    """
    llm = ChatOpenAI()
    # Set up a parser + inject instructions into the prompt template.
    parser = PydanticOutputParser(pydantic_object=ResourceItem)
    prompt_template = map_prompt(parser, params)
    chain = LLMChain(llm=llm, verbose=True, prompt=prompt_template)
    result = chain.run(params)
    try:
        return parser.parse(result).json()
    except Exception as ex:
        print(ex)
        return {'name': result}

    # token_usage = result.llm_output['token_usage']
    # output = result.generations[0][0].text
    # item = parser.parse(output).dict()
    #
    # return {'prompt_uuid': str(uuid.uuid4())} | item | token_usage


def map_prompt(parser, params):
    action_type = params.get('action_type')
    source = params.get('source')

    if action_type == 'merge':
        return item_title_prompt(parser)
    elif action_type == 'regenerate':
        return item_regenerate_prompt(parser)
    elif action_type == 'translate':
        return item_translate_prompt(parser)
    elif source is not None and source != "":
        return item_follow_up_prompt(parser)
    else:
        return item_create_prompt(parser)


print(lambda_handler())
