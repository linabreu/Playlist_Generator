#!/usr/bin/env python3

#program allows user to build a playlist

def display_menu():

    print("Welcome to the Playlist Generator")
    print()
    print("Show - Shows current playlist")
    print("Add - Add a song to your playlist")
    print("Remove - Delete a song from your playlist")
    print("Quit - Exit program")

def show(playlist):
    if len(playlist) == 0:
        print("There are no songs in your playlist.\n")
        return
    else:
        i = 1
        for song in playlist:
            print(str(i) + "." + song) #prints: i. song
            i += 1
        #end for
    #endif
    print()

def add(playlist):
    song = input("Name of song: ") #prompt for name of the song
    playlist.append(song) #add it to the playlist
    print(song + " was added to your playlist. \n")#print confirmation message

def remove(playlist):
    song_num = int(input("Please enter a song number: "))
    if song_num < 1 or song_num > len(playlist):
        print("Error. Please enter a valid song number. \n")
    else:
        song = playlist.pop(song_num-1)
        print("This song has been deleted from your playlist.\n")

def main():

    keep_going = True
    playlist = []

    display_menu()
    while True:        
        option = input("Enter what you would like to do to your playlist: ")
        print()
        if option == "show":
            show(playlist)
        elif option == "add":
            add(playlist)
        elif option == "remove":
            remove(playlist)
        elif option == "find":
            find_by_year(playlist)
        elif option == "quit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            
    print("Thank you for using the Playlist Generator")
            

if __name__ == "__main__":
    main()
