# working through the second quant connect tutorial with additional practice from Automate the boring stuff
#Logical operations and loops

print(1 == 0) #equals
print(1 == 1)
print(1 != 0) #DNE
print(5 >= 5) #Greater than
print(5 >= 6)

#Boolians
print((2 > 1) and (3 >2))
print((2 > 1) and (3 < 2))
print((2 > 1) or (3 < 2))
print((2 < 1) and (3 < 2))


#If conditionals

i = 0
if i == 0:
    print('true')


p = (1 > 0)
q = (2 > 3)
if p and q:
    print('both true')
elif q and not p:
    print('q is false')
else:
    print('Throne of lies')

Name = input('what is your name: ' ' ') # Automate the boring stuff p 39
if Name == 'Alice':
    print('Hello Alice')
else:
    print('hello stranger')

Name = input('What is your name: ')
Age = input('How old are you: ')
Age = int(Age)

if Name == 'Alice' and Age == 12:  #ABS p 41
    print('Hello Alice')
elif Name != 'Alice' or Age < 12:
    print('Hello young', Name)
else:
    print('Stranger danger')


i = 0
while i < 5:
    i += 1
    print(i)

spam = 0
while spam <= 5:
    print('Spam Spam Spam')
    spam += 1

for x in [1,2,3,4,5]:
    print(x)


stocks = ['APPL', 'GOOG', 'IBM', 'FB', 'F', 'V', 'G', 'GE'] #example from pairs trading algo
Selected = ['APPL', 'IBM']
new_list = []
for stock in stocks:  # type: str
    if stock not in Selected:
        new_list.append(stock)
print(new_list)

for stock in stocks:
    print(stock)
    if stock == 'FB':
        break

squares = []
for i in [1,2,3,4,5]:
    squares.append(i**2)
print(squares)
