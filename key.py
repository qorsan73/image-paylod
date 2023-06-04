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
print('my namber', +967737572399)
print("\n\033[1;33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
print("Select operation:")
print("1. paylod image")
print("2. paylod APK")
print("3. my youtube ")
print("4. my telegram")
degree = int (input("Enter operation number (1): "))

qorsan = ('bash pig.sh')

taiz = ("bash APK.sh")

mostafa = ()
aldobaei = ()

if degree ==  1:
    print()
    os.system(qorsan)
elif degree ==   2:
    print()
    os.system(taiz)
elif degree == 3:
    print(mostafa)
elif degree == 4:
    print(aldobaei)
else:
    print("Invalid input!")
