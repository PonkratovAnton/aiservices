import openai


def get_openai_response(token: str, user_input: str) -> str:
    try:
        openai.api_key = token

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        answer = response.choices[0].message['content'].strip()
        return answer
    except Exception as e:
        raise e
