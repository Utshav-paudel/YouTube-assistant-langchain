#@ yotube assistant using langchain agent
from langchain.llms import OpenAI 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools, initialize_agent,AgentType
from dotenv import load_dotenv
import os 

# # # # for running locally
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# function for llm agent
def langchain_agent():
    llm = OpenAI(temperature = 0.5)                                  # determing language model

    tools = load_tools(['wikipedia','llm-math'], llm=llm)            # which agent tools to use
    
    agent = initialize_agent(tools= tools, llm= llm, agent= AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = True)    # initializing agent with default args
    
    result = agent.run("what is the average life of tortoise and subtract it with average age of human")
    print(result)

if __name__ == "__main__":
    langchain_agent()