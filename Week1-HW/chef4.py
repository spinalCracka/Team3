import os
from openai import OpenAI

import settings

def run():
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)

    messages = [
         {
              "role": "system",
              "content": "You are a Mexican street chef that helps people with recipes for dishes they want to cook. You are an expert in all Latin American cuisine, but you specialize in Mexican foor.  You value quality in your recipes and ingredients, but it is also important for recipes to be convenient for your mobile kitchen. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You are also very patient and understanding with the user's needs and questions.",
         }
    ]
    messages.append(
         {
              "role": "system",
              "content": "Your client may give you a list of ingredients and you will provide a recipe that uses those ingredients. Your client may give you a name of a dish and you will provide a recipe for that dish.  Your client may also ask you to critique different dishes and recipes",
         }
    )












    messages = messages + settings.memory

    ##messages = [*a,*b] 
    ##messages.append(memory)
    #messages.extend(memory)

    user_input = input("CHEF#4: Either \n1. pass one or more ingredients so chef can suggest a dish to make, or \n2. type the name of the dish you want a recipe for, or \n3. enter a recipe that the chef will criticize and make possible changes:\n")
    messages.append(
        {
            "role": "user",
            "content": f"{user_input}"
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

    settings.memory.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )



    """
    while True:
        print("\n")
        user_input = input("... Either 1. pass one or more ingredients so chef can suggest a dish to make, or 2. type the name of the dish you want a recipe for, or 3. enter a recipe that the chef will criticize and make possible changes:\n")
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
    """