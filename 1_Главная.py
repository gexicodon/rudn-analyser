import streamlit as st

st.set_page_config(
    page_title="Анализатор успеваемости",
    page_icon="📊",
    layout="wide"
)


st.markdown(
    """
    <div style="
        padding: 2.5rem 3rem;
        border-radius: 18px;
        background: linear-gradient(135deg, #1f2937, #111827);
        color: white;
        margin-bottom: 2rem;
    ">
        <h1 style="font-size: 3rem; margin-bottom: 0.5rem;">
            📊 Анализатор успеваемости
        </h1>
        <p style="font-size: 1.2rem; opacity: 0.9;">
            Инструмент для анализа оценок, посещаемости  
            и выявления студентов группы риска
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    ### 🎯 Что умеет приложение
    - Анализирует **оценки и посещаемость**
    - Показывает **проблемные предметы**
    - Выявляет **студентов группы риска**
    - Помогает принимать решения на основе данных
    """
)

st.divider()


col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        ### 👤 Студенты
        - Индивидуальная динамика
        - История оценок
        - Посещаемость во времени
        """
    )

with col2:
    st.markdown(
        """
        ### 📚 Предметы
        - Средние показатели
        - Разброс оценок
        - Сравнение дисциплин
        """
    )

with col3:
    st.markdown(
        """
        ### 📈 Аналитика
        - Корреляции
        - Тренды
        - Автоматические инсайты
        """
    )

st.divider()


st.markdown(
    """
    ### 🚀 Как начать работу
    1. Загрузите CSV-файл с данными студентов  
    2. Перейдите в раздел анализа  
    3. Используйте фильтры и вкладки для исследования данных  
    """
)


st.markdown(
    """
    <div style="
        padding: 1.5rem;
        border-radius: 14px;
        border: 1px solid #e5e7eb;
        margin-top: 2rem;
        text-align: center;
    ">
        <h3>📂 Готовы начать?</h3>
        <p>Загрузите CSV-файл и переходите к анализу данных</p>
    </div>
    """,
    unsafe_allow_html=True
)
