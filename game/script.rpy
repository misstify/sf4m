# The script of the game goes in this file.



# Ideally id make a class for characters and their variables

define al = Character('Alex', color="#c8ffc8")
define jo = Character('Jolee', color="#c8c8ff")
define ta = Character('Taylor', color="#c8ffc8")
define th = Character('Thomas', color="#c8c8ff")
define pl = Character('Player', color="#c8ffc8")

init python in heartLevels:
    al_heart = 0
    jo_heart = 0
    ta_heart = 0
    th_heart = 0
    pl_heart = 0

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
