#Write a Python Program for Fibonacci numbers.

def fibo(input_number):
  fibonacci_ls=[]
  for count_term in range(input_number):
    if count_term==0:
      fibonacci_ls.append(0)
    elif count_term==1:
      fibonacci_ls.append(1)
    else:
      fibonacci_ls.append(fibonacci_ls[count_term-2]+fibonacci_ls[count_term-1])
  return fibonacci_ls


number = int(input("Enter how much terms you want?\t:\t"))
ls = fibo(number)
print(ls)

'''
#if you want to print without list type, so in place of print(ls), you can use below lines of code
for item in ls:
  print(item, end=' ')

#in place of define fuction you may also use only for loop
https://github.com/panchaly75/MyCaptainPythonProjects/blob/main/project03.py
in this above github link has same code with for loop
'''

#https://colab.research.google.com/drive/1gK-J2dPT7Cn5HP0EFNJrf0S-6x0pyWki?usp=sharing
