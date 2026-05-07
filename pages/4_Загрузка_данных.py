import streamlit as st
import pandas as pd

from analysis.preprocessing import validate_frame, preprocess

st.header("📁 Загрузка CSV-файла")
st.set_page_config(
    page_icon="📊",
)

uploaded_file = st.file_uploader(
    "Загрузите CSV с оценками",
    type=['csv', 'xlsx', 'xls']
)

if uploaded_file:
    try:
        file_extension = uploaded_file.name.split('.')[-1].lower()

        if file_extension in ['xlsx', 'xls']:
            raw_df = pd.read_excel(uploaded_file, engine='openpyxl')
        elif file_extension == 'csv':
            try:
                raw_df = pd.read_csv(uploaded_file, encoding='cp1251', sep=';')
            except:
                try:
                    raw_df = pd.read_csv(uploaded_file, encoding="utf-8", sep=';')
                except:
                    raw_df = pd.read_csv(uploaded_file, encoding="cp1251", sep=',')
        st.subheader("Сырые данные")
        st.dataframe(raw_df, use_container_width=True)

        validate_frame(raw_df)

        clean_df = preprocess(raw_df)
        st.session_state["data"] = clean_df

        st.success("✅ Данные успешно загружены и обработаны")

        st.subheader("Очищенные данные")
        st.dataframe(clean_df, use_container_width=True)

    except Exception as e:
        st.error(f'Произошла ошибка: {e}')

