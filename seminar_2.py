# 1.	На вход подается текст, содержащий разные буквы латинского алфавита и символы пунктуации. Нужно найти букву, которая встречается чаще всего. Если таких букв больше одной, то нужно вернуть ту, что стоит выше в алфавите. Регистр букв не учитывается, то есть «А» == «а».
text = '!!!!!!!!!!abcdaaaaaBBBBBfghjkl'
text = text.lower()
maximum = 0
c=[]
for el in text.split():
    for i in el:
        if text.count(i)>=maximum and 'A'<i<'z':
            maximum = text.count(i)
            c+=i
m=0
for item in c:
    if ord(item)>m:
        m=ord(item)            
print(chr(m))
# 2.	На вход подается строка, состоящая из слов и чисел, разделенных одним пробелом. Слова состоят только из букв. Определить, имеется ли в передаваемой строке непрерывная последовательность из трех слов.
text = 'aaaa dddd dksldk 4656'
c=0
a=0
for el in text.split():
    if el.isalpha():
        c+=1
        if c==3:
            a=1
    elif el.isdigit:
        c=0
        
if a>0:
    print('yes')
else:
    print('no')            
# 3.	Найти максимальную длину непрерывной последовательности одинаковых букв во входной строке.
text='vvaaaabbbbcbcccccc'
maximum=0
a=text[0]
b=0
for i in range(len(text)):
    if text[i]==a:
        maximum+=1
    else:
        maximum=1
    if maximum>=b:
        b=maximum
    a=text[i]  
print(b)  
# 4.	На вход подается строка, содержащая латинские буквы, знаки пунктуации и пробелы. Необходимо вернуть строку собранную из букв в верхнем регистре соединенных без пробелов в порядке появления.
text = 'aaOaa ddoOdd dkOsldk 4R656'
a=[]
for el in text.split():
    for i in range(len(el)):
        if el[i].isupper():
            a+=el[i]
print(''.join(a))
# 5.	На вход подается массив чисел. Необходимо отсортировать массив по частоте элементов. Если два элемента имеют одинаковую частоту, то нужно отсортировать по порядку появления в массиве.
ar = [2,1,2,1,4,2,1,1,4,3,3]
arr=[]
maximum=0
for el in ar:
    if ar.count(el)<=maximum and el not in arr:
        arr+=[el]*ar.count(el)
    elif ar.count(el)>maximum and el not in arr:
        arr=[el]*ar.count(el)+arr
        maximum=ar.count(el)
print(arr)
# 6.	На вход подается список уникальных значений (set) и одно число. Необходимо вернуть ближайшее ко входному значение из списка. Если значений два, то нужно вернуть наименьшее. В задаче участвуют только целые числа.
a,n,maxi,mini={1,2,4,5,6},3,set(),set()
for el in a:
    if el>n:
        maxi.add(el)
    elif el<=n:
        mini.add(el)
d=min(maxi)
b=max(mini)
if d-n>=n-b:
    print(b)
else:
    print(d)
# 7.	Необходимо найти количество путей, которыми шашка может пройти в дамки по шахматной доске 8x8, при условии, что двигаться можно только по диагонали вверх. На вход подается две координаты стартовой позиции.
def road(x,y,N):
    if y==8:
        return N
    if x==1:
        return road(2, y+1, N)
    if x==8:
        return road(7, y+1, N)
    return (road(x+1, y+1, N) + road(x-1, y+1, N))
x=int(input("номер строки "))
y=int(input("номер столбца "))
print(road(x,y,1))