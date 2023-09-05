from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df_userdata = pd.read_csv('src/usersdata.csv')

@app.get("/")

@app.get("/")

def userdata(User_id: str):
    # Filtra el DataFrame para obtener los datos del usuario específico
    user_data = df_userdata[df_userdata['User_id'] == User_id]

    if user_data.empty:
        return {"message": "Usuario no encontrado"}

    # Calcula la cantidad de dinero gastado por el usuario
    total_spent = user_data['price']

    # Calcula el porcentaje de recomendación en base a reviews.recommend
    recommendation_percentage = user_data['recommendation_percent']

    # Obtiene la cantidad de elementos del usuario
    num_items = user_data['items_count']

    return {
        "User_id": User_id,
        "Total_spent": total_spent,
        "Recommendation_percentage": recommendation_percentage,
        "Num_items": num_items
    }