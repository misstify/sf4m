# The script of the game goes in this file.



# Ideally id make a class for characters and their variables

define al = Character('Alex', color="#c8ffc8")
define jo = Character('Jolee', color="#c8c8ff")
define ta = Character('Taylor', color="#c8ffc8")
define th = Character('Thomas', color="#c8c8ff")
define pl = Character('Player', color="#c8ffc8")

# Heart levels to keep track of romance options
init python in heartLevels:
    # 0=gpa_rock, 1=alex, 2=jolee, 3=taylor, 4=thomas
    hearts = {
        1 : 0,
        2 : 0,
        3 : 0,
        4 : 0
    }

    # Find out who your date is at end of game
    def findDate():
        # make sure romance level has hit "dateable" level
        datable = 10
        max_romance = max(hearts.values())
        # If date threshold not met, return gpa_rock code
        if max_romance < datable:
            return 0
        # Otherwise find and return key corresponding to person with highest romance, choosing first person in event of tie
        else:
            for key in hearts:
                if hearts[key] == max_romance:
                    return key
    # Jump to appropriate label for ending, gpa_rock if invalid input given
    def jumpToDate(char_name):
        switch(char_name){
            case 0:
                renpy.jump("gpa_rock_end")
            case 1:
                renpy.jump("alex_end")
            case 2:
                renpy.jump("jolee_end")
            case 3:
                renpy.jump("taylor_end")
            case 4:
                renpy.jump("thomas_end")
            default:
                renpy.jump("gpa_rock_end")
        }

define place1 = int(0) # placeholder "points" variable
define place2 = int(0) # placeholder "points" variable


# The game starts here.
label start:


# Start at sbu play talks to them self
    scene SBU
    with dissolve
    # play music "illurock.ogg"

    pl "words go brrrrr"
    pl "words go brrrrr"
    pl "words go brrrrr"


    menu:
        "Go into forum":
            jump welcome

        "Don't go into room":
            jump leave
    # needs close statement here


# Decides to enter club room
    label welcome:

        scene SF4M
        with dissolve
        # play music "illurock.ogg" fadeout 1.0 fadein 1.0

        pl "words go brrrrr"

        show taylor
        with dissolve

        ta "words"
        pl "words go brrrrr"
        ta "words"

        show taylor at right
        show alex at left
        # play sound "oof"

        al "jumping in with words"
        ta "words"
        pl "words go brrrrr"
        al "words"
        ta "more words"


    menu:
        "Watch something on hulu":
            hide taylor
            hide alex
            jump hulu

        "Watch something on netflix":
            hide taylor
            hide alex
            jump netflix
    # needs close statement here


    label hulu:

            $ place1 += 1
            show thomas

            th "words"

            show alex at right
            show thomas at left

            al "words"

            hide alex
            hide thomas
            jump spiel
    # needs close statement here

    label netflix:

            $ place2 += 1
            show jolee

            jo "words"

            show jolee at right
            show taylor at left

            ta "words"

            hide jolee
            hide taylor
            jump spiel
    # needs close statement here

    label spiel:

        show jolee

        jo "spiel"




# This ends the game.
    return


# Don't enter club
    label leave:
        pl "words go brrrrr"
        " - Lazy Ending"
    return
