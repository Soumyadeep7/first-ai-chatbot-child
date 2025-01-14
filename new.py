import openai

# Set your API key here
openai.api_key = "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"

def chat_with_gpt(prompt, chat_log):
    # Append the user input to the chat log
    chat_log.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=chat_log
    )
    # Get the assistant's reply
    ai_reply = response.choices[0].message.content.strip()
    # Append the AI's response to the chat log
    chat_log.append({"role": "assistant", "content": ai_reply})
    return ai_reply

if __name__ == "__main__":
    chat_log = []  # Initialize chat log
    print("Chat with GPT (type 'quit', 'exit', or 'bye' to end):")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye!")
            break
        response = chat_with_gpt(user_input, chat_log)
        print(f"GPT: {response}")
