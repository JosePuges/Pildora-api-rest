

from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df = pd.read_csv("ventas.csv")


@app.get("/")
def home():
    return {"bienvenido": "Pildora API-REST"}

@app.get("/ventas")
def get_ventas():
    return df.to_dict(orient="records")



@app.get("/ventas/por-pais")
def ventas_por_pais():
    result = df.groupby("pais")["precio"].sum().reset_index()
    return result.to_dict(orient="records")

@app.get("/ventas/top-productos")
def top_productos():
    result = df.groupby("producto")["precio"].sum().sort_values(ascending=False)
    return result.head().to_dict()