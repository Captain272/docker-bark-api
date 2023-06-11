from fastapi import FastAPI
from bark import Bark

app = FastAPI()
bark = Bark()

@app.post("/generate")
async def generate(prompt: str):
    response = bark.generate(prompt)
    return {"response": response}