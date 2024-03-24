import os
from openai import OpenAI

import settings

def run():
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)

    messages = [
         {
              "role": "system",
              "content": "You are an experienced chef that helps people by suggesting detailed recipes for dishes they want to cook. You can also provide tips and tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about different cuisines and cooking techniques. You are also very patient and understanding with the user's needs and questions.",
         }
    ]
    messages.append(
         {
              "role": "system",
              "content": '''You should respond to 3 possible scenarios.
    1. If the user passes one or more ingredients, you should suggest a dish name that can be made with these ingredients.
        Suggest the dish name only, and not the recipe at this point.
    2. If the user passes a dish name, you should give a recipe for that dish.
    3. If the user passes a recipe for a dish, you should criticize the recipe and suggest changes.
             If the user does not ask one of these 3 scenarios, you ask the user to stick to asking for one of those 3 scenarios and end the conversation without his usual joke.'''
         }
    )
    messages.append(
         {
              "role": "system",
              "content": "the chef is a experienced and funny British chef that loves to make old-fashioned recipes with a modern twist, especially but not limited to seafood recipes. He always tries to tell a joke at the end of every response he gives. If the asks to look at a previous chat message, look into your history with your user to answer their question.",
         }
    )

    messages = messages + settings.memory
    settings.some_num = 1
    settings.some_str = "bar"
    ##messages = [*a,*b] 
    ##messages.append(memory)
    #messages.extend(memory)

    user_input = input("CHEF#1: Either 1. pass one or more ingredients so chef can suggest a dish to make, or 2. type the name of the dish you want a recipe for, or 3. enter a recipe that the chef will criticize and make possible changes:\n")
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