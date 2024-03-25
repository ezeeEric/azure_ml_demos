import os
import openai
from openai import OpenAI
from botbuilder.core import TurnContext, ActivityHandler, MessageFactory
from botbuilder.schema import ChannelAccount
from config import DefaultConfig

# Initialize OpenAI API
openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()

CONFIG = DefaultConfig()

my_assistant = client.beta.assistants.retrieve(assistant_id=CONFIG.ASSISTANT_ID)
my_thread = client.beta.threads.create()


class AssistantBot(ActivityHandler):
    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):

        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    MessageFactory.text(f"Hello, I'm a generic ChatGPT bot!")
                )

    async def on_message_activity(self, turn_context: TurnContext):
        user_message = turn_context.activity.text
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{user_message}"},
        ]

        # chat_response = self.generate_chatgpt_response(messages)
        chat_response = self.generate_assistant_response(messages, user_message)

        if chat_response:
            await turn_context.send_activity(MessageFactory.text(chat_response))
        else:
            await turn_context.send_activity(
                MessageFactory.text("I'm sorry, I didn't understand your request.")
            )

    def generate_assistant_response(self, messages: list, user_message: str):
        # Step 3: Add a Message to a Thread
        my_thread_message = client.beta.threads.messages.create(
            thread_id=my_thread.id,
            role="user",
            content=f"{user_message}",
        )
        print(f"This is the message object: {my_thread_message} \n")

        # Step 4: Run the Assistant
        my_run = client.beta.threads.runs.create(
            thread_id=my_thread.id,
            assistant_id=my_assistant.id,
            instructions="Please address the user as Rok Benko.",
        )
        print(f"This is the run object: {my_run} \n")

        while my_run.status in ["queued", "in_progress"]:
            keep_retrieving_run = client.beta.threads.runs.retrieve(
                thread_id=my_thread.id, run_id=my_run.id
            )
            print(f"Run status: {keep_retrieving_run.status}")

            if keep_retrieving_run.status == "completed":
                print("\n")

                # Step 6: Retrieve the Messages added by the Assistant to the Thread
                all_messages = client.beta.threads.messages.list(thread_id=my_thread.id)

                print("------------------------------------------------------------ \n")

                print(f"User: {my_thread_message.content[0].text.value}")
                print(f"Assistant: {all_messages.data[0].content[0].text.value}")

                return all_messages.data[0].content[0].text.value
            elif (
                keep_retrieving_run.status == "queued"
                or keep_retrieving_run.status == "in_progress"
            ):
                pass
            else:
                print(f"Run status: {keep_retrieving_run.status}")
                break
