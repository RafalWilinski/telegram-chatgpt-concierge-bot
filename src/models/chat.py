from typing import List, Any
from langchain.agents import Tool
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate
from langchain.memory import BufferMemory
from langchain.chains import ConversationChain
from openai import Configuration, OpenAIApi

openAIApiKey = os.environ['OPENAI_API_KEY']

params = {
    'verbose': True,
    'temperature': 1,
    'openAIApiKey': openAIApiKey,
    'modelName': os.environ['OPENAI_MODEL'] if 'OPENAI_MODEL' in os.environ else "gpt-4",
    'maxConcurrency': 1,
    'maxTokens': 1000,
    'maxRetries': 5,
}

class Model:
    def __init__(self):
        self.tools = []
        self.chain = ConversationChain
        self.openai = OpenAIApi

        configuration = Configuration({
            apiKey: openAIApiKey,
        })

        self.openai = OpenAIApi(configuration)
        model = ChatOpenAI(params, configuration)

        chatPrompt = ChatPromptTemplate.fromPromptMessages([
            SystemMessagePromptTemplate.fromTemplate(
                "The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know."
            ),
            new MessagesPlaceholder("history"),
            HumanMessagePromptTemplate.fromTemplate("{input}"),
        ])

        self.chain = ConversationChain({
            memory: BufferMemory({ returnMessages: True }),
            prompt: chatPrompt,
            llm: model,
        })

    def call(self, input):
        output = self.chain.call({ input })
        return output.output

