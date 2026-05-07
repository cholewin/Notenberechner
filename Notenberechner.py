import streamlit as st
import pandas as pd

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Cyber Notenrechner",
    page_icon="⚡",
    layout="wide"
)

# =====================================================
# CYBERPUNK CSS
# =====================================================

st.markdown("""
<style>

/* ===================================================== */
/* BACKGROUND */
/* ===================================================== */

.stApp {
    background:
        radial-gradient(circle at top left, #ff00ff22, transparent 25%),
        radial-gradient(circle at bottom right, #00ffff22, transparent 25%),
        linear-gradient(135deg, #050816 0%, #0d1229 100%);
    color: white;
}

/* animated grid */
.stApp::before {
    content: "";
    position: fixed;
    width: 100%;
    height: 100%;

    background-image:
        linear-gradient(rgba(0,255,255,0.05) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,255,255,0.05) 1px, transparent 1px);

    background-size: 40px 40px;

    animation: moveGrid 20s linear infinite;

    z-index: -1;
}

@keyframes moveGrid {
    from {
        transform: translateY(0px);
    }
    to {
        transform: translateY(40px);
    }
}

/* ===================================================== */
/* TITLE */
/* ===================================================== */

.cyber-title {

    text-align: center;

    font-size: 70px;

    font-weight: 900;

    background: linear-gradient(
        90deg,
        #00ffff,
        #ff00ff,
        #00ffff
    );

    background-size: 300%;

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    animation: glow 6s linear infinite;
}

@keyframes glow {

    0% {
        background-position: 0%;
        filter: drop-shadow(0 0 10px #00ffff);
    }

    50% {
        background-position: 100%;
        filter: drop-shadow(0 0 25px #ff00ff);
    }

    100% {
        background-position: 0%;
        filter: drop-shadow(0 0 10px #00ffff);
    }
}

.cyber-sub {

    text-align: center;

    color: #9aa4c7;

    font-size: 20px;

    margin-top: -20px;

    margin-bottom: 40px;
}

/* ===================================================== */
/* GLASS CARD */
/* ===================================================== */

.cyber-card {

    background: rgba(255,255,255,0.04);

    border: 1px solid rgba(0,255,255,0.2);

    border-radius: 25px;

    padding: 30px;

    backdrop-filter: blur(18px);

    box-shadow:
        0 0 20px rgba(0,255,255,0.15),
        0 0 40px rgba(255,0,255,0.1);

    animation: fadeIn 0.8s ease;
}

.cyber-card:hover {

    transform: translateY(-4px);

    transition: 0.3s;

    box-shadow:
        0 0 30px #00ffff66,
        0 0 60px #ff00ff33;
}

/* ===================================================== */
/* BUTTON */
/* ===================================================== */

.stButton > button {

    width: 100%;

    background: linear-gradient(
        90deg,
        #ff00ff,
        #00ffff
    );

    color: white;

    border: none;

    border-radius: 18px;

    padding: 14px;

    font-size: 18px;

    font-weight: bold;

    box-shadow:
        0 0 15px #00ffff66,
        0 0 25px #ff00ff44;

    transition: 0.3s ease;
}

.stButton > button:hover {

    transform: scale(1.03);

    box-shadow:
        0 0 25px #00ffff,
        0 0 45px #ff00ff;
}

/* ===================================================== */
/* DATA EDITOR */
/* ===================================================== */

[data-testid="stDataEditor"] {

    border-radius: 20px;

    overflow: hidden;

    border: 1px solid #00ffff44;

    box-shadow:
        0 0 20px rgba(0,255,255,0.1);
}

/* ===================================================== */
/* METRICS */
/* ===================================================== */

[data-testid="metric-container"] {

    background: rgba(255,255,255,0.05);

    border: 1px solid rgba(0,255,255,0.15);

    padding: 20px;

    border-radius: 20px;

    box-shadow:
        0 0 15px rgba(0,255,255,0.1);
}

/* ===================================================== */
/* FADE */
/* ===================================================== */

@keyframes fadeIn {

    from {
        opacity: 0;
        transform: translateY(20px);
    }

    to {
        opacity: 1;
        transform: translateY(0px);
    }
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="cyber-title">
⚡ CYBER NOTENRECHNER
</div>

<div class="cyber-sub">
Neon UI • Animationen • Futuristisches Design
</div>
""", unsafe_allow_html=True)

# =====================================================
# CARD START
# =====================================================

st.markdown("<div class='cyber-card'>", unsafe_allow_html=True)

# =====================================================
# START DATA
# =====================================================

faecher = [
    "📐 Mathe",
    "📖 Deutsch",
    "🌍 Englisch"
]

df = pd.DataFrame({
    "Fach": faecher,
    "Klassenarbeit 1": [0, 0, 0],
    "Klassenarbeit 2": [0, 0, 0],
    "Mündliche Note": [0, 0, 0],
    "Referat": [0, 0, 0],
})

# =====================================================
# DATA EDITOR
# =====================================================

edited_df = st.data_editor(
    df,
    num_rows="fixed",
    use_container_width=True
)

st.divider()

# =====================================================
# GRADE CALCULATION
# =====================================================

def berechne_note(row):

    punkte = 0
    gewicht = 0

    if row["Klassenarbeit 1"] > 0 and row["Klassenarbeit 2"] > 0:

        ka = (
            row["Klassenarbeit 1"]
            + row["Klassenarbeit 2"]
        ) / 2

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

# =====================================================
# COLOR FUNCTION
# =====================================================

def farbe_note(val):

    if val is None:
        return ""

    if val < 2:
        return """
        background-color: #00ff99;
        color: black;
        font-weight: bold;
        """

    elif val < 3:
        return """
        background-color: #00ffff;
        color: black;
        font-weight: bold;
        """

    elif val < 4:
        return """
        background-color: #ffd166;
        color: black;
        font-weight: bold;
        """

    elif val < 5:
        return """
        background-color: #ff4d6d;
        color: white;
        font-weight: bold;
        """

    else:
        return """
        background-color: #ff0033;
        color: white;
        font-weight: bold;
        """

# =====================================================
# BUTTON
# =====================================================

if st.button("⚡ Gesamtnoten berechnen"):

    result_df = edited_df.copy()

    result_df["Gesamtnote"] = result_df.apply(
        berechne_note,
        axis=1
    )

    # Durchschnitt
    durchschnitt = result_df["Gesamtnote"].mean()

    c1, c2 = st.columns(2)

    c1.metric(
        "📊 Durchschnitt",
        round(durchschnitt, 2)
    )

    beste = result_df["Gesamtnote"].min()

    c2.metric(
        "🏆 Beste Note",
        round(beste, 2)
    )

    styled_df = result_df.style.applymap(
        farbe_note,
        subset=["Gesamtnote"]
    )

    st.markdown("## ✅ Ergebnisse")

    st.dataframe(
        styled_df,
        use_container_width=True
    )

st.markdown("</div>", unsafe_allow_html=True)
