import random
import re

class SimpleChatBot:
    def __init__(self):
        self.responses = {
            "привет": [
                "Привет! Как дела?", 
                "Здорово! Как проходит твой день?", 
                "Хай! Чем могу помочь?", 
                "Привет, что нового у тебя?"
            ],
            "как дела": [
                "У меня всё в шоколаде, спасибо! А у тебя?", 
                "Отлично, все огонь! Как твой день?"
            ],
            "расписание": [
                "Расписание на сегодня:\n1. Математика - 9:00\n2. Русский язык - 10:00\n3. Физика - 11:00",
                "Сегодня у нас:\n1. Математика - 9:00\n2. Русский язык - 10:00\n3. Физика - 11:00"
            ],
            "кто ты": [
                "Я бот, созданный для общения и помощи. Обрати внимание, что я могу делать ошибки!", 
                "Я твой виртуальный помощник, рад тебя видеть! Помни, я не идеален и могу ошибаться."
            ],
            "нужна помощь": [
                "Если нужна помощь, я всегда на связи! Напоминаю, что могу ошибаться!", 
                "Что-то не так? Спрашивай, я тут, чтобы помочь!"
            ],
            "математика": [
                "Какую задачу ты хочешь решить? Я постараюсь помочь, но учти, что могу ошибаться!"
            ],
            "айсер": [
                "Aiser Sarinov — талантливый разработчик и создатель этого бота. Он стремится сделать общение с технологиями более доступным!"
            ],
            "пока": [
                "До свидания! Удачи в делах!", 
                "Пока! Будь на волне, до скорой встречи!"
            ],
            "что нового": [
                "Всё по кайфу! Как у тебя дела?"
            ],
            "генерируй текст": [
                "Напиши, о чём ты хочешь, чтобы я написал текст. Учти, что я могу ошибаться!"
            ],
            "сәлем": [
                "Сәлем! Қалайсың?", 
                "Сәлем! Күндерің қалай өтуде?"
            ],
            "қалайсың": [
                "Менде бәрі жақсы, рахмет! Сенде ше?"
            ],
            "көмек керек": [
                "Егер көмек керек болса, мен әрдайым бармын! Мен қателесетінімді ұмытпа!", 
                "Не болды? Сұра, мен көмек көрсету үшін осындамын!"
            ],
            "жоспар": [
                "Бүгінгі жоспар:\n1. Математика - 9:00\n2. Қазақ тілі - 10:00\n3. Физика - 11:00"
            ],
            "такпак": [
                "Таспен ұрсаң, тасқа ұрылады.",
                "Сөз - көңілдің күмісіндей."
            ]
        }
        self.learned_responses = {}

    def learn_response(self, question, answer):
        self.learned_responses[question] = answer
        print(f"Запомнил: '{question}' -> '{answer}'")

    def solve_math(self, expression):
        try:
            cleaned_expression = re.sub(r'[^0-9+\-*/().]', '', expression)
            result = eval(cleaned_expression)
            return f"Ответ: {result}"
        except Exception:
            return "Извини, я не смог решить этот пример."

    def get_response(self, user_input):
        user_input = user_input.lower()

        # Проверка на казахский язык
        if any(char in user_input for char in 'қңүә'):
            if "айсер" in user_input:
                return random.choice(self.responses["айсер"])
            
            if "такпак" in user_input:
                return random.choice(self.responses["такпак"])

            if "жоспар" in user_input:
                return random.choice(self.responses["жоспар"])

            for key in self.responses.keys():
                if key in user_input:
                    return random.choice(self.responses[key])

            return "Кешір, мен түсінбеймін. Басқа нәрсені сұрауға болады!"
        
        # Ответы на русском
        if "айсер" in user_input:
            return random.choice(self.responses["айсер"])
        
        if "математика" in user_input:
            return self.responses["математика"][0]
        
        if re.search(r'\d+[+\-*/]\d+', user_input):
            return self.solve_math(user_input)

        if "расписание" in user_input:
            return random.choice(self.responses["расписание"])

        for key in self.responses.keys():
            if key in user_input:
                return random.choice(self.responses[key])

        return "Извини, я не понимаю. Можешь попробовать спросить что-то другое! Помни, что я могу делать ошибки."

    def chat(self):
        print("Вы пишете Боту.")
        print("Создано Aiser Team.")
        print("Введите 'пока' для завершения беседы.")

        while True:
            user_input = input("Вы: ")
            if user_input.lower() == 'пока':
                print("Бот: Пока, до встречи!")
                break
            response = self.get_response(user_input)
            print("Бот:", response)
            if "не понимаю" in response or "кешір" in response:
                user_feedback = input("Какой правильный ответ? ")
                self.learn_response(user_input, user_feedback)

# Запуск бота
chatbot = SimpleChatBot()
chatbot.chat()
