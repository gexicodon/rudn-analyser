import streamlit as st
import pandas as pd
from analysis.risk import find_risk_students

st.header("🚨 Студенты группы риска")


if "data" not in st.session_state:
    st.warning("Сначала загрузите CSV-файл")
    st.stop()

df = st.session_state["data"]

if df.empty:
    st.warning("Данные пустые")
    st.stop()


risk_df = find_risk_students(df)


if risk_df.empty:
    st.success("🎉 Студенты группы риска не обнаружены")
    st.info("Резких падений успеваемости не зафиксировано")
    st.stop()


c1, c2, c3 = st.columns(3)

c1.metric(
    "👥 Студентов риска",
    risk_df["student_id"].nunique()
)

c2.metric(
    "📚 Предметов с падением",
    risk_df["subject"].nunique()
)

c3.metric(
    "📉 Максимальное падение",
    f"{risk_df['delta'].min():.1f}"
)

st.divider()


display_cols = [
    "student_id",
    "subject",
    "date",
    "score",
    "delta",
]

table_df = (
    risk_df[display_cols]
    .sort_values("delta")
    .reset_index(drop=True)
)


st.subheader("📋 Детализация")

st.dataframe(
    table_df,
    use_container_width=True,
    hide_index=True
)


st.caption(
    "⚠️ В таблице показаны случаи резкого падения оценки "
    "по сравнению с предыдущим результатом по предмету"
)
