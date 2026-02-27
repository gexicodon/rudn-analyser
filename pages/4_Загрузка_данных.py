import streamlit as st
import pandas as pd

from analysis.preprocessing import validate_frame, preprocess

st.header("📁 Загрузка CSV-файла")

uploaded_file = st.file_uploader(
    "Загрузите CSV с оценками",
    type='csv'
)

if uploaded_file:
    try:
        raw_df = pd.read_csv(uploaded_file, encoding="cp1251", sep=';')
        st.subheader("Сырые данные")
        st.dataframe(raw_df,use_container_width=True)

        validate_frame(raw_df)

        clean_df = preprocess(raw_df)
        st.session_state["data"] = clean_df

        st.success("✅ Данные успешно загружены и обработаны")

        st.subheader("Очищенные данные")
        st.dataframe(clean_df, use_container_width=True)

    except Exception as e:
        st.error(f"❌ Ошибка при обработке файла: {e}")