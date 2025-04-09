from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI

def get_llm_chain():
    prompt = PromptTemplate.from_template(
        "Plan a {days}-day trip to {destination} with a budget of ${budget}. Include hotel, flights, and activities."
    )
    llm = ChatOpenAI(temperature=0.7)
    return LLMChain(llm=llm, prompt=prompt)

