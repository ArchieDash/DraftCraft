def avg(data):
    marks = [int(x) for x in data.split()]
    avg = sum(marks)/len(marks)
    return avg

def main():
    challengers = int(input('Количество претендентов:'))
    for n in range(challengers):
      judge = input('\nОценки судей (через пробел):')
      people = input('Оценки народного голосования (через пробел):')
      mark = avg(judge) + avg(people)
      print(f'Итоговая оценка претендента № {n+1}: {mark}\n')

        
main()

# Powered by Archie Dash. Thx for using ^^
