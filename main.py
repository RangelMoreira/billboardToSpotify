from billBoardSongs import BillBoardSongs
from spotfy import Spotify

should_continue = 'y'
while should_continue == 'y':
    date_to_travel = input("Which year do you want to travel? Type the date in this format YYYY-MM-DD ")
    b = BillBoardSongs()
    tracks = b.bring_all_titles(date_to_travel)
    if tracks:
        s = Spotify()
        s.create_list(date_to_travel, tracks)
    else:
        print("Oops, no records found for that date")

    should_continue = input("Do you want to create a new playlist? y/n ")
