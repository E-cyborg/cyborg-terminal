import os
import random

def current_path():
    print(os.getcwd())

def ls():
    path = os.getcwd()
    print("\n", os.listdir(path), "\n")

def banner():
    clear()
    banner1=('''
           ______     _____      _____     ____________            __________         ____________           ___________     
          /  ____|    \    \    /    /    |   ______   \          /  ______  \        |  _______  |         /  _______  \    
         /  /           \  \    /  /      |  |      |  |         /  /      \  \       |  |     |  |        /  /       \  \   
        /  /             \  \  /  /       |  |      |  |        /  /        \  \      |  |     |  |       /  /         \  \  
        |  |              \  \/  /        |  |______|  /        |  |        |  |      |  |_____|  |       |  |         |___| 
        |  |               \    /         |  |______  |         |  |        |  |      |  |___    /        |  |   ______      
        |  |                |  |          |  |      |  \        |  |        |  |      |  |   \  \         |  |   |__   \     
        \  \                |  |          |  |      |  |        \  \        /  /      |  |    \  \        \  \      |  |     
         \  \_____          |  |          |  |______|  |         \  \______/  /       |  |     \  \        \  \_____|  |     
          \ ______|        |____|         |____________/          \__________/       |____|    \____\       \________ _/      
          
        ''')
    banner2=('''
         HELLO! THIS IS A CYBORG TERMINAL 
            DID YOU GET THE PERMISION
              TO USE THIS TEMINAL !!''')
    selected_banner = random.choice([banner1, banner2])
    print(selected_banner)

def clear():
    os.system('cls')

def help():
    clear()
    banner()
    print('''
    This is the help command
           
help        : print this statement
ls          : print the files in the current working dir
pwd         : print the current working path
cd ..       : move to the parent directory
cd path     : change the current working directory to the specified path
exit        : exit the program       
            
''')

def trrying(user):
    try:
        os.system(user)
        print("\n")
    except TypeError as e:
        print("This is not the right command \n")


def changing_dir(path):
    try:
        os.chdir(path)
    except FileExistsError as e:
        print("This path did not exist")
    except FileNotFoundError as e:
        print("This path did not exist")
import nmap




def main():
    clear()
    banner()
    user = "xyz"
    while user.lower() not in ["exit", "e"]:
        current_path()
        print("|--(CYBORG)-> ", end="")
        user = None
        user = input()


        if user.lower() == "exit" or user.lower() == "e":
            exit()
        elif user.lower() == "help" or user.lower() == "h":
            help()
        elif user.lower() == "nmap":
            print("NMAP IS IN WORKING STATUS")
        elif user.lower() == "ls":
            ls()
        elif user.lower() == "banner":
            banner()
        elif user.startswith("cd "):
            path=user.split(" ")[1]
            changing_dir(path)

        else:
            trrying(user)

if __name__ == "__main__":
    main()



