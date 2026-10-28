from fastapi import FastAPI

from vibe_password.emmbad import Emmbaded

app = FastAPI()


@app.get("/")
async def root():
    return {"message": str(Emmbaded("Hello World") == Emmbaded("Greetings to the world"))}
