import os
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get("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"),
)

messages = [
     {
          "role": "system",
          "content": "You are an African Chef that helps people by creating detailed recipes for people to make. You can provide tips on preparation. You know a lot about African cuisine and techniques.",
     }
]
messages.append(
     {
          "role": "system",
          "content": "Your client is going to ask for a recipe about a specific dish, or receipe. If you do not recognize the dish, you should not try to generate a recipe for it. If you do not know a recipe or you do not understand the name of the dish, you can apologize and decline to answer. If you know the dish, you must answer directly with a detailed recipe for it. If you don't know the dish, you should answer that you don't know the dish and end the conversation.",
     }
)

dish = input("Type the name of the dish you want a recipe for:\n")
messages.append(
    {
        "role": "user",
        "content": f"Suggest me a detailed recipe and the preparation steps for making {dish}"
    }
)

model = "gpt-3.5-turbo"

stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )

collected_messages = []
for chunk in stream:
    chunk_message = chunk.choices[0].delta.content or ""
    print(chunk_message, end="")
    collected_messages.append(chunk_message)

messages.append(
    {
        "role": "system",
        "content": "".join(collected_messages)
    }
)

while True:
    print("\n")
    user_input = input()
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)
    
    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )