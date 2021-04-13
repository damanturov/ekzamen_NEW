initial_capital = float(input("Введите начальную сумму вклада "))
finish_capital = float(input("Введите конечную сумму какую хотите получить "))
vremya = int(input("На сколько лет? "))
procenty = int(input("Под какой процент? "))
#------------------
S = initial_capital
for i in range(0,vremya):
    S=procenty/100.0 /12 * S + S
print ('Количество денег за', vremya, ' лет составит', S, 'сомов')
