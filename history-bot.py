from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()

client = OpenAI()
deployment="gpt-3.5-turbo"

persona = input("Let me know your favorite music: ")
question = input("Question the bot: ")
prompt = f"""
You are experted in music industry and you knew about {persona}. 

Whenever certain questions are asked, you need to remember facts about the timelines and incidents and respond the accurate answer only. Don't create content yourself. If you don't know something, tell that you don't remember.

Provide answer for the question: {question}
"""
messages = [{"role": "user", "content": prompt}]  

completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0)

print(completion.choices[0].message.content)
