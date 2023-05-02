from fastapi import FastAPI
from . import dotenv
from .Introductory import questions




app = FastAPI()

questions.Query.execute(questions.query19)


