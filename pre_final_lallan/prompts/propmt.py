"""
This file is made to provide methods to loads the prompt
"""

from langchain_core.prompts import PromptTemplate


def prompt_character(prompt_template_address):
    """
    This function loads the prompt from provided location
    of the prompt. Please provide absolute path to the prompt
    in case of any error.
    :param prompt_template_address: location of the prompt
    :return: prompt_text: string
    """
    prompt_text = open(prompt_template_address, 'r')
    return PromptTemplate.from_template(prompt_text.read())

