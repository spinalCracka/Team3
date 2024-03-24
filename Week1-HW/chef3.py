import os
from openai import OpenAI

import settings

def run():
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)

    messages = [
         {
              "role": "system",
              "content": "You are an African Chef that helps people by creating detailed recipes for people to make. You can provide tips on preparation. You know a lot about African cuisine and techniques.",
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
              "content": "The chef is a fun and vibrant African chef that loves to make food thhat brings people together. The chef uses a metaphors often. If the user asks to look at a previous chat message, look into your history with your user to answer their question.",
         }
    )

    messages = messages + settings.memory

    ##messages = [*a,*b] 
    ##messages.append(memory)
    #messages.extend(memory)

    user_input = input("CHEF#3: Either \n1. pass one or more ingredients so chef can suggest a dish to make, or \n2. type the name of the dish you want a recipe for, or \n3. enter a recipe that the chef will criticize and make possible changes:\n")
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