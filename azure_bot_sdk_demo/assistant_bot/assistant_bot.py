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
                output_text = f"Assistant Name: {my_assistant.name}\n\n"
                for key, val in my_assistant:
                    output_text += f"{key}: {val}\n\n"
                output_text += f"Thread ID: {my_thread.id}\n"
                await turn_context.send_activity(MessageFactory.text(output_text))

    async def on_message_activity(self, turn_context: TurnContext):

        chat_response = self.generate_assistant_response(
            user_message=turn_context.activity.text
        )

        if chat_response:
            await turn_context.send_activity(MessageFactory.text(chat_response))
        else:
            await turn_context.send_activity(
                MessageFactory.text(
                    f"Invalid user message: {turn_context.activity.text}"
                )
            )

    def generate_assistant_response(self, user_message: str):
        _ = client.beta.threads.messages.create(
            thread_id=my_thread.id,
            role="user",
            content=f"{user_message}",
        )

        # TODO streaming events in run
        # stream = client.beta.threads.runs.create(
        #     thread_id=my_thread.id, assistant_id=my_assistant.id, stream=True
        # )

        # for event in stream:
        #     print(event)

        run = client.beta.threads.runs.create(
            thread_id=my_thread.id, assistant_id=my_assistant.id
        )

        while run.status in ["queued", "in_progress"]:
            keep_retrieving_run = client.beta.threads.runs.retrieve(
                thread_id=my_thread.id, run_id=run.id
            )

            if keep_retrieving_run.status == "completed":
                all_messages = client.beta.threads.messages.list(thread_id=my_thread.id)
                return all_messages.data[0].content[0].text.value
            elif (
                keep_retrieving_run.status == "queued"
                or keep_retrieving_run.status == "in_progress"
            ):
                pass
            else:
                raise Exception(f"Run status: {keep_retrieving_run.status}")
