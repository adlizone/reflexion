import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
import json
import time

key = "C3A38YrHYOzDQMZyjWykMF82LVe8AEX2Gvy4h76HLTzjZLqdIPs3JQQJ99BCACfhMk5XJ3w3AAAAACOGB1iu"
endpoint = "https://aadil-m8isd264-swedencentral.services.ai.azure.com/models"

class AzureModel():
    def __init__(self, name: str):
        self.name = name
        self.api_key = key  # Fetch API key from environment variables
        self.api_url = endpoint  # DeepSeek API endpoint

    def get_response(self, Dialog: str) -> str:

        try:
            # Set up the API request
            
            client = ChatCompletionsClient(
                endpoint=endpoint,
                credential=AzureKeyCredential(key),
            )
            
            api_response = client.complete(
                messages=[Dialog],
                max_tokens=2048,
                temperature=0.8,
                top_p=0.1,
                presence_penalty=0.0,
                frequency_penalty=0.0,
                model=self.name
            )

            text = api_response.choices[0].message.content
            
        except Exception as e:
            # Handle errors
            has_error = True
            text = f"Error: {str(e)}"

        finally:
            time.sleep(1)
            return text