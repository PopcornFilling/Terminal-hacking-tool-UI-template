#    Created by Julius Alexnader Aka linux-fisher
#    age: 15y
#    This was made for my Educational reason, I has eager to learn to make this but i didnt know and still dont know what its called to make this type of stuff in you open to 
#    use in terminal. But im super happy that im able to make one, Im still learning and have a long way to go. I also didthis so people wont call me a script kitty no more.      


#   import things we need!

from termcolor import colored, cprint
import os, time


#   Header
os.system("clear")
cprint("""
          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
         |                                                           |
         |         $print                                            |  
         |         ██╗  ██╗███████╗██╗     ██╗      ██████╗          |     
         |         ██║  ██║██╔════╝██║     ██║     ██╔═══██╗         |   
         |         ███████║█████╗  ██║     ██║     ██║   ██║         |  
         |         ██╔══██║██╔══╝  ██║     ██║     ██║   ██║         |  
         |         ██║  ██║███████╗███████╗███████╗╚██████╔╝         |  
         |         ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝          |   
         |    ██╗    ██╗ ██████╗ ██████╗  ██████╗ ██╗     ██████╗    |   
         |    ██║    ██║██╔═══██╗██╔══██╗██╔═══██╗██║     ██╔══██╗   |   
         |    ██║ █╗ ██║██║   ██║██████╔╝██║   ██║██║     ██║  ██║   |   
         |    ██║███╗██║██║   ██║██╔══██╗██║   ██║██║     ██║  ██║   |   
         |    ╚███╔███╔╝╚██████╔╝██║  ██║╚██████╔╝███████╗██████╔╝   |   
         |     ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═════╝    |                      
         |                                                           |   
          %%%%%%%%%%%%%%%%%%%[MADE BY LINUX-fIsHEr]%%%%%%%%%%%%%%%%%%
          
                         
                         
                          MY FIRST PROJECT FROM FUN AND MY I.S.L 
                                    Version :: 0.00      """, 'red', attrs=["bold"] )
print("\n") 
input("> Press Enter to continue...")
time.sleep(1)
os.system('clear')
def Choosing():
    cprint("Choose Which thing you want to learn about ", 'red', attrs=['bold']) 
    print("  ") 
    print("  1 - Real meaning of SCRIPT KITTY") 
    print("  2 - Best Way to learn Ethical Hacking") 
    print("  3 - My Hacking tool FramDOC")
    print("  4 - Don't be a Jerk bro!") 
    print("  5 - Persional Info") 
    print("") 
    return " "

pcking = True  
while pcking: 
    print(Choosing())
    mod = input("> Select a Input number to see mode... ")
    if mod in ["1", "2", "3", "4", "5"]: 
        pcking = False  
        cprint('[+]> Sorry Nothing yet I need to add more stuff later on in the future... =(', 'green', attrs=['bold'])
        time.sleep(2.30)
        os.system('clear')
    else: 
        os.system('clear')
        input("[!]> Click Enter to try agian...")
        time.sleep(1)
        os.system('clear') 
        pcking = True
