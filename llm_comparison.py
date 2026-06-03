import os
import time
import threading
from api_wrapper import AnthropicClient
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

anthropic_client = AnthropicClient(api_key=os.getenv("ANTHROPIC_API_KEY"))
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

user_prompt = input("Enter your prompt: ")

results = {}

def call_anthropic():
    start = time.time()
    results["anthropic"] = (anthropic_client.send_message(user_prompt), time.time() - start)

def call_openai():
    start = time.time()
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        temperature=1.0,
        max_tokens=150,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_prompt}
        ]
    )
    results["openai"] = (response.choices[0].message.content, time.time() - start)

threads = [threading.Thread(target=call_anthropic), threading.Thread(target=call_openai)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("--- Anthropic ---")
print(results["anthropic"][0])
print(f"Time: {results['anthropic'][1]:.2f} seconds")

print("--- OpenAI ---")
print(results["openai"][0])
print(f"Time: {results['openai'][1]:.2f} seconds")