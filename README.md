# 📘 Guía completa: API REST + PokéAPI (basado en notebooks)

## 🧠 Introducción

Este proyecto se explica en dos notebooks:

1. 📊 Notebook 1 → Consumo de PokéAPI y transformación de datos
2. 📈 Notebook 2 → Visualización con Streamlit

El objetivo es entender **cómo pasar de datos externos a una aplicación visual**.

---

# 🌐 1. ¿Qué es una API?

Una API es un sistema que permite que dos aplicaciones se comuniquen.

👉 En nuestros notebooks:

- Nosotros somos el cliente (Python)
- PokéAPI es el servidor
- Pedimos datos y recibimos una respuesta

👉 Flujo real:

```
Python → request → PokéAPI → response (JSON)
```

---

# 🏗️ 2. ¿Qué es REST?

REST es una forma de organizar APIs.

👉 Analogía:

Es como un plano de arquitectura que define cómo se construyen las APIs.

En nuestro caso:

```
https://pokeapi.co/api/v2/pokemon
```

👉 usamos GET para obtener datos.

---

# 📦 3. ¿Qué es JSON?

Cuando usamos la API en el notebook:

```python
response = requests.get(url)
data = response.json()
```

👉 obtenemos un JSON.

Ejemplo:

```json
{
  "name": "pikachu",
  "weight": 60
}
```

👉 JSON es un formato clave-valor.

---

# 🔍 4. Exploración del JSON (Notebook 1)

En el notebook usamos:

```python
data.keys()
```

👉 Esto nos muestra la estructura del JSON.

Luego:

```python
data["results"]
```

👉 accedemos a los datos reales.

---

# 🔁 5. Llamadas a la API (Notebook 1)

Primero obtenemos una lista de Pokémon:

```python
response = requests.get(f"{BASE_URL}?limit=5")
```

Luego, para cada Pokémon:

```python
poke_data = requests.get(pokemon["url"]).json()
```

👉 Esto es importante:

- Primera llamada → lista
- Segunda llamada → detalle

---

# 📊 6. Transformación con pandas

En el notebook hacemos:

```python
results.append({
    "name": poke_data["name"],
    "height": poke_data["height"],
    "weight": poke_data["weight"],
    "base_experience": poke_data["base_experience"]
})
```

👉 Seleccionamos solo datos útiles.

Luego:

```python
df = pd.DataFrame(results)
```

👉 Convertimos a tabla.

---

# 📈 7. Análisis de datos

En el notebook:

```python
df.describe()
```

👉 obtenemos estadísticas.

También:

```python
df.sort_values("base_experience")
```

👉 analizamos los datos.

---

# 🔧 8. Función reutilizable

Creamos:

```python
def get_pokemon_data(limit=5):
```

👉 Esto permite reutilizar todo el proceso.

---

# 📊 9. Notebook 2 — Streamlit

Aquí convertimos el análisis en una app.

Ejemplo:

```python
st.title("Dashboard Pokémon")
st.dataframe(df)
```

👉 Streamlit permite:

- ver tablas
- crear gráficos
- mostrar métricas

---

# 🔄 10. Flujo completo del proyecto

```
PokéAPI
   ↓
requests (Python)
   ↓
JSON
   ↓
pandas (DataFrame)
   ↓
Streamlit
   ↓
Usuario
```

---

# 🎯 11. Qué estás aprendiendo realmente

Este proyecto enseña:

- cómo consumir APIs
- cómo entender JSON
- cómo transformar datos
- cómo analizarlos
- cómo visualizarlos

---

# 🚀 12. Conclusión

Este proyecto conecta todo el proceso de datos.

👉 Desde obtener datos hasta mostrarlos en una aplicación.

---

# 💬 Frase final

"He utilizado una API externa para obtener datos, los he transformado con Python y los he visualizado en una aplicación interactiva."

