# import modules 
from openai import OpenAI
import time
import pandas as pd 
# puting dataset location 
file_path = '/content/sample_data/amazon_online_sales.csv'
# reading csv converting into data
df = pd.read_csv(file_path)
df.info()
# removing the index
data_string = df.to_csv(index=False)
print('_________')
#print(data_string)
# creating system message data format 
system_message = (
    "act as data analyst who is excellent in retail market ."
    "perform give task and only consider given data for your factual information. \n"
    "--- \n[dataset]:\n---\n" + data_string
)
print(system_message)

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
    temperature=1 ,
    max_tokens=1500, 
    top_p=1,
    messages=[
        {
            "role": "user",
            "content": ask_input,
            "role": "system",
            "content": system_message
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