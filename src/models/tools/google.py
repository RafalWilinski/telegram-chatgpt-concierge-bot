from langchain.base import DynamicTool
from langchain.utils import google

class GoogleTool(DynamicTool):
    name = "Google Search Tool"
    description = "This is Google. Use this tool to search the internet. Input should be a string"
    async def func(self, searchPhrase):
        try:
            response = await google.search(searchPhrase, page=0, safe=False, parse_ads=False)
            print({googleResponse: response})
            return JSON.stringify({
                results: response.results,
                featured: response.featured_snippet,
            })
        except Exception as error:
            print(error)
            return "Failed to get results from Google. Do not try using Google again."