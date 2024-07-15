from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()

client = OpenAI()

deployment="gpt-3.5-turbo"

no_musics = input("Number of musics need (for example, 5): ")

genres = input("List of genres you want (for example, rock, hip hop): ")

extra = input("Your requirment (for example, background music, upbeat): ")

prompt = f"Show me {no_musics} musics with the following genres: {genres}. Thos musics require {extra}: "
messages = [{"role": "user", "content": prompt}]

completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=600, temperature = 0.1)

print("Musics:")
print(completion.choices[0].message.content)

old_prompt_result = completion.choices[0].message.content
prompt_list = "Produce a new music list, and please don't include musics that I already have: "

new_prompt = f"Given musics {old_prompt_result}, new list: {prompt_list}"
messages = [{"role": "user", "content": new_prompt}]
completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=600, temperature=0)

print("\n=====Music list ======= \n")
print(completion.choices[0].message.content)