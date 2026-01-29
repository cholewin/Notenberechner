import streamlit as st

st.set_page_config(
    page_title="Notenrechner",
    layout="centered"
)

st.title("📊 Notenrechner")
st.write("Du kannst Leistungen auch als **nicht vorhanden** markieren 📱")

# Fach auswählen
fach = st.selectbox(
    "📘 Fach auswählen",
    ["Mathe", "Deutsch", "Englisch", "Biologie", "Geschichte"]
)

st.divider()
st.subheader("✏️ Deine Noten")

# Klassenarbeit 1
ka1_vorhanden = st.toggle("Klassenarbeit 1 geschrieben?", value=True)
ka1 = st.number_input(
    "Note Klassenarbeit 1",
    min_value=1.0, max_value=6.0, step=0.1,
    disabled=not ka1_vorhanden
)

# Klassenarbeit 2
ka2_vorhanden = st.toggle("Klassenarbeit 2 geschrieben?", value=True)
ka2 = st.number_input(
    "Note Klassenarbeit 2",
    min_value=1.0, max_value=6.0, step=0.1,
    disabled=not ka2_vorhanden
)

# Mündlich
muendlich_vorhanden = st.toggle("Mündliche Note vorhanden?", value=True)
muendlich = st.number_input(
    "Mündliche Note",
    min_value=1.0, max_value=6.0, step=0.1,
    disabled=not muendlich_vorhanden
)

# Referat
referat_vorhanden = st.toggle("Referat gehalten?", value=False)
referat = st.number_input(
    "Referat Note",
    min_value=1.0, max_value=6.0, step=0.1,
    disabled=not referat_vorhanden
)

st.divider()

def berechne_note():
    punkte = 0
    gewicht = 0

    if ka1_vorhanden:
        punkte += ka1 * 0.2
        gewicht += 0.2

    if ka2_vorhanden:
        punkte += ka2 * 0.2
        gewicht += 0.2

    if muendlich_vorhanden:
        punkte += muendlich * 0.5
        gewicht += 0.5

    if referat_vorhanden:
        punkte += referat * 0.1
        gewicht += 0.1

    if gewicht == 0:
        return None

    return round(punkte / gewicht, 2)

if st.button("📐 Gesamtnote berechnen", use_container_width=True):
    note = berechne_note()

    if note is None:
        st.warning("Bitte mindestens eine Leistung auswählen 🙂")
    else:
        if note < 2:
            st.success(f"🎉 Deine Note in {fach}: {note}")
        elif note < 3:
            st.info(f"😊 Deine Note in {fach}: {note}")
        elif note < 4:
            st.warning(f"😐 Deine Note in {fach}: {note}")
        else:
            st.error(f"😟 Deine Note in {fach}: {note}")
