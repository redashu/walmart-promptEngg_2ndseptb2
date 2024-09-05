# import modules 
from openai import OpenAI
import time
# define the apiKey
ashuKey = ""
# using apiKEy 
client = OpenAI(api_key=ashuKey)
# asking input from user 
ask_input = input("type User prompt here ..")
#print(dir(client))
# selecting LLM 
ashu_response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {
            "role": "user",
            "content": ask_input
        }
    ]
)
# collecting 
print('_______________')
print('_______________')
print('_______________')
time.sleep(1)
output = ashu_response.choices[0].message.content
print(output)