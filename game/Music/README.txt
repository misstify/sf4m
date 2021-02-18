Music formating is as follows
play music "<loop 4.0>music/file.oga"

loop will loop the track starting at the specified number of seconds into the track
music/ is pointing the code to this folder
all files are .oga


Each track is looped at different points in the track, the points for each track are
jolee 4.0    play music "<loop 4.0>music/jolee.oga" volume 0.6
alex 10.0    play music "<loop 10.0>music/alex.oga" volume 0.6
taylor 6.5   play music "<loop 6.5>music/taylor.oga" volume 0.6
thomas 0.5   play music "<loop 0.5>music/thomas.oga" volume 0.6
forum 26.766 play music "<loop 26.766>music/forum.oga" volume 0.6
sbu 22.4833  play music "<loop 22.4833>music/sbu.oga" volume 0.6
spooky 3.5   play music "<loop 3.5>music/spooky.oga" volume 0.6


The ending requires the noloop clause since it doesnt loop   play music "music/ending.oga" noloop 

Finally use define config.main_menu_music = "music/mainmenu.oga" to make the start screen have music