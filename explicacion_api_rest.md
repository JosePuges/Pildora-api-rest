# 📘 Explicación sencilla de una API REST con FastAPI

## 🧠 ¿Qué estás viendo en este código?

Este código crea una **API REST** usando Python.

Una API REST es un sistema que permite **pedir datos (request)** y recibir una **respuesta (response)**, normalmente en formato JSON.

---

# 🔄 Flujo general

```
Cliente (navegador / Python / Postman)
        ↓ request
API (FastAPI)
        ↓ procesa datos
Respuesta JSON
```

---

# 🧩 1. Importaciones

```python
from fastapi import FastAPI
import pandas as pd
```

- `FastAPI` → sirve para crear la API
- `pandas` → sirve para trabajar con datos (como el CSV)

---

# 🚀 2. Crear la aplicación

```python
app = FastAPI()
```

Esto crea la API.

👉 Es como encender el servidor donde vivirán los endpoints.

---

# 📂 3. Cargar el dataset

```python
df = pd.read_csv("prestamos_biblioteca_publica.csv")
```

- Se carga el archivo CSV
- Se guarda en un DataFrame (`df`)

👉 Este DataFrame será la fuente de datos de la API

---

# 🌐 4. ¿Qué es un endpoint?

Un **endpoint** es una URL donde puedes pedir información.

Ejemplo:

```
http://localhost:8000/prestamos
```

---

# 🏠 5. Endpoint raíz

```python
@app.get("/")
def home():
    return {"message": "API Biblioteca funcionando"}
```

## ¿Qué hace?

- `@app.get("/")` → define una ruta
- Cuando alguien entra en `/`
- Devuelve un mensaje

👉 Sirve para comprobar que la API funciona

---

# 📊 6. Endpoint: todos los préstamos

```python
@app.get("/prestamos")
def get_prestamos():
    return df.to_dict(orient="records")
```

## ¿Qué hace?

- Convierte el DataFrame en JSON
- Devuelve todos los datos

## Ejemplo respuesta:

```json
[
  {"categoria_libro": "ficcion", "idioma": "es"}
]
```

---

# 🔢 7. Endpoint: total de préstamos

```python
@app.get("/prestamos/total")
def total_prestamos():
    return {"total_prestamos": len(df)}
```

## ¿Qué hace?

- Cuenta el número de filas
- Devuelve el total

---

# 📚 8. Endpoint: préstamos por categoría

```python
@app.get("/prestamos/por-categoria")
def prestamos_categoria():
    result = df.groupby("categoria_libro").size().reset_index(name="total")
    return result.to_dict(orient="records")
```

## ¿Qué hace?

1. Agrupa por categoría
2. Cuenta cuántos hay
3. Devuelve el resultado en JSON

---

# 🌍 9. Endpoint: por idioma

```python
@app.get("/prestamos/por-idioma")
def prestamos_idioma():
    result = df.groupby("idioma").size().reset_index(name="total")
    return result.to_dict(orient="records")
```

👉 Igual que el anterior pero agrupando por idioma

---

# 📅 10. Endpoint: por mes

```python
@app.get("/prestamos/por-mes")
def prestamos_mes():
    result = df.groupby("mes").size().reset_index(name="total")
    return result.to_dict(orient="records")
```

👉 Permite analizar la actividad por meses

---

# ⏱️ 11. Endpoint: duración media

```python
@app.get("/prestamos/duracion-media")
def duracion_media():
    return {"duracion_media": df["duracion_prestamo_dias"].mean()}
```

## ¿Qué hace?

- Calcula la media
- Devuelve un número

---

# 🔥 12. Conceptos clave de API REST

## ✔ Request
Petición que hace el cliente

Ejemplo:
```
GET /prestamos
```

## ✔ Response
Respuesta de la API

Ejemplo:
```json
[{"categoria":"ficcion"}]
```

## ✔ JSON
Formato de datos

## ✔ GET
Método para obtener datos

---

# 🎯 RESUMEN FINAL

Este código:

✔ Carga un dataset
✔ Crea una API
✔ Define endpoints
✔ Devuelve datos en JSON

---


# 🧠 VISIÓN GLOBAL

```
CSV → Pandas → FastAPI → Endpoints → JSON → Cliente
```



