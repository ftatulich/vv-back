from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.google_tables import append_table
from services.email import send_email

app: FastAPI = FastAPI()


origins = ["http://localhost", '*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.post('/saveOrder')
async def save_order(answers: dict[str, list[str]]):
    append_table(answers=answers['answers'])
    return answers