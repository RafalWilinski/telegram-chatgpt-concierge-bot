import sys
import json
import requests
from typing import Any, Dict, List, Optional, Tuple, Union
 
class Tool:
    pass
 
class ChatOpenAI:
    pass
 
class ChatPromptTemplate:
    @staticmethod
    def fromPromptMessages(param: List[Any]) -> Any:
        pass

class SystemMessagePromptTemplate:
    @staticmethod
    def fromTemplate(param: str) -> Any:
        pass
 
class MessagesPlaceholder:
    def __init__(self, param: str) -> None:
        pass
 
class HumanMessagePromptTemplate:
    @staticmethod
    def fromTemplate(param: str) -> Any:
        pass
 
class BufferMemory:
    def __init__(self, param: Dict[str, bool]) -> None:
        pass
 
class ConversationChain:
    def __init__(self, param: Dict[str, Any]) -> None:
        pass
 
    async def call(self, param: Dict[str, str]) -> Any:
        pass
 
class Configuration:
    def __init__(self, param: Dict[str, str]) -> None:
        pass
 
class OpenAIApi:
    def __init__(self, param: Configuration) -> None:
        pass
 
openAIApiKey = os.environ["OPENAI_API_KEY"]
 
params = {
    "verbose": True,
    "temperature": 1,
    "openAIApiKey": openAIApiKey,
    "modelName": os.environ.get("OPENAI_MODEL", "gpt-4"),
    "maxConcurrency": 1,
    "maxTokens": 1000,
    "maxRetries": 5,
}
 
class Model:
    def __init__(self) -> None:
        configuration = Configuration({"apiKey": openAIApiKey})
        self.openai = OpenAIApi(configuration)
        model = ChatOpenAI(params, configuration)
        chatPrompt = ChatPromptTemplate.fromPromptMessages(
            [
                SystemMessagePromptTemplate.fromTemplate(
                    "The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know."
                ),
                MessagesPlaceholder("history"),
                HumanMessagePromptTemplate.fromTemplate("{input}"),
            ]
        )
        self.chain = ConversationChain(
            {
                "memory": BufferMemory({"returnMessages": True}),
                "prompt": chatPrompt,
                "llm": model,
            }
        )

    async def call(self, input: str) -> Any:
        output = await self.chain.call({"input": input})
        return output.output

