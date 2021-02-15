# The script of the game goes in this file.
# Ideally id make a class for characters and their variables

define al = Character('Alex', color="#c8ffc8")
define jo = Character('Jolee', color="#c8c8ff")
define ta = Character('Taylor', color="#c8ffc8")
define th = Character('Thomas', color="#c8c8ff")
define pl = Character("[name]")
define rj = Character('Egotistical Student', color="#2F2F2F")

# Initialize placeholder values for characters for ease of use
define gpa_rock = 0
define alex = 1
define jolee = 2
define taylor = 3
define thomas = 4

# Heart levels to keep track of romance options
init python in heartLevels:
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
                obj[0](obj[1])

# The game starts here.
label start:
# Start at sbu play talks to them self
    scene sbu
    with dissolve

    python:
        name = renpy.input("Welcome to SBU, what is your preferred name?", length=32)
        name = name.strip()

        if not name:
            name="Samuel Stanley"

# Just using the quotes without an ID is narration. pl will be used for actual dialogue.
    "Stony Brook University. Land of the Seawolf, Home of Student Debt."
    "Even as a commuter, the student fees are ridiculous - but all in the name of pleasing my parents."
    "I don't really have a clue how I got into this place considering that I spend most of my time procrastinating and sleeping."
    "But here it is! The campus, bustling with students new and old. Barely a few weeks in and already dying inside."
    "I mean-!"
    "I'm not failing already or anything, but CSE 101 is harder than I expected. I need something to take the edge off."
    "Today is the Involvement fair, a festival of sorts where all the clubs set up tables and stands to show off to new students."
    "I mostly showed up because someone posted on the school subreddit that there was a cotton candy machine."
    "What can take the edge off more than free food?"
    "Unfortunately, it’s been 15 minutes and the line isn’t moving."
    "As I wait though, I see this tall guy that was screaming about… some kind of club I think?"

    show npc
    with dissolve

    "Come join the Science Fiction Forum! One of the oldest clubs on campus, literally anyone and everyone can fit in!"
    rj "I personally can endorse this club as one of the best, or your money back!"
    rj "Just go down the stairs in the SAC Commuter Lounge and hang a left!"
    "As I look over to the Student Activities Center, I stop and think for a moment."
    "I'd hung out in the Commuter Lounge there before and definitely recall being a bit confused at the loud sounds that came from the basement now and then."
    "Did they really come from some wild book club that was hidden away down there? Maybe I should go check it out."

    hide npc

    menu:
        "Leave the line":
            jump welcome

        "Stay where you are":
            jump leave
    # needs close statement here


# Decides to enter club room
    label welcome:

        "The line for cotton candy hasn’t moved for a good five minutes… it couldn’t hurt to go check this club out while waiting for the line to shrink a bit right?"

        scene forumhallway

        "Heading inside, my cotton candy mission failed, I face a room with a propped open door. It has a black poster saying, ‘SF4M Movie Nights!’ with a collage of superheroes around it."
        "I can hear the sounds of a television playing what I think is Jimmy Neutron? And some voices arguing."

        menu:
            "Hesitate and linger in the hallway":
                jump linger

            "Go inside the room":

                jump inside

# Hesitates before entering the forum
    label linger:

        "As I hear one of the voices hit a peak with a loud cackle and the sound of something being knocked over, I stop myself from fully walking in and look through the doorway."

        scene forummainclapcheeks
        with dissolve

        "Inside I see a bunch of students. A tall pair of students are bickering in front of a television, the beanie’d girl brandishing a playstation controller while a tired-looking boy gestures to a DVD case in his hands."
        "A couch separates them from another guy-girl pair who sit at the table, chatting more calmly… albeit they seem to be eyeing the loud pair."

        show taylor at right

        ta "If I wanted to watch a scaly giant scream at people, I’d go upstairs to the involvement fair and advertise the club with RJ!"

        show alex at left

        al "I haven’t seen Splice and I don’t intend on changing that today!"
        "I have no idea what Splice is, but based on the tired guy’s reaction, can’t be that good of a movie."

        hide taylor
        hide alex
        show jolee

        "The girl from the table turns and looks at me. She’s Asian, a large pair of glasses in front of her squinting eyes as she peers over. It seems more like she just can’t see rather than her being suspicious though."
        jo "Oh hello! Are you new?"
        "The boy next to her looks up from the papers before them and grins."

        show thomas at right

        th "Another person from the involvement fair?"

        show taylor at left

        ta "Spiiiiel! And Alex can’t do it, he messed up last time!"

        hide thomas
        show alex at right

        al "Oh, I messed up? You don’t even do it at all-!"
        pl "Spiel…?"
        "I get my answer as the girl at the table suddenly dives into a prepared speech of sorts."

        hide taylor
        hide alex

        jo "Hello and welcome to the Science Fiction Forum!"
        jo "We are the largest free-lending library on the eastern seaboard with an array of books, board games and movies in the genres of science fiction, fantasy and horror."
        jo "We’re one of the oldest clubs on campus and-"

        show taylor at left

        ta "We got netflix, you can take a nap and the room is basically open into the SAC closes at midnight, come on in."

        jump postspiel

# Goes straight into the forum
    label inside:
        scene forummainclapcheeks
        with dissolve
        # play music "illurock.ogg" fadeout 1.0 fadein 1.0
        # play sound "oof"

        "I walk inside just in time to see a water bottle fly across the room, the girl it’s presumably being aimed at hopelessly failing at catching it while the other girl who threw it cackles as it clatters on the floor."

        show taylor at left

        ta "Come on Jolee, you weren’t even close!"

        show jolee at right

        jo "It’s not my fault I’m blind!"
        "The boy sitting next to the poor-sighted girl picks up her water bottle and places it on the table before he points to a paper on the table."

        show thomas

        th "I’d like to at least decide on what event we should host first before I have to head to my next class…"
        ta "Events are for nerds, just put on a great movie like Splice and we’ll be set."

        hide jolee
        hide thomas
        show alex

        "A tall, tired-looking boy glares at the beanie-wearing girl before he brandishes a DVD case to her."
        al "I haven’t seen Splice and I don’t intend on changing that today!"
        ta "Oh uh… hey look a new person!"
        "She suddenly looks over the boy’s shoulder and points to me, causing everyone’s attention to be redirected to me."
        pl "Uh… hi?"

        show jolee

        jo "Oh hello! Are you new?"
        pl "Yeah, I just heard some guy upstairs talking about this place."
        ta "Ah, the power of RJ screaming never fails us."
        al "Who’s gonna give him the spiel?"
        pl "The spiel?"
        "I get my answer as the girl at the table suddenly launches into a prepared speech of sorts."
        jo "Hello and welcome to the Science Fiction Forum!"
        jo "We are the largest free-lending library on the eastern seaboard with an array of books, board games and movies in the genres of science fiction, fantasy and horror."
        jo "We’re one of the oldest clubs on campus and-"
        ta "We got netflix, you can take a nap and the room is basically open into the SAC closes at midnight, come take a load off."

        jump postspiel

# Recoverge after the Hesitate/Go Inside choice
    label postspiel:

        jo "Taylor, we at least have to make the club sound good."
        ta "Am I wrong though in that most people come here to sleep and watch the latest netflix releases?"
        th "She’s not wrong."
        al "If you’re someone with taste though, we have Hulu also."
        ta "First you insult Splice, now Hulu? That’s two strikes nerd."
        al "First off, Splice is a movie that deserves to be insulted! Second off, Hulu is just better. You don’t see Hulu removing good stuff so often."
        ta "That’s because no one is looking at Hulu to begin with."
        jo "Are you two just constantly looking for things to argue about today?"
        "Taylor turns to look at me and smirks as she points at me once more."
        ta "Yo, new person, what’s your name?"

    menu:
        "I'm [name], but everyone just calls me [name].":
            jump intro1

        "Name's [name].":
            jump intro2

    label intro1:

        "She snickers at my response."
        ta "Nice one."

        jump questioned

    label intro2:

        "She nods her head to me."
        ta "[name], got it, I probably won't remember that."

        jump questioned

# After choosing how you introduce yourself
    label questioned:

        ta "So which do you prefer, Netflix or Hulu?"

    menu:
        "Hulu or bust":
            hide taylor
            hide alex
            jump hulu

        "Netflix all the way":
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
        python in heartLevels:
            # Grab two options
            options = [hearts["ALEX"], hearts["JOLEE"]]
            # Show menu with options
            charChosen = renpy.display_menu([("Alex", "ALEX"), ("Jolee","JOLEE")])
            charChosen = charChosen.capitalize()
            # Jump to appropriate label
            renpy.say(charChosen,"ALEX")
            #renpy.jump(charChosen)



# This ends the game.
    return


# Don't enter club
    label leave:
        "I watch as the guy stands in the way of a nearby student and begins expound on how he’s president of the club and made it great again or something."
        "It’s probably for the best that I just leave it be… right?"
        "Time to wait another 15 minutes for this stupid cotton candy…"

        "Ending A: What if?"
    return
