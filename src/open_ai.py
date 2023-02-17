import openai
import os 
import dotenv

dotenv.load_dotenv("../.env")

# Replace YOUR_API_KEY with your OpenAI API key
openai.api_key = os.environ.get("OPEN_AI_TOKEN")

def get_open_ai(prompt: str) -> str:

    model_engine = "text-davinci-003"

    # Set the maximum number of tokens to generate in the response
    max_tokens = 1024

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print the response
    return completion.choices[0].text