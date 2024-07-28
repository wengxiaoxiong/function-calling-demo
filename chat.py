from tenacity import retry, wait_random_exponential, stop_after_attempt


def chat_completion_request(client, messages, tools=None, tool_choice=None, model="gpt-4o-mini"):
    @retry(wait=wait_random_exponential(multiplier=1, max=40), stop=stop_after_attempt(3))
    def request():
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                tools=tools,
                tool_choice=tool_choice,
            )
            return response
        except Exception as e:
            print("Unable to generate ChatCompletion response")
            print(f"Exception: {e}")
            return e

    return request()
