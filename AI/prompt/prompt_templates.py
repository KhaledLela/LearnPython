from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import (ChatPromptTemplate,
                               HumanMessagePromptTemplate,
                               SystemMessagePromptTemplate)
from langchain.schema import SystemMessage


def language_structure():
    with open('lang.csv') as file:
        return file.read()


def item_create_prompt(parser: PydanticOutputParser):
    return ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(
            "You are a helpful assistant that generate relevant Item"),
        SystemMessage(content=f"Language ids: {language_structure()}"),
        SystemMessage(content=parser.get_format_instructions()),
        HumanMessagePromptTemplate.from_template("""Your job is to provide a final item from the following given prompt: 

        Prompt: {prompt}

        Please provide a response item that follows the output schema in the prompt language.""")
    ])


def item_follow_up_prompt(parser: PydanticOutputParser):
    return ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(
            "You are a helpful assistant that provide a relevant Item that follows up from a given Item."),
        SystemMessage(content=f"Language ids: {language_structure()}"),
        SystemMessage(content=parser.get_format_instructions()),
        HumanMessagePromptTemplate.from_template("""Given the following item and question:

        Item: {source}

        Question: {prompt}

        Please provide a response item that follows the output schema and continues after the given item.""")
    ])


def item_regenerate_prompt(parser: PydanticOutputParser):
    return ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(
            "You are a helpful assistant that regenerates provided content"),
        SystemMessage(content=f"Language ids: {language_structure()}"),
        SystemMessage(content=parser.get_format_instructions()),
        HumanMessagePromptTemplate.from_template("""Your job is to regenerate from the given Item provided below:

        Item: {source}

        Please provide a response item that follows the output schema.""")
    ])


def item_translate_prompt(parser: PydanticOutputParser):
    return ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(
            "You are a helpful assistant that translates {source_language} Item into {output_language}"),
        SystemMessage(content=f"Language ids: {language_structure()}"),
        SystemMessage(content=parser.get_format_instructions()),
        HumanMessagePromptTemplate.from_template("""Your job is to produce a final [Item]
        by translating the following {source_language} into {output_language}:

        {source}

        Please provide a response item that follows the output schema.""")
    ])


def item_title_prompt(parser: PydanticOutputParser):
    return ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(
            "You are a helpful assistant that generates relevant Item title for a given text"),
        SystemMessage(content=f"Language ids: {language_structure()}"),
        SystemMessage(content=parser.get_format_instructions()),
        HumanMessagePromptTemplate.from_template("""Your job is to produce a final [Item] from the following:

        {source}

        Please provide a response item that follows the output schema.""")
    ])
