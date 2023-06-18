from langchain import PromptTemplate
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate

"""
https://python.langchain.com/en/latest/modules/chains/index_examples/summarize.html#:~:text=refine_prompt%3Drefine_prompt
"""


def chain_map_reduce_template():
    prompt_template = """Write a concise summary of the following:


    {text}


    CONCISE SUMMARY IN {language}:"""
    prompt = PromptTemplate(template=prompt_template, input_variables=["text", "language"])
    return {"chain_type": "map_reduce", "map_prompt": prompt, "combine_prompt": prompt}


def chain_refine_template():
    prompt_template = """Write a concise summary of the following:


    {text}


    CONCISE SUMMARY IN {language}:"""
    prompt = PromptTemplate(template=prompt_template, input_variables=["text", "language"])
    refine_template = (
        "Your job is to produce a final summary\n"
        "We have provided an existing summary up to a certain point: {existing_answer}\n"
        "We have the opportunity to refine the existing summary"
        "(only if needed) with some more context below.\n"
        "------------\n"
        "{text}\n"
        "------------\n"
        "Given the new context, refine the original summary in {language}\n"
        "If the context isn't useful, return the original summary."
    )
    refine_prompt = PromptTemplate(
        input_variables=["existing_answer", "text", "language"],
        template=refine_template,
    )
    return {"chain_type": "refine", "question_prompt": prompt, "refine_prompt": refine_prompt}
