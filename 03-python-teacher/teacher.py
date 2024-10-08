import os
import ollama 
from ollama import Client 


ollama_client = Client(host='http://host.docker.internal:11434')
#ollama_client = Client(host='http://ollama-service:11434')

with open('./system-instructions.md', 'r') as file:
    system_instructions = file.read()

memory=[]

while True:
    user_input = input("🤖 (type 'bye' to exit):> ")
    if user_input.lower() == "bye":
        print("👋 Goodbye!")
        break
    else:
        messages=[
              {'role': 'system', 'content': system_instructions},
        ]
        messages.extend(memory)
        messages.append({'role': 'user', 'content': user_input})
        
        stream = ollama_client.chat(
        #model='qwen2.5-coder:7b',
        model='mistral-small:latest',
            messages= messages,
            options={"temperature":0.0},
            stream=True,
        )

        memory.append({'role': 'user', 'content': user_input})

        answer = ""

        for chunk in stream:
          print(chunk['message']['content'], end='', flush=True)
          answer += chunk['message']['content']

        print("\n")

        memory.append({'role': 'assistant', 'content': answer})

        with open('answer.md', 'w') as file:
            file.write(answer)