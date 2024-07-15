from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()

client = OpenAI()

deployment="gpt-3.5-turbo"

prompt = "Đây là bài hát nào: một con vịt xòe ra hai cái cánh"
messages = [{"role": "user", "content": prompt}]  

completion = client.chat.completions.create(model=deployment, messages=messages)

print(completion.choices[0].message.content)
