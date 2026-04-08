import os
from api_wrapper import AnthropicClient
from dotenv import load_dotenv

load_dotenv()

client = AnthropicClient(api_key=os.getenv("ANTHROPIC_API_KEY"))

user_prompt = input("Enter your prompt: ")

response = client.send_message(user_prompt)
  

print(response)