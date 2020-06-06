#!/usr/bin/env python3

#program allows user to build a playlist

def display_menu():

    print("Road Trip Playlist Creator")
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
            row = song
            print(str(i) + ". " + row[0] + " by "
                  + str(row[1]))
            i += 1
        #end for
    #endif
    print()

def add(playlist):
    title = input("Name of song: ") #prompt for name of the song
    artist = input("Name of artist: ")
    song = []
    song.append(title)
    song.append(artist)
    playlist.append(song)
    print(song[0] + " was added to your playlist. \n")#print confirmation message

def remove(playlist):
    song_num = int(input("Please enter a song number: "))
    if song_num < 1 or song_num > len(playlist):
        print("Error. Please enter a valid song number. \n")
    else:
        song = playlist.pop(song_num-1)
        print("This song has been deleted from your playlist.\n")

def main():

    
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
            
    print("Thank you for using the RoadTrip Playlist Creator")
            

if __name__ == "__main__":
    main()
