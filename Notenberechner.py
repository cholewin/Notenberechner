import streamlit as st
import pandas as pd

st.set_page_config(page_title="Notenrechner", layout="wide")

st.title("📊 Notenrechner für Schüler")
st.write("Die Farben zeigen dir sofort, wie gut deine Note ist 😊")

# Startdaten
faecher = ["Mathe", "Deutsch", "Englisch"]

df = pd.DataFrame({
    "Fach": faecher,
    "Klassenarbeit 1": [0, 0, 0],
    "Klassenarbeit 2": [0, 0, 0],
    "Mündliche Note": [0, 0, 0],
    "Referat": [0, 0, 0],
})

edited_df = st.data_editor(
    df,
    num_rows="fixed",
    use_container_width=True
)

st.divider()

def berechne_note(row):
    punkte = 0
    gewicht = 0

    if row["Klassenarbeit 1"] > 0 and row["Klassenarbeit 2"] > 0:
        ka = (row["Klassenarbeit 1"] + row["Klassenarbeit 2"]) / 2
        punkte += ka * 0.4
        gewicht += 0.4

    if row["Mündliche Note"] > 0:
        punkte += row["Mündliche Note"] * 0.5
        gewicht += 0.5

    if row["Referat"] > 0:
        punkte += row["Referat"] * 0.1
        gewicht += 0.1

    if gewicht == 0:
        return None

    return round(punkte / gewicht, 2)

# Farb-Funktion
def farbe_note(val):
    if val is None:
        return ""
    if val < 2:
        return "background-color: #7CFC98"  # grün
    elif val < 3:
        return "background-color: #C6F6C6"  # hellgrün
    elif val < 4:
        return "background-color: #FFD580"  # orange
    elif val < 5:
        return "background-color: #FFB3B3"  # hellrot
    else:
        return "background-color: #FF6961"  # rot

if st.button("📐 Gesamtnoten berechnen"):
    result_df = edited_df.copy()
    result_df["Gesamtnote"] = result_df.apply(berechne_note, axis=1)

    styled_df = result_df.style.applymap(
        farbe_note,
        subset=["Gesamtnote"]
    )

    st.subheader("✅ Ergebnisse")
    st.dataframe(styled_df, use_container_width=True)
