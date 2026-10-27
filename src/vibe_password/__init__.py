import os

from dotenv import load_dotenv
from openai import OpenAI

from .emmbad import Emmbaded


def main() -> None:
    load_dotenv()
    api_key = os.getenv("OPEN_ROUTER")
    model = os.getenv("MODEL")

    if api_key == None or model == None:
        print("invalid env")
        return

    config = {
        "client": OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key
        ),
        "model": model

    }
    embad1 = Emmbaded(config,"I love my little sister!")
    embad2 = Emmbaded(config,"I adore my little precious sister")
    print(embad1 == embad2)
