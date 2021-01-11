import pandas as pd
import random

data = pd.read_csv("cities.csv")["cities"].to_list()


class Bot():
    def __init__(self):
        pass
    
    def get_city(self, pool):
        return random.choice(pool)


class Player():
    def __init__(self):
        pass
    
    def answer(self):
        answer = input("Город: ").strip().capitalize()
        return answer


def get_pool(city):
    return list(filter(lambda x: x.startswith(get_last_letter(city)), data))


def get_last_letter(word):
    for letter in word.upper()[::-1]:
        if letter not in ["Ь", "Й", "Ы", "Ц"]:
            return letter


def casefold(pool):
    return[item.casefold() for item in pool]


def main():
    bot = Bot()
    player = Player()
    question = random.choice(data)
    data.remove(question)
    print(question)
    session = [question]
    while True:
        pool = get_pool(question)
        print(f"options: {len(pool)}")
        answer = player.answer()
        if len(pool) == 0:
            print("Города кончились! :Р\nВы проиграли.")
            break
        elif answer == "X":
            break
        elif answer == "Hint":
            print(random.choice(get_pool(question)))
            continue
        elif answer == "S":
            print(session)
            continue
        elif ((answer.casefold() in casefold(data)) or (answer.casefold() in casefold(session))) and (answer[0] != get_last_letter(question)):
            print(f"Название города должно начинаться с {get_last_letter(question)}")
            continue
        elif (answer.casefold() in casefold(session)):
            print("Такой город уже был. Не повторяйся! :Р")
            continue
        elif (answer.casefold() not in casefold(data)) and (answer.casefold() not in casefold(session)):
            print("Я такого города не знаю :(")
            continue
        else:
            for item in pool:
                if item.casefold() == answer.casefold():
                    data.remove(item)
            session.append(answer)
        pool = get_pool(answer)
        if len(pool) == 0:
            print("Я сдаюсь. Ты победил!")
            break
        question = bot.get_city(pool)
        data.remove(question)
        session.append(question)
        print(question)
    print(session)


main()