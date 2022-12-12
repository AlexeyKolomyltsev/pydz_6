# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.

def multiple_chain(chain, indexes):
    multiple = 1
    for i in indexes:
        multiple *= chain[i]
    return multiple

n = int(input("Введите число "))
chain = list(range(-n, n+1))
print(chain)
index_position = list(map(int, input(f'Введите через пробел индексы от 0 до {n * 2} ').split(' ')))
print(index_position)

print(f'Произведение элементов на указанных индексах = {multiple_chain(chain, index_position)}')