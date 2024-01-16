import os

from langchain.chains import LLMChain
from langchain.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI


def get_output_parser(pydantic_model):
    return PydanticOutputParser(pydantic_object=pydantic_model)


def get_LLMChain(prompt_template):
    llm = ChatOpenAI(temperature=0, model_name="gpt-4",
                     openai_api_key=os.getenv("OPENAI_API_KEY"), request_timeout=120)
    chain = LLMChain(llm=llm, verbose=True, prompt=prompt_template)
    return chain


def language_structure():
    return "1,en-US,4,sv,5,es,6,ar,7,fr,8,yo,9,de,10,ot,11,ta,12,pt-BR"
