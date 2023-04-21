from langchain.base import DynamicTool
from googlesearch_py import search

class GoogleTool(DynamicTool):
    name = "Google Search Tool"
    description = "This is Google. Use this tool to search the internet. Input should be a string"
    async def func(self, searchPhrase):
        try:
            response = await search(searchPhrase,num=5)
            print(response)
            result='{'
            for i in response:
                result=result+'"url":"'+i['url']+'","title":"'+i['title']+'","description":"'+i['description']+'",'
            return result
        except Exception as error:
            print(error)
            return "Failed to get results from Google. Do not try using Google again."