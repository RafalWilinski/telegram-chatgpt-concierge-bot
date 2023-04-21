import json
import os
import time
from datetime import datetime
from typing import Dict

import google.auth
import google.oauth2.credentials
import google_auth_oauthlib.flow
import requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from langchain.agents import AgentExecutor, Tool, initialize_agent_executor
from langchain.chat_models import ChatOpenAI
from langchain.memory import BufferMemory

openAIApiKey = os.environ['OPENAI_API_KEY']

params = {
  'verbose': True,
  'temperature': 1,
  'openAIApiKey': openAIApiKey,
  'modelName': os.environ.get('OPENAI_MODEL', 'gpt-3.5-turbo'),
  'maxConcurrency': 1,
  'maxTokens': 1000,
  'maxRetries': 5,
}


class Model:
    def __init__(self):
        self.tools: Tool
        self.executor: AgentExecutor
        self.openai: ChatOpenAI
        self.model: ChatOpenAI

        self.tools = [googleTool]
        self.openai = OpenAIApi(configuration)
        self.model = ChatOpenAI(params, configuration)

    def call(self, input: str):
        if not self.executor:
            self.executor = initialize_agent_executor(
                self.tools,
                self.model,
                "chat-conversational-react-description",
                True
            )
            self.executor.memory = BufferMemory({
                "returnMessages": True,
                "memoryKey": "chat_history",
                "inputKey": "input",
            })

        response = self.executor.call({ "input": input })

        print("Model response: " + response)

        return response.output
