from typing import List, Union
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import random

app = FastAPI()

templates = Jinja2Templates(directory="templates")

WORDS = ["cigar", "rebut", "sissy", "humid", "abduct", "whoop", "apple", "alert", "dodge", "steer", "thank", "dream", "drop", "eat", "fetch"]
GUESSES = 6
CHAR_LIMIT = 5


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "guesses": GUESSES, "char_limit": CHAR_LIMIT})


@app.post("/guess")
async def guess(request: Request, guess: str):
    if len(guess) != CHAR_LIMIT:
        raise HTTPException(status_code=400, detail="Guess must be 5 characters long")

    if guess not in WORDS:
        raise HTTPException(status_code=400, detail="Guess is not a valid word")

    word = random.choice(WORDS)

    result = []
    for i in range(CHAR_LIMIT):
        if guess[i] == word[i]:
            result.append("green")
        elif guess[i] in word:
            result.append("yellow")
        else:
            result.append("gray")

    return {"result": result}
