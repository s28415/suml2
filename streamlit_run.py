import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import os
from transformers import pipeline

st.success('Gratulacje! Z powodzeniem uruchomiłeś aplikację')
st.title('Translator')
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("minimal-modern-language-translation-app-symbol-user-interface-theme-3d-illustration-rendering-icon-isolated-png.png")

st.subheader('Instrukcja:')
st.write('Ta aplikacja pozwala na tłumaczenie tekstu z języka angielskiego na niemiecki oraz analizowanie wydźwięku emocjonalnego tekstu. '
         'Wybierz odpowiednią opcję z menu, aby rozpocząć.')


st.header('Przetwarzanie języka naturalnego')

option = st.selectbox(
    "Opcje",
    [
        "Wydźwięk emocjonalny tekstu (eng)",
        "Tłumaczenie tekstu (angielski na niemiecki)",
    ],
)

if option == "Wydźwięk emocjonalny tekstu (eng)":
    text = st.text_area(label="Wpisz tekst")
    if text:
        classifier = pipeline("sentiment-analysis")
        answer = classifier(text)
        st.write(answer)
elif option == "Tłumaczenie tekstu (angielski na niemiecki)":
    text = st.text_area(label="Wpisz tekst w języku angielskim do tłumaczenia")
    if text:
        translator = pipeline("translation_en_to_de")

        with st.spinner('Tłumaczenie...'):
            try:
                time.sleep(2)
                translation = translator(text)
                st.success('Tłumaczenie zakończone!')
                st.write("Tłumaczenie na niemiecki:", translation[0]['translation_text'])
            except:
                st.error("Stał się błąd")
