# Import the modules needed to run the script.
import sys, os, math, sea_depth_scanner, navigation_controller

def clear_console():
    os.system('cls')
    
def input_data(file_name, mode):
    if mode == 1:
        with open(file_name) as input:
            data = list(map(int, input.readlines()))
    if mode == 2:
        with open(file_name) as input:
            data = list(input.readlines())
    
    return data

# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    choice = math.inf
    while choice != "0":
        clear_console()
        print("Welcome to the Submarine system main menu.\n Please select an option:")
        print("0. Exit")
        print("1. Sea floor depth scanner")
        print("2. Navigation controller")
        
        choice = input(" >> ")
        
        if (choice == "1"):
            sea_depth_scanner_menu()
        elif (choice == "2"):
            navigation_controller_menu()
            
        
def sea_depth_scanner_menu():
    data = input_data("inputs/day-1.txt", 1)
    sds = sea_depth_scanner.SeaDepthScanner()
    
    clear_console()
    print("Select your scan rate:")
    print("1. Slow")
    print("2. Fast")
    
    choice = input(" >> ")
    
    if(choice == "1"):
        sds.slow(data)
    
    if(choice == "2"):
        sds.fast(data)
        
    input("Press any button to continue...")
    
def navigation_controller_menu():
    data = input_data("inputs/day-2.txt", 2)
    nav = navigation_controller.NavigationController()
    
    clear_console()
    print("Select your scan rate:")
    print("1. Standard Mode")
    print("2. Aim Mode")
    
    choice = input(" >> ")
    
    if(choice == "1"):
        nav.standard_mode(data)
    
    if(choice == "2"):
        nav.aim_mode(data)
        
    input("Press any button to continue...")
    
main_menu()
    