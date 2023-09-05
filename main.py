from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df_userdata = pd.read_csv('src/usersdata.csv')

@app.get("/")
async def root():
    return { ''' Hola! Este es un proyecto individual para la carrera de Data Science de Henry. Te recomiendo leer el README'''}