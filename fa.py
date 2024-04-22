from fastapi import FastAPI
from utils import write_to_json, fc
from rchain import rag_chain
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
import sys

# C:\Users\preda\.conda\envs\lallan
### API Code ###
# Use the following code in terminal to activate:
"""uvicorn fa:app --reload"""

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the directory containing your HTML files as a static directory
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Return the HTML content using FileResponse
    return FileResponse("static/index.html")


@app.get("/chat/{user_id}/{prompt}")
async def chat(user_id: str, prompt: str):
    response = rag_chain.invoke(prompt)

    write_to_json({"prompt": prompt, "response": response}, fc(user_id))
    write_to_json({"user": user_id}, "user.json")
    return {
        f"{user_id}": prompt,
        "Lallan": f"""{response}"""
    }