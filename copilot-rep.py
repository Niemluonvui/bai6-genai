from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY']
  )

deployment="gpt-3.5-turbo"

question = input("Helping service here, please let me know you have any question in your python coding progress: ")
prompt = f"""
You are an expert on the python language.

Whenever certain questions are asked, you need to provide response in below format.

- Concept
- Example code showing the concept implementation
- explanation of the example and how the concept is done for the user to understand better.

Provide answer for the question: {question}
"""
messages = [{"role": "user", "content": prompt}]  

completion = client.chat.completions.create(model=deployment, messages=messages)

print(completion.choices[0].message.content)