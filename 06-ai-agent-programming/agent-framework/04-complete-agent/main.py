from langgraph.graph import StateGraph, START,END
from typing_extensions import TypedDict
from tools import tools
from llm import DeepSeek
from langchain_core.prompts import ChatPromptTemplate

class State(TypedDict):
    ingredients: str
    ret: list

def fcAgent(state):
    prompt = ChatPromptTemplate.from_template("请问我今天能吃上{ingredients}吗？")
    llm = DeepSeek().bind_tools(tools)
    chain = prompt | llm

    return {
        "ingredients": state["ingredients"],
        "ret": [chain.invoke({"ingredients":state["ingredients"]})]
    }


def callTools(state):
    for tool_call in state["ret"][-1].tool_calls:
        tool_name = tool_call["name"]
        tool_args = tool_call.function.arguments
        print(tool_name, tool_args)

    last_ret = state["ret"]
    print(last_ret)
    return {
        "ingredients": state["ingredients"],
        "ret": last_ret + ["搜到了红烧{}的菜谱".format(state["ingredients"])]
    }

if __name__ == "__main__":
    sg = StateGraph(State)

    # 定义节点
    sg.add_node("fcAgent", fcAgent)
    sg.add_node("callTools", callTools)

    # 定义起始边
    sg.add_edge(START, "fcAgent")

    sg.add_edge("fcAgent", "callTools")
    sg.add_edge("callTools", END)

    graph = sg.compile()
    ret = graph.invoke({"ingredients": "酸菜鱼"})

    #print(ret)
    
