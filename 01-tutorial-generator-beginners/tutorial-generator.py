import os
import ollama 
from ollama import Client 

ollama_client = Client(host='http://host.docker.internal:11434')

with open('./system-instructions.md', 'r') as file:
    system_instructions = file.read()
with open('./tutorial-instructions.md', 'r') as file:
    tutorial_instructions = file.read()
with open('./user-instructions.md', 'r') as file:
    user_instructions = file.read()

stream = ollama_client.chat(
    #model='qwen2.5-coder:7b',
    model='mistral-small:latest',
    messages=[
        {'role': 'system', 'content': system_instructions},
        {'role': 'system', 'content': tutorial_instructions},
        {'role': 'user', 'content': user_instructions},
    ],
    options={"temperature":0.0},
    stream=True,
)

tutorial = ""

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
    tutorial += chunk['message']['content']

print("\n")

with open('tutorial-beginners.md', 'w') as file:
    file.write(tutorial)
