from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import (ChatPromptTemplate,
                               HumanMessagePromptTemplate,
                               SystemMessagePromptTemplate, AIMessagePromptTemplate)
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
        # AIMessagePromptTemplate.from_template(""),
        HumanMessagePromptTemplate.from_template("""
        {source}
        {prompt}
        """)
    ])


def item_regenerate_prompt(parser: PydanticOutputParser):
    return ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(
            "You are a helpful assistant that regenerates relevant completion ITEM from source"),
        SystemMessage(content=f"Language ids: {language_structure()}"),
        SystemMessage(content=parser.get_format_instructions()),
        HumanMessagePromptTemplate.from_template("""Regenerate ITEM from the following:""")
    ])


def item_translate_prompt(parser: PydanticOutputParser):
    return ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(
            "You are a helpful assistant that translates {source_language} to {output_language}"),
        SystemMessage(content=f"Language ids: {language_structure()}"),
        SystemMessage(content=parser.get_format_instructions()),
        HumanMessagePromptTemplate.from_template("""Translate the following ITEM {source_language} to {output_language}:
    
        {source}
        
        """)
    ])


def item_title_prompt(parser: PydanticOutputParser):
    return ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(
            "You are a helpful assistant that generates relevant ITEM title for a given text"),
        SystemMessage(content=f"Language ids: {language_structure()}"),
        SystemMessage(content=parser.get_format_instructions()),
        HumanMessagePromptTemplate.from_template("""Generate a concise summary from the follow as item title:
    
        {source}
        
        """)
    ])
