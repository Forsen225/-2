import streamlit as st
import matplotlib.pyplot as plt
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
    energy_consumption = 0.2 * data_size * distance / 1000
    processing_time = 0.8 * data_size * distance / 1000
    resistance = "Очень высокая"
    return energy_consumption, processing_time, resistance

def run_simulation(data_size, key_length, distance):
    aes_result = simulate_aes(data_size, key_length)
    rsa_result = simulate_rsa(data_size, key_length)
    qkd_result = simulate_qkd(data_size, distance)

    results = {
        "Метод": ["AES-256", "RSA", "QKD"],
        "Энергопотребление (ед.)": [aes_result[0], rsa_result[0], qkd_result[0]],
        "Время обработки (сек.)": [aes_result[1], rsa_result[1], qkd_result[1]],
        "Устойчивость": [aes_result[2], rsa_result[2], qkd_result[2]],
    }

    return results

# Интерфейс приложения
st.title("Моделирование шифрования для спутников")
data_size = st.number_input("Размер данных (КБ):", min_value=1, value=100)
key_length = st.number_input("Длина ключа (бит):", min_value=1, value=256)
distance = st.number_input("Расстояние до наземной станции (км):", min_value=1, value=1000)

if st.button("Запустить моделирование"):
    results = run_simulation(data_size, key_length, distance)
    st.write("Результаты моделирования:")
    st.table(results)

    methods = results["Метод"]
    energy = results["Энергопотребление (ед.)"]
    time_processing = results["Время обработки (сек.)"]

    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Методы')
    ax1.set_ylabel('Энергопотребление', color='tab:red')
    ax1.bar(methods, energy, color='tab:red', alpha=0.6, label='Энергопотребление')
    ax1.tick_params(axis='y', labelcolor='tab:red')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Время обработки', color='tab:blue')
    ax2.plot(methods, time_processing, color='tab:blue', marker='o', label='Время обработки')
    ax2.tick_params(axis='y', labelcolor='tab:blue')

    fig.tight_layout()
    st.pyplot(fig)
