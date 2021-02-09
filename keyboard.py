qwerty = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
rus = "йцукенгшщзхъфывапролджэячсмитьбю."
qwerty = [s for s in qwerty]
rus = [s for s in rus]
eng_to_rus = dict(zip(qwerty, rus))
rus_to_eng = dict(zip(rus, qwerty))

def translator(string):
    if string.strip().lower()[0] in eng_to_rus.keys():
        db = eng_to_rus
    else:
        db = rus_to_eng
    return "".join([db.get(letter, " ") for letter in string])


def main():
    while True:
        string = input("Paste a string here (type q to quit): ")
        if string.strip().lower() in ["q", "й"]:
            break
        translation = translator(string)
        print(f"Translation: {translation}")


if __name__ == "__main__":
    main()