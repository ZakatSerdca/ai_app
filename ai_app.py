import os

import openai
from dotenv import load_dotenv


def main():
    load_dotenv("config.env")

    # Получение API-ключа из переменной окружения config.env
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("Ошибка: API-ключ не найден. Проверьте файл config.env")
        return

    openai.api_key = api_key

    print("Добро пожаловать! Введите ваш запрос (или 'exit' для выхода):")

    while True:
        # Получение пользовательского запроса
        user_input = input("Вы: ")

        # Проверка на выход из приложения
        if user_input.lower() == "exit":
            print("Выход из приложения. До свидания!")
            break

        try:
            # Отправка запроса в ChatGPT
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Или другой доступный модельный идентификатор
                messages=[{"role": "user", "content": user_input}],
            )

            # Получение и вывод ответа
            answer = response["choices"][0]["message"]["content"]
            print(f"ChatGPT: {answer}")

        except Exception as e:
            print(f"Ошибка при взаимодействии с нейронной сетью: {e}")


if __name__ == "__main__":
    main()
