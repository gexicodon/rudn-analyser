import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from analysis.insights import generate_insights
import numpy as np

st.header("📊 Статистика")


if "data" not in st.session_state:
    st.warning("Сначала загрузите CSV-файл")
    st.stop()

df = st.session_state["data"]

if df.empty:
    st.warning("Данные пустые")
    st.stop()


st.sidebar.header("Фильтры")

min_score = st.sidebar.slider(
    "Минимальный балл",
    float(df["score"].min()),
    float(df["score"].max()),
    float(df["score"].min())
)

df = df[df["score"] >= min_score]


c1, c2, c3 = st.columns(3)

c1.metric("📈 Средний балл", round(df["score"].mean(), 2))
c2.metric("🟢 Среднее кол-во пропусков", f"{df['attendance'].mean():.1f}%")
c3.metric("👥 Кол-во записей", len(df))

st.divider()


st.subheader("🧠 Автоматические инсайты")

insights = generate_insights(df)

if insights:
    for insight in insights:
        st.info(insight)
else:
    st.success("Нет критических отклонений — показатели в норме 👍")
st.divider()

st.subheader("Распределение оценок")

score_dist = df["score"].value_counts().sort_index()
st.bar_chart(score_dist)


st.subheader("Корреляция показателей")

numeric_cols = ["score", "attendance"]
corr_matrix = df[numeric_cols].corr()

fig, ax = plt.subplots(figsize=(4, 3))
im = ax.imshow(corr_matrix, vmin=-1, vmax=1)

ax.set_xticks(range(len(numeric_cols)))
ax.set_yticks(range(len(numeric_cols)))
ax.set_xticklabels(numeric_cols)
ax.set_yticklabels(numeric_cols)

for i in range(len(numeric_cols)):
    for j in range(len(numeric_cols)):
        ax.text(j, i, f"{corr_matrix.iloc[i, j]:.2f}",
                ha="center", va="center")

fig.colorbar(im, ax=ax)
ax.set_title("Балл VS Пропуски")

st.pyplot(fig)


st.subheader("Пропуски vs Балл")

fig2, ax2 = plt.subplots()
ax2.scatter(df["attendance"], df["score"], alpha=0.6)
ax2.set_xlabel("Кол-во пропусков (%)")
ax2.set_ylabel("Балл")

st.pyplot(fig2)
