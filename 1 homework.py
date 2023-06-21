slovo = str(input('Введите слово: '))
n=len(slovo)
k=0
n=n-1
i = 1
while n-i >= i:
    if slovo[i] == slovo[n-i]:
        i+=1
    else:
        k=1
        break
if k==1:
    print('False')
else:
    print ('True')