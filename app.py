
import streamlit as st
import requests
import pandas as pd

BASE_URL = "https://pokeapi.co/api/v2/pokemon"

@st.cache_data
def get_pokemon_data(limit=10):
    response = requests.get(f"{BASE_URL}?limit={limit}")
    data = response.json()
    results = []

    for pokemon in data["results"]:
        poke_response = requests.get(pokemon["url"])
        if poke_response.status_code == 200:
            poke_data = poke_response.json()
            results.append({
                "name": poke_data["name"],
                "height": poke_data["height"],
                "weight": poke_data["weight"],
                "base_experience": poke_data["base_experience"]
            })

    return pd.DataFrame(results)

st.title("Dashboard Pokémon con Streamlit")

limit = st.slider("Número de Pokémon", min_value=5, max_value=30, value=10)

df = get_pokemon_data(limit)

col1, col2, col3 = st.columns(3)
col1.metric("Total Pokémon", len(df))
col2.metric("Peso medio", round(df["weight"].mean(), 2))
col3.metric("Altura media", round(df["height"].mean(), 2))

st.subheader("Tabla de datos")
st.dataframe(df)

st.subheader("Top experiencia base")
top_df = df.sort_values("base_experience", ascending=False)
st.bar_chart(top_df.set_index("name")["base_experience"])

st.subheader("Peso por Pokémon")
st.bar_chart(df.set_index("name")["weight"])
