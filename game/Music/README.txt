Music formating is as follows
play music "<loop 4.0>music/file.oga"

loop will loop the track starting at the specified number of seconds into the track
music/ is pointing the code to this folder
all files are .oga


Each track is looped at different points in the track, the points for each track are
jolee 4.0
alex 10.0 play music "<loop 10.0>music/alex.oga"
taylor 6.5 play music "<loop 6.5>music/taylor.oga"
thomas 0.5 play music "<loop 0.5>music/thomas.oga"
forum 26.766
sbu 22.4833
spooky 3.5 play music "<loop 3.5>music/spooky.oga"
The ending requires the noloop clause since it doesnt loop

Finally use define config.main_menu_music = "music/mainmenu.oga" to make the start screen have music