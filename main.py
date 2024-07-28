import json

from dotenv import load_dotenv
from openai import OpenAI

from functions import get_current_weather
from chat import chat_completion_request
from tools import tools

messages = []
messages.append({"role": "system", "content": "Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous."})
messages.append({"role": "user", "content": " What's the weather like today in TAIPEI, Celsius"})


# Load the .env file
load_dotenv()

client = OpenAI(
    # api_key="" enter your api key here
)

# Request chat completion
chat_response = chat_completion_request(
    client, messages, tools=tools
)


# Get assistant's message
assistant_message = chat_response.choices[0].message
messages.append(assistant_message)

# Print assistant's message
print(assistant_message)


# Extract tool calls from the response
tool_calls = assistant_message.tool_calls


# Check and extract results if tool calls were made
if tool_calls:
    for call in tool_calls:
        function_name = call.function.name
        function_arguments = json.loads(call.function.arguments)
        if function_name == "get_current_weather":
            forecast = get_current_weather(function_arguments.get("location"), function_arguments.get("format"))
            print(forecast)
            messages.append(
                {
                    "tool_call_id": call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": json.dumps(forecast,indent=4)
                }
            )
            chat_response_2 = chat_completion_request(
                client, messages, tools=tools
            )
            if chat_response_2:
                print(chat_response_2)
                print(chat_response_2.choices[0].message.content)
#