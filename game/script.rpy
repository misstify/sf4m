# The script of the game goes in this file.
# Ideally id make a class for characters and their variables

define al = Character('Alex', color="#c8ffc8")
define jo = Character('Jolee', color="#c8c8ff")
define ta = Character('Taylor', color="#c8ffc8")
define th = Character('Thomas', color="#c8c8ff")
define pl = Character("[name]")

# Initialize placeholder values for characters for ease of use
define gpa_rock = 0
define alex = 1
define jolee = 2
define taylor = 3
define thomas = 4

# Heart levels to keep track of romance options
init python:
    # Initialize heart values
    hearts = {
        "ALEX" : 0,
        "JOLEE" : 0,
        "TAYLOR" : 0,
        "THOMAS" : 0
    }

    # Update heart values
    def updateHearts(char_name, value):
        hearts[char_name] += value

    # Determine final day choice options
    def findDates():
        # Get all values from dictionary
        heart_values = hearts.values()
        # Sort heart values
        heart_values.sort()
        res = []
        # Iterate through keys in hearts to get the two options
        for name in hearts:
            if hearts[name] == heart_values[-1] or hearts[name] == heart_values[-2]:
                res.append(name)
        return res

    # Jump to appropriate label for ending, gpa_rock if invalid input given
    def jumpToDate(char_name):
        if char_name == "GPA_ROCK":
            renpy.jump("gpa_rock_end")
        elif char_name == "ALEX":
            renpy.jump("alex_end")
        elif char_name == "JOLEE":
            renpy.jump("jolee_end")
        elif char_name == "TAYLOR":
            renpy.jump("taylor_end")
        elif char_name == "THOMAS":
            renpy.jump("thomas_end")
        else:
            renpy.jump("gpa_rock_end")

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
            for name in hearts:
                if hearts[name] == max_romance:
                    jumpToDate(name)

define place1 = int(0) # placeholder "points" variable
define place2 = int(0) # placeholder "points" variable

# Go backwards wheeeee
init python in rewind:
    # Stack to store messages
    stack = []
    # Method to initialize stack
    def init_stack(lab):
        stack.append(lab)
    # Method to store messages in stack
    def store_msg(char_name, msg):
        stack.append((char_name, msg))
    # Method to rewind time
    def rewind_msgs():
        while len(stack) != 0:
            # if stack has reached bottom jump to label
            if len(stack) == 1:
                renpy.jump(stack[0])
            # otherwise display message
            else:
                obj = stack[-1]
                renpy.say(obj[0], obj[1])

# The game starts here.
label start:
# Start at sbu play talks to them self
    scene sbu
    with dissolve

    python:
        name = renpy.input("What is your name?", length=32)
        name = name.strip()

        if not name:
            name="Samuel Stanley"

    # Nate's using this to test, feel free to comment out for your testing
    jump finalChoices

    pl "Stony Brook University. Land of the Seawolf, Home of Student Debt. Even though I don't dorm, the student fees are ridiculous but all in the name of pleasing my parents."
    pl "I don't really have a clue how I got into this place considering that I spend most of my time procrastinating and sleeping."
    pl "But here it is right in front of me! Barely a few weeks in and already dying inside."
    pl "I mean-!"
    pl "I'm not failing already or anything, but CSE 101 is harder than I expected. I need something to take the edge off."
    pl "Today is the Involvement fair, or at least, the fair was going on earlier. I mostly showed up because someone posted on the school subreddit that there was a cotton candy machine."
    pl "What can take the edge off more than free food?"

    menu:
        "Go into forum":
            jump welcome

        "Don't go into room":
            jump leave
    # needs close statement here


# Decides to enter club room
    label welcome:

        scene sf4m
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

    # Nate testing ability to choose between two date options
    label finalChoices:
        $ updateHearts("THOMAS", 1)
        python:
            # Grab two options
            options = findDates()
            # Show menu with options
            charChosen = renpy.display_menu([("[options[0]]", "[options[0]]"), ("[options[1]]","[options[1]]")])
            charChosen = charChosen.capitalize()
            # Jump to appropriate label 
            renpy.say(charChosen,"[charChosen]")
            #renpy.jump(charChosen)



# This ends the game.
    return


# Don't enter club
    label leave:
        pl "words go brrrrr"
        " - Lazy Ending"
    return
