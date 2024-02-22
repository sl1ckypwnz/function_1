def f(i):  return 1 if i == 1 else i * f(i - 1)

n = int(input('Ввод числа:  '))

f1 = [f(n - i) for i in range(n)]

print('Результат:  ', f1)