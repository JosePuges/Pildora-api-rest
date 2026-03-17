
from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df = pd.read_csv("prestamos_biblioteca_publica.csv")

@app.get("/")
def home():
    return {"message": "API Biblioteca funcionando"}

@app.get("/prestamos")
def get_prestamos():
    return df.to_dict(orient="records")

@app.get("/prestamos/total")
def total_prestamos():
    return {"total_prestamos": len(df)}

@app.get("/prestamos/por-categoria")
def prestamos_categoria():
    result = df.groupby("categoria_libro").size().reset_index(name="total")
    return result.to_dict(orient="records")

@app.get("/prestamos/por-idioma")
def prestamos_idioma():
    result = df.groupby("idioma").size().reset_index(name="total")
    return result.to_dict(orient="records")

@app.get("/prestamos/por-mes")
def prestamos_mes():
    result = df.groupby("mes").size().reset_index(name="total")
    return result.to_dict(orient="records")

@app.get("/prestamos/duracion-media")
def duracion_media():
    return {"duracion_media": df["duracion_prestamo_dias"].mean()}
