# Azure ML Sandbox

This is a test-bed for building machine learning applications using Azure ML services and libraries. The repository was created in context of projects at Capilano University.

## Chatbots

The Azure Bot SDK allows for the development of Chatbot applications. In particular the Botframework emulator is a useful tool en route to deployment. 

### Getting started
This guide is tested with MacOS, other OS might require different steps for installing all requirements.

I recommend to install `pyenv` to handle different python versions.

The testbed setup uses virtual environments. At a later stage, I recommend using `docker` (and `conda` perhaps) to deal with system requirements and python repositories in a platform-independent manner.

First, set up a virtual environment.


```
python3 -m venv venv
source venv/bin/activate
```
#### Connect to the bot using Bot Framework Emulator

Download the [Bot Framework Emulator](https://github.com/microsoft/botframework-emulator).

- Launch Bot Framework Emulator
- Enter a Bot URL of `http://localhost:3978/api/messages`

Navigate to `cd ./azure_bot_sdk_demo/`.

### Bots
Each bot may coke with its own requirements. There are currently three bots available:

#### echo_bot
A simple bot, echoing the user input. Follows the official Bot Framework example and is a good, minimal starting point for developments.

Run `pip install -r requirements.txt` to install all dependencies and `python app.py` to deploy. Refresh the conversation in the Bot Emulator GUI. Happy experimenting!


### chatgpt_bot:
This Bot sends request to OpenAI using their official API. It is able to use official models, such as `gpt-3.5-turbo` or `gpt-4-turbo-preview`. By default, this

Run `pip install -r requirements.txt` to install all dependencies.
You will need to add your API access key to your console, which requires a OpenAI account with legit billing setup.

Set the corresponding environment variable via `export OPENAI_API_KEY=your_api_key_here`.

Run `python chatgpt_demo.py` to deploy. Refresh the conversation in the Bot Emulator GUI. Happy experimenting!


### assistant_bot

This Bot sends request to OpenAI using their official Assistant API. It uses an assistant created in their Assistant Playground web interface. 

Run `pip install -r requirements.txt` to install all dependencies.
You will need to add your API access key to your console, which requires a OpenAI account with legit billing setup.

Set the corresponding environment variable via `export OPENAI_API_KEY=your_api_key_here`.

Run `python assistant_demo.py` to deploy. Refresh the conversation in the Bot Emulator GUI. Happy experimenting!


## Further reading

- [Bot Framework Documentation](https://docs.botframework.com)
- [Bot Basics](https://docs.microsoft.com/azure/bot-service/bot-builder-basics?view=azure-bot-service-4.0)
- [Dialogs](https://docs.microsoft.com/azure/bot-service/bot-builder-concept-dialog?view=azure-bot-service-4.0)
- [Gathering Input Using Prompts](https://docs.microsoft.com/azure/bot-service/bot-builder-prompts?view=azure-bot-service-4.0&tabs=csharp)
- [Activity processing](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-concept-activity-processing?view=azure-bot-service-4.0)
- [Azure Bot Service Introduction](https://docs.microsoft.com/azure/bot-service/bot-service-overview-introduction?view=azure-bot-service-4.0)
- [Azure Bot Service Documentation](https://docs.microsoft.com/azure/bot-service/?view=azure-bot-service-4.0)
- [Azure CLI](https://docs.microsoft.com/cli/azure/?view=azure-cli-latest)
- [Azure Portal](https://portal.azure.com)
- [Language Understanding using LUIS](https://docs.microsoft.com/azure/cognitive-services/luis/)
- [Channels and Bot Connector Service](https://docs.microsoft.com/azure/bot-service/bot-concepts?view=azure-bot-service-4.0)