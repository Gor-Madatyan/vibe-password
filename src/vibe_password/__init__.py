import os

from dotenv import load_dotenv
from openai import OpenAI

CONFIG = {}

def main() -> None:
    load_dotenv()
    api_key = os.getenv("OPEN_ROUTER")
    model = os.getenv("MODEL")

    if api_key == None or model == None:
        print("invalid env")
        return

    global CONFIG
    CONFIG = {
        "client": OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key),
        "model": model,
    }


main()
