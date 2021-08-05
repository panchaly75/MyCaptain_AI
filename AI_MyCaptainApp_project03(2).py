#Write a Python Program to Print all positive numbers in a range.

int_ls = []
print("Enter how much integers you want ?\t:\t", end='')

for i in range(int(input())):
  value = int(input(f"Enter no. {i+1}\t:\t"))
  int_ls.append(value)

print(list(filter(lambda x : x>0 , int_ls)))




#https://github.com/panchaly75/MyCaptainPythonProjects/blob/main/project04.py
#https://colab.research.google.com/drive/1D2FysNF0ueUoxfv2xvBk4dY4sg_JcPTQ?usp=sharing
