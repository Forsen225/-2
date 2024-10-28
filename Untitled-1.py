import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Функции для моделирования различных методов шифрования
def simulate_aes(data_size, key_length):
    energy_consumption = 0.1 * data_size * key_length / 128
    processing_time = 0.5 * data_size * key_length / 256
    resistance = "Высокая"
    return energy_consumption, processing_time, resistance

def simulate_rsa(data_size, key_length):
    energy_consumption = 0.5 * data_size * key_length / 2048
    processing_time = 2 * data_size * key_length / 2048
    resistance = "Средняя"
    return energy_consumption, processing_time, resistance

def simulate_qkd(data_size, distance):
    energy_consumption = 0.3 * data_size * distance / 1000
    processing_time = 1.0 * data_size * distance / 1000
    resistance = "Очень высокая"
    return energy_consumption, processing_time, resistance

def simulate_qkd_with_ai(data_size, distance):
    # Оптимизируем QKD с ИИ для значительного уменьшения энергопотребления и времени обработки
    # Допустим, что МО позволяет уменьшить энергопотребление на 80% и время обработки на 90%
    optimized_weights = [0.2, 0.1]  # [коэффициент для энергии, коэффициент для времени]
    energy_consumption = 0.3 * data_size * distance / 1000 * optimized_weights[0]
    processing_time = 1.0 * data_size * distance / 1000 * optimized_weights[1]
    resistance = "Очень высокая"
    return energy_consumption, processing_time, resistance, optimized_weights

# Функция для запуска моделирования
def run_simulation(data_size, key_length, distance):
    aes_result = simulate_aes(data_size, key_length)
    rsa_result = simulate_rsa(data_size, key_length)
    qkd_result = simulate_qkd(data_size, distance)
    qkd_ai_result = simulate_qkd_with_ai(data_size, distance)

    results = {
        "Методы": ["AES-256", "RSA", "QKD", "QKD с ИИ"],
        "Энергопотребление (ед.)": [aes_result[0], rsa_result[0], qkd_result[0], qkd_ai_result[0]],
        "Время обработки (сек.)": [aes_result[1], rsa_result[1], qkd_result[1], qkd_ai_result[1]],
        "Устойчивость": [aes_result[2], rsa_result[2], qkd_result[2], qkd_ai_result[2]],
        "Оптимизированные веса": ["-", "-", "-", f"{qkd_ai_result[3][0]:.2f}, {qkd_ai_result[3][1]:.2f}"]
    }

    return pd.DataFrame(results)

# Интерфейс Streamlit
st.title("Моделирование шифрования для спутников с использованием Plotly")
data_size = st.number_input("Размер данных (КБ):", min_value=1, value=100)
key_length = st.number_input("Длина ключа (бит):", min_value=1, value=256)
distance = st.number_input("Расстояние до наземной станции (км):", min_value=1, value=1000)

if st.button("Запустить моделирование"):
    df_results = run_simulation(data_size, key_length, distance)
    st.write("Результаты моделирования:")
    st.dataframe(df_results)

    # Построение графика с помощью Plotly
    fig = px.bar(df_results, 
                 x="Методы", 
                 y="Энергопотребление (ед.)", 
                 title="Энергопотребление различных методов шифрования",
                 labels={"Энергопотребление (ед.)": "Энергопотребление"},
                 text="Энергопотребление (ед.)")

    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(yaxis_title="Энергопотребление (ед.)", xaxis_title="Методы")

    # Добавление второго графика на тот же график для времени обработки
    fig.add_scatter(x=df_results["Методы"], y=df_results["Время обработки (сек.)"], mode='lines+markers', name='Время обработки', yaxis='y2')

    # Настройка осей
    fig.update_layout(
        yaxis2=dict(
            title='Время обработки (сек.)',
            overlaying='y',
            side='right'
        )
    )

    st.plotly_chart(fig)
