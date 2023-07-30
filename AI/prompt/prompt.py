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
    params = {"action_type": "prompt", "prompt": "add more 5",
              "source": "{\"text\":\"<ol>\\n<li>The Great Pyramids of Giza<\\\/li>\\n<li>The Sphinx<\\\/li>\\n<li>The Egyptian Museum<\\\/li>\\n<li>Karnak Temple Complex<\\\/li>\\n<li>Valley of the Kings<\\\/li>\\n<li>Ancient City of Luxor<\\\/li>\\n<li>Abu Simbel<\\\/li>\\n<li>White Desert<\\\/li>\\n<li>Mount Sinai<\\\/li>\\n<li>Alexandria<\\\/li>\\n<\\\/ol>\"}"}
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
