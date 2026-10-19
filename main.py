from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage

from dotenv import load_dotenv
load_dotenv()

#Schema
class Add(BaseModel):
    """Add 2 numbers together"""
    a:int=Field(description = "First number")
    b:int=Field(description = "Second number")
    
#LLM
llm = ChatGroq(
    model = "openai/gpt-oss-120b"
)
initial_chain = llm.bind_tools(tools = [Add])
#Ask llm to add numbers


#Extract and add
def extract_and_add(response):
    if not response.tool_calls:
        raise ValueError(f"The modeol did not call the tool. It answered: {response.content}")
    tool_call = response.tool_calls[0]
    a = tool_call["args"]["a"]
    b = tool_call["args"]["b"]
    return a + b


if __name__ == "__main__":
    question = "Add 1 and 40"
    response = initial_chain.invoke([HumanMessage(content = question)])
    result = extract_and_add(response)     
    print(f"LLM extracted: 'a' = {response.tool_calls[0]["args"]["a"]},'b' = {response.tool_calls[0]["args"]["b"]}") 
    print(f"result: {result}")