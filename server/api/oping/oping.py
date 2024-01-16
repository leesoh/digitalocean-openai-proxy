from openai import OpenAI


def send(user_prompt: str):
    with open("tools/extwis/system.md") as file:
        system_prompt = file.read()
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return f"{completion.choices[0].message.content}"
