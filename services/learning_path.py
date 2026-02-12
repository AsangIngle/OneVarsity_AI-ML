from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = Ollama(model="llama3")

prompt = PromptTemplate(
    input_variables=["goal", "level"],
    template="""
You are an expert AI mentor.

Create a structured learning path.

Goal: {goal}
Current Level: {level}

Return:

1. Foundations
2. Core Skills
3. Projects
4. Advanced Topics
5. Timeline (weeks)
6. Recommended resources
"""
)

chain = LLMChain(llm=llm, prompt=prompt)

def generate_learning_path(goal, level):

    return chain.run({
        "goal": goal,
        "level": level
    })
