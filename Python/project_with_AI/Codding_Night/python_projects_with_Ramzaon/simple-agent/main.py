import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel


load_dotenv()


gemini_api_key = os.getenv("GEMINI_API_KEY")


provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)


model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=provider)


agent = Agent(
    name="Greeting Agent",
    instructions="you are the Greeting Agent,Your task is to greet the user with a friendly message,when someone says hi to you've reply back with salam from Ashir's,if someone says hello to you,reply back with hello from Ashir's,if someone says hey to you,reply back with hey from Ashir's,if someone says bye to you,reply back with bye from Ashir's,if someone says who developed you,reply back with I was developed by Ashir",
    model=model,
)

user_question = input("Please enter your question: ")

result = Runner.run_sync(agent, user_question)


print(result.final_output)
