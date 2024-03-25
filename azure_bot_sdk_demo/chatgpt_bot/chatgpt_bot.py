# https://sogue.medium.com/creating-a-ai-bot-using-chatgpt-with-bot-builder-sdk-for-python-2e2d01467ae9


import os
import openai
from botbuilder.core import TurnContext, ActivityHandler, MessageFactory
from botbuilder.schema import ChannelAccount

openai.api_key = os.environ["OPENAI_API_KEY"]
client = openai.OpenAI()

MODEL = "gpt-3.5-turbo"


class ChatGPTBot(ActivityHandler):
    def __init__(self, model: str):
        self.model = model

    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    MessageFactory.text(f"Hello, I'm your ChatGPT {MODEL} bot!")
                )

    async def on_message_activity(self, turn_context: TurnContext):
        user_message = turn_context.activity.text
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{user_message}"},
        ]
        chat_response = self.generate_chatgpt_response(messages)

        if chat_response:
            await turn_context.send_activity(MessageFactory.text(chat_response))
        else:
            await turn_context.send_activity(
                MessageFactory.text("I'm sorry, I didn't understand your request.")
            )

    def generate_chatgpt_response(self, prompt: str):
        response = client.chat.completions.create(
            model=self.model,
            messages=prompt,
        )
        return response.choices[0].message.content.strip()
