# Chat with an intelligent assistant in your terminal
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="https://d893-2601-1c2-100-ded-5878-1a5-36ba-ac5b.ngrok-free.app/v1", api_key="lm-studio")

history = [
    {
        "role": "system", 
        "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."
    }
]

user_input = ""

while not user_input == "quit":
    user_input = input(" what do you want to do today? >")
    print(user_input)
    if user_input == "save recipe":
        ## save the last recipe
        pass ## for you to implement!

    history.append({
        "role": "user", 
        "content": user_input
    })

    completion = client.chat.completions.create(
        model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
        messages=history,
        temperature=0.7
    )

    ai_response = completion.choices[0].message.content

    print(ai_response)

    history.append({
        "role": "assistant",
        "content": ai_response
    })

