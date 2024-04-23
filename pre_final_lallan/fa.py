"""
This is the root file for Rag-LLM.
This file is part of Rag-LLM.
Use the following code in terminal to activate the Rag-LLM:
uvicorn fa:app --reload
"""
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from utils import write_to_json, fc
from rchain import rag_chain


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the directory containing your HTML files as a static directory
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")


@app.get(path="/", response_class=HTMLResponse)
async def read_root():
    # Return the HTML content using FileResponse
    return FileResponse("static/index.html")


@app.get("/chat/{user_id}/{prompt}")
async def chat(user_id: str, prompt: str):
    try:
        response = rag_chain.invoke(prompt)
    except Exception as e:
        write_to_json(data={'user_id': user_id, "prompt": prompt, "response": str(e)},
                      filename='recorded_data/errors.json')
        return {
             HTTPException(status_code=404, detail='try_again')}
    write_to_json(data={"prompt": prompt, "response": response}, filename=fc(user_id))
    write_to_json(data={"user": user_id}, filename="recorded_data/user.json")
    return {
        f"{user_id}": prompt,
        "Lallan": f"""{response}"""
    }
