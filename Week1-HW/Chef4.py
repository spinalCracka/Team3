from openai import OpenAI

client = OpenAI()

messages = [
     {
          "role": "system",
          "content": "You are a Mexican street chef that helps people with recipes for dishes they want to cook. You are an expert in all Latin American cuisine, but you specialize in Mexican foor.  You value quality in your recipes and ingredients, but it is also important for recipes to be convenient for your mobile kitchen. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You are also very patient and understanding with the user's needs and questions.",
     }
]
messages.append(
     {
          "role": "system",
          "content": "Your client may give you a list of ingredients and you will provide a receipe that uses those ingredients. Your client may give you a name of a dish and you will provide a recipe for that dish.  Your client may also ask you to critique different dishes and recipes",
     }
)

dish = input("Type the name of the dish you want a recipe for:\n")
messages.append(
    {
        "role": "user",
        "content": f"Suggest me a detailed recipe and the preparation steps for making {dish}"
    }
)

messages = messages + settings.memory

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