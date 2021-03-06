#1.	Вернуть первый элемент, третий элемент, второй с конца элемент входного массива.
ar = [int(el) for el in input().split()]
print(ar[1],ar[2],ar[len(ar)-2])
#2.	Дан массив чисел и число N. Возвести число в позиции N в степень N. Если это невозможно, то вернуть -1.
ar = [int(el) for el in input().split()]
N = int(input())
c=0
if len(ar)>=N:
    c=ar[N-1]**N
    print(c)
else:
    print('-1')
#3.	Найти второй индекс входного символа во входной строке.
str = input()
letter = input()
if str.count(letter)>=2:
    print(str.find(letter,2))
else:
    print('не удалось найти повторное вхождение символа во входной строке')
#4.	Найти количество нулей в конце входного числа.
number = input()
c=0
for i in "".join(reversed(number)):
    if i!='0':
        break
    c+=1
print(c)
#5.	Представить входную строку в обратном порядке.
string = input()
print("".join(reversed(string)))#second way - print(str[::-1])
#6.	Проверить состоит ли входной массив исключительного из одного и того же значения.
ar = input()
if ar.count(ar[1])==len(ar):
    print('yes')
else:
    print('no')
#7.	Проверить сложность пароля во входной строке. Пароль должен содержать, как минимум, одну букву в нижнем регистре, одну букву в верхнем регистре, одну цифру и не содержит никаких других символов. Минимальная длина пароля 16 символов.
password = input()
c=0
for i in range(0,len(password)):
    if 'a'<=password[i]<='z' or 'A'<=password[i]<='Z' or '0'<=password[i]<='9':
        c+=1    
    else:  #если пароль содержит символы кроме букв и цифр, то цикл прерывается и пароль не считается правильным
        c=0     
        break
if len(password)>=16	& c>=3:
    print('yes')
else:
    print('no')
#8.	Во входном списке имеются вложенные списки, которые также могут иметь вложенные списки. Необходимо вытянуть список в одномерный массив (flatten).
def flatten(somelist):
    for elem in somelist:
        if isinstance(elem, list) and not isinstance(elem, str):
            yield from flatten(elem)
        else:
            yield elem
lst = [1, [2, 3], [4, [6, 7]]]
print(list(flatten(lst)))
#9.	На вход принимается словарь(dict), в котором ключами являются строки (str), а значениями числа (float). Необходимо вернуть ключ максимального значения.
dictionary = {'l': 33, 'k': 532, 'b': 2124}
print(max(dictionary, key=dictionary.get))
#10.	Дан непустой список целых чисел (X). Необходимо вернуть список, содержащий только неуникальные значения из входного списка. Порядок чисел не должен меняться.
X = [1,2,2,4,5,11,3,1,3,3,13,33,22,23]
n=[]
for i in X:
    if X.count(i)>1:
        n.append(i)
print(n)
