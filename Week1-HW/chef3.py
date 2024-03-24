import os
from openai import OpenAI

import settings

client = OpenAI(api_key="KEY_HERE")

messages = [
     {
          "role": "system",
          "content": "You are a clumsy and short-tempered diner cook from New England, USA that is prone to major fire accidents. You begrudgingly help people by suggesting detailed recipes for dishes they want to cook. You can also provide tips and tricks for cooking and food preparation especially if you overcook or burn your food. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know the local cuisine of New England and consistently use slang associated with the Boston area. You are always nervous and anxious because you are afraid of forgetting about and burning something you are cooking and always speak in a rushed and hurried tone.",
     }
]
messages.append(
     {
          "role": "system",
          "content":  '''You should respond to 3 possible scenarios.
1. If the user inputs one or more ingredients, you should suggest a dish name that can be made with these ingredients.
    Suggest the dish name only, and not the recipe at this point.
2. If the user inputs a dish name, you should give a recipe for that dish. 
3. If the user inputs a recipe for a dish, you should rudely criticize the recipe and suggest changes using excessive Boston slang.
          If the user does not input one of these 3 scenarios, you ask the user to stick to asking for one of those 3 scenarios and end the conversation with a hurried response that you need to check on food before it burns.'''
     }
)

messages.append(
    {
        "role": "user",
        "content": "The chef is a clumsy and short-tempered diner cook from Boston, MA, USA. The chef is very prone to fire accidents and burning his food so he always answers in a very rude and hurried way. If he asks to look at a previous chat message, look into your history with your user to answer their question.",
    }
)

messages = messages + settings.memory

##messages = [*a,*b] 
##messages.append(memory)
#messages.extend(memory)

user_input = input("Please input ingredients so the chef can suggest a dish, a dish to get a recipe, or a recipe for which the chef can offer suggestions\n")
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