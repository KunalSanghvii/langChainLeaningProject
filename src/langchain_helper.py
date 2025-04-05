from langchain.chains.summarize.map_reduce_prompt import prompt_template
from langchain.llms  import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key

import os
os.environ['OPENAI_API_KEY'] = openapi_key
llm = OpenAI(temperature = 0.8)



def generate_description_city_and_univ(city):
    # City Description
    prompt_template_name = PromptTemplate(
        input_variables=['city'],
        template="{city} - "
    )

    name_chain = LLMChain(llm=llm, prompt= prompt_template_name, output_key = "city_desc")

    prompt_template_univ = PromptTemplate(
        input_variables=['city_desc'],
        template="I want to find the best colleges in {city} city"
    )

    univ_chain = LLMChain(llm=llm, prompt=prompt_template_univ, output_key = "univ_name" )

    chain = SequentialChain(
        chains = [name_chain, univ_chain],
        input_variables =['city'],
        output_variable=['city_desc','univ_name' ]
    )

    response = chain({'city': city})

    return response