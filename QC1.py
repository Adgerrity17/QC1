#working through part 1 of the quant connect introduction to Fiancial Python

#basic variable types
#string
my_string = 'welcome to '
my_string2 = 'Quantconnect'
print(my_string + '' + my_string2) #a plus can join two strings


my_int = 10
print(my_int)
print(type(my_int))

my_string = '100'
print(type(my_string))
my_int = int(my_string)
print(type(my_int))

my_float = 1.0
print(type(my_float))

my_float= float(my_string)
print(type(my_float))

#Basic math
print('Addition ', 1+1)
print('Subtraction', 5-2)
print('Multiplication', 2*3)
print('Division', 10/2)
print('exponite', 2**2)

#lists
my_list = ['Quant', 'Connect', 1,2,3]
print(my_list)
print(len(my_list))
print(my_list[1])
print(my_list[len(my_list) - 1])
my_list[2] = 'go'
print(my_list)
print(my_list[1:3])
print(my_list[1:])
print(my_list[:3])

my_list = ['Hell0', 'Quant']
my_list.append('Hello')
print(my_list)
my_list.remove('Hello')
print(my_list)

my_tuple = ('Welcome','to','Quantconnect')
print(my_tuple)
print(my_tuple[1:])

stock_list = ['APPL','GOOG','IBM','APPL','IBM','FB','F','GOOG']
stock_set = set(stock_list)
print(stock_set)

#Dictonary
my_dict = {'APPL' : 'Apple', 'FB' : 'Facebook', 'GOOG' : 'Alphabet'}
print(my_dict['GOOG'])
my_dict['GOOG'] = 'Alphabet Co'
print(my_dict['GOOG'])
print(my_dict.keys())


#String opperations
my_str = 'Welcome to QuantConnect'
print(my_str[8:])


practice = ('Counting the number of es in this sentence')
print(practice.count('e'))
print(practice.find('e'))
print(practice.replace('e','a'))

time = '2018-10-24 12:04:00'
splitted_list = time.split(' ')
date = splitted_list[0]
time = splitted_list[1]
print(date, time)
hour = time.split(':')[0]
print(hour)

#formatting
my_time = 'Hour: {}, Minute: {}'.format(9, 43)
print(my_time)

print('pi is %f' % 3.14)
print('%s to %s' % ('Welcome', 'QuantConnect'))