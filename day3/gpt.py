from openai import OpenAI
import time as t 
import os 

# using openai API 
myapI = ""
client = OpenAI(api_key=myapI)
response = client.chat.completions.with_raw_response.create(
    model = "gpt-4o-mini",
    messages = [{
        "role": "user",
        "content": "tell me a capital of India ?"
    }]
)

# printin output of prompt 
parsed_response = response.parse()
print(parsed_response)