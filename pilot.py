import streamlit as st
import pandas as pd

# --------------------------------------------------
# BASE DE DATOS 
# --------------------------------------------------

minerales_arcilla = pd.DataFrame([
    {"Mineral": "Caolinita", "Formula": "Al2Si2O5(OH)4", "Grupo": "Arcilla",
     "Pico_Principal": 12.3, "Picos_Secundarios": "20.3, 24.8, 35.0, 38.5"},
    {"Mineral": "Illita", "Formula": "KAl2(AlSi3O10)(OH)2", "Grupo": "Arcilla",
     "Pico_Principal": 8.836, "Picos_Secundarios": "17.653, 19.8, 22.842, 23.901, 25.727, 26.668, 31.171, 35.0, 45.187, 61.845"},
    {"Mineral": "Muscovita", "Formula": "KAl2(AlSi3O10)(OH)2", "Grupo": "Mica",
     "Pico_Principal": 8.856, "Picos_Secundarios": "17.775, 26.789, 35.983, 45.8"},
    {"Mineral": "Montmorillonita", "Formula": "(Na,Ca)0.33(Al,Mg)2Si4O10(OH)2·nH2O", "Grupo": "Esmectita",
     "Pico_Principal": 6.0, "Picos_Secundarios": "19.8, 26.5, 35.0"},
    {"Mineral": "Halloysita", "Formula": "Al2Si2O5(OH)4·2H2O", "Grupo": "Arcilla",
     "Pico_Principal": 11.8, "Picos_Secundarios": "20.1, 24.8"},
    {"Mineral": "Clorita", "Formula": "(Mg,Fe,Al)6(Si,Al)4O10(OH)8", "Grupo": "Clorita",
     "Pico_Principal": 6.2, "Picos_Secundarios": "12.5, 18.8, 25.0"},
    {"Mineral": "Cuarzo", "Formula": "SiO2", "Grupo": "Silicato",
     "Pico_Principal": 26.664, "Picos_Secundarios": "20.88, 36.583, 39.502, 50.188, 60.024"},
    {"Mineral": "Sanidina", "Formula": "KAlSi3O8", "Grupo": "Feldespato K",
     "Pico_Principal": 27.4, "Picos_Secundarios": "21.0, 23.7, 24.3, 30.0"},
    {"Mineral": "Ortoclasa", "Formula": "KAlSi3O8", "Grupo": "Feldespato K",
     "Pico_Principal": 27.5, "Picos_Secundarios": "22.0, 24.2, 30.0"},
    {"Mineral": "Microclina", "Formula": "KAlSi3O8", "Grupo": "Feldespato K",
     "Pico_Principal": 27.4, "Picos_Secundarios": "22.1, 24.0, 30.1"},
    {"Mineral": "Albita", "Formula": "NaAlSi3O8", "Grupo": "Plagioclasa",
     "Pico_Principal": 22.0, "Picos_Secundarios": "27.9, 28.1, 40.7"},
    {"Mineral": "Anortita", "Formula": "CaAl2Si2O8", "Grupo": "Plagioclasa",
     "Pico_Principal": 27.8, "Picos_Secundarios": "22.9, 28.2, 30.0"},
    {"Mineral": "Calcita", "Formula": "CaCO3", "Grupo": "Carbonato",
     "Pico_Principal": 29.4, "Picos_Secundarios": "39.4, 43.1, 47.5, 48.5"},
    {"Mineral": "Dolomita", "Formula": "CaMg(CO3)2", "Grupo": "Carbonato",
     "Pico_Principal": 31.0, "Picos_Secundarios": "41.1, 45.8, 50.5"},
    {"Mineral": "Hematita", "Formula": "Fe2O3", "Grupo": "Óxido",
     "Pico_Principal": 33.2, "Picos_Secundarios": "24.1, 35.6, 49.5, 54.1"},
    {"Mineral": "Goethita", "Formula": "FeO(OH)", "Grupo": "Óxido/Hidróxido",
     "Pico_Principal": 21.2, "Picos_Secundarios": "33.2, 36.6, 53.2"},
    {"Mineral": "Anatasa", "Formula": "TiO2", "Grupo": "Óxido",
     "Pico_Principal": 25.3, "Picos_Secundarios": "37.8, 48.0, 55.1"},
    {"Mineral": "Rutilo", "Formula": "TiO2", "Grupo": "Óxido",
     "Pico_Principal": 27.4, "Picos_Secundarios": "36.1, 41.2, 54.3"},
    {"Mineral": "Halita", "Formula": "NaCl", "Grupo": "Cloruro",
     "Pico_Principal": 31.7, "Picos_Secundarios": "45.5, 56.5, 66.3"},
    {"Mineral": "Silvita", "Formula": "KCl", "Grupo": "Cloruro",
     "Pico_Principal": 28.4, "Picos_Secundarios": "40.6, 50.3, 58.7"},
    {"Mineral": "Crisotilo", "Formula": "Mg3Si2O5(OH)4", "Grupo": "Asbesto",
     "Pico_Principal": 12.0, "Picos_Secundarios": "24.3, 35.4, 60.0"},
    {"Mineral": "Amosita", "Formula": "(Fe,Mg)7Si8O22(OH)2", "Grupo": "Asbesto",
     "Pico_Principal": 10.5, "Picos_Secundarios": "28.5, 33.0, 36.0"},
    {"Mineral": "Crocidolita", "Formula": "Na2Fe5Si8O22(OH)2", "Grupo": "Asbesto",
     "Pico_Principal": 10.4, "Picos_Secundarios": "28.2, 34.8, 36.2"},
    {"Mineral": "Tremolita", "Formula": "Ca2Mg5Si8O22(OH)2", "Grupo": "Anfibol/Asbesto",
     "Pico_Principal": 10.5, "Picos_Secundarios": "28.8, 31.0, 36.5"},
])

# --------------------------------------------------
# FUNCIONES DE BÚSQUEDA
# --------------------------------------------------

def buscar_por_angulo(df, angulo, tolerancia):
    resultados = []

    for _, fila in df.iterrows():
        # Pico principal
        diferencia = abs(fila["Pico_Principal"] - angulo)
        if diferencia <= tolerancia:
            resultados.append({
                "Mineral": fila["Mineral"],
                "Formula": fila["Formula"],
                "Tipo": "Principal",
                "Pico": fila["Pico_Principal"],
                "Diferencia": round(diferencia, 3)
            })

        # Picos secundarios
        for texto_pico in fila["Picos_Secundarios"].split(","):
            pico = float(texto_pico.strip())
            diferencia = abs(pico - angulo)
            if diferencia <= tolerancia:
                resultados.append({
                    "Mineral": fila["Mineral"],
                    "Formula": fila["Formula"],
                    "Tipo": "Secundario",
                    "Pico": pico,
                    "Diferencia": round(diferencia, 3)
                })

    resultados_df = pd.DataFrame(resultados)
    if len(resultados_df) > 0:
        resultados_df = resultados_df.sort_values("Diferencia")
    return resultados_df


def buscar_por_nombre(df, nombre):
    return df[df["Mineral"].str.lower() == nombre.lower()]


# --------------------------------------------------
# INTERFAZ 
# --------------------------------------------------

st.title("XRD Mineral Assistant")
st.subheader("Identificación mineralógica mediante Difracción de Rayos X (XDR)")

st.write("Bienvenido al sistema de identificación mineralógica")
st.write("Cementos Pacasmayo - Planta Piura")
st.sidebar.title("Opciones")

modo = st.sidebar.radio("Modo de búsqueda", ["Buscar por Ángulo", "Buscar por Mineral"])

st.divider()

if modo == "Buscar por Ángulo":
    st.subheader("Búsqueda por ángulo 2θ")

    angulo = st.number_input("Ángulo 2θ (°)", min_value=0.0, max_value=90.0, value=26.6)
    tolerancia = st.number_input("Tolerancia (±°)", min_value=0.1, max_value=5.0, value=0.5)

    if st.button("Buscar"):
        resultados = buscar_por_angulo(minerales_arcilla, angulo, tolerancia)

        if len(resultados) == 0:
            st.warning("No se encontraron coincidencias.")
        else:
            st.success(f"Se encontraron {len(resultados)} coincidencia(s).")
            st.dataframe(resultados)

else:
    st.subheader("Búsqueda por nombre de mineral")

    nombre = st.text_input("Nombre del mineral", placeholder="Ej: Cuarzo")

    if st.button("Buscar"):
        resultado = buscar_por_nombre(minerales_arcilla, nombre)

        if len(resultado) == 0:
            st.warning("No se encontró ese mineral.")
        else:
            st.success("Mineral encontrado")
            st.dataframe(resultado)

st.divider()
with st.expander("Ver base de datos completa"):
    st.dataframe(minerales_arcilla)