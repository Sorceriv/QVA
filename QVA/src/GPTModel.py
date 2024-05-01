from openai import OpenAI

# Currently can't work, ran out of free credits :<

client = OpenAI(api_key="")

def chat(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

while True:
    user_input = input("You: ")
    response = chat(user_input)
    print("Chatbot: ", response)

    if user_input.lower() in ["exit"]:
        break