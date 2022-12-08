text = open('list.txt', 'r', encoding="utf-8")
numberlines = text.read().split().count('--')
sum = 0
listProducts = []
while True:
    try:
        continuation = int(input('Якщо хочете додати продукт введіть 1, якщо ні - 0 '))
        if continuation == 1:
            product = input('Введіть назву одиного продукта в однині ')
            for i in product:
                if i in "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя' ":
                    pass
                else:
                    print('Треба вводти тільки українські літери, символи та числа не можна')
                    break
            listProducts.append(product.lower())
        elif continuation == 0:
            break
        else:
                print('Треба вводити або 0 або 1')
    except:
        print('Треба вводити тільки числа!!!')

text = open('list.txt', 'r', encoding="utf-8")
arr = text.read()
for i in listProducts:
    if i in arr:
        text = open('list.txt', 'r', encoding="utf-8")
        for k in range(numberlines):
            lines = text.readline().split()
            if i in lines:
                price = lines[-1]
                sum = sum + float(lines[-1])
    else:
        print('Ціна на','<',i,'>', 'невідома, тому сума буде без її урахування')
print('Сумма вашої покупки становить: ',sum, 'грн')

