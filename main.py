from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df_userdata = pd.read_csv('src/usersdata.csv')
df_countreviews = pd.read_csv('src/countreviews.csv')

@app.get("/")
async def root():
    return { ''' Hola! Este es un proyecto individual para la carrera de Data Science de Henry. Te recomiendo leer el README'''}

@app.get("/userdata/")

def userdata(User_id: str):
    try:
    
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
    except Exception as e:
        return {"error": str(e)}

@app.get('/countreviews/')
def countreviews(start_date: str, end_date: str):
    try:
        # Convierte las fechas de entrada a objetos datetime
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        # Convierte la columna 'date' del DataFrame a objetos datetime
        df_countreviews['posted'] = pd.to_datetime(df_countreviews['posted'])

        # Filtra el DataFrame para obtener revisiones en el rango de fechas dado
        filtered_reviews = df_countreviews[(df_countreviews['posted'] >= start_date) & (df_countreviews['posted'] <= end_date)]

        # Cuenta la cantidad de usuarios únicos que realizaron revisiones en el rango de fechas
        num_users = filtered_reviews['user_id'].nunique()

        # Calcula el porcentaje de recomendación promedio de los usuarios
        recommendation_percentage = (filtered_reviews['recommend'].mean() * 100) if not filtered_reviews.empty else 0.0

        return {
            "Start_date": start_date,
            "End_date": end_date,
            "Num_users": num_users,
            "Recommendation_percentage": recommendation_percentage
        }
    except Exception as e:
        return {"error": str(e)}