from openai import OpenAI
import os
import time
from dotenv import load_dotenv
from termcolor import colored
import threading

load_dotenv()
model = os.getenv('MODEL')
api_endpoint = os.getenv('API_ENDPOINT')
openai_key = os.getenv('API_KEY')

openai_api_base = api_endpoint + '/v1'

client = OpenAI(
    api_key = openai_key,
    base_url = openai_api_base,
)

def chat_completion_request_openai(messages, client, request_number):
    start_time = time.time()

    chat_response=client.chat.completions.create(
        model = model,
        messages = messages,
        temperature = 0,
        max_tokens = 500
    )

    response_time = time.time() - start_time

    if chat_response.choices:
        completion_text = chat_response.choices[0].message.content
    else:
        completion_text = None


    # Calculate tokens per second
    prompt_tokens = chat_response.usage.prompt_tokens if completion_text is not None else None
    tokens_generated = chat_response.usage.completion_tokens if completion_text is not None else None
    tokens_per_second = tokens_generated/response_time if response_time != 0.0 else None

    # Print time taken and tokens per second
    print(f"----------Request number #{request_number}----------")
    print(f"Total Time Taken: {response_time:.2f} seconds")
    print(f"Prompt tokens: {prompt_tokens:.2f}")
    print(f"Tokens generated: {tokens_generated:.2f}")
    print(f"Tokens per Second:  {tokens_per_second:.2f}")

    return(completion_text)

def send_request_every_x_seconds():
    for i in range(100):
        threading.Timer(0.125*i, send_request, args = (i+1,)).start()

def send_request(request_number):
    messages = [
        {"role": "user", "content":" Write a long essay on the topic of spring"}
    ]
    chat_completion_request_openai(messages, client, request_number)


def pretty_print_conversation(messages):
    role_to_color = {
        "system": "red",
        "user": "green",
        "assistant": "blue",
        "tool": "magenta"
    }
    for message in messages:
        color = role_to_color.get(message["role"], "grey")
        print(colored(f"{message['role']}: {message['content']}\n", color))

send_request_every_x_seconds()
