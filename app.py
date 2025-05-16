import streamlit as st


st.title("Szacowanie ceny mieszkania")
with st.form(key="parametry_mieszkania"):
    st.subheader("Wybierz parametry mieszkania")

    st.date_input("Wybierz rok budowy")
    st.select_slider("Liczba pokoi", options=[1,2,3,4,5,6,7,8,9,10])
    st.number_input("Piętro", min_value=0, max_value=50)
    st.number_input("Metraż (w metrach kwadratowych)",min_value=20, max_value=500)
    st.selectbox("Dzielnica", [ "Bemowo", "Białołęka", "Bielany", "Mokotów", "Ochota", "Praga-Południe", "Praga-Północ", "Rembertów", "Śródmieście", "Targówek", "Ursus", "Ursynów", "Wawer", "Wesoła", "Wilanów", "Włochy", "Wola", "Żoliborz"])
    st.selectbox("Wyposażenie", ['Tak', 'Nie'])
    pressed_button = st.form_submit_button(label="Wyślij")
    if pressed_button:
        st.warning("Wkrótce dostępne")
        
st.title("AI Odpowiadacz (Streamlit)")
question = st.text_input("Zadaj pytanie:")

if question:
    st.write(f"Odpowiedź: To jest przykładowa odpowiedź na pytanie '{question}'.")
