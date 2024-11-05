#choose an operation
print('Please enter an option 1-5')
print('   1: Add two numbers')
print('   2: Subtract two numbers')
print('   3: Multiply two numbers')
print('   4: Divide two numbers')
print('   5: Exponentiate two numbers')

z=input('Your choice: ')
print('\n')

print('Please enter the first number')
a=float(input('First number: '))
print('Please enter the second number')
b=float(input('Second number: '))
print('\n')

#if/elif statements to compute the chosen operation
if z=='1':
  c = a+b
  print('a+b=',c)
elif z=='2': 
  c = a-b # your code goes here
  print('a-b=',c)
elif z=='3': 
  c = a*b # your code goes here
  print('a*b=',c)
elif z=='4': 
  if b==0:
    print('Illegal division -- denominator equals zero')       
  else:
    c = a/b # your code goes here
    print('a/b=',c)
elif z=='5': 
  c = a**b # your code goes here
  print('a^b=',c)
else:
  print('Invalid entry')
print("Bye Bye")
