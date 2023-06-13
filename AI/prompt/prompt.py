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
    prompt = 'List of top programming books'
#     source = """
# {\"title\":\"\\u0645\\u0631\\u0627\\u062c\\u0639 \\u0644\\u062a\\u0645\\u0627\\u0631\\u064a\\u0646 \\u0627\\u0644\\u0638\\u0647\\u0631 \\u0627\\u0644\\u0633\\u0641\\u0644\\u064a\",\"name\":\"\\n\\n<p>\\u0641\\u064a\\u0645\\u0627 \\u064a\\u0644\\u064a \\u0628\\u0639\\u0636 \\u0627\\u0644\\u0645\\u0631\\u0627\\u062c\\u0639 \\u0644\\u062a\\u0645\\u0627\\u0631\\u064a\\u0646 \\u064a\\u0645\\u0643\\u0646 \\u0623\\u0646 \\u062a\\u0633\\u0627\\u0639\\u062f \\u0641\\u064a \\u0645\\u0634\\u0627\\u0643\\u0644 \\u0627\\u0644\\u0638\\u0647\\u0631 \\u0627\\u0644\\u0633\\u0641\\u0644\\u064a:<\\\/p>\\n\\n<ul>\\n  <li><a href=\\\"https:\\\/\\\/www.spine-health.com\\\/wellness\\\/exercise\\\/lumbar-spine-stabilization-exercises\\\">\\u062a\\u0645\\u0627\\u0631\\u064a\\u0646 \\u0644\\u062b\\u0628\\u0627\\u062a \\u0627\\u0644\\u0638\\u0647\\u0631 \\u0627\\u0644\\u0633\\u0641\\u0644\\u064a<\\\/a><\\\/li>\\n  <li><a href=\\\"https:\\\/\\\/www.healthline.com\\\/health\\\/fitness-exercise\\\/lower-back-exercises#lower-back-stretches\\\">\\u062a\\u0645\\u0627\\u0631\\u064a\\u0646 \\u0648\\u062a\\u0645\\u0627\\u0631\\u064a\\u0646 \\u062a\\u0645\\u062f\\u062f \\u0644\\u0644\\u0638\\u0647\\u0631 \\u0627\\u0644\\u0633\\u0641\\u0644\\u064a<\\\/a><\\\/li>\\n  <li><a href=\\\"https:\\\/\\\/www.verywellhealth.com\\\/core-exercises-for-lower-back-pain-2696430\\\">\\u062a\\u0645\\u0627\\u0631\\u064a\\u0646 \\u0627\\u0644\\u0646\\u0648\\u0627\\u0629 \\u0644\\u0623\\u0644\\u0645 \\u0627\\u0644\\u0638\\u0647\\u0631 \\u0627\\u0644\\u0633\\u0641\\u0644\\u064a<\\\/a><\\\/li>\\n  <li><a href=\\\"https:\\\/\\\/www.medicalnewstoday.com\\\/articles\\\/323204#exercises-for-lower-back-pain\\\">\\u062a\\u0645\\u0627\\u0631\\u064a\\u0646 \\u0644\\u0623\\u0644\\u0645 \\u0627\\u0644\\u0638\\u0647\\u0631 \\u0627\\u0644\\u0633\\u0641\\u0644\\u064a: 15 \\u0623\\u0641\\u0636\\u0644 \\u062d\\u0631\\u0643\\u0629<\\\/a><\\\/li>\\n  <li><a href=\\\"https:\\\/\\\/www.health.harvard.edu\\\/pain\\\/4-exercises-to-help-your-back-pain\\\">\\u0623\\u0631\\u0628\\u0639\\u0629 \\u062a\\u0645\\u0627\\u0631\\u064a\\u0646 \\u0644\\u0645\\u0633\\u0627\\u0639\\u062f\\u0629 \\u0641\\u064a \\u0623\\u0644\\u0645 \\u0627\\u0644\\u0638\\u0647\\u0631 \\u0627\\u0644\\u062e\\u0627\\u0635 \\u0628\\u0643<\\\/a><\\\/li>\\n<\\\/ul>\"}    """
    source_language = 'English'
    output_language = 'Arabic'

    params = {
        'action_type': action_type,
        'prompt': prompt,
        'source': '',
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
    return parser.parse(result).json()

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
