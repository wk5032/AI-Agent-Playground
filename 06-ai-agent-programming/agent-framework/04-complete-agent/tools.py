from langchain_core.tools import tool

@tool
def supermarket(ingredients:str):
    """用于查询在超市中有没有买到食材"""
    if ingredients=="羊排":
        return "羊排买到了"
    else:
        return "没有买到"

@tool
def recipe(ingredients:str):
    """用于查询有没有在抖音上找到菜谱"""
    if ingredients=="羊排":
        return "找到了红烧羊排的菜谱"
    else:
        return "没有找到"

@tool
def cooking(ingredients:str):
    """用于查询菜有没有做好"""
    if ingredients=="羊排":
        return "红烧羊排做好了"
    else:
        return "糊锅了"

tools = [supermarket, recipe, cooking]