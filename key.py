#by qorsan taiz
#"https://github.com/qorsan73"
import os
try :
    import pyfiglet
    import requests
except:
    os.system("clear")
    os.system('pip3 install pyfiglet')
    os.system('pip3 install requests')    
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'

logo = ('             Qorsan ')
print(Z+logo)
print('my namber:', +967737572399)
print('github:' ,"https://github.com/qorsan73")
print('by:' ,"qorsan taiz")
print("\n\033[1;33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
print("Select operation:")
print("1. paylod image")
print("2. paylod APK")
print("3. paylod Audie")
print("4. my youtube ")
print("5. my telegram")
degree = int (input("Enter operation number (1-5): "))

qorsan = ('bash pig.sh')

taiz = ("bash APK.sh")

mostafa = ("bash losiphar.sh")
aldobaei = ()

if degree ==  1:
    print()
    os.system(qorsan)
elif degree ==   2:
    print()
    os.system(taiz)
elif degree == 3:
    print()
    os.system(mostafa)
elif degree == 4:
    os.system("xdg-open https://youtube.com/@hacking-world> /dev/null")
elif degree == 5:
    os.system("xdg-open https://t.me/qorsantaez73/dev/null")
else:
    print("Invalid input!")
