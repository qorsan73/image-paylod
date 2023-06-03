import os
try :
    import pyfiglet
    import requests
except:
    os.system('pip3 install pyfiglet')
    os.system('pip3 install requests')    
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'

logo = pyfiglet.figlet_format('             Qorsan ')
print(Z+logo)
print(+967737572399)
print("\n\033[1;33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
print("Select operation:")
print("1. on the tool")
degree = int(input("Enter operation number (1): "))
mostafa=os.system("bash run.sh")

if degree ==  1 :
    print(mostafa)
else:
    print("Invalid input!")
