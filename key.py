#by qorsan taiz
#"https://github.com/qorsan73"
from datetime import *

def dan(y=0,m=0,d=0):
 date = datetime.now()
 if len(list(str(y))) == 4:
  if m <= 12 and m > 0:
   if d <= 31 and d > 0:
    if date.year <= y:
     if date.month <= m:
      if date.day < d:
       return True
x = dan(2023,6,8)
     #هنا تخلي تاريخ الايقاف
if x:pass
else:quit(' Bad TM STOB !!!')
print(" God \n Tele : @qorsantaez73")

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
print("3. my youtube ")
print("4. my telegram")
degree = int (input("Enter operation number (1-4): "))

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
    os.system("xdg-open https://youtube.com/@hacking-world> /dev/null")
elif degree == 4:
    os.system("xdg-open https://t.me/qorsantaez73/dev/null")
else:
    print("Invalid input!")
