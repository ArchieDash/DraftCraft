def avg(data):
    marks = [int(x) for x in data.split()]
    avg = sum(marks)/len(marks)
    return avg

def main():
    judge = input('Оценки судей (через пробел):')
    people = input('Оценки народного голосования (через пробел):')
    mark = avg(judge) + avg(people)
    print(f'Итоговая оценка: {mark}')

main()

# Powered by Archie Dash. Thx for using ^^
