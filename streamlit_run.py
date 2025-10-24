import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import os
from transformers import pipeline

st.success('Gratulacje! Z powodzeniem uruchomiłeś aplikację')
st.title('Translator')

st.subheader('Instrukcja:')
st.write('Ta aplikacja pozwala na tłumaczenie tekstu z języka angielskiego na niemiecki oraz analizowanie wydźwięku emocjonalnego tekstu. '
         'Wybierz odpowiednią opcję z menu, aby rozpocząć.')

df = pd.read_csv("DSP_4.csv", sep = ';')
st.dataframe(df)

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
            time.sleep(2)
            translation = translator(text)
            st.success('Tłumaczenie zakończone!')
            st.write("Tłumaczenie na niemiecki:", translation[0]['translation_text'])
