#My log names and where all entries will be appended to

game_log = []
movie_log = []
series_log = []

#Name of the file where data will be saved and loaded from
#Imported time to allow me to add a desired delay in seconds
filename = "media_log.txt"
import time

#Created saving method that would save the media entries
#Used "w" and .write to write data to the file
#Used \n for new line so the saved lists are on a diferent lines
#str is to allow the variable to become a string to be saved in the media_log.txt

def save_data(filename):
    with open(filename, 'w') as f:
        f.write(str(game_log) + '\n')
        f.write(str(movie_log) + '\n')
        f.write(str(series_log) +'\n')

#Use .readline() to read each line of code and assign it to it's variable
#Use .strip() to remove any characters or spaces that aren't wanted

#Used eval to interpret what is left of ex. game_log_str after .strip has removed unnecessary
#characters then assigns it to the global variables in game_log, movie_log, and game_log

def load_save_data(filename):
    with open(filename, 'r') as f:
        game_log_str = f.readline().strip()
        movie_log_str = f.readline().strip()
        series_log_str =f.readline().strip()
    global game_log, movie_log, series_log
    game_log = eval(game_log_str)
    movie_log = eval(movie_log_str)
    series_log = eval(series_log_str)
    
#Remaining functions are specificially used for when the user selcts options from menu and sub menus    

#Defined add_game_entry that appends the game_name and game_rating
#Then us save_data function to save to entries into .txt file
#Added a delay for user experiance and apperance
#Added a print statement for user experiance and apperance
    
def add_game_entry():
    game_name = input("Enter game name: ")
    game_rating = input("Enter game rating: ")
    game_log.append((game_name, game_rating))
    save_data(filename)
    time.sleep(1)
    print("Entry was successfully added")
    
#Created a function that would allow user to enter another entry after entry is created
#Used .upper to allow the user to use either upper or lower case "Y"
#Then added my add_game_entry function to route the user back to that function if selecting "Y"
    
def new_game_entry():
    while True:
        adding_new_entry = input("Add another entry? Y/N: ")
        if adding_new_entry.upper() != "Y":
            break
        add_game_entry()

#Defined view_game_log
#Added print statement and delay for user experience and apperance
#Used enumerate to assign a number to the entiers in a list
#Used +1 so the list would start at number 1
#entry[0] refers to name and entry[1] refers to rating

def view_game_log():
    print("Loading...")
    time.sleep(2)
    print("Game Log:")
    for g, entry in enumerate(game_log):
        print(f"{g+1}, {entry[0]} - {entry[1]}")
    print(" ")
        
#All remaining functions for movies and series are the same as game functions above
#Copied and pasted same functions as above from the game catergory to reflect for movies and series

def add_movie_entry():
    movie_name = input("Please enter movie name: ")
    movie_rating = input("Please enter rating: ")
    movie_log.append((movie_name, movie_rating))
    save_data(filename)
    time.sleep(1)
    print("Entry was successfully added")

def new_movie_entry():
    while True:
        adding_new_movie_entry = input("Add another entry? Y/N: ")
        if adding_new_movie_entry.upper() != "Y":
            break
        add_movie_entry()

def view_movie_log():
    print("Loading...")
    time.sleep(2)
    print("Movie Log:")
    for m, entry in enumerate(movie_log):
        print(f"{m+1}, {entry[0]} - {entry[1]}")
    print(" ")
        
def add_series_entry():
    series_name = input("Enter series name: ")
    series_rating = input("Enter series rating: ")
    series_log.append((series_name, series_rating))
    save_data(filename)
    time.sleep(1)
    print("Entry was successfully added")
    
def new_series_entry():
    while True:
        adding_series_entry = input("Add another entry? Y/N: ")
        if adding_series_entry.upper() != "Y":
            break
        add_series_entry()
        
def view_series_log():
    print("Loading...")
    time.sleep(2)
    print("Series Log:")
    for s, entry in enumerate(series_log):
        print(f"{s+1}, {entry[0]} - {entry[1]}")
    print(" ")

#This function is very simiular to the function of view_log function but uses .pop to remove from list
#All delete functions are very similar, copy + paste, just changing what log is attached to .pop
#entry[0] refers to name of content, entry[1] refers to rating
#Used int so user input is interpreted as an integer
#(choice - 1) helps adjust the numerical index
    
def delete_game_entry():
    print("Select the game to delete:")
    for g, entry in enumerate(game_log):
        print(f"{g+1}. {entry[0]} - {entry[1]}")

    choice = int(input("Enter the number corresponding to the game: "))

    deleted_game = game_log.pop(choice - 1)
    print(f"Deleted entry: {deleted_game[0]} - {deleted_game[1]}")

def delete_movie_entry():
    print("Select the game to delete:")
    for m, entry in enumerate(movie_log):
        print(f"{m+1}. {entry[0]} - {entry[1]}")

    choice = int(input("Enter the number corresponding to the movie: "))

    deleted_movie = movie_log.pop(choice - 1)
    print(f"Deleted entry: {deleted_movie[0]} - {deleted_movie[1]}")

def delete_series_entry():
    print("Select the game to delete:")
    for s, entry in enumerate(series_log):
        print(f"{s+1}. {entry[0]} - {entry[1]}")

    choice = int(input("Enter the number corresponding to the series: "))

    deleted_series = series_log.pop(choice - 1)
    print(f"Deleted entry: {deleted_series[0]} - {deleted_series[1]}")
    
def main_menu():
    while True:
        main_menu_input = input("Main Menu? Y/N: ")
        if main_menu_input.upper() != "Y":
            break

#The program loads any data that was previously entered from the save file "medialog.txt"
load_save_data(filename)

#Created my while true loop giving user options to choose from
#Added print statements that have a space to add a line between the lines of code for apperance
#Used "choice" to reference to for the user input

while True:
    print("Options:")
    print(" ")
    print("1. Create new entry")
    print("2. Delete entry")
    print("3. View log")
    print(" ")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Please choose: ")
        print(" ")
        print("1. Video Game")
        print("2. Movie")
        print("3. Series")
        print(" ")
#Use "choice1" to diferenciate from "choice" from first user options if user selected option 1.
#User has options to select from, allowing them different options that route to those specific functions
        choice1 = input("Enter your choice: ")
        if choice1 == "1":
            add_game_entry()
            print(" ")
            new_game_entry()
        elif choice1 == "2":
            add_movie_entry()
            print(" ")
            new_movie_entry()
        elif choice1 == "3":
            add_series_entry()
            print(" ")
            new_series_entry()
#Placed the appropriate delete_entry functions to the different choices
#Placed save_data(filename), after selected media is deleted, the file will save the updated list
    elif choice == "2":
        print("Please choose a log to delete from: ")
        print(" ")
        print("1. Video Games")
        print("2. Movies")
        print("3. Series")
        print(" ")
        choice2 = input("Enter your choice: ")
        if choice2 == "1":
            delete_game_entry()
            save_data(filename)
        elif choice2 == "2":
            delete_movie_entry()
            save_data(filename)
        elif choice2 == "3":
            delete_series_entry()
            save_data(filename)

#If user chose option 3, I used "choice3" to diferenciate from other "choice" options from above
#Once option 3 is selected, they then select which log they would like to view, then going to that function  
    elif choice == "3":
        print("Please choose a log: ")
        print(" ")
        print("1. Video Games")
        print("2. Movies")
        print("3. Series")
        print(" ")
        choice3 = input("Enter your choice: ")
        if choice3 == "1":
            view_game_log()
        elif choice3 == "2":
            view_movie_log()
        elif choice3 == "3":
            view_series_log()
            
#If user selects anything aside from 1,2,3 the user will be prompted with this print statement            
    else:
        print("Option not available: ")
#User is asked if they would like to go to the main menu, if yes the loop will break and start over the while true loop
    main_menu_input = input("Main Menu? Y/N: ")
    if main_menu_input.upper() != "Y":
        break
