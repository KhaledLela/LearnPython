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
            "You are a helpful assistant that generate relevant ITEM"),
        SystemMessage(content=f"Language ids: {language_structure()}"),
        SystemMessage(content=parser.get_format_instructions()),
        HumanMessagePromptTemplate.from_template("""Your job is to provide a final relevant ITEM based on: {prompt}


            [ITEM] must have all "required": ["title", "language_id", "tag_names", "name"]
            """)
    ])


def item_follow_up_prompt(parser: PydanticOutputParser):
    return ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(
            "You are a helpful assistant that effectively produce a final ITEM without repetition"),
        SystemMessage(content=f"Language ids: {language_structure()}"),
        SystemMessage(content=parser.get_format_instructions()),
        HumanMessagePromptTemplate.from_template("""Your job is to provide a final [ITEM] with {prompt}.

        You must effectively follow up the given content provided below:

        {source}

        [ITEM] must have all "required": ["title", "language_id", "tag_names", "name"]
        """)
    ])


def item_regenerate_prompt(parser: PydanticOutputParser):
    return ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(
            "You are a helpful assistant that regenerates relevant completion [ITEM] from source"),
        SystemMessage(content=f"Language ids: {language_structure()}"),
        SystemMessage(content=parser.get_format_instructions()),
        HumanMessagePromptTemplate.from_template("""Your job is to regenerate a relevant ITEM from the given content provided below:

        {source}

        [ITEM] must have all "required": ["title", "language_id", "tag_names", "name"]
        """)
    ])


def item_translate_prompt(parser: PydanticOutputParser):
    return ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(
            "You are a helpful assistant that translates {source_language} to {output_language}"),
        SystemMessage(content=f"Language ids: {language_structure()}"),
        SystemMessage(content=parser.get_format_instructions()),
        HumanMessagePromptTemplate.from_template("""Your job is to produce a final [ITEM]
        by translating the following {source_language} into {output_language}:

        {source}

        [ITEM] must have all "required": ["title", "language_id", "tag_names", "name"]
        """)
    ])


def item_title_prompt(parser: PydanticOutputParser):
    return ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(
            "You are a helpful assistant that generates relevant ITEM title for a given text"),
        SystemMessage(content=f"Language ids: {language_structure()}"),
        SystemMessage(content=parser.get_format_instructions()),
        HumanMessagePromptTemplate.from_template("""Your job is to produce a final ITEM from the following:

        {source}
        """)
    ])
