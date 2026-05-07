import pandas as pd
from analysis.risk import find_risk_students
def generate_insights(df: pd.DataFrame) -> list[str]: # Функция генерации краткой сводки
    insights = [] # Возвращает список с краткими сведениями, которые выводятся на странице "Статистика"


    corr = df["attendance"].corr(df["score"])
    if corr < -0.6:
        insights.append(
            f"📉 Обнаружена сильная отрицательная корреляция между пропусками и баллом ({corr:.2f})"
        )
    elif corr < -0.3:
        insights.append(
            f"📊 Пропуски умеренно влияют на снижение балла ({corr:.2f})"
        )
    else:
        insights.append(
            f"ℹ️ Связь между пропусками и баллом слабая ({corr:.2f})"
        )


    risk_df = find_risk_students(df)
    if not risk_df.empty:
        insights.append(
            f"⚠️ Выявлено {risk_df['student_id'].nunique()} студентов группы риска"
        )


    high_absence = df[df["attendance"] > df["attendance"].median()]
    low_absence = df[df["attendance"] <= df["attendance"].median()]

    if not high_absence.empty and not low_absence.empty:
        delta = low_absence["score"].mean() - high_absence["score"].mean()
        if delta > 0:
            insights.append(
                f"⬇️ Студенты с большим числом пропусков в среднем учатся хуже на {delta:.2f} балла"
            )


    worst = df.nsmallest(5, "score")
    if not worst.empty:
        insights.append(
            "🚨 Обнаружены студенты с аномально низкими баллами"
        )

    return insights
