from openai import OpenAI
from settings import ENV_API_KEY, ENV_BASE_DEEPSEEK_URL

class DeepSeek:
    def __init__(self):
        self.client = OpenAI(api_key=ENV_API_KEY, base_url=ENV_BASE_DEEPSEEK_URL)
    
    def check_key(self):
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": "Hello"},
            ],
            stream=False
        )

        print(response.choices[0].message.content)




