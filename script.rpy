# The script of the game goes in this file.
# Ideally id make a class for characters and their variables

define al = Character('Alex', color="#FFFF32")
define jo = Character('Jolee', color="#FFAE19")
define ta = Character('Taylor', color="#E50000")
define th = Character('Thomas', color="#66B2FF")
define pl = Character("[name]")
define rj = Character('Egotistical Student', color="#FFFFFF")
define mv = Character('Mysterious Voice', color="#FFFFFF")
define gpa = Character("GPA Rock", color="#FFFFFF")

#Main menu music
define config.main_menu_music = "music/mainmenu.oga"

# Initialize placeholder values for characters for ease of use
define gpa_rock = "GPA_ROCK"
define alex = "ALEX"
define jolee = "JOLEE"
define taylor = "TAYLOR"
define thomas = "THOMAS"
define jmp = "JMP"
define msg = "MSG"
define scn = "SCN"
define shw = "SHW"
define hde = "HDE"
define has_rewinded = False

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
        # sort result
        res.sort()
        # jump to appropriate label
        renpy.jump(res[0]+res[1])
        return res

    # Find out who your date is at end of game
    def findDate(char_name):
        romance_level = hearts[char_name]
        # If date threshold not met, return gpa_rock code
        if romance_level < 5:
            return char_name.lower()+"_gpa_rock_end"
        # Otherwise find and return key corresponding to person with highest romance, choosing first person in event of tie
        else:
            renpy.jump(char_name.lower()+"_end")

# Go backwards wheeeee
    # Stack to store messages
    stack = []

    # Method to do action based on object type
    def run_action(action):
        # Check type of message stored
        if action[0] == "MSG":
            renpy.say(action[1].capitalize(), action[2])
        elif action[0] == "SCN":
            renpy.scene()
            renpy.show(action[1])
        elif action[0] == "SHW":
#            if action[2]:
#                renpy.show(action[1], action[2])
#           else:
            renpy.show(action[1])
        elif action[0] == "HDE":
            renpy.hide(action[1])
        elif action[0] == "JMP":
            renpy.jump(action[1])
    # Method to store messages in stack
    def store_action(category, *args):
        action = []
        action.append(category)
        for arg in args:
            action.append(arg)
        # Do action before storing
        if len(stack) != 0:
            run_action(action)
        # Add tags to text to speed up CPS
        if action[0] == "MSG":
            action[2] = "{cps=150}" + action[2] + "{/cps}{nw}"
        # Add action to stack
        stack.append(action)
    # Method to rewind time
    def rewind():
        while len(stack) != 0:
            # Grab last object on stack
            obj = stack.pop()
            run_action(obj)

# The game starts here.
label start:

    scene sbuoutside
    with dissolve
    play music "<loop 22.4833>music/sbu.oga" volume 0.6

    # Nates testing cheaty jump
    $ name = "test"
    jump alex_end

    python:
        name = renpy.input("Welcome to SBU, what is your preferred name?", length=32)
        name = name.strip()

        if not name:
            name="Samuel Stanley"

# Just using the quotes without an ID is narration. pl will be used for actual dialogue.

    scene monday
    "..."

    scene sbuoutside

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
    "Come join the Science Fiction Forum! One of the oldest clubs on campus, literally anyone and everyone can fit in!"
    rj "I personally can endorse this club as one of the best, or your money back!"
    rj "Just go down the stairs in the SAC Commuter Lounge and hang a left!"
    "As I look over to the Student Activities Center, I stop and think for a moment."
    "I'd hung out in the Commuter Lounge there before and definitely recall being a bit confused at the loud sounds that came from the basement now and then."
    "Did they really come from some wild book club that was hidden away down there? Maybe I should go check it out."

    menu:
        "Leave the line":
            jump welcome

        "Stay where you are":
            jump endinga
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

        $ta = "???"
        $al = "???"
        $th = "???"
        $jo = "???"

        "As I hear one of the voices hit a peak with a loud cackle and the sound of something being knocked over, I stop myself from fully walking in and look through the doorway."

        scene forummainclapcheeks
        with dissolve
        play music "<loop 26.766>music/forum.oga" volume 0.6

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

        show thomas at right

        "The boy next to her looks up from the papers before them and grins."
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
        play music "<loop 26.766>music/forum.oga" volume 0.6
        $ta = "???"
        $al = "???"
        $th = "???"
        $jo = "???"

        "I walk inside just in time to see a water bottle fly across the room, the girl it’s presumably being aimed at hopelessly failing at catching it while the other girl who threw it cackles as it clatters on the floor."

        show taylor at left

        ta "Come on Jolee, you weren’t even close!"

        show jolee at right

        jo "It’s not my fault I’m blind!"

        show thomas

        "The boy sitting next to the poor-sighted girl picks up her water bottle and places it on the table before he points to a paper on the table."
        th "I’d like to at least decide on what event we should host first before I have to head to my next class…"
        ta "Events are for nerds, just put on a great movie like Splice and we’ll be set."

        hide jolee
        hide thomas
        show alex at right

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

        hide taylor
        hide alex

        jo "Hello and welcome to the Science Fiction Forum!"
        jo "We are the largest free-lending library on the eastern seaboard with an array of books, board games and movies in the genres of science fiction, fantasy and horror."
        jo "We’re one of the oldest clubs on campus and-"

        show taylor at left

        ta "We got netflix, you can take a nap and the room is basically open into the SAC closes at midnight, come take a load off."

        jump postspiel

# Recoverge after the Hesitate/Go Inside choice
    label postspiel:

        $ta = "???"
        $al = "???"
        $th = "???"
        $jo = "???"

        jo "Taylor, we at least have to make the club sound good."
        ta "Am I wrong though in that most people come here to sleep and watch the latest netflix releases?"

        show thomas at right

        th "She’s not wrong."

        hide thomas
        show alex at right

        al "If you’re someone with taste though, we have Hulu also."
        ta "First you insult Splice, now Hulu? That’s two strikes nerd."
        al "First off, Splice is a movie that deserves to be insulted! Second off, Hulu is just better. You don’t see Hulu removing good stuff so often."
        ta "That’s because no one is looking at Hulu to begin with."
        jo "Are you two just constantly looking for things to argue about today?"
        "Taylor turns to look at me and smirks as she points at me once more."

        hide jolee
        hide alex
        hide taylor
        show taylor

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

        $ta = "???"
        $al = "???"
        $th = "???"
        $jo = "???"

        ta "So which do you prefer, Netflix or Hulu?"

    menu:
        "Hulu or bust":
            jump hulu

        "Netflix all the way":
            jump netflix
    # needs close statement here

    label hulu:

            $ta = "???"
            $al = "???"
            $th = "???"
            $jo = "???"

            show alex at right

            al "A-ha! Take that, 'nerd'!"
            "The tired boy seems invigorated as the girl gives me an annoyed glare before she just grabs a pillow off of the couch."
            ta "I'm hitting one of you with this, choose wisely fools."
            al "Ha, I'll happily take the blow to protect the new member actually being cultured."

            hide alex
            hide taylor

            jump split
    # needs close statement here

    label netflix:

            $ta = "???"
            $al = "???"
            $th = "???"
            $jo = "???"

            ta "Ha, see, new guy got taste."

            show alex at right

            al "You don't even own Netflix!"
            ta "I don't need it when I can mooch off of you guys though."
            "The girl at the table groans."

            show taylor at left
            show jolee

            jo "Taylor why?"
            ta "Taylor yes."

            hide alex
            hide jolee
            hide taylor

            jump split
    # needs close statement here

# Post Hulu/Netflix but before the first split
    label split:

        "Taylor falls back on the couch, hugging onto a giant blue couch pillow as the boy at the table speaks up, waving a hand at me."

        show thomas

        $th = "Thomas"
        $ta = "Taylor"
        $al = "Alex"
        $jo = "Jolee"

        th "[name] was it? Nice to meet you. I’m Thomas."

        show jolee at left

        jo "Oh, and I’m Jolee! Over there is Taylor and Alex."

        show alex at right

        al "Hiya."
        pl "Nice to meet you all."
        jo "This is just an open room, so feel free to sit and relax or go and come back later."
        al "Maybe if you go and come back, there will actually be something on the TV by then."
        pl "It’s alright, I don’t have class for a bit anyway."

        hide jolee
        show taylor at left

        ta "Are you a resident or commuter?"
        pl "Commuter. Take the train here. Getting a car on campus seems like a lot honestly."
        th "Ah, it kind of is but if you need help I can walk you through it. I just moved my truck to one of the other parking lots earlier."
        pl "You had to move parking lots…?"
        th "Yeah, all in the name of not getting tickets."
        ta "Imagine not going into copious amounts of debt to stay in a dirty little room with someone else."

        hide thomas
        show jolee

        jo "You are here on basically full scholarship and you’re the reason our dorm is dirty."
        ta "...I plead the fifth."
        "As Taylor and Jolee begin to banter, I look and see Alex trying to lean over and take a controller off from the table."
        "Taylor seems to follow my gaze and suddenly hits Alex with a pillow."
        ta "Don’t try to grab the remote when I’m not looking, you’re not sneaking anything on!"
        al "The silence is deafening and I’m shiftholder so I can overrule you."
        ta "That insinuates I respect your authority."
        "The two of them start bickering again, Jolee offering me an apologetic smile before she goes back to talking to Thomas about the papers they seem to be writing on."
        "Maybe I should go talk to one of these pairs."

        hide jolee
        hide taylor
        hide alex

    menu:
        "Go over to Taylor and Alex":
            jump taconvo

        "Go over to Jolee and Thomas":
            jump jtconvo
    # needs close statement (i don't know why we put these here but ok)

# Talking to Taylor and Alex
    label taconvo:

        scene forumalt
        with dissolve

        show taylor at left
        show alex at right

        ta "I reject your reality and substitute my own."
        al "You are not even in this reality."
        "The two of them are still going at it even as I walk over, with no sign of stopping."
        ta "Oh, hey [name]. Care to contribute a vote to the Splice Party?"
        pl "What exactly is Splice?"
        al "An awful movie, don’t look it up."
        ta "I’d look it up for you but I’m not trying to get a mature rating y’know?"
        al "You’re not mature at all."
        pl "If it’s that bad a movie, why do you want to put it on?"
        al "She always suggests Splice whenever we aren’t sure what to put on the tv."
        ta "They put a limit on me, but because the semester just started I haven't used my splice ticket for this month and can still ask to put it on."
        al "And you can do that when I’m not here. Just let me enjoy my Godzilla."
        ta "Hm… I mean I could, but where’s the fun in that?"
        "Alex looks at Taylor as if he wants to strangle her but she doesn’t even falter as she fiddles with the controller in her hands."

        menu:
            "Taylor, just let Alex put on his Godzilla":
                jump godzilla

            "Alex, just let Taylor put on Splice.":
                jump splice

        label godzilla:

            $ updateHearts("ALEX", 1)

            pl "Taylor, just let him put on Shin Godzilla."
            pl "I don’t want my first movie in here to be some creepy, r-rated flick anyway."
            "Taylor pouts while Alex seems revitalized, holding a hand out for the controller."
            al "Two against one Taylor."
            "She makes a whole show of rolling her eyes and dramatically smacking the controller in his hand."
            ta "Fine, I suppose I’ll just have to torment you all later."
            ta "I totally will start with you though [name]."
            pl "I am quaking in my boots."
            "Alex snorts before he goes to put the DVD in."
            al "You can sit on the couch if you want though [name], come watch with us."
            ta "Just treat the couch like a child you don’t abuse."

            jump taconvo2

        label splice:

            $ updateHearts("TAYLOR", 1)

            pl "Alex, just let Taylor put on Splice."
            pl "She said herself that you all apparently limit her to only being able to do it once a month."
            pl "So if she does it now, she won’t be able to put it on for awhile, right?"
            "Alex grimaces at my logic."
            al "I mean… you’re not wrong."
            "Before he can put his DVD down though, Taylor busts out laughing."
            ta "Oh my gods, did- did you really just convince him to watch Splice? Jesus, [name], you’re great."
            ta "I was just messing with him, I wasn’t actually going to put it on."
            al "Why must you torture me?"
            ta "Because it’s fun. Now put on your Godzilla before I change my mind and make us watch Spiderverse for the 10th time this week instead."
            "As Alex goes to put the DvD into the playstation, Taylor waves her hand towards me."
            ta "You, new nerd, come chill out with us, you get the honor of sitting on the couch. Just treat it like a child you don’t abuse."

            jump taconvo2

# The Taylor-Alex conversation continues post-movie choice
    label taconvo2:

        pl "A child I don’t…?"
        ta "You see this futon thing on the floor against the wall?"
        pl "Yeah… is that someone sleeping on it?"
        al "That’s Mike, he sleeps here a lot, don’t worry about it. We just wake him whenever he has class."
        ta "Somehow we learn his class schedule before our own honestly."
        pl "That’s nice of you."
        ta "Yeah, he's a nice guy."
        ta "But basically, this futon used to be the old forum couch. The first time someone sat on it though it collapsed under their weight."
        pl "...The couch was to blame for that one, right?"
        ta "Oh nah yeah, it was a cheap couch, the forumite wasn't a former character on 'My 600-pound life' or anything."
        "Alex sits on the opposite end of the couch, leaving the spot in the middle open. I sit down between the two of them as he starts up the DVD."
        al "Yeah well, I wouldn’t recommend napping here unless you want a certain someone going through your phone."
        ta "I have no idea who you’re talking about."
        ta "On a completely unrelated note though [name], we have this awesome phone charging port if you want to charge your phone."
        al "Leave your phone unattended at your own risk."
        "Looking down at my phone, it’s at 50 percent so it could use the charge before class. Plus, it’s locked."
        "I pass it over, watching as Taylor plugs it into the mess of blue led lights and wires."
        ta "It won’t explode, promise."
        pl "I didn’t think it would."
        al "Alright, Godzilla time!"
        ta "I wish I had popcorn to throw at the screen."
        al "Shh, it’s going to start."
        "I chuckle at the two of them before settling back into the couch and looking over at the television as the movie begins."

        jump endday1

# The Jolee-Thomas conversation begins
    label jtconvo:

        show jolee at left
        show thomas at right

        jo "We just have the leftover yarn from last semester’s event taking up so much space, I want to get rid of it."
        th "Yes, but we can do that event at any time, being able to get everyone together for a gaming event will be harder if we wait until later in the semester when midterms kick off."
        "Compared to the other two, this calm discussion is a welcome diversion."
        jo "Oh, hey [name]. You can sit and set up your laptop if you want, there’s a power-strip under the table."
        th "Don’t mind us, we’re just trying to organize some events for the club, both of us are eboard members."
        pl "Oh eboard? That means you guys help run the club right?"
        th "Correct. Jolee is the treasurer and I’m historian."
        pl "I haven’t heard of ‘historian’ being a big position in a club before."
        jo "The forum has a president, vice president and all that though, but we have some other positions to help run things."
        jo "I wasn’t kidding in the spiel, we are one of the oldest clubs on campus!"
        pl "That’s crazy honestly."
        th "The story as to why is kind of funny, but we really should get this done before I start reciting old forum events."
        jo "Right, right, sorry, I keep getting distracted…"
        pl "What are you guys stuck on?"
        th "We have an Events Coordinator who's usually supposed to handle it, but she’s…"
        "Thomas looks over to Taylor who is currently laughing maniacally as she rips Alex’s cap off of his head and throws it on top of one of the cabinets."
        pl "...I see the issue."
        th "Yeah. So we have two events already planned out right now. A gaming night, and a crochet night, it’s just a matter of which to hold first."
        jo "I just think having people crochet little hearts would be a bit more appropriate to Valentine’s Day than playing the Untitled Goose Game."
        th "I don't care less about the holiday, I just want to see some geese creating chaos."
        pl "You don’t strike me as the chaotic type Thomas."
        th "I am a simple man who likes geese is all."
        jo "I don’t enjoy the holiday either but it’s about what’s fitting."
        th "...What if we have a crochet event for Saint Patrick’s day instead?"
        jo "Thomas!"

        menu:
            "I think Jolee's right, crochet night is better.":
                jump crochet

            "I think Thomas's right, gaming night is better.":
                jump gaming

        label crochet:

            $ updateHearts("JOLEE", 1)

            pl "I think Jolee is right, a crochet night is more fitting for Valentine’s day."
            pl "Being able to knit little hearts and presents for people sounds really nice."
            "Jolee lights up with a surprised smile as she looks over at me."
            jo "You really think so?"
            pl "Yeah, definitely."
            th "Yeah, I guess that does kind of trump my idea… what if I make the goose my valentine though-"
            jo "Thomas."
            th "Right, right, we can schedule it next month."

            jump jtconvo2

        label gaming:

            $ updateHearts("THOMAS", 1)

            pl "I think Thomas is right, a gaming night would be a nice break from all the lovey-dovey stuff."
            pl "Not to mention he did say before that it’s harder to host this kind of event later because people will have midterms and such."
            th "See, [name] agrees with my logic."
            jo "I mean, if you both really think so then yeah, we can hold the gaming event now and the crochet event later."
            "Jolee awkwardly gathers up her papers while Thomas grins over at me, nodding."
            th "Does that mean I’ll see you there then? It’ll probably be held over the weekend through our discord."
            pl "Oh, uh, totally, I just have to be invited to the discord."
            th "Sure, just add me on discord. It’s Geesegun#0601."
            pl "You.. really like geese huh?"
            th "I said it once, I’ll say it a million times - I am just a simple man who likes geese."

            jump jtconvo2

# The Jolee-Thomas conversation continues post-choice
    label jtconvo2:

        jo "Thanks for the tie-breaker vote though [name]. Even if we don’t go full into arguments like the other two, we can get really stuck sometimes."
        pl "It’s no sweat, I’ll happily break any others you have if you need me to."
        pl "How come the other eboard members don’t help vote on things though?"
        th "Well our president, RJ, is upstairs barking at the involvement fair."
        jo "Our Vice President and Secretary, Ken and Angela, are both studying abroad together in Norway and timezones make it hard for them."
        th "And like I said, our actual Coordinator…"
        ta "I will fight this to the grave, I have nothing to live for anyway!"
        al "Just give me the controller!"
        jo "I’ll uh, go settle those two actually."

        hide jolee
        hide thomas
        show thomas

        "Jolee goes over to the couch as Thomas shrugs."
        th "Club’s a bit empty because of all this but, it’s home, y’know?"
        pl "I definitely can see why people don’t stick around, but I can see plenty of reasons why I’d want to stick around though."
        th "Heh, glad you’re enjoying our insanity."

        hide thomas
        show taylor at left
        show jolee
        show alex at right

        ta "I will not yield!"
        jo "I will buy you ramen if you do."
        ta "...I have been bribed."
        al "Really, you accept her bribes but not mine?!"

        hide taylor
        hide jolee
        hide alex
        show thomas

        th "Care to watch the movie?"
        pl "Huh?"
        "I look away from the chaotic scene to look back over at Thomas who seems to be looking at me with an almost analytical eye."
        th "Me and Jolee have to fill out the rest of this paperwork for the events, just thought you’d have a better view of the movie from on the couch."
        pl "Oh uh, I guess. You guys don’t need any more help?"
        th "Nah, once we get past our stubbornness, we can get things done pretty quickly around here."
        pl "I’ll take your word for it."
        "Jolee groans as she sits back down at the table."

        show jolee at left

        jo "Children, all of you are children."
        th "Yes, children who need to be advertised to if we plan on having either of these events be a success. Let’s get these event applications done."
        jo "Right, right."
        pl "I’ll talk to you guys later then."
        jo "Oh, see ya [name]."
        th "Later."
        "I go over to the couch to join the movie screening."

        hide jolee
        hide thomas

        scene forumalt

        show taylor at left
        show alex at right

        pl "Care for another viewer?"
        ta "Nah, feel free to sit."
        al "We’re finally watching Godzilla like I wanted."
        ta "Oh hush nerd, you just got Jolee on your side."
        al "And I’ll do it again. Godzilla time. [name] come join us."
        ta "Shh, the stupid monster flick is starting."
        "I sit between the two of them, leaning back on the couch as we all turn our attention to the movie."

        jump endday1

# Ending Scene of Day 1
    label endday1:

        scene timeskip
        " "
        scene forumalt

        "As the movie’s credits roll, I look over to see Taylor asleep, hugging onto the blue couch pillow, while Alex is grinning, more awake than ever."
        "Before he can say anything though, my phone’s alarm starts going off."

        show taylor at left

        ta "Huh, what, morning already?"

        show alex at right

        al "Phone call?"
        "I lean forward to check and my eyes bulge at the time."
        pl "Shit, that’s my alarm for class, I should go."
        al "Ah, definitely don’t want to be late for that, see you dude."
        ta "Hmm.. yeah, bye…"
        "I look away from Alex and the half-awake Taylor to wave to the still-working Jolee and Thomas."
        pl "Bye guys!"

        hide taylor
        hide alex
        show jolee at left
        show thomas at right

        jo "Have fun in class!"
        th "Later."
        "I jog out of the forum… I might stop by again tomorrow."

# Beginning of Day 2

    label tuesday:

        scene tuesday
        "..."

        scene sbuoutside
        with dissolve
        play music "<loop 22.4833>music/sbu.oga" volume 0.6

        "Dawn of the Second Day… or at least the afternoon of it."
        "I walk out of the SAC cafeteria, stomach full of mediocre food and an hour left before my next class starts."
        "As I go to leave the building, I pause for a moment."
        "Rather than go sit in the library and play on my phone there is a different place I could go…"
        "Turning away from the outside world, I head downstairs to the basement of the SAC, popping my head into the forum."

        scene forummainclapcheeks
        with dissolve
        play music "<loop 26.766>music/forum.oga" volume 0.6

        show taylor at left
        show jolee

        ta "...and then I’ll change his profile picture to a catgirl so if he wants to try and get his account access back from me, he’ll have to admit that his tinder account is the one advertising itself as a catgirl."
        jo "...’owo’?"
        ta "Yes, ‘owo’."
        pl "Am I interrupting something?"
        ta "Oh hey [name]! Nah, nothing besides the usual plans for world domination."
        "Taylor and Jolee are sitting together at the back tables. Thomas silently looks up and nods to me while Alex waves from the couch."

        show alex at right

        al "Hey [name]!"
        jo "Glad to see we didn’t scare you away."
        pl "Nah, this seems like a nice place to hang out."
        ta "It’s the aura of Valentine’s day, it causes single people to all congregate together."
        al "What better place for us to all be than a basement?"
        ta "Exactly! Let our lack of romantic luck flow through you!"
        "I go over to the table, sitting down in one of the free chairs as I look at everyone."
        pl "What, does this club have a singles curse?"
        al "I mean, we are a bunch of weebs and nerds sitting in a basement."
        th "The club does have a few curses, but being single isn’t one of them."
        ta "I’m trying to curse some people this year, but only to buy me some discount chocolate."
        jo "Of course you are Taylor."
        ta "What? You don’t like V-day either."
        al "I believe you mean National Singles day."
        pl "Well I mean, I…"

        hide jolee
        hide alex
        hide taylor

        menu:
            "Hate it.":
                jump vjolee

            "Get depressed from it.":
                jump valex

            "Am hoping for love.":
                jump vnone

            "Don't care.":
                jump vtom

            "Can't  wait to buy discount chocolate.":
                jump vtaylor

    label vjolee:

        $ updateHearts("JOLEE", 1)

        show taylor at left
        show jolee
        show alex at right

        pl "...I hate Valentine’s day honestly."
        ta "Damn, man’s got strong feelings about the capitalist holiday."
        pl "I’ve just never been able to enjoy it honestly, not even when I was younger."
        jo "It’s alright [name]!"
        "I look over to find Jolee offering me a kind smile."
        jo "Valentine’s day is actually my parent’s anniversary so it’s never been the happiest day for me either."
        jo "Nothing kills the fun of it than having to always spend it planning surprises and presents for other people you know?"
        pl "Yeah, I definitely get how that could ruin your taste for the day."
        jo "It’s alright, I’m still happy to try and organize events and such for the club - I can at least enjoy what goes on here."
        al "What even are we doing this year?"
        ta "As the Event Coordinator, I still say that we should just spend all the budget that would go towards an event on buying out the entire Valentine’s aisle at CVS."
        ta "We all can feast on the chocolate as we watch panicked husbands come in to get last minute gifts and sell them the flowers we have at a mark-up."
        jo "As Treasurer, I still say that’s not happening. Also, I think that last part is illegal."
        al "Even if not, it’s still wrong."
        "I meet Jolee’s eyes as she glances back over, smiling slightly as she rolls her eyes at Taylor continuing to try and defend the idea."
        th "We put in the applications for both of our upcoming events so hopefully we can start advertising them and get them approved."
        al "I don’t care which one we went with honestly, it’s not like we had any plans."

        jump prehistory

    label valex:

        $ updateHearts("ALEX", 1)

        show taylor at left
        show jolee
        show alex at right

        pl "...I get depressed around this time every year honestly."
        jo "Don’t enjoy being reminded about how single you are?"
        ta "Well at least he doesn’t have to see Angela and Ken being lovey-dovey this time around, the lovebirds are studying abroad together!"
        al "Don’t worry [name], I get you."
        "I look over to find Alex completely turned on the couch, nodding to me with an understanding expression."
        al "Valentine’s day has never exactly been the happiest time of the year for me either."
        pl "Did something bad happen when you were younger?"
        al "Ah… story for another time."
        ta "Well, you can get the joys of experiencing it with us."

        hide alex
        show thomas at right

        th "That isn’t exactly going to be making him any happy memories Taylor."
        ta "Well it makes me happy to see you all suffer so I say we should open the forum on the weekend."
        jo "You don’t get up before 3 on the weekend Taylor."
        ta "When I said ‘we should open the forum’, I meant all of you do and I come watch later."
        "I catch Alex’s eye as he looks from everyone else over to me from his spot on the couch. His usually tired expression seems to perk up for a moment as he grins at me before looking back at the others."
        th "This is why you don’t have a room key."
        ta "You all are just afraid of me growing too powerful."

        hide thomas
        show alex at right

        al "Ah yes, that’s it and not you skipping every GBM meeting."
        ta "GBM meeting is a redundant phrase so your point is invalid, hush."

        hide alex
        hide taylor
        hide jolee

        jump prehistory

    label vnone:

        show 4pspread

        pl "...I’m honestly hoping for love this year. I don’t know, I’m feeling optimistic."
        th "Nothing wrong with optimism I guess."
        ta "If you get crushed by whoever you plan on confessing to dude, I will happily take whatever chocolate you buy for them on their behalf."
        "I look between everyone only to find that no one seems to agree with my perspective on this."
        jo "It’s alright [name], if you have someone you care about and want to confess to, I’d say get it over with and do it quickly."
        jo "A lot of people have anxiety about it, but… I mean, it helps to not dwell on it."
        ta "That’s too wholesome for me, change the channel on that one Jolee."
        jo "Go grab the remote and put something on yourself."
        ta "But laaaaazy."
        jo "Not my problem."
        "Taylor groans as she sinks into her chair, looking at her laptop screen."

        jump prehistory

    label vtom:

        $ updateHearts("THOMAS", 1)
        show 4pspread

        pl "...I don’t care to be completely honest."
        pl "Not from a ‘oh it’s all about selling chocolate perspective’, but I just can’t find myself getting all worked up about a random day when you just have to confess to someone, or else."
        th "I can agree with that view honestly."
        "I look over to find Thomas looking over his now-closed laptop, nodding at me with the corners of his lips just slightly upturned."
        th "I could care less about all this. I’ll accept the discounted chocolate and free candy, but beyond that I’m good."
        jo "I can get that, but I’ve been stuck dealing with too many anniversary dinners to be so nonchalant."
        al "Your parents anniversary?"
        jo "Yup, they got married on Valentine’s day and it’s been haunting me my entire life."
        ta "Look at the bright side, you technically won the adoption lottery by getting stuck with us."
        jo "I did?"
        al "Yeah, I’ll beg to differ on that one."
        "Thomas and I both look back at each other as the others begin chatting about Jolee’s family."
        "He offers me a shrug before smirking more prominently and turning to watch them once more."
        jo "I mean, the food here is better in China, albeit not by much."
        ta "Stony Brook is a province of China by some definitions, it’s like you never left!"
        th "By the Urban Dictionary you mean."
        ta "Close enough, it’s a dictionary."

        jump prehistory

    label vtaylor:

        $ updateHearts("TAYLOR", 1)

        pl "...I honestly just am waiting to buy some discount chocolate after all this."

        show taylor at left

        ta "My dude!"
        pl "I look over at Taylor immediately holds up her hand for a high-five towards me, smacking her hand on instinct as she laughs."
        ta "Forget the romance, this is a holiday of sugar highs and money lows!"

        show alex at right

        al "Your money is always ‘low’."
        ta "Hence why I’m currently figuring out how to blackmail RJ by holding his discord account ransom until he gives me some chocolate."

        show jolee

        jo "Damn Taylor, if you want someone to confess to you that badly, there’s a whole anime club down the hall that would love to have a female member."
        ta "Oh shut up, I’m in this for the food."
        "Taylor’s cheeks turn slightly red as she turns away from Jolee to look at me."
        ta "[name], you said you had a car right?"
        pl "I do but I take the train to campus."
        ta "Dammit! My quest for chocolate continues…"

        hide jolee
        show thomas
        "She turns to look at Thomas."
        th "...No."
        "She pouts and turns away."

        jump prehistory

# Conversation between Vday choice and Forum History Choice
    label prehistory:

        hide jolee
        hide thomas
        hide alex
        hide taylor
        show 4pspread

        "The conversation falls into a lull for a moment as we all look back at our screens."
        "I unlock my laptop and click through Blackboard, checking my class notifications."
        "One of the chairs suddenly squeaks, and I look up to see Taylor standing up with a groan, dragging herself around the couch."
        "She completely faceplants on it, flopping next to Alex who seems unbothered enough that this is probably normal."
        jo "You okay there T?"
        "Taylor gives a muffled response into a pillow."
        al "Said she’s bored I think."
        jo "Didn’t you have some homework due?"
        "Her head appears over the back of the couch, looking over at us."
        ta "Yeah, I have to interview people who can talk about what Stony Brook was like pre-2000."
        pl "Interview?"
        ta "I am the rare humanities major here, studying Journalism."
        pl "Ah, yeah Stony Brook is a pretty STEM-focused school. Is everyone else here studying STEM courses?"
        th "I’m physics, mostly astronomy-related stuff."
        al "Same - on the physics part, not the astronomy one."
        jo "And I’m biomedical engineering and loving it."
        "Jolee’s deadpan expression hints to her sarcasm."
        ta "[name], you’re new right? You haven’t heard any forum stories yet."
        pl "What kind of stories?"
        "Taylor grins as she looks over at Thomas. The boy seems to feel her gaze and sighs."
        th "You can’t always use the club for all of our journalism articles Taylor."
        ta "But hypothetically if you were to tell [name] some stories and I just happened to write it down as something I heard on campus…?"
        al "Your ability to avoid doing work astonishes me sometimes,"
        ta "You’ve known me for what, two years now? Why is this still surprising?"
        "Taylor scrambles up from the couch and goes back to her laptop, rapidly typing as she looks expectantly at me and Thomas."
        ta "Well?"
        th "...[name], is there something that you want to know about the forum?"
        pl "I don’t even know what kind of stories there are."
        jo "You could just show him the museum Tom."
        pl "You guys have a museum?"
        al "We call it the museum, but it’s just this."
        "Alex leans over the couch and gestures to the short cabinet resting against it."
        th "I mean, it’s either that or the logbooks."
        ta "The logbook we have out right now only has quotes and writings from like 2016, I need older stuff."
        pl "You guys log events in stuff in a book?"
        ta "It’s more like we just write down funny quotes that sound great out of context."
        jo "And the moments when you all share a brain cell."
        al "Emphasis on one brain cell."
        "Thomas stands up during the conversation and gestures for me to follow, walking over to the cabinet and pointing out some of the items through the windowed door."
        th "This is just a little museum of some of the more important relics. There’s the Fahrenheit 451 book from the fire, the lost book of the forum that was returned during the 50th-"
        pl "Is that a wrapper from White Castle…?"
        th "...Taylor."
        "Thomas turns to look at Taylor who suddenly looks away whistling."
        ta "Wonder how that got there. Well, I’m sure Sherman would love to know he’s being immortalized-"
        th "This is a locked cabinet."
        ta "...All the more reason to know it couldn’t have ever been me."
        jo "Didn’t you offer to pick the lock on the door when we got locked out that one time?"
        ta "HEY, Thomas, you can just talk about the GPA rock to [name] before they do something stupid like uncover it!"
        pl "The GPA rock…?"
        "I look over to Taylor and follow her pointing hand to see what looks like a giant pile of…"
        "Battlestar Galactica keychains?"
        "Moving closer I can see that the keychains have been woven together like chainmail and cover, indeed a giant boulder that’s just sitting next to the door."
        pl "How did I never notice this?"
        th "Most people don’t until it’s pointed out to them, don’t feel bad."
        al "We have a lot of random stuff around here that’s usually more distracting."
        ta "But come on, get on with the questioning! This article is due at midnight and I’d like to pretend that I didn’t wait until the last minute!"

        hide 4pspread

        jump choiceloop

    # Setting up a looping menu for Thomas talking about Forum History

    menu choiceloop:
        th "So, what do you want to know about [name]?"

        "Fahrenheit 451 and the Fire":
            jump f451

        "White Castle and Sherman":
            jump raftenberg

        "GPA Rock":
            jump rockstory

        "I'm good":
            jump loopend

    label f451:

        show thomas

        pl "I’d like to know more about this Fahrenheit 451 book and the fire you mentioned."
        pl "This copy of it does look like it’s been burnt, did you guys set it on fire or something?"
        th "Ah, that. Well this wasn’t us, this is something that happened back in the 1980s."
        th "You see, long ago, the four elements lived in harmony-"

        show taylor at left

        ta "Thomas, I can’t use THAT in my article-!"
        th "But everything changed when the forum fire happened."
        th "Back in 1986, the forum wasn’t in this room but was being run out of one of the dorms."
        th "Suffice to say, one idiot student later, and the dorm had a giant fire."

        show jolee at right

        jo "This was back when smoking in these kinds of areas was allowed, it’s believed that someone didn’t put a cigarette out properly and it caused the whole thing."
        th "The forum at the time lost pretty much most of its collection of books, memorabilia, artwork, all of it."
        th "But, you see, what makes the story worth telling is that our shelves were alphabetical at the time so the fire was able to only burn through A-M before being put out."
        th "Somehow though, this copy of Fahrenheit 451 survived almost completely intact besides the cover and edges being a bit worse for wear."
        th "We like to think the lessons of the novel is something we as a library of science fiction should strive for. We still have the book and memorialize it today too."
        ta "I thought we kept it just because it’s ironic as hell."
        th "That too."
        pl "Jeez, that’s crazy. And you guys said you’re the largest library or something like that…?"
        jo "Yeah, even after losing half of our collection back then, we built it back even larger than before. We’re the largest free-lending library on the eastern seaboard."
        ta "We don’t beat out the New York public library system, but in terms of free-lending without cards and such, no one on this side of the Mississippi beats us."

        hide jolee
        hide thomas
        hide alex
        hide taylor

        jump choiceloop

    label raftenberg:

        show thomas

        pl "So why did you put a White Castle wrapper in here Taylor? Who’s Sherman?"
        ta "Oh, Sherman was an old student from like the 70s or something."
        th "Ah, the unfortunate tale of Sherman Raftenburg."
        th "You see, every year on the 8th of February, we used to hold an anniversary for this long lost forumite."
        th "It is passed down by the orators that one insignificant night where Sherman was almost certainly drunk with friends, they were pulling some stupid antics."
        th "You know Frey Hall yes?"
        pl "Yeah, I have some math course in there."
        th "Then you may have noticed that there are some large vents out there with giant vent covers."
        th "But, long ago on that insignificant night… the vents were uncovered. Stony Brook wasn’t particularly caring about student safety back in those days."
        th "So Sherman decided it would be an excellent idea to jump over this uncovered steam vent."
        th "The first time, he jumped through it and successfully landed on the other side."
        th "The second time, again, he jumped through the billowing steam and once again appeared on the other side."
        th "The third time…"
        th "The third time, he was not as lucky."
        pl "You mean he?"
        th "He fell into the vent. And was steamed alive."

        show taylor at left

        ta "Yeah, if you look in the cabinet, one of those old newspapers has the article about it. I scoped it out, it’s not even a wives’ tale."
        th "He was steamed alive for 18 seconds and his parents were paid restitution in $18,000 - $1,000 for each second he suffered."
        ta "That part I’m less sure about, but I mean, I wouldn’t put it past Stony Brook."
        pl "How does this all connect to White Castle though?"
        th "The tradition to remember Sherman was that they would make a pilgrimage to White Castle and purchase burgers there as they are… steamed."
        ta "Old forumites are crazier than we are honestly, I just leave some wrapped around or draw a burger on the white board, those guys went hard though."

        show jolee at right

        jo "Don’t forget  the screaming."
        pl "The screaming…?!"
        th "Yes, following the pilgrimage, they travel to the steam vent in question and place these burgers as an offering."
        th "The final step of the ritual is for the forum president to jump over the steam vent three times and on the third, all participants then scream for 18 seconds."
        pl "..."
        ta "..."
        th "..."
        jo "...So, you can understand why we don’t really do that anymore."
        pl "Yeah."
        ta "Yeah."
        th "Yeah."

        hide jolee
        show alex at right

        al "Would it be wrong of me to say I’m hungry now?"
        ta "I’d say no, but I know Jolee will disagree with me."
        jo "Yup."

        hide jolee
        hide thomas
        hide alex
        hide taylor

        jump choiceloop

    label rockstory:

        show thomas

        pl "I have to ask, what is up with this rock?"
        th "Yeah, so as you’ve noticed, we have this giant rock here."
        th "A long time ago, in a Stony Brook building far, far away, a forumite brought a rock into the forum."
        th "We don’t know where he got it. We don’t know how he was able to move it."
        th "What we do know is that somehow it ended up in the forum and every since then, we’ve just… moved it to every following location of the forum."

        show alex at right

        al "It’s basically part of the family now."

        show taylor at left

        ta "Except it’s cursed."
        pl "I feel like someone did mention the forum having a curse or two."
        al "Yeah, this is one of them."
        th "You see, this rock is known as the GPA rock because it will drain the GPA of those who stand near it, causing depression, apathy, confusion and extreme laziness."
        th "Of course, the only logical way of preventing this catestrope is by sealing the GPA rock with a chainmail made from Battlestar Galactica keychains."
        pl "Where did you guys even get this many keychains?"
        th "Simple really. The forum used to hold a convention years ago, and during the planning of one of these, there was an error in ordering keychains."
        th "With hundreds of extra keychains on their hands, shrewd forumites decided to weave them into this blessed chainmail to seal the great GPA rock and protect all future forumites to come."
        ta "Yeah, usually we uncover it only during involvement fairs so the president can wear the chainmail to attract new forumites but this year RJ was complaining it hurt his back too much and refused."
        al "It’s much heavier than you expect."
        th "All the more reason not to uncover it."
        ta "Unless of course… you want to tempt fate [name]?"
        pl "What?"
        ta "You’re free to uncover the rock if you dare."
        th "I wouldn’t recommend it."

        hide alex
        hide thomas
        hide taylor
        show 4pspread

        jo "Taylor, why are you trying to kill his GPA, he just got here."
        ta "Well I mean, I could show him Ascension and get the same effect by getting him addicted to that game."
        pl "What’s Ascension?"
        th "A board game that killed the GPA of the last historian and forced him to leave the club."
        ta "It’s fun but dangerous. That old historian was one of the few people who have uncovered the GPA rock so I maintain that the rock did it and Ascension was just the curse kicking in."
        al "Still though, leave their GPA alone."
        ta "Well I think that’s up to them to decide, no?"

        hide 4pspread

# Endings stored at the bottom of the script
        menu:
            "Uncover the GPA Rock":
                jump endingb

            "Leave it be":
                jump refusal

        label refusal:

            show 4pspread

            pl "Nah, I’m good. I’d rather not tempt fate like that."
            jo "Smart move."
            th "Honestly."
            ta "Aww, and here I was hoping to induct him into the Ascension cult."
            pl "Maybe later?"
            al "Don’t encourage her, she really isn’t kidding."
            ta "Blood for the blood god, cards for the card throne!"

            hide 4pspread

            jump choiceloop

# Release from the forum history loop
    label loopend:

        show 4pspread

        pl "I think I’m good on old forum stories."
        th "Well if you’re ever curious let me know, there’s a lot more where that came from."
        ta "I could always use more padding for this article, this stuff is way more interesting than writing about the ‘Bridge to Nowhere’ for the fifth time."
        pl "Bridge to nowhere?"
        jo "Stony Brook has a lot of weird stories, even outside the forum. Like the time it built a bridge to nowhere."
        ta "That proceeded to collapse on people and had to be torn down like within a year of being finished or something like that."
        al "Suffice to say, Stony Brook has never been the best place to go to school."
        pl "I’ll say, some of these stories are kind of concerning."
        th "What’s your opinion on history though [name]?"
        pl "My opinion?"
        "I look over to see Thomas looking at me with a curious expression, almost analytical."
        th "Yeah, how do you feel about it?"
        ta "History is for neeeerds-"
        jo "This is a nerd club and you got a perfect score in your history classes in high school didn’t you?"
        ta "Why must you counter my sass?"
        al "Because you deserve it, let them answer."

        hide 4pspread

        menu:
            "History is neat.":
                jump neatnerd

            "I'd rather make history.":
                jump neatchad

# Opinion on History
    label neatnerd:

        $ updateHearts("THOMAS", 1)

        pl "I guess History is just… pretty neat?"
        pl "I like learning about all this, not really sure how to elaborate on it besides that."

        show thomas

        "Thomas nods approvingly as he pats the cabinet."
        th "I can appreciate it, it’s fun to learn about all these different things."

        show taylor at left

        ta "You can learn about me when I do something like rob fort knox and end up in your textbooks."

        hide taylor
        hide thomas

        jump classwalkja

    label neatchad:

        $ updateHearts("TAYLOR", 1)

        pl "History is cool and all, but I’d rather make history than learn it."

        show taylor

        ta "Oh? Do I hear the sounds of a getaway driver?"
        "Taylor perks up and looks at me with an expression that concerns me and my jail-less life."
        pl "Not trying to become the next Billy the Kid."
        ta "Boo, no fun. You’ll be the alibi then though."

        hide taylor

        jump classwalkja

# Leaving for Class with Jolee and Alex

    label classwalkja:

        show 4pspread

        "I stop as my phone begins to go off, forming a chorus as Jolee and Alex’s ping along as well."
        ta "Oh, all of you have class now, neat. Guess I’m in charge!"
        th "No, I’m staying in here as well."
        ta "Damn, worth a try."
        jo "Come on you two, let’s grab our stuff, doesn’t help to be late. Taylor, no killing Thomas."
        ta "No promises!"
        "We all stand, putting away our laptops and grabbing our backpacks."
        "Taylor and Thomas wave as we head out of the room and up the stairs, pausing as we reach the door outside."

        hide 4pspread
        show alex at left
        show jolee at right

        al "[name], which way are you heading? I’m going by Harriman, Jolee is going near Life Sciences."

        hide alex
        hide jolee

        menu:
            "Jolee is going my way.":
                jump joleewalk

            "Alex is going my way.":
                jump alexwalk

    label joleewalk:

        $ updateHearts("JOLEE", 1)

        show alex at left
        show jolee at right

        pl "Oh, I’m going Jolee’s way then."
        jo "Nice, let’s walk together!"
        al "Alright, then I’ll catch you two later."

        hide alex
        hide jolee

        scene sbuoutside
        show jolee
        play music "<loop 10.0>music/jolee.oga" volume 0.6

        "Alex gives us a wave as he heads left and we head right. I slow my pace a bit for Jolee as we both move in silence for a moment."
        jo "So.. you enjoying the club [name]?"
        pl "Yeah, everyone is pretty nice, even if I don’t know you all that well yet."
        jo "Ah, well is there something specific you want to know?"
        pl "About the club?"
        jo "The club, everyone in it, whatever. Could probably answer something before we get across campus."

        menu:
            "What's up with Thomas?":
                jump jothopinion

            "What's Taylor like?":
                jump jotaopinion

            "What kind of person is Alex?":
                jump joalopinion

            "I want to know more about you.":
                jump jojoopinion

        # Jolee's opinion of Thomas
        label jothopinion:

            $ updateHearts("THOMAS", 1)

            jo "Thomas?"
            pl "Yeah, he strikes me as a bit… I don’t know."
            jo "Tom’s honestly a pretty chill guy. He’s just a giant meme lord."
            pl "Really?"
            jo "He runs some meme reddit accounts or discords or whatever, hard to pin down what he’s focusing on sometimes."
            jo "But, even if he doesn’t always listen, he’s got a good sense of right and wrong."
            jo "Oh, and he takes the best nature photos!"
            pl "He likes photography?"
            jo "He’s a hobbyist I guess. Lots of times he takes photos of animals on campus. Mostly geese, but sometimes he gets pictures of the deer or raccoons that you see around."
            pl "And he’s studying astronomy, yeah?"
            jo "Yeah, for a STEM major, he does have the artsy vibes at heart just a little bit."
            jo "I appreciate what he does for the club though, it’s nice to have someone to just talk to in the mornings when it’s calm, or when we close up the club at night to just walk across campus with."
            jo "If you ever need to talk, he probably could offer an ear and some sound advice."

            jump jowalkbye

        # Jolee's opinion of Taylor
        label jotaopinion:

            $ updateHearts("TAYLOR", 1)

            jo "Oh Taylor?"
            jo "Well, we’re roommates in Hamilton together, so I guess I do kind of know her the best."
            pl "How’s living with her? She is a bit…"
            jo "A bit much?"
            "Jolee laughs, shrugging slightly as we walk."
            jo "She’s super lazy but if you ever ask her for help she'll do everything she can for you."
            jo "Don’t tell her I told you this, but she’s actually in a ton of discord servers just to give advice to people."
            pl "Like what, a ‘Dear Abby’ type thing, where people confess their woes?"
            jo "Nah, she just frequents a lot of discord support servers. Like, whenever there’s one made for freshman, she always jumps in and spends a lot of her free time reading through every question she can."
            pl "That’s pretty dedicated."
            jo "She definitely has that air of someone who doesn’t care, but she does… only about a select few things though."
            jo "To be honest though, both of us pretty much spend all our time in two places - our dorms or the forum."
            pl "Do you guys not like any parts of campus?"
            jo "I know Taylor goes out for walks sometimes just to clear her head or explore a new area, but I prefer sticking in the comfort zone. She calls me though if she finds something crazy though, or sends me pictures."

            jump jowalkbye

        # Jolee's opinion of Alex
        label joalopinion:

            $ updateHearts("ALEX", 1)

            jo "Alex? Which Alex?"
            pl "There’s more than one?"
            jo "Oh wait, there’s only one in this game, sorry."
            jo "Yeah, Alex is a bigger weeb than me and there’s no better way of describing him. I say this as someone who colors manga pages in her free time."
            pl "I guess that falls in line with him wanting to watch Godzilla so badly."
            jo "Yeah, we can’t put on anime during the main hours in the forum, but him and a lot of people prefer us to the anime club."
            pl "So, he just puts on similar stuff until late?"
            jo "Well he has other tastes of course, but he’s even learning Japanese for his language requirement."
            jo "I applaud his dedication. Though, if I needed to take a language course, I probably would’ve done the same."
            pl "Do you know anything else about him?"
            jo "Honestly… not really."
            jo "Don’t get me wrong, it’s not like being a weeb is his only character trait - I just don’t know him that well."
            jo "He’s a bit awkward at times and it’s the type to really be the conversation starter y’know?"
            jo "I’m not much different so we just… don’t talk a lot. We vibe though, when it’s just us and I pop on some lofi music, there’s no better time to do homework or unwind."

            jump jowalkbye

        # Jolee's opinion of herself
        label jojoopinion:

            $ updateHearts("JOLEE", 1)

            jo "Me?"
            "Jolee seems taken aback for a moment, looking away from me to the path ahead of us."
            jo "Oh well uh… I guess I’m just the responsible one."
            jo "Not the best at anything, but I try my best at everything, you know?"
            pl "You do have that ‘mom friend’ vibe."
            jo "Ha, yeah. The club is basically the local kindergarten so it’s a good fit."
            jo "I just want everyone to be happy here or at least comfortable."
            pl "Are you happy here?"
            jo "Am… I happy?"
            pl "Yeah. It goes both ways after all."
            "She seems to look away from me even more pointedly and I see her cheek redden a bit more prominently."
            jo "Ah, well… I guess I am pretty happy in the club lately. Don’t worry too much about me [name], make sure you take care of yourself."

            jump jowalkbye

        # Jolee Walk End Scene
        label jowalkbye:

            "She stops as she nods to the nearby building."
            jo "This is my stop. See you around?"
            pl "Yeah - see ya!"
            "I wave as she turns to head to her class, hustling off to mine immediately after."
            "Maybe I could put this knowledge to good use?"

            jump wednesday

    label alexwalk:
        scene sbuoutside
        show alex
        play music "<loop 10.0>music/alex.oga" volume 0.6

        $ updateHearts("ALEX", 1)

        "Me and Alex walk in silence for a moment after Jolee gives a wave and heads off on her own trek across campus."
        al "So…"
        pl "So…"
        "He chuckles, reaching to rub the back of his neck."
        al "Sorry. I’m not the best at one-on-one conversation."
        pl "It’s alright, I’m still the ‘new person’ after all."
        al "Are you enjoying the club so far at least? I know we can be a bit… ‘much’ for some people."
        pl "No worries, I think you all are pretty fun honestly, even if I don’t know you all that well yet."
        al "Was there someone or something you wanted to know more about? We got another minute before we get there."

        menu:
            "What's up with Thomas?":
                jump althopinion

            "What do you think of Taylor?":
                jump altaopinion

            "What kind of person is Jolee?":
                jump aljoopinion

            "Tell me about yourself.":
                jump alalopinion

        # Alex opinion on Thomas
        label althopinion:

            $ updateHearts("THOMAS", 1)

            al "Thomas? Bit of a wild card I guess. I can’t always get a good read on him."
            al "To be perfectly honest, I’m not certain what he thinks of me at times, but I’d like to be better friends."
            pl "I’m not the best at reading him either, but he seems like a cool guy."
            al "Yeah, he’s pretty smart and definitely can be very passionate about his interests. Especially geese."
            pl "What is up with the geese thing?"
            al "He just really likes nature I guess. I mean, he’s studying physics like me but he’s focusing on astronomy, spends his free time taking pictures of animals on campus…"
            al "Tom even tried to organize a whole club around watching nature on campus at some point I think. Don’t know if it ever went anywhere though."
            pl "Wow, sounds like passionate definitely is the best way to describe him then."
            al "Without a doubt."

            jump alwalkbye

        # Alex opinion on Taylor
        label altaopinion:

            $ updateHearts("TAYLOR", 1)

            al "Taylor?"
            al "Taylor’s a mischievous imp at times, but if you need her, she’ll come through without a doubt."
            pl "Yeah, she definitely seems to like messing with you guys."
            al "That’s just who she is honestly. Sometimes she may push it too far but she usually tries to apologize in her own way and make up for it."
            al "Plus, she honestly is fun to talk with. Like, outside of the jokes and banter, she’s pretty engaging when she chills out."
            al "I lose track of the time sometimes when talking with her."
            pl "It’s always really nice when you can find someone like that, to just let the hours go by when you talk with them."
            "Alex looks at me for a moment before he laughs and shakes his head slightly."
            al "Sounds like you’d like to experience it for yourself."
            pl "Oh, well I-I mean, I just meant-"
            al "No, no, I’m not here to judge. Just… good luck with that."

            jump alwalkbye

        # Alex opinion on Jolee
        label aljoopinion:

            $ updateHearts("JOLEE", 1)

            al "Jolee? Group mom, simple as that."
            al "She is the closest thing to a group mom the forum has, even if she is a bit soft on all of us sometimes."
            pl "She definitely seems like she has to reign you guys in now and then."
            al "Jolee’s just a super supportive person who wants the best for us. You can tell she loves to help out."
            al "I do hope she takes care of herself enough though."
            pl "Does she not sometimes?"
            al "Well I mean, I can relate to the whole idea of forgetting to focus on self-care now and then, and she’s the type to put others before herself."
            al "Like if you’re stepping on her foot, she’ll just sit there and let it happen then tell you sorry when you notice and try to apologize."

            jump alwalkbye

        # Alex opinion on himself
        label alalopinion:

            $ updateHearts("ALEX", 1)

            al "About me…?"
            "He seems confused for a moment before he shrugs a bit with a sigh, not saying anything right away."
            pl "Don’t like talking about yourself?"
            al "To be honest, I’m not very good at talking at all."
            pl "You didn’t really strike me as that type in the forum."
            al "Well yeah, everyone in there is a friend of mine to some extent and you honestly surprised me with how easy I find it to talk to you [name]."
            "Alex gives me a tired smile for a moment before his face falls, looking forward as we keep walking."
            al "I don’t know I just… feel like I’m the living embodiment of min-maxing?"
            pl "Like in games?"
            al "Yeah, I’m just all or nothing with the things I do. I can hyperfixate on things I care about with ease, but on the flip side I forget to eat or just utterly fail at understanding social cues."
            pl "Did you eat today?"
            al "Ha, don’t worry. Between Jolee mothering all of us and Taylor harassing me to eat, it’s hard to forget when I come to campus."
            pl "Well, even if you think you’re bad at all this social stuff, I’m happy to still try to be your friend."
            al "Heh, thanks [name]. Maybe we can talk more later."

            jump alwalkbye

        # Alex Walking Scene End
        label alwalkbye:

            "He stops as he nods to the nearby building."
            al "This is my stop. See you around?"
            pl "Yeah - see ya!"
            "I wave as he turns to head to his class, hustling off to mine immediately after."
            "Maybe I could put this knowledge to good use?"

            jump wednesday

# Beginning of Day 3
    label wednesday:

        stop music fadeout 1.0
        scene wednesday

        "..."

        scene forumhallway

        "Wednesday is here, and after sleeping on the long train ride onto campus, I make my way towards the Student Activities Center."

        scene forummainclapcheeks
        play music "<loop 26.766>music/forum.oga" volume 0.6

        "The basement is surprisingly quiet as I approach, but it’s obviously why when I enter to find just Jolee, Thomas and Alex all sitting at the back table with their laptops."
        show 4pspread
        "Jolee notices me first, giving me a wave."
        jo "Morning [name]."
        al "Heyo."
        th "Just got on campus?"
        pl "Hey guys. And yeah, I have a few hours to kill before class so I figured it’d be more fun to spend it here than just sitting in silence upstairs."
        al "Good choice, you can enjoy the peace and quiet of the morning forum."
        pl "Yeah, I think this is the first time I've seen a 'calm' forum."
        "I sit down at the table with them, pulling my own laptop out to boot it up."
        th "Well, we do have four people here now."
        pl "Is there a special thing you guys do for four people in the room…?"
        th "Nah, it just means we could probably play a board game to kill time."
        al "It’d have to be a short one though if [name] has class, no Terraforming Mars or anything like that."
        jo "Yeah and I don’t feel like suffering through us attempting to play jenga again, even if Taylor isn’t here."
        "As if summoned by Jolee’s words, Taylor suddenly charges into the room with a laugh and brandishing something in her hands."
        ta "Hey guys, look at what I just stol- I mean, recovered from the Anime club!"
        "She holds up a small navy blue box that has the Bat symbol on it along with the words ‘Love Letter’."
        al "You got the game back from them!?"
        jo "I’m more concerned about how exactly she got it back from them."
        "Taylor just leans back and kicks the door stand up, the door swinging shut just as an angry voice from down the hall can be heard."
        ta "Don’t worry about it - hey [name] want to play Love Letter?"

        menu:
            "Sure, I've played Love Letter before.":
                jump noinstruct

            "I haven't played Love Letter before.":
                jump yesinstruct

    label noinstruct:

        pl "Sure, I’ve played before, I know how the game works."
        ta "Sweetness, let’s go nerds. This is Batman edition so instead of calling them ‘guard’ cards or whatever, we have Batman, Robin and the rogues gallery."
        th "I guess this is what we’re doing then."
        al "Hell yeah, you guys are going down."
        "Taylor quickly deals out the cards and I pick up mine, carefully looking at the others."

        jump loveletter

    label yesinstruct:

        pl "I’d be up for it, but I haven’t played it before."
        ta "Eh, you’ll learn as you go."
        jo "We can just explain it to him."
        ta "Fine, fine, but explain quickly, you nerds are going to have to leave for class in like, 40 minutes or whatever."
        jo "It’s really simple [name]. This one just happens to be fashioned after Batman characters but basically, there’s a bunch of different cards, each with a different value and role."
        jo "We each get dealt a card at random, and then on our turns we draw a second one. We choose to either play our old or our new card. Every card has its instructions written on it-"
        ta "Taking too loooong~"
        "As Jolee tries to explain, Taylor’s already taken the cards out and begun dealing them."
        "Jolee sighs and Alex leans over to me."
        al "Just read the instructions on the cards, if you get the batman one try to guess what cards people have, and the goal is to end the round with the highest value card. It’s really easy to pick up!"
        "He offers me a reassuring smile and I nod as I pick up the card I was dealt."

        jump loveletter

    # Love Letter Game commences
    label loveletter:

        "I sigh as I pick up two batmans - the guard card, all I can do is try to guess what cards other people have."
        "I could just go for a hail mary and hope that one of them already has a joker, the highest-value card."
        "But who could be holding it?"

        menu:
            "Taylor, smirking as she meets your eye.":
                jump lltaylor

            "Jolee, anxiously looking at everyone.":
                jump lljolee

            "Thomas, fiddling calmly with his cards.":
                jump llthomas

            "Alex, who seems confused as he looks at his cards.":
                jump llalex

        # J'accuse Taylor
        label lltaylor:
            hide 4pspread
            show taylor
            "Taylor seems confident as she looks at me, it has to be her, right?"
            "I throw my batman card on the table and point to her."
            pl "Do you have the joker?"
            "She cackles and shakes her head."
            ta "Nah, I was just baiting you to waste your cards honestly."
            hide taylor
            jump taylorturn

        # J'accuse Jolee
        label lljolee:
            hide 4pspread
            show taylor
            "Jolee seems nervous, it has to be her right?"
            "I throw my batman card on the table and point to her."
            pl "Do you have the joker?"
            jo "Huh? Me? Oh no, sorry."
            pl "Dang, you looked like you were worried about something."
            jo "Oh I’m just always stressed like this, don’t mind it."
            hide jolee
            jump taylorturn

        # J'accuse Thomas
        label llthomas:
            hide 4pspread
            show thomas
            "Thomas has a perfect poker face right now, maybe it’s him?"
            "I throw my batman card on the table and point to him."
            pl "Do you have the joker?"
            th "Nah."
            "He just shrugs at me and I sigh, letting my extended arm fall."
            hide thomas
            jump taylorturn

        # J'accurse Alex
        label llalex:
            hide 4pspread
            show alex
            "Alex seems confused despite being so excited earlier. Maybe it’s him?"
            "I throw my batman card on the table and point to him."
            pl "Do you have the joker?"
            al "I uh.. I do."
            pl "Nice!"
            al "But I somehow have two of them."
            hide alex
            jump llcontinue

        # If Alex isn't accused, proceeds to Taylor's turn
        label taylorturn:
            hide 4pspread
            show taylor
            "Taylor draws a card happily."
            ta "My turn~!"
            "She looks between all of us for a moment before suddenly pointing at Alex."
            ta "I play Catwoman, let me look at your cards nerd."
            al "If you insist."
            "The two of them lean in, Alex letting her peek at his cards. Almost immediately, her expression grows as confused as him."
            jo "What is it?"
            ta "Alex, how the hell do you have two jokers?"
            hide taylor
            jump llcontinue

# All the choices of the love letter game reconverge
    label llcontinue:
        show 4pspread
        al "I have no idea how this happened."
        th "Perhaps the anime club mixed some of the cards up when they took the game?"
        ta "I mean, this wasn’t me for once, so it probably would have to be them?"
        al "I’ll uh, just slide one of these to the side…"
        pl "Does this mean we’re starting over?"
        ta "It could be interesting to try to play this with two jokers in the deck. I mean, if you get one it’s great, if you get two, you’re screwed."
        th "Wouldn’t be the first time we try to break a game."
        jo "I’m fine with whatever honestly, so long as the games don’t take too long, some of us have class soon."
        "As everyone starts discussing the new game, I pause feeling a… strange sensation in my stomach."
        jo "You alright there [name]? Looking a bit green."
        ta "Oh gods, don’t puke on the table please."
        pl "I’m fine just… where’s the bathroom?"
        th "Down the hall to the right."
        pl "Thanks, excuse me."

        scene forumhallway

        "I excuse myself, holding my stomach as I stumble down the hallway."
        "I just felt fine before - did I accidentally eat some undercooked chicken from the cafeteria or something?"
        "Pushing open the door to the bathroom, I cough, gripping the edges of the sink."

        scene mirror
        play music "<loop 3.5>music/spooky.oga" volume 0.6

        "Nausea, this is definitely some really strong nausea."
        "Looking up at the mirror however, I stop."
        pl "...the fuck?"
        "I have no reflection."
        "There’s nothing there at all but the rest of the room."
        "For a moment I wonder if it’s a trick image but reaching over to flick the paper towels, I can see their reflection move as normal."
        mv "Just go…"
        "I jump back from the mirror."
        pl "Hello? What the hell is going on?"
        mv "Stop this… this pain…"
        mv "You’re ruining it, all of it."
        mv "Just go."
        mv "Go."
        mv "GO!"
        "I feel a force knock into my back and find myself grabbing onto the sink for balance once more before my head bashes into the mirror."

        scene fallenmirror

        "But when I look up again the mirror is… gone."
        "There’s just a brown outline on the wall where it would have been."
        pl "...What kind of fumes are in this bathroom?"
        "Feeling the wall, there’s definitely no mirror and looking around I can’t see anyone else here, or even any kind of microphone they could use to speak in here so clearly."
        "Unsure of what else to do and the nausea having passed, I make my way back down the hall and to the forum."
        scene forummainclapcheeks
        play music "<loop 26.766>music/forum.oga" volume 0.6

    # Two choices code
    label dualScene:
        # Jump to label for appropriate scene
        $ findDates()

    # Beginning of after choice options
    label ALEXJOLEE:
        "I walk in to find Jolee and Alex sitting at the tables alone, each cutting shapes out of pink construction paper."
        show jolee at left
        show alex at right
        jo "Oh, hey [name]! You were gone so long we were getting a bit worried. You feeling alright?"
        pl "...Yeah. Yeah I feel fine. Where’d Taylor and Thomas go?"
        jo "Oh, you were gone for so long they had to leave for class."
        al "Unfortunately they didn’t leave fast enough to avoid Taylor’s latest idea."
        jo "It’s not that bad Alex."
        pl "I assume all this paper is part of it?"
        jo "Yeah. We were talking about manga and Taylor mentioned that it would be festive if there were cherry blossoms put up around the room."
        al "But somehow it went from putting them up around the room to putting it up in the hallway to help draw people into the room."
        pl "Do people come into the basement that often? I hadn’t had reason to come down here before I heard about you guys."
        jo "The bank is down the hall and whenever the ATM upstairs breaks, people come to use the one down here. We usually get a lot of people stopping by when that happens."
        al "I still think Taylor has purposefully broke that thing a few times somehow."
        pl "How do you even break an ATM?"
        jo "No idea, but I wouldn’t put it past her."
        "I sit at the table, looking at the randomly cut pink paper."
        pl "So, we’re cutting these out and what, taping it to the wall outside?"
        al "Basically."
        jo "If you want to help it’d be appreciated. There’s some spare scissors over there."
        pl "It’d feel kind of wrong if I just watched you guys do all the work."
        al "Definitely feels kind of ‘wrong’ with how sore my hands are already getting."
        "Quiet music plays from the tv as we all sit there, working on this goofy project."
        "After a bit, Jolee speaks up."
        jo "Do you guys want to try and start taping some of this to the hallway?"
        al "Yeah, we’re just making a mess of paper scraps right now to be honest."
        pl "It’d probably be fastest if one person put them up and someone else continued cutting?"
        jo "I’m too short to put up the top part of the tree without help honestly."
        al "And my hand is getting sore from all this cutting honestly."
        pl "You two could go in the hallway while I keep cutting?"
        jo "It wouldn’t be right to make you do the rest of this on your own though."
        al "I mean, I don’t see a problem with it-"
        jo "Alex."
        al "Yeah, yeah. [name] do you have a preference in all this?"

        menu:
            "I can help Jolee put up the tree in the hall.":
                jump jahelpjolee

            "I can put up the leaves with Alex.":
                jump jahelpalex

        # Help Jolee over Alex
        label jahelpjolee:
            pl "I kind of want to go out in the hall with Jolee to tape parts of this up. Hand’s kind of getting sore too."
            "Alex lets out a groan but nods."
            al "Yeah, alright, but we better swap places after a bit before my fingers fall off."
            "Jolee looks up at me surprised for a moment before she nods."
            jo "Alright, let’s gather all of these and head out there."
            "Our arms are filled with paper and duct tape as we move out into the hallway."

            jump joleehallway

        # Help Alex over Jolee
        label jahelpalex:
            "I can just put up the leaves with Alex - his hands could use the rest and you don’t have to worry about trying to reach the hallway ceiling Jolee."
            jo "I can agree to that, I definitely don’t feel like balancing on a stepstool right now."
            "Alex gives me a grateful nod and puts down the scissors, gathering up paper instead."
            al "This definitely seems less painful. Why do we only have child-sized scissors?"
            jo "These are me-sized but yeah, not fun for you guys. We might allocate for bigger ones if we can’t find any of the other pairs."
            "Arms full, I look at Alex and we both head out into the hallway to work."

            jump alexhallway

    label ALEXTAYLOR:
        "I walk in to find Taylor brandishing duct tape and pink construction paper to Alex, grinning widely as she whirls around to look at me."
        show alex at left
        show taylor at right
        ta "[name] hey! I was wondering if you fell in and drowned or something. Feeling better?"
        pl "...Yeah. Yeah I feel fine. Where’d Jolee and Thomas go?"
        ta "Oh, you were gone for so long they had to leave for class."
        al "Yes, and unfortunately I’ve been left in here alone with Taylor in the meantime."
        ta "You say that like you don’t love this tree idea."
        pl "Tree idea?"
        al "She wants to put up a cherry blossom tree in the hallway with paper."
        ta "Yup, there’s no better way to spend my time when I have homework due at midnight!"
        al "...Taylor why."
        ta "There’s no point in being grown up if you can’t act childish sometimes. Now take this duct tape, it’s sakura time."
        al "Taylor, why do you have duct tape?"
        ta "...The man who sleeps with a machete is a fool every night but one?"
        pl "Now that one definitely was stolen from online."
        ta "I am a bundle of references in a hoodie, yes, whatever, Sakura Time!"
        "Taylor rushes around, pulling more paper and scissors off of the shelves."
        ta "Come on you two, I think it would do us all good this year if we had a nice cherry blossom staring us in the face?"
        pl "How did this even start?"
        al "We were talking about a manga we’ve been reading together called Komi-san. It’s near Valentine’s day in the story’s timeline."
        ta "Oda is moving the plot as slow as molasses though, so we suffer."
        al "But yeah, the conversation just went from manga to Japan to cherry blossoms and now…"
        "Alex gestures to the grinning Taylor as she dumps another stack of pink paper onto the table."
        ta "You say that like my idea is a bad thing."
        al "It’s a tiring one. These scissors are too small for my hands, they’re getting sore."
        ta "Get smaller hands."
        pl "Something tells me that’s not possible for him."
        ta "I dunno, there’s a cosmetic surgery for everything these days. Grab some scissors [name], I’ll need the power to make up for Alex."
        pl "I guess I’m helping."
        "I sit at the table with them as music plays from the tv. All of us sitting there, working on this goofy project."
        "After a bit, Taylor speaks up."
        ta "Do you guys want to try and start taping some of this to the hallway?"
        al "Yeah, we’re just making a mess of paper scraps right now to be honest."
        pl "It’d probably be fastest if one person put them up and someone else continued cutting?"
        ta "I dunno if I feel like getting up."
        al "Well my hand is getting sore from all this cutting honestly."
        pl "Alex can put it up while we keep cutting?"
        ta "I don’t feel like cutting either though."
        al "You have to do one or the other Taylor, this was all your idea."
        ta "Fine, fine.. [name] what do you feel like doing?"

        menu:
            "I can go into the hall with Taylor to put up leaves.":
                jump athelptaylor

            "I can put up the leaves with Alex.":
                jump athelpalex

        # Help Taylor over Alex
        label athelptaylor:

            pl "I’ll go with you into the hallway Taylor, we can put up the leaves together."
            "Alex lets out a groan but nods."
            al "Yeah, alright, but we better swap places after a bit before my fingers fall off."
            ta "Ooo teamwork? Sounds like my kind of game, you can do the taping and I’ll do the directing."
            "Alex leans forward, stage-whispering to me."
            al "Good luck."
            "Taylor lightly smacks him upside the head before she walks past, a bundle of paper in her other arm."
            ta "Let’s go dude, to the hall!"

            jump taylorhallway

        # Help Alex over Taylor
        label athelpalex:

            "I can just put up the leaves with Alex - his hands could use the rest and you can’t skimp out on doing anything then Taylor."
            "Taylor lets out a groan of protest but grabs the scissors."
            ta "Fine, fine, all in the name of hallway memes."
            "Alex gives me a grateful nod and puts down the scissors, gathering up paper instead."
            al "This definitely seems less painful. Why do we only have child-sized scissors?"
            ta "I don’t know, ask Jolee. She buys these supplies and coincidentally these scissors are the perfect size for her hands!"
            "Arms full, I look at Alex and we both head out into the hallway to work."

            jump alexhallway

    label ALEXTHOMAS:
        "I walk in to find Alex and Thomas sitting at the tables alone, each cutting shapes out of pink construction paper."
        show alex at left
        show thomas at right
        th "Oh hey [name]. You took quite a bit in there, are you okay?"
        pl "...Yeah. Yeah I feel fine. Where’d Taylor and Jolee go?"
        al "You were gone for long enough that they had to go to class. You missed Jolee telling Taylor she wasn’t allowed to skip class again and dragging her away."
        pl "Sounds like I missed quite the show then. What’s all this though?"
        th "Before she was dragged off, she came up with the idea of creating a paper cherry blossom tree in the hallway."
        pl "How’d the discussion go from Love Letter to that?"
        al "Because we started talking about manga and no discussion here really stays on topic for long. And now my hands are being tortured from it."
        th "To be honest, I’m just glad she’s trying to advertise our events for once."
        pl "You guys want my help?"
        al "Please."
        "I walk, taking the scissors handed to me by Alex and sit at the table, joining them as I start cutting out nonsensical shapes from the construction paper."
        "Quiet music plays from the tv as we all sit there, working on this goofy project before Thomas speaks up."
        th "Do you guys want to try and start taping some of this to the hallway?"
        al "Yeah, we’re just making a mess of paper scraps right now to be honest."
        pl "It’d probably be fastest if one person put them up and someone else continued cutting?"
        th "I’m too short to put up the top part of the tree without help honestly."
        al "And my hand is getting sore from all this cutting honestly."
        pl "You two could go in the hallway while I keep cutting?"
        th "It wouldn’t be right to make you do the rest of this on your own though."
        al "I mean, I don’t see a problem with it-"
        th "Alex."
        al "Yeah, yeah. [name] do you have a preference in all this?"

        menu:
            "I can set up the tree in the hall with Thomas.":
                jump tahelpthomas

            "I can put up the leaves with Alex.":
                jump tahelpalex

        label tahelpthomas:

            "I think both of us should put up the tree in the hallway Thomas."
            th "Really? I kind of thought… well alright."
            "He seems almost taken aback for a moment before he just returns to his usual calm state."
            "Alex lets out a groan, but nods in agreement as well."
            al "One of you better swap with me before my fingers fall off though."
            th "Don’t worry, we won’t leave you to die. Probably."
            "Thomas has a sly grin as he gathers up some paper and tape, nodding his head to the hallway."
            th "Shall we?"
            pl "Let’s go."

            jump thomashallway

        label tahelpalex:

            "I can just put up the leaves with Alex - his hands could use the rest and you don’t have to worry about trying to reach the hallway ceiling Thomas."
            th "I can agree to that. I definitely don’t feel like balancing on a stepstool right now to try to reach the top part of the hallway anyway."
            "Alex gives me a grateful nod and puts down the scissors, gathering up paper instead."
            al "This definitely seems less painful. Why do we only have child-sized scissors?"
            th "These are definitely better sized for me and Jolee rather than anyone else. We might allocate for bigger ones if we can’t find any of the other pairs."
            "Arms full, I look at Alex and we both head out into the hallway to work."

            jump alexhallway

    label JOLEETAYLOR:
        "I walk in to find Taylor brandishing duct tape and pink construction paper to Jolee, grinning widely as she whirls around to look at me."
        show jolee at right
        show taylor at left
        ta "[name] hey! I was wondering if you fell in and drowned or something. Feeling better?"
        pl "...Yeah. Yeah I feel fine. Where’d Alex and Thomas go?"
        ta "Oh, you were gone for so long they had to leave for class."
        jo "And in the meantime, Taylor had… an idea."
        ta "Why do you say like I just showed you a millipede from under a rock?"
        pl "I assume all this paper is part of it?"
        jo "Yeah. We were talking about manga and Taylor mentioned that it would be festive if there were cherry blossoms put up around the room."
        ta "Yeah, but then I realized that if we put them up outside the room, that counts as advertising and that means I’m technically doing my job so they can’t oppose me!"
        pl "Do people come into the basement that often? I hadn’t had reason to come down here before I heard about you guys."
        jo "The bank is down the hall and whenever the ATM upstairs breaks, people come to use the one down here. We usually get a lot of people stopping by when that happens."
        ta "And if the ATM just happens to break again after we put this up, I’ll have not only done my job, but I will have done it well."
        pl "Taylor, have you broken the ATM before?"
        jo "How do you even break an ATM?"
        ta "Don’t worry about it. [name] come sit, less talky, more cutty."
        "I sit at the table, looking at the randomly cut pink paper."
        pl "So, we’re cutting these out and what, taping it to the wall outside?"
        jo "Basically."
        ta "Let’s go!"
        "Quiet music plays from the tv as we all sit there, working on this goofy project."
        "After a bit, Jolee speaks up."
        jo "Do you guys want to try and start taping some of this to the hallway?"
        ta "I mean we could, but I don’t feel like getting up."
        jo "Well, I can’t really reach the ceiling of the hallway if I go start doing it."
        pl "I could do that while both of you keep cutting?"
        ta "I don’t feel like cutting either though."
        jo "You have to do one or the other Taylor, this was all your idea."
        ta "Fine, fine.. [name] what do you feel like doing?"

        menu:
            "I can go into the hall with Taylor to put up leaves.":
                jump jothelptaylor

            "I can help Jolee put up the tree in the hall.":
                jump jothelpjolee

        label jothelptaylor:

            pl "I’ll go with you into the hallway Taylor, we can put up the leaves together."
            jo "I can agree to that, I definitely don’t feel like balancing on a stepstool right now."
            ta "Ooo teamwork? Sounds like my kind of game, you can do the taping and I’ll do the directing."
            "Jolee leans forward, stage-whispering to me."
            al "Good luck."
            "Taylor waves Jolee off as she walks past me, a bundle of paper in her other arm."
            ta "Let’s go dude, to the hall!"

            jump taylorhallway

        label jothelpjolee:

            "I kind of want to go out in the hall with Jolee to tape parts of this up. Hand’s kind of getting sore too."
            "Taylor lets out a groan of protest but grabs the scissors."
            ta "Fine, fine, all in the name of hallway memes."
            "Jolee looks up at me surprised for a moment before she nods."
            jo "Alright, let’s gather all of these and head out there."
            "Our arms are filled with paper and duct tape as we move out into the hallway."

            jump taylorhallway

    label JOLEETHOMAS:
        "I walk in to find Jolee and Thomas sitting at the tables alone, each cutting shapes out of pink construction paper."
        show jolee at left
        show thomas at right
        jo "Oh, hey [name]! You were gone so long we were getting a bit worried. You feeling alright?"
        pl "...Yeah. Yeah I feel fine. Where’d Taylor and Alex go?"
        jo "Oh, you were gone for so long they had to leave for class. I had to yell at Taylor to not skip and stay to work on all this."
        pl "Sounds like I missed quite the show then. What’s all this though?"
        th "Before she was dragged off, she came up with the idea of creating a paper cherry blossom tree in the hallway."
        pl "How’d the discussion go from Love Letter to that?"
        jo "Because we started talking about manga and no discussion here really stays on topic for long."
        th "To be honest, I’m just glad she’s trying to advertise our events for once."
        pl "You guys want my help?"
        th "It’d be appreciated."
        "I walk, taking the scissors handed to me by Jolee and sit at the table, joining them as I start cutting out nonsensical shapes from the construction paper."
        "Quiet music plays from the tv as we all sit there, working on this goofy project before Thomas speaks up."
        th "Do you guys want to try and start taping some of this to the hallway?"
        jo "Yeah, we’re just making a mess of paper scraps right now to be honest."
        pl "It’d probably be fastest if one person put them up and someone else continued cutting?"
        th "I’m too short to put up the top part of the tree without help honestly."
        jo "I’m pretty much in the same boat."
        pl "You two could stay here while I work in the hallway?"
        th "It wouldn’t be right to make you do the rest of this on your own though."
        jo "We’d probably end up cutting faster than you put them up and cut to much or end up helping you anyway."
        pl "Then I suppose…"

        menu:
            "I can set up the tree in the hall with Thomas.":
                jump tjohelpthomas

            "I can help Jolee put up the tree in the hall.":
                jump tjohelpjolee

        label tjohelpthomas:

            "I think both of us should put up the tree in the hallway Thomas."
            th "Really? I kind of thought… well alright."
            "He seems almost taken aback for a moment before he just returns to his usual calm state."
            jo "I can agree to that, I definitely don’t feel like balancing on a stepstool right now."
            th "Alright then, let’s head out there then."
            "Thomas gathers up some of the paper and tape before nodding to me."
            th "Shall we?"
            pl "Let’s go."

            jump thomashallway

        label tjohelpjolee:

            "I kind of want to go out in the hall with Jolee to tape parts of this up. Hand’s kind of getting sore anyway."
            th "I’m fine with that, I’ll stay in here and cut and you guys can work out there."
            "Jolee looks up at me surprised for a moment before she nods."
            jo "Alright, let’s gather all of these and head out there."
            "Our arms are filled with paper and duct tape as we move out into the hallway."

            jump joleehallway

    label TAYLORTHOMAS:
        "I walk in to find Taylor brandishing duct tape and pink construction paper to Thomas, grinning widely as she whirls around to look at me."
        show taylor at right
        show thomas at left
        ta "[name] hey! I was wondering if you fell in and drowned or something. Feeling better?"
        pl "...Yeah. Yeah I feel fine. Where’d Jolee and Alex go?"
        ta "Oh, you were gone for so long they had to leave for class."
        th "Taylor came up with this tree idea before they left though."
        pl "Yeah, what is all this?"
        ta "We’re making a tree!"
        "Taylor starts bouncing up and down in place like an excited kid."
        th "Taylor, you are quite literally running and bouncing with scissors in your hand."
        ta "There’s no point in being grown up if you can’t act childish sometimes. Now take this duct tape, it’s sakura time."
        pl "Why do you have duct tape?"
        ta "...The man who sleeps with a machete is a fool every night but one?"
        th "Now that one definitely was stolen from online."
        ta "I am a bundle of references in a hoodie, yes, whatever, Sakura Time!"
        "Taylor rushes around, pulling more paper and scissors off of the shelves."
        ta "Come on you two, I think it would do us all good this year if we had a nice cherry blossom staring us in the face?"
        pl "How did this even start? What happened to Love Letter?"
        th "We were talking about manga because no discussion here really stays on topic for long. Manga led to talks about Japan, cherry blossoms and lo and behold, here we are."
        ta "This is me doing my job advertising events so they can’t stop me."
        th "To be honest, I’m just glad she’s trying to advertise our events for once."
        pl "So, you guys want my help?"
        th "It’d be appreciated."
        "I walk, taking the scissors handed to me by Taylor and sit at the table, joining them as I start cutting out nonsensical shapes from the construction paper."
        "Quiet music plays from the tv as we all sit there, working on this goofy project before Thomas speaks up."
        th "Do you guys want to try and start taping some of this to the hallway?"
        ta "I don’t feel like getting up."
        th "I’m too short to put up the top part of the tree without help honestly."
        pl "I could put it up while you two keep cutting?"
        ta "I don’t feel like cutting either though."
        th "You have to do one or the other Taylor, this was all your idea."
        ta "Fine, fine.. [name] what do you feel like doing?"

        menu:
            "I can go into the hall with Taylor to put up leaves.":
                jump tthelptaylor

            "I can set up the tree in the hall with Thomas.":
                jump tthelpthomas

        label tthelptaylor:
            pl "I’ll go with you into the hallway Taylor, we can put up the leaves together."
            th "I can agree to that, I’ll keep cutting while you two are out there."
            ta "Ooo teamwork? Sounds like my kind of game, you can do the taping and I’ll do the directing."
            th "Just don’t let her make you do all the work."
            pl "I think I’ll be fine."
            "Taylor waves Thomas off as she walks past me, a bundle of paper in her other arm."
            ta "Let’s go dude, to the hall!"

            jump taylorhallway

        label tthelpthomas:
            "I think both of us should put up the tree in the hallway Thomas."
            th "Really? I kind of thought… well alright."
            "He seems almost taken aback for a moment before he just returns to his usual calm state."
            "Taylor lets out a groan of protest but grabs the scissors."
            ta "Fine, fine, all in the name of hallway memes."
            th "Alright then, let’s head out there then."
            "Thomas gathers up some of the paper and tape before nodding to me."
            th "Shall we?"
            pl "Let’s go."

            jump thomashallway

    label joleehallway:

        scene forumhallway
        show jolee
        play music "<loop 4.0>music/jolee.oga" volume 0.6

        "Out in the hall, both of us drop the supplies on the ground, Jolee groaning as she stands back up. Her back audibly cracks."
        pl "That sounded pleasant."
        jo "It feels better than it sounds promise."
        pl "Here, how about I pass you the materials for now so you don’t have to keep leaning down?"
        jo "That’d be great thanks."
        "I sit on the ground, grabbing paper and attaching pieces of tape to them before passing them up to Jolee. I pause on one of them, holding it up to her to show off the detailed flower that’s been drawn on it."
        pl "Hey, this one has a doodle on it."
        "She looks back and seems embarrassed for a moment."
        jo "Oh sorry, that’s mine! I was drawing on the papers earlier before you came back."
        pl "It’s really good honestly."
        jo "Nah, I just make trash honestly."
        "Taking them from me, our hands brush against each other before she turns to press the pink scraps to the wall."
        pl "So… how come your back is so noisy? Is it just backpack trauma?"
        "She lets out a light laugh. Her voice reminds me of a piano for a moment, a nice melody reaching my ears."
        jo "Noisy is one way to describe it. I just hunch over a lot, there’s not really any chronic issues that I know of."
        jo "I don’t have the medical history to really go off of y’know?"
        pl "Why not?"
        jo "Oh we may not have mentioned it, but I’m adopted. Born in china, abandoned at a factory and brought over here when I was a baby."
        pl "If you did I forgot sorry. But that’s…neat?"
        jo "It’s not a fun story, I’m not offended if you call it awful or anything. It’s just what happens over there. They want sons, not daughters. Especially not blind, half-deaf daughters like me."
        pl "You shouldn’t be so hard on yourself!"
        jo "It’s not even exaggeration, I’m actually legally blind. No idea how I got a license. "
        pl "For someone who’s half-blind, you’re a really good artist."
        jo "I’m not that good honestly…"

        menu:
            "You really shouldn’t be so hard on yourself.":
                jump joleepos

            "You shouldn’t have such low standards.":
                jump joleeneg


        label joleepos:

            $ updateHearts("JOLEE", 1)

            jo "I mean I-"
            pl "No, I mean it. You’re being way too harsh on yourself when you’re obviously doing a lot."
            pl "You make this great art despite being half blind, you’re helping run this club and studying biomedical engineering on top of all this, probably one of the hardest majors taught here."
            jo "I…"
            "Jolee stands there as if frozen for a moment, her arm still mid-motion of sticking the paper to the wall."
            "I feel almost embarrassed myself just from the second-hand strength of the feeling."
            pl "I’m sorry if I-"
            jo "No, no, no, I’m sorry, you’re fine!"
            jo "That just.. took me off guard. Thank you though."
            "She smiles at me and I almost instantly return one."
            jo "Let’s get these papers up though. Thomas will start to wonder what we’re doing out here."

            jump joleehallwayend

        label joleeneg:

            jo "I’ve had to deal with shitty things my entire life. And at some point, I accepted that I couldn’t change it, so I stopped caring."
            "She looks almost annoyed for a moment before she continues."
            jo "..sorry that came out ruder than I intended it."
            pl "No, it’s alright, I sort of overstepped myself I guess."
            jo "Let’s just put up the rest of this paper."

            jump joleehallwayend

# Ending scene for Jolee in the Hallway
    label joleehallwayend:

        play music "<loop 3.5>music/spooky.oga" volume 0.6

        "Both of us fall into a comfortable silence as well as a nice rhythm of me attaching tape to the papers as well as her putting them on the walls."
        "Jolee starts humming a song I can’t quite place."
        pl "Drawing and singing. Are you a triple threat and going to start dancing to?"
        "She stops and cracks another smile."
        jo "I did a lot of dancing when I was younger. I did ballet, a bit of jazz, I did gymnastics a bunch as well."
        pl "Damn, you really are a triple threat then!"
        jo "Don’t do anymore and definitely can’t stand en pointe anymore, but I’m still pretty flexible."
        "I go to respond and hand her another piece of paper but stop as I realize we’ve exhausted the entire pile."
        pl "Oh, we’re out. Guess we should get more from Thomas."
        "I go to stand up and dust myself off when I feel Jolee suddenly grab my sleeve, tugging on it for a moment."
        pl "What is it?"
        jo "Before I forget - would it be alright if I got your phone number? I have most people’s numbers in the forum and if you’re going to be hanging around…"
        "She trails off but I nod and pull out my phone."
        pl "Sure, no problem. You can put your number in mine and text yourself."
        jo "That works, thanks."
        "She pulls the screen close, squinting at it before she slowly types in her name and number in the open contact."
        "Afterwards she hands it back to me."
        jo "Thanks again."
        pl "Heh, it’s no big deal, honest."
        "Jolee lingers for a moment before she rushes past me back into the room."
        "I follow her inside and we get more paper to complete the ‘art’ piece…."
        hide jolee
        jump thursdayjolee


    label alexhallway:
        scene forumhallway
        show alex
        play music "<loop 10.0>music/alex.oga" volume 0.6

        "Alex groans as we dump the supplies on the ground, flexing his hands."
        pl "Those scissors really did a number on you, huh?"
        al "Yeah, probably should’ve stopped sooner."
        pl "Why didn’t you?"
        "I lean down to grab some paper and tape, beginning the process pressing them into the wall."
        al "Well even if it’s just another crazy Taylor idea, I do want to help. I may not be an eboard member right now, but I still try to do my part."
        pl "Yeah, I can understand that. Want to contribute like everyone else and all that."
        al "Exactly. Rather do something besides watch tv and read comics."
        pl "You know for the ‘biggest library on the seaboard’ or whatever it was, I haven’t seen a lot of reading go on."
        al "Heh, yeah it’s an on-going joke pretty much, the old librarian was said to have never learned how to read."
        pl "I mean, if he’s made it this far, no reason to learn now!"
        pl "So what kind of comics do you read?"
        al "I was looking for some recommendations honestly. Thinking about breaking out a new manga series just because I’ve been in a bit of a lull. No one on the discord can really give me something new though."
        pl "Discord?"
        al "Oh right, you’re new. Yeah, the forum has a discord server. I can add you if you want?"
        pl "I’d like that, yeah."
        al "Here, you can put your discord information in my phone."
        "Alex holds out his phone, the discord app opened and add-friend tab selected. I put in my information and send the request."
        pl "Cool, I’ll accept it later and you can send me the invite."
        al "Awesome then. You can see me fill up the japan channel with memes."
        pl "You like anime and manga a lot?"
        al "Yeah I’m one of the official weebs of the forum."
        pl "What’s your favorite?"
        al "Gundam, without a doubt."
        pl "I feel like I’ve heard of gundam but I’m not positive. What’s it about?"
        "For a moment it seems like I opened the floodgates as Alex’s face lights like up like an evening sky in the countryside, nothing but hope and stars."
        al "Well you see…"
        al "{cps=150}Gundam is a massively popular giant robot franchise from Japan that's been running since the late 70s and defined the mecha genre as we know it with the original series Mobile Suit Gundam from 1979 which was a show that was hard science-fiction for the most part.{/cps}{nw}"
        al "{cps=150}It lasted 43 episodes and wasn't particularly successful at the time, facing cancellation but allowed to finish its story, it only became popular through the compilation film trilogy that succeeded it which trimmed about 10 hours of fat from the original series in total.{/cps}{nw}"
        al "{cps=150}Nowadays it's recognized, along with other Gundam series as phenomenal examples of anti-war narratives with shows that despite the spectacle of giant robots are about people, the hopes for the growth of humanity, and a reflection of the hell people are capable of.{/cps}{nw}"
        al "{cps=150}Getting into an old anime series is rough for a lot of people, and the '79 TV series has definite signs of aging, so I wouldn't recommend it for newcomers. I'd personally suggest Mobile Suit Gundam: Iron-Blooded Orphans from 2015, which is the series I started with.{/cps}{nw}"
        al "{cps=150}It's a complete standalone so you don't need to worry about any of the other Gundam works to be released over the years. Also, as a franchise over 40 years old now, it's a franchise that's been highly malleable, whether you want hard sci-fi anti-war or basically Street Fighter with robots like Mobile Fighter G Gundam, Gundam has something for you.{/cps}{nw}"
        al "{cps=150}If you wanna see the upcoming Gundam movie, you'd have to watch a good amount of the 'Universal Century' timeline. Gundam has multiple different continuities and Universal Century is the largest one, it includes the original '79 series among others.{/cps}{nw}"
        al "{cps=150}To watch the new movie, you'd have to watch a bare minimum of Gundam '79, Zeta Gundam, Gundam ZZ, Gundam CCA, Gundam Unicorn, and maybe Gundam NT to get the big picture of what's going on in this movie.{/cps}{nw}"
        al "{cps=150}If you get really into the series, there's the plastic model kits based on robots from the show known as gunpla, which come in-{/cps}{nw}"
        "Alex stops suddenly, his face turning a fierce red as he shrinks in on himself, looking away from me."
        al "Sorry, I uh…"
        "So quickly he goes from rambling about Gundam to being at a loss for words."

        menu:
            "I'm listening to you Alex.":
                jump alexpos

            "Look me in the eyes Alex.":
                jump alexneg

        label alexpos:

            $ updateHearts("ALEX", 1)

            pl "It’s alright, I’m listening to you Alex."
            "He comes out of the turtle shell that he’s turned his jacket into, nodding slightly as he gives me a sheepish grin."
            al "I just uh…"
            pl "Really like gundam?"
            al "Yeah. There aren’t a lot of people in the forum who are into it."
            pl "I don’t think any of them could compare to your dedication."
            al "Ah, I don’t think that’s really a good thing honestly."
            pl "Why not?"
            al "Well.. hyperfixating and all that, y’know? Sometimes I don’t do the best when it comes to listening as well as talking."
            pl "Don’t worry Alex, I’ll let you know if I ever need you to stop and listen - but it would be wrong if I didn’t give you the same courtesy. Even if you do have a lot to say."
            "There’s a twinkle of something in his eye as he seems to relax a bit more, nodding once more."
            al "Yeah… alright."

            jump alexhallwayend

        label alexneg:

            pl "Come on, look me in the eyes Alex."
            "He seems to almost retreat even further into his jacket like a turtle into its shell, looking at my eyes for a moment before they flicker away once more before he can even finish a sentence."
            al "I-I-I’m sorry, it’s just…"
            pl "Just what?"
            al "Eye contact can get a bit… uncomfortable for me."
            pl "Oh. My bad then."
            al "It’s, It’s cool. I’ll just. Shut up now."
            "We both fall into an uncomfortable silence for a moment, the only sounds in the hall being the rustle of papers and the faint beeping of the ATM from down the hall."

            jump alexhallwayend

    label alexhallwayend:

        "After a bit of work on the tree, Alex speaks up again, pointing to the empty space between us."
        al "Ah, we ran out of paper."
        pl "I can go grab some more from inside?"
        al "Actually, I should probably head out soon. I have to catch an earlier train to get home. Doctor’s appointment."
        pl "Oh, alright then…"
        al "Well, I mean, we’ll probably still be working on this tomorrow honestly, I doubt we can make this thing in one night."
        pl "You’re not wrong."
        al "I’ll see you tomorrow then [name]."
        "Alex gives a wave before he heads inside the clubroom, leaving me a moment to myself in the hallway to look at the half-finished creation before I follow him in."
        hide alex
        jump thursdayalex

    label thomashallway:

        scene forumhallway
        show thomas
        play music "<loop 0.5>music/thomas.oga" volume 0.6

        "Both of us come out into the hall, dropping our shared piles of materials as Thomas examines the wall for a moment."
        th "Hm, maybe we should outline it before we get started?"
        pl "Sure, but how do we do that?"
        "Thomas pulls out his phone and takes a picture of the wall."
        "I lean over his shoulder curiously as he opens the photo in an editing app and begins drawing out how the tree could be shaped on the wall."
        th "Hmm… we could probably have the trunk go like this, it can curve with these branches… and the rest can just be pink."
        "Even if it ‘s just a sketch for planning, he seems pretty skilled for someone just drawing with their finger."
        pl "Can you send me that?"
        th "Send you-?"
        "He turns to look at me and we both flinch back, realizing how close together we had been. Thomas reaches a hand up to push his glasses up on his nose."
        th "Ahem. Sorry, you just… startled me."
        pl "I was just looking at the plan!"
        th "No, it’s alright. Here, you can put your number in my phone if you want me to send it."
        "Thomas looks away from me as he holds his phone out, an empty contact on the screen."
        "I take it from him, quickly entering my name and number, sending a message so I could save his number later."
        "By habit I hit the home button and find myself faced with the homescreen of the usual array of apps - groupme, blackboard, reddit - with a photo of a goose in a pond as the background."
        pl "You really like your geese huh?"
        th "Yes, yes I do."
        "Thomas takes his phone back and goes to pick up some of the paper scraps, putting tape on the backs of them."
        th "I have a soft spot I guess for them. Things like the Untitled Goose Game just gave me more reason to appreciate them."
        pl "The game where you just tried to cause chaos?"
        th "I relate to it."
        "Thomas has a sly smile on his face again as he slaps another piece of paper to the wall."
        pl "Is this related or unrelated to that hoodie of yours?"
        th "Heh, a lot of people comment on it sooner."
        pl "So who is SBUgeese?"
        th "All I can say to that is… honk."
        pl "...honk?"
        th "Honk."
        pl "Alright then, I won’t question you."
        th "I won’t kill you if you do question me."
        pl "Why do you go straight to death?"
        th "I dunno."

        menu:
            "You seem like you meme a lot.":
                jump thomaspos

            "Why are you so serious?":
                jump thomasneg

        label thomaspos:

            $ updateHearts("THOMAS", 1)

            pl "To be honest Tom, you seem like you like to meme a lot."
            th "Well… yeah."
            "He shrugs as he keeps adding things to the wall."
            th "I do a lot of stupid random stuff on campus. I wear shorts in the snow. I find quiet spots to take naps and be alone."
            pl "You sit in a basement, putting paper trees on walls."
            th "Ha, yes and that. But, I just like saying, making and being memes a lot of times."
            pl "You didn’t come across like that in the beginning."
            th "Well… a lot of people aren’t who they seem to be, no? That’s why there’s the whole ‘don’t just a book’ by its cover saying."
            th "It’s just a matter of being lucky enough to learn about other sides of them."
            pl "That’s… kind of deep honestly."
            th "Better out than in I always say."
            pl "...Was that a Shrek reference."
            "He doesn’t respond right away, just widening his grin."
            th "So… pass me that paper?"

            jump thomashallwayend

        label thomasneg:

            th "Serious?"
            pl "Yeah you seem just really serious to me. Hard to read almost."
            th "That’s not how I really try to come off. I don’t think I’m that serious a person."
            pl "Maybe I’ve just misunderstood you then sorry."
            th "I…hm."
            "He stops for a moment and I turn to see him pensively looking down at one of the papers."
            pl "What is it?"
            th "I’m trying to figure out how to best explain this, like… people are like onions."
            pl "Right…"
            th "People have layers."
            pl "Is… is this a Shrek reference right now?"
            th "That’ll do [name], that’ll do."

            jump thomashallwayend

    label thomashallwayend:

        "I hand Thomas another taped piece of paper and he presses it to the wall before stepping back to look at our progress."
        th "I think this is good for now. We can probably finish it after the others come back from class, or maybe in the morning."
        pl "You sure you want to leave it here?"
        "He looks at me for a moment and shrugs."
        th "Eh, there’s always tomorrow right?"
        pl "I guess you’re right."
        "With a calm grin, Thomas waves for me to follow him and we both head inside the forum."
        hide thomas
        jump thursdaythomas

    label taylorhallway:
        scene forumhallway
        show taylor
        play music "<loop 6.5>music/taylor.oga" volume 0.6

        "I follow Taylor out into the hall and watch as she immediately dumps all our materials to the ground and claps her hands together."
        ta "Alright let’s make something of all this. [name], quick, start taping things to the wall!"
        pl "You mean we, right?"
        ta "Come on, fuel my laziness for just a little bit?"
        pl "This was your idea wasn’t it?"
        "Taylor groans, melodramatically shaking her arms around for a moment before she kneels down, grabbing some of the paper and putting it on the wall."
        ta "Fine, fine, whatever, I guess."
        pl "You really have a lazy streak don’t you?"
        ta "Me? Lazy? Never."
        "She smirks through her sarcasm before her expression clears for a moment and she speaks a bit more seriously."
        ta "I’m honestly better than coming up with ideas than executing them."
        pl "The others made it sound more like you…"
        ta "Skip out on my responsibilities?"
        pl "Yeah."
        ta "Ha, I don’t blame them. I do make big deal out of things like never attending meeting or doing my job in the laziness way or refusing to get two-factor authentication on my discord account-"
        pl "I mean it is safer isn’t isn’t it?"
        ta "I will die on this hill, hush."
        ta "But I do.. Do things? I just, kind of, don’t like doing them so obviously if that makes sense."
        pl "You won’t attend the meeting but you’ll spend your evening making a tree in the hallway just to bring in new members."
        "She swings her head around to look at me almost suspiciously before she cracks a smile."
        ta "Be careful Mr. [name], I’ll have to take you out if you learn any more of my game so easily."
        "We put up more and more of the pink petals before Taylor turns to look at me suddenly."
        ta "Hey, would you rather be the last person on earth or permanently invisible?"
        pl "That’s an… odd question?"
        ta "Yes, it is a question. What’s your answer?"
        pl "Well why do you ask?"
        ta "Because I want to know if it’s like mine."
        pl "Then which would you prefer?"
        ta "That just makes it easier for you to know which to say now doesn’t it? That’s not how the game should be played."
        pl "This is a game now?"
        ta "Always has been. Now pick nerd."

        menu:
            "Permanently invisible.":
                jump taylorhw1

            "The Last Person on Earth.":
                jump taylorhw2

        label taylorhw1:

            pl "Then I guess I’d rather be permanently invisible."
            ta "Why?"
            pl "I dunno,  just think that would be the better choice than not having anyone else around me."
            ta "I see…"

            jump taylorhwcontinue

        label taylorhw2:

            pl "Then I guess I’d rather be the last person on earth."
            ta "Why?"
            pl "I dunno, just think that would be the better choice than not being able to ever be seen again."
            ta "I see.."

            jump taylorhwcontinue

    label taylorhwcontinue:

        "We work in silence for a few moments before Taylor speaks up."
        ta "Not going to ask for my answer?"
        pl "I figured that you would share it if you wanted to."
        ta "Touche."
        ta "To be honest, I won’t hold your choice against you, I honestly wouldn’t like either of those. You probably weren’t sure which to pick anyway."
        ta "I can’t stand being alone. But I definitely wouldn’t survive being invisible either."
        pl "I figure you’d go around pranking people if you were invisible."
        ta "Heh, yeah I give off those vibes don’t I?"
        "I look over to Taylor and she’s still smiling but she doesn’t meet my gaze for a moment."
        ta "What kind of person do you think I am [name]?"
        pl "What kind of person?"
        ta "Yeah. You’re new, you don’t have any baggage or crazy memories or anything like that with me to affect your opinion. I want the freshest answer I can get. What kind of person do you think I am?"

        menu:
            "You seem like you love your friends.":
                jump taylorpos

            "You seem like you want to have fun.":
                jump taylorneg

        label taylorpos:

            $ updateHearts("TAYLOR", 1)

            pl "You seem like you really care about your friends."
            ta "Really?"
            "She looks over at me and there’s genuine surprise in her expression. The corners of her lips upturn though, as if the shock is a happy one."
            ta "Huh. I… alright."
            pl "What is it?"
            ta "Heh, nothing. I just like the way you think dude."
            "Taylor seems to have perked up a bit more, if that was even possible, bouncing slightly on her heels before she suddenly turns to me with a more mischievous look."

            jump taylorhallwayend

        label taylorneg:

            pl "You seem like you just want to have fun."
            ta "A fun-lover, eh?"
            pl "Yeah, I wouldn’t want to get between you and your latest plan."
            ta "Huh… alright."
            "I look over at her again and for a moment I feel like there’s disappointment in her eyes before she looks at me with a bright expression, the previous emotions wiped away in an instant."

            jump taylorhallwayend

    label taylorhallwayend:

        ta "Hey [name], care to do me a favor?"
        pl "What exactly does this favor entail?"
        ta "Give me your phone number."
        pl "You...want my number?"
        ta "Well… hypothetically speaking, when you left your phone plugged into the charging station I may have been messing with it and took a funny picture of Alex."
        ta "So moreso, I want to give you my number for photo sending purposes."
        pl "Wait, when were you-"
        ta "Don’t sweat the details dude, just let your next words be 'Here’s my phone, put in your contact information Taylor…'"
        "For all her bravado, her hoodie pocket keeps twitching like she’s fidgeting her hands."
        "I sigh but take out my phone, shielding it as I put in the code before handing it to her with a blank contact up on the screen."
        pl "Alright, here you go. I’ll send you the photo after I get to class."
        "Her grin widens as she snatches the phone and rapidly puts the details."
        ta "Awesome! I won’t make you late for class though, see ya [name]!"
        "Taylor haphazardly tosses my phone back to me, but I’m thankfully able to catch it, though she’s already back in the clubroom before I can say anything else."
        "Looking down, I can see, indeed, a number is there, and she put her name as ‘Forum Knight’... I’ll assume there’s a story behind that one."
        "Saving the questions for later, I tuck my phone away and follow her inside."
        hide taylor
        jump thursdaytaylor

    # Beginning of Thursday - Different Version for each route
    label thursdayjolee:

        scene thursday
        "..."

        scene sbuoutside

        "Thursday morning comes and with it, my dreaded 8am class."
        "It’s not even one that happens on Tuesday also, it’s just a blemish on my schedule, dooming me to sleep in and miss it at least once."
        "And this was one such morning."
        "Running across campus to get there in time, I didn’t realize I left something behind until midway through the lecture, my phone buzzed in my pocket."
        jo "Hey, do you have your ID?"
        jo "I don’t know your last name but the picture looks like you."
        "She sends me a photo of her hand clasped around what is indeed my ID, the background mostly concrete except for this blurry streak of color I can’t quite place."
        "I quickly message her back."
        pl "That is it thanks! I didn’t even realize I lost it."
        jo "It’s no problem. Are you in class now?"
        pl "Yeah, it’s about to end soon. Can I meet you at the forum or somewhere to get it, I need it to buy lunch before my next one."
        "There’s a moment where she doesn’t respond right away and I stare at the three dots for a minute."
        jo "Meet me at the Chatime truck outside of the SAC."
        "Chatime truck?"
        "I think for a moment, not completely sure of what that is before I recall a strange little trailer thing that I see appear in random places on campus. Guess she means that."
        pl "Alright, I’ll be there in ten or so."
        jo "No rush - I’ll probably still be waiting. You want me to get you something?"
        "I have no idea what they sell there but still find myself agreeing in my reply."
        pl "Sure, surprise me!"
        "Almost immediately I flinch and put my phone away as the Professor announces a surprise quiz, groaning with everyone else as we all just want to leave."
        "It seems like eternity before I’m able to scratch a quick response on some scrap paper and drop it off at the front of the hall before jogging out and around the building, making my way to the SAC."

        scene chatime

        "The lines around both of the windows are so long and dense, I almost miss the sight of Jolee until I spot her short figure through the crowd."

        show jolee

        pl "Hey Jolee!"
        "She doesn’t seem to hear me so I get closer. I reach to tap her shoulder and she jolts before turning and relaxing as she sees me."
        pl "Sorry, didn’t mean to scare you."
        jo "Ah no it’s alright. Not the best at keeping an eye out for people."
        "She adjusts her classes before gesturing to the truck in front of us."
        jo "Have you been here before?"
        pl "No, but I can see that I might be the only person who can say that."
        jo "Ha, yeah it’s a pretty popular spot on campus. It started appearing when the boba tea trend took off and it’s been basically a mainstay ever since. You can even use dining dollars here."
        pl "Really? Well if I ever need to buy overpriced campus currency, I’ll make sure to keep that in mind."
        jo "Ah, I forgot you were a lucky commuter who isn’t forced into a meal plan."
        pl "Lucky is relative. At least if you’re late you can just run across campus rather than speeding to the train station and praying you don’t get a ticket."
        jo "Oh no, did you oversleep this morning?"
        pl "Yeah, slept right through the alarm. Got up like 30 minutes late and had to hightail it all the way here. Probably how I ended up dropping the ID."
        jo "Oh right, the ID!"
        "Jolee jolts as if she just remembered that’s why she invited me here. She reaches into her pocket and hands it to me."
        pl "Thanks a bunch, I honestly don’t want to drop $20 on a new one so soon."
        jo "It’s honestly really lucky I even saw it all things considered."
        pl "Well I’m glad you’re balancing me out."
        "I pause as Jolee seems embarrassed again, looking away from me. Before I can ask though, a different voice calls her name out from the chatime truck."
        jo "Oh, here!"
        "She goes over and gets two cups from the window, coming back and holding one out to me."
        pl "Considering that you found my ID, shouldn’t I be the one treating you?"
        jo "I’m paying it forward, you can get the next one."
        pl "Next one hm? I guess I wouldn’t mind enjoying some boba every thursday."
        "I press the straw to my lips…"
        pl "Especially as you have excellent taste in tea."
        jo "Oh I uh, just got you my usual…"
        "She trails off, letting the slurp of her straw finish her sentence."
        jo "Anything fun go on in your class?"
        pl "Just the usual droning and pop quiz."
        jo "Ah, bummer sorry."
        jo "Oh, we’re holding some people up I think - want to move somewhere?"
        "She tries to move forward and away from the line, but bumps into someone else."
        jo "Sorry!"
        "She moves back and bumps again - but into me. I reach my free arm down to put it onto her shoulder and steady her."
        jo "Sorry, sorry, I’m not the best at walking straight."
        pl "You apologize too much, it’s fine, honest."
        "Bashful, she quietly speaks."
        jo "Where do you want to go…?"

        menu:
            "Lead her to a nearby bench.":
                jump joleedatepos

            "Shrug and leave it to her decision.":
                jump joleedateneg

        label joleedatepos:

        $ updateHearts("JOLEE", 1)

        "I firmly put an arm around her shoulders, steering Jolee carefully through the crowd."
        "I feel one of her hands grab onto my arm as we make our way there, both sitting down on a nearby bench."
        "Going to say something I look down at her only to find she’s completely reddened up, her pale skin now resembling a tomato more than anything."
        pl "Sorry! I should have-"
        jo "It’s fine."
        "Her voice is so quiet I almost missed her words."
        "She lets go of my arm - I didn’t even realize she was still holding onto me."
        jo "I’m uh… not trying to get in the way or anything."
        pl "Jolee, you’re not in the way. It’s not your fault you have poor vision or hearing or whatever else may be an issue."
        jo "I mean-"
        pl "No. Listen, what causes it, genetics?"
        jo "Uh, maybe a bit? The main theory is the smog in China. You know, chinese countryside doesn’t have the best medical care or living conditions…"
        jo "By the time my family brought me here I was already losing the lottery, whether it be genetic, environment or something else."
        pl "Then it’s not your fault."
        jo "I could be more careful-"
        pl "No, you’re doing fine. You need to take care of yourself just as much as you take care of everyone else."
        pl "And if you need a bit of help navigating because your eyes were messed up by circumstances out of your control, then I’ll help you."
        "She doesn’t respond for a moment, leaning down and letting her hair shroud her face."
        "For a moment I’m worried I crossed a line before she squeaks out."
        jo "[name]... you’re too nice to me."
        pl "No, if anything, I think you’re too nice to everyone else."
        "She brushes her hair back and I can see a smile on her face as she lifts the boba tea up to her face and takes a sip."
        pl "Okay?"
        jo "...Okay. I’ll put my faith in you then [name]."
        "Jolee looks up at me, holding out her hand as she doesn’t quite meet my gaze."
        jo "Guide me back to the forum?"
        "I take her hand in mine."
        pl "Of course."
        "Getting up from the bench, hand-in-hand, I begin to walk across the wide path with her, going to make our way past the truck and back into the SAC."

        jump joleedateend

        label joleedateneg:

        "I shrug nonchalantly and look around the area before back down at her."
        pl "I don’t really care where we go, up to you."
        jo "Um.."
        "Jolee looks around, squinting as she tries to locate something, the crowd still flowing around us."
        jo "Let’s just head towards the forum I guess."
        "She turns to head around the truck before I grab her sleeve."
        pl "Uh, isn’t it this way?"
        jo "Oh, uh, yeah, right, sorry…"
        "She stammers before going to lead me the other way, both of us beginning to make our way to the front doors of the SAC."

        jump joleedateend

    label joleedateend:

        "The two of us do our best to navigate through the crowd before I slow, feeling that sickening feeling in my stomach again. Jolee looks back at me, concerned."
        jo "[name]?"
        "I cough as I try to answer, nausea making me almost want to kneel over suddenly. Why is this happening again?"
        jo "What happened, was it the tea?"
        pl "N-no it’s just-"
        "Suddenly I hear a familiar voice as a force slams itself into my back. I stumble forward, narrowly avoiding crashing into Jolee."
        mv "Whoa, sorry dude!"
        "I turn around to see a short kid on a skateboard, a wet, sticky feeling settling into my back as he holds the remains of a now-crushed boba cup."
        mv "My bad bro, gotta jet though!"
        "Looking at his face, I can only see the shadow of his hood as he suddenly whizzes away as quickly as he appeared."
        jo "Oh no, your clothes! Are you okay?"
        pl "I’m… fine?"
        "The nauseous feeling disappears as I take Jolee’s hand to stand up, flinching as I feel tea run down my back."
        pl "My clothes around though. I have class soon too, I can’t even go home to change."
        jo "Here, come on, let’s get to the forum. We have some spare clothes laying around, you can find something your size to wear."
        "I let Jolee lead me towards the door, my mind still on what just happened. That can’t all have just been a coincidence… was it?"

        jump friday

    label thursdayalex:

        scene thursday
        "..."

        scene sbuoutside
        "Thursday morning comes and with it, my dreaded 8am class."
        "It’s not even one that happens on Tuesday also, it’s just a blemish on my schedule, dooming me to sleep in and miss it at least once."
        "And this was one such morning."
        "Running across campus to get there in time, I didn’t realize I left something behind until midway through the lecture, my phone buzzed in my pocket."
        al "Hey, do you have your ID?"
        al "I don’t know your last name but the picture looks like you."
        "He sends me a picture of him holding out what is, indeed, my school ID. The background seems to be the parking lot by the train station - I probably dropped it in my rush to get to class."
        "I eye my lecturing professor before I quickly message him back."
        pl "That is it thanks! I didn’t even realize I lost it."
        al "It’s no problem. Are you in class now?"
        pl "Yeah, it’s about to end soon. Can I meet you at the forum or somewhere to get it, I need it to buy lunch before my next one."
        "There’s a moment where he doesn’t respond right away and I stare at the three dots for a minute."
        al "Think you could meet me at the rec center?"
        "My mind conjures up the image of the recreation center, the wide open windows that show off copious amounts of student athletes that all look better than you working out. Alex didn’t strike me as the type but good for him."
        pl "Sure, I’ll head there after this class wraps up. See you in 10?"
        al "Cool, I’ll meet you in the lobby."
        "Almost immediately I flinch and put my phone away as the Professor announces a surprise quiz, groaning with everyone else as we all just want to leave."
        "It seems like eternity before I’m able to scratch a quick response on some scrap paper and drop it off at the front of the hall before jogging out and around the building, making my way to the center."

        scene arcade
        show alex

        "Inside, I look around the lobby confused for a moment before I find Alex, not in workout gear with a gym bag, but standing in front of one of the lobby’s arcade machines, his hands skillfully moving the joystick as he focuses on the game."
        "I walk over to him."
        pl "This does seem a bit more your speed than an intense workout."
        "He doesn’t even flinch as I appear next to him, his concentration apparently strong as steel."
        al "Well, most of the machines here don’t need quarters to play so.."
        "He pauses, a beat passing before the game seems to take a moment to progress to the next level and he looks at me."
        al "Ah, this is where I come to relax sometimes, if I don’t feel like going to the forum just yet."
        pl "Definitely is quieter."
        "Alex digs into his pocket before holding out his ID."
        al "Here’s one slightly scuffed ID card."
        pl "Hey, so long as it still works! I don’t feel like dropping $20 on a new one so soon."
        "His attention is drawn back to the machine as the next level kicks off and he starts playing again."
        pl "You come here a lot I take it?"
        al "Mhm. Most of the leaderboard is me."
        al "May just be because no one else really plays on these though."
        "I lean close to him to peer at the screen, the mess of pixel figures being both unrecognizable and difficult to understand."
        "Alex goes to turn his head slightly towards me and I feel the hair sticking out from under his cap brush against my face."
        "Both of us flinch back but before we can say anything, a game over screen appears between us."
        pl "Ah, sorry!"
        al "N-no that was my bad, it’s fine."
        "He reaches up, lifting up his cap slightly to smooth his hair before he sets it atop his head once more."
        al "Do you want to give it a try?"
        pl "Sure, what kind of game is this?"
        al "It’s a knock-off frogger, somehow combined with Galactica and Pac-man."
        pl "...what?"
        al "Yeah, I don’t really get it either, I just go with it. It’s pretty fun once you get the hang of it."
        "Moving back, he lets me step up to the plate and I grab the joystick in hand, my other hovering over the buttons."
        "The screen lights up as I start a new game, presented with a small pixelated frog."
        "Bold text scrolls across the screen: ‘You are a frog in a land of toads and tadpoles. With no one left to understand you and your kind, seek out a kindred spirit.’"
        pl "This.. this is a children’s arcade game right?"
        al "I don’t think this ended up here because it sold well or anything to be fair."
        "The game surprisingly fits his description pretty well with how chaotic it is jumping from one style to another."
        pl "Are all the arcade games here this existential?"
        al "This is the only one that regularly isn’t broken so I couldn’t say. I do relate to it a bit though."
        pl "Relate how?"
        al "Like I...I’m not trying to sound pretentious. But, sometimes I do think about how lonely it is to be human."
        pl "I don’t think that’s pretentious. Philosophical maybe but not that pretentious. It’s just a bit lonely being the only… you I guess?"
        "Alex stares at the screen as he speaks, the blue and green lights flashing on his face as I see something hollow in his eyes."
        al "Well, we all exist in our own minds and all that we have in there are sketches of people in our lives, good and bad. We're practically in our own mental universes with occasional, brief interactions."
        al "And sometimes I find myself wishing that even if I’m in a world of ‘toads and tadpoles’, that I could somehow find a way to invite someone fully into my head, to know them and to let them know me, even if only briefly."
        al "But then I think about what would happen if someone knew me fully. How would their view change? Would they be disgusted? Would they hate me? Would I even be able to handle that vulnerability?"
        pl "..."
        al "..."
        al "That was… darker than I meant it to be sorry."
        "He reaches up and rubs his face with one hand, letting his eyes stay closed for a moment as I see his ears begin to turn red."

        menu:
            "I feel like I could trust you if such a possibility existed.":
                jump alexdatepos

            "You can trust me with your mind.":
                jump alexdateneg

        label alexdatepos:

            $ updateHearts("ALEX", 1)

            pl "If we were able to mindmeld and lower that barrier for just a bit, I feel like I could trust you Alex."
            al "You.. really?"
            "He lowers his hand to look at me with faint surprise."
            al "You haven’t really known me for that long though, no offense."
            pl "I know I’ve only been in the club for like a week or so at this point, but I do feel like I could trust you to see into my mind, even if you don’t think you’d be comfortable enough to return the favor."
            pl "To be honest, I kind of fear the vulnerability too, but I’d like to understand someone in that way to. It’s a two way street, but there’s no rule saying you have to ride both routes at the same time y’know?"
            al "...Yeah."
            "Alex softly smiles at me and holds my gaze for a moment."
            "Both of us are ripped out of the moment though as my lack of attention finally causes the game to beep with a ‘game over’ screen. Alex laughs at the interruption."
            pl "...there goes that game."
            al "Can’t have you ruining my leaderboard. Scoot over, let me show you how you play."
            "I let Alex lightly hip check me out of the way, leaning against the Machine and watching him start to play."

            jump alexdateend

        label alexdateneg:

            pl "You can trust me with your mind Alex, I wouldn’t do anything bad with it."
            al "You...really?"
            "He lowers his hand but his gaze is a bit wary."
            al "I haven’t really known you for that long though, no offense."
            al "I mean, I don’t think of the people in my life as strangers or anything like that but…"
            "He trails off, shifting uncomfortably in place as he looks away from my eyes to the game screen again."
            pl "It’s alright, there’s no pressure. I’m just letting you know that you can trust me."
            al "...Right."

            jump alexdateend

    label alexdateend:

        play music "<loop 3.5>music/spooky.oga" volume 0.6

        "The silence is interrupted as someone walks up to us. A guy, dressed in an ‘Athletic Teams’ hoodie and sweatpants, holding out a box of candy bars to us both."
        mv "Hi, we’re raising awareness for ALS by giving out free candy bars."
        al "Free you say?"
        "Alex immediately turns and is handed two of them without fanfare while I look at the figure for a moment. Its voice is… I try to place it but I have to press a hand to my stomach as nausea suddenly rises up."
        al "Oh, these are nut-free right?"
        mv "Of course! Keep an eye out for our fundraiser next week, we’ll be raffling off gift baskets at the LDS center!"
        "Pushing through the nausea, I put it together-"
        "It’s the same voice from the bathroom!"
        "Before I can call out though, Alex suddenly opens the wrapper only to drop the candy bar and cover his mouth."
        al "Shit, wait no that has peanuts sticking out of it, what the hell?"
        pl "Are you allergic?"
        al "Deathly! Get rid of it!"
        "I grab the bar and go over, throwing it out in a trash can by the very confused lobby staff. Alex is still covering his face with his sleeves when I go back over to him."
        al "The label said ‘nut free’ in big, bold font, on top of them saying it was, what the fuck was that?"
        pl "Listen, I don’t know what was up with that but-"
        "He stops me, waving his hands as he grabs his backpack."
        al "I need fresh hair and to wash my hands and you really should too before you head to the forum. I’ll see you later."
        "He seems understandably panicked as he rushes off in the direction of the bathrooms as I’m left there, looking over to the arcade machine."
        "As I sling my backpack back on, I realize that I can’t even recall what the guy’s face really looked like."
        "That couldn’t have just been bad luck… right?"

        jump friday

    label thursdaythomas:

        scene thursday
        "..."
        scene sbuoutside

        "Thursday morning comes and with it, my dreaded 8am class."
        "It’s not even one that happens on Tuesday also, it’s just a blemish on my schedule, dooming me to sleep in and miss it at least once."
        "And this was one such morning."
        "Running across campus to get there in time, I didn’t realize I left something behind until midway through the lecture, my phone buzzed in my pocket."
        th "Hey, is this your ID? I found it in one of the train station parking lot."
        th "I don’t know your last name but the picture looks like you."
        "He sends me a picture of her holding out what is, indeed, my school ID."
        "I eye my lecturing professor before I quickly message him back."
        pl "That is it thanks! I didn’t even realize I lost it."
        th "Are you in class right now?"
        pl "Yeah, I must’ve dropped it on my way."
        pl "Can I meet you at the forum or somewhere to get it, I need it to buy lunch before my next one."
        "There’s a moment where he doesn’t respond right away and I stare at the three dots for a minute."
        th "Do you know where Roth Pond is?"
        pl "I assume it’s in Roth Quad? I haven’t been there, but I know generally where it is."
        th "Yup. I’ll be here for awhile, stop by whenever your class is done."
        "Almost immediately I flinch and put my phone away as the Professor announces a surprise quiz, groaning with everyone else as we all just want to leave."
        "It seems like eternity before I’m able to scratch a quick response on some scrap paper and drop it off at the front of the hall before jogging out and around the building, making my way to the Roth."


        scene rothpond
        show thomas

        "I arrive at the lake, slowly revolving around its edge before I spot Thomas on the shore. He’s leaning back and smiling at some geese swimming around, his phone up and seemingly taking photos of the scene."
        pl "Hey Thomas."
        th "Oh, [name], hey."
        "He reaches into his pocket and pulls out my ID card, giving it to me."
        th "Here you go. Try not to lose it again, it costs $20 to replace those."
        pl "Yeah, I definitely don’t feel like dropping any money on that right now."
        th "I’ll uh… see you later I guess. You have class right?"
        "Thomas fiddles with his phone for a moment before hugging his knees closer to his chest, looking at the lake’s surface."
        pl "Well, I think I can spare a bit to relax. Class doesn’t start for another hour or so."
        "I sit down next to him before I look at his wide-eyed expression and suddenly feel awkward."
        pl "I mean, it’s alright if I-"
        th "It is."
        "He messes with his phone again for a moment before he continues."
        th "I don’t really have a lot of people who hang out with me here."
        pl "I’d think you have a bunch of friends in the forum that you can ask to come with."
        th "Well this is moreso my place to come if I want to spend time away from the forum."
        pl "Ah, I see. Guess it’s a bit hard, wanting to spend time away from the forum but not wanting to sit alone all the time?"
        th "Exactly!"
        pl "I can get that feeling, especially when in class you want people you can talk to to ask about assignments or study with but you don’t want to actually… talk to people."
        th "Heh, well don’t let your memes be dreams [name], you should talk to someone."
        pl "Well I could say the same thing to you, can’t I?"
        th "Touche I suppose."
        "We fall silent for a moment before Thomas breaks it."
        th "What do you want to know then?"
        pl "Hm?"
        th "Well, I like not sitting alone and making new friends. So, let’s talk. What do you want to know about me? We did talk a bit yesterday but... "
        pl "Obviously you’re not all ‘honks’ and photos."
        th "That’s one way to say it, yeah."

        menu:
            "What do you like about the forum?":
                jump thomasdateneg

            "What do you do in your offtime?":
                jump thomasdatepos

        label thomasdateneg:

            "Thomas frowns slightly."
            th "The forum? You’re not curious about anything else?"
            pl "I couldn’t really think of another question sorry."
            th "It’s alright just… I dunno, the forum is a place to hang with my friends and make memories I guess."
            th "Not sure there’s much more I can say on it."
            pl "Alright."
            "We fall into an uncomfortable silence as neither of us seem sure of what else to say."

            jump thomasdateend

        label thomasdatepos:

            $ updateHearts("THOMAS", 1)


            pl "What do you do in your offtime? Besides, y’know, goose photography."
            th "Heh, my offtime eh? I guess this does take up a decent bit of my time."
            th "But besides this and memeing around… I think the thing I like to do the most is look at the sky."
            pl "Like, cloud-watching?"
            th "Stargazing mostly. I am studying Astronomy so…"
            pl "So if I was to say that pluto should be a planet..?"
            "He narrows his eyes at me but cracks a smile."
            th "I’m sorry, but I’d have to remove you for this transgression."
            pl "Fair enough, I take it back."
            th "Eh, it’s all water down the duck’s back."
            pl "Don’t you mean goose?"
            "Thomas stops for a moment before he laughs, his hand being pressed to his chest for a moment."
            th "...I think you’re fitting in fine [name]."
            "He goes to place his hand down and I feel it graze against mine. Instinctively, we both look down and then at each other."
            "But after a moment, his smile relaxes and he leaves it there, leaning back as we both fall into a pleasant silence."

            jump thomasdateend

    label thomasdateend:

        play music "<loop 3.5>music/spooky.oga" volume 0.6

        "As we sit by the lakeside, I watch the water’s surface for a moment before I feel a wave of nausea wash over me. I jerk my hand to my mouth and Thomas looks over at me, concerned."
        th "You feel alright [name]?"
        pl "I just…"
        "I go to try to stand up only to feel a sudden force in my back."
        th "[name]!"
        pl "Shit-!"
        "I go careening forward and hit the surface of the pond face-first, the water quickly giving way to mud."
        "I feel Thomas’s hands reach and grab onto my shirt, struggling to pull me out of the water, but I’m able to land on my back on the pondside, the entire scene gathering plenty of attention of the various dorms looking down on us."
        th "[name] are you okay?!"
        "I cough out some pond muck but give him a thumbs-up as I catch my breath."
        pl "...y-yeah. It felt like something… knocked me in."
        "I look around but there’s no one but us."
        th "You’re soaked and covered in mud! Come on, there’s some spare clothes in the forum. We can probably get you into the rec center so you can shower there maybe?"
        pl "That works…"
        "He pulls me up and I let Thomas start leading me down the path."
        "Was this shit luck or… was that really similar to what happened to me in the bathroom?"

        jump friday

    label thursdaytaylor:

        scene thursday
        "..."
        scene sbuoutside

        "Thursday morning comes and with it, my dreaded 8am class."
        "It’s not even one that happens on Tuesday also, it’s just a blemish on my schedule, dooming me to sleep in and miss it at least once."
        "And this was one such morning."
        "Running across campus to get there in time, I didn’t realize I left something behind until midway through the lecture, my phone buzzed in my pocket."
        ta "Hey nerd, do you have your ID?"
        ta "I don’t know your last name but the picture looks like you."
        "She sends me a picture of her holding out what is, indeed, my school ID. The background seems to be outside of the SAC. Guess I dropped it as I ran past."
        "I eye my lecturing professor before I quickly message her back."
        pl "That is it thanks! I didn’t even realize I lost it."
        ta "I guess I can give it back to you, but you need to buy me lunch sometime. Are you in a class right now?"
        pl "Yeah, it’s about to end soon. Can I meet you at the forum or somewhere to get it, I need it to buy lunch before my next one."
        "There’s a moment where she doesn’t respond right away and I stare at the three dots for a minute."
        ta "Think you could meet me outside the SAC? The side entrance, facing the library."
        pl "Alright, I’ll be there in ten."
        "Almost immediately I flinch and put my phone away as the Professor announces a surprise quiz, groaning with everyone else as we all just want to leave."
        "It seems like eternity before I’m able to scratch a quick response on some scrap paper and drop it off at the front of the hall before jogging out and around the building, making my way to the SAC."

        scene sbuoutside
        show taylor

        "I find Taylor waiting outside, her head bopping along to music from her headphones before she pulls them out at my approach."
        ta "Took you long enough dude, I was ready to sit down - and let me warn you, when that happens I don’t get back up."
        pl "The class had a pop quiz at the end, I got held up in the dogpile to hand the paper in."
        ta "Ah yes, large lecture halls. I don’t have such issues with my humanities lifestyle."
        "She reaches into her pocket as she tosses me back my ID."
        ta "Try not to lose it again, hm? It’s $20 for a replacement."
        pl "I won’t, I was just running late this morning and must’ve dropped it in the rush."
        ta "Ah, imagine not having the luxury of being able to wake up ten minutes before class and getting there with five to spare."
        pl "Hardy har har, not all of us can be residents or so lazy as to not run to class."
        ta "For your information, I do exercise in some capacity. I was actually on my way to go do that now."
        pl "Where, the gym? You don’t have a gym bag."
        ta "No, somewhere even better."
        ta "I’ll allow you to join me… if you do something for me."

        menu:
            "I'll do whatever you want.":
                jump taylord1

            "Is this your way of inviting me?":
                jump taylord2


        label taylord1:

            ta "Then perish."
            ta "Nah just kidding, but I do intend to bug you to buy me food sometime in the future."

            jump taylordcon

        label taylord2:

            ta "Hush with your logic, all I ask is for sustenance.."
            pl "Sustenance?"
            ta "I know I look skinny, but I can outeat anyone in the forum and then some. It takes a lot to sustain this mortal form."

            jump taylordcon

    label taylordcon:

        ta "Even if you can’t buy me something now though, I’ll let you tag along anyway though. Gets a bit awkward going there alone honestly."
        pl "You want me for company because it’s convenient? I’m honored."
        ta "Gods, don’t get a big head. If I felt like going down stairs I would go grab people from there but you’re already here, on ground level."
        "She waves for me to follow her."
        ta "Come on, it’s in the Staller Center."
        pl "Isn’t that the big music-theatre thing?"
        ta "Yup. And within there’s something much more fun than an old music room."
        "I follow Taylor across campus and we slip into the large building with ease. She moves through the maze inside like it’s second nature and eventually we end up at the door of what seems like a disused classroom."
        pl "Is this where you push me in and I’m never seen again?"
        ta "You wish, you’re not allowed to escape this life that quickly nerd. Feast your eyes upon this!"

        scene vrroom

        "She pushes the door open to reveal a large projector and screen set up displaying a steam library, connected to a dual-monitor computer and a Vive headset."
        ta "Welcome to the secret VR studio on campus!"
        "A student sits at the computer, turning around to give a wave."
        ta "Oh yeah and this is Ned, the room monitor. He fuels my madness by downloading beat saber mods when I’m not looking."
        ta "But yeah, this is my favorite place on campus honestly besides the forum, it just opened last spring."
        pl "This is amazing! Who set this up, who runs it?"
        ta "One of the campus’s many great, kooky professors set it up through the iCreate. Honestly I’m glad he did though."
        ta "Would be a shame if something crazy like a pandemic happened and caused it to shut down right after it opened and probably sabotaged all the professor’s efforts, especially after he said that he’s been fighting with administration for years to open it."
        ta "..."
        pl "..."
        ta "...MIX Studio space on iCreate, look it up."
        ta "Anyway!"
        ta "It’s Beat Saber time?"
        pl "They have Beat Saber?"
        ta "Dude, they have so many games honestly, but Beat Saber is probably one of the few forms of exercise I can do without breaking my body in two."
        pl "Really? You don’t strike me as fragile."
        ta "Yeah, people usually don’t realize it until I’m already dying inside. I once pulled my shoulder in high school trying to lift a kettlebell weight that was only like, 5 pounds - I got a whole mess of lung and muscle problems."
        ta "Probably should be more careful but eh, I’ll try anything once."
        "She reaches up and I watch Taylor pull off her glasses and the beanie. She pulls out a scrunchie, tying her hair back before she goes to put the headset on."
        ta "Alrighty, beam me up Scotty, let’s go!"
        "The desk monitor starts up Beat Saber and Taylor immediately selects one of the hardest songs I can see."
        pl "You sure about this?"
        ta "Of course, I’m an expert Beat Saber player at this point."

        scene timeskip
        "..."

        scene vrroom
        ta "Oh gods, why did I think Camellia was a good idea, it’s never a good idea-!"
        "She laughs as her arms flail around, the screen showing her lightsabers missing nearly every block before the entire scene collapses into a ‘game over’."
        pl "You say that a lot."
        "Taylor reaches up to push the headset up, blinking a few times before she focuses on me."
        ta "What, that something I did wasn’t a good idea? That’s usually the catchphrase of people around me rather than my directly."
        pl "No, ‘gods’. You say it as a plural rather than singular."
        ta "Oh. Well, yeah."
        pl "You believe in multiple?"
        ta "Nah, I believe in ‘God’ to some extent. I just don’t think the dude deserves to be worshipped."
        ta "Plus, I like to think that there’s some weird, probably primordial force going on. Fate, life, whatever."
        pl "Like Karma?"
        ta "Yeah, something like that. It’s an on-going joke in the forum that this is an anime and I’m just one of the main characters."
        pl "I could believe that."
        ta "You don’t know the half of it dude, there’s so many things that happen that it just can’t be coincidence. Not even big things, sometimes it’ll be something small like me declaring I don’t want to go to class and getting an email a few minutes later."
        "She slips the headset back on and goes to start a new level."
        pl "That’s probably the best superpower."
        ta "If you think that’s good, wait until you meet Ken. That guy has some big luck energy! You know one time during a DnD game, he rolled like three nat 20s in a row-"
        "Taylor stops as the room monitor cuts her off, asking if she can wait to start another level as he needs to use the bathroom."
        ta "Oh sure dude. You know I’ll guard this room with my life, I’ll cover for you."
        "He thanks her and darts out quickly, legs slightly crossed as she runs."
        ta "Pfft, Ned always starts his shift with a big gulp from 7/11 and wonders why he can never get through the entire thing without taking a break."
        "She pulls the Vive off entirely, shaking out her hair. She looks at me, a faint outline from where the device pressed against her face, her hair otherwise gently framing her grinning expression."
        "Taylor places it down as she grabs her glasses but doesn’t put them on, sitting next to me."
        ta "Well [name], how’s your first trip to the VR studio?"
        pl "Might be a bit more fun if I got to play it."
        ta "Oh haha. Fine, when Sir Small-bladder gets back, we can set it up for your vision and height and shit. I’ll throw you into Camelia and see how you like it."
        pl "I probably could nail that level."
        ta "Willing to bet on it?"
        pl "...Alright, I’m not that confident."
        ta "Mhm, that’s what I thought."
        "Taylor leans back in the seat, letting her eyes shut for a moment as her head rests on the wall. I look at her for a moment. Without the beanie or glasses on, it’s pretty easy to pick out things like the bags under her eyes or the small streaks of grey going through her hair."
        ta "I can feel you looking at me."
        "She creaks one of her eyes open at me, chuckling."
        ta "What’s up?"
        pl "Nothing much. You just don’t really…"
        ta "Relax? Take the beanie off?"
        pl "Both?"
        ta "Ah, well, in the vein of being the anime character, where am I without my dramatic backstory?"
        pl "How dramatic?"
        ta "A Silent Voice levels of drama? Probably a bit shorter than Clannad, maybe sprinkled in some Persona 5 levels of utter bs-itude… do you get any of these references?"

        menu:
            "Yes.":
                jump taylord3

            "No.":
                jump taylord4

        label taylord3:

            ta "Well good because I got more."

            jump taylordcon2

        label taylord4:

            ta "Well too bad because I got more."

            jump taylordcon2

    label taylordcon2:

        pl "Dare I ask how many more?"
        ta "Enough to fill up the time before Ned is done drowning probably."
        pl "He’s been gone for awhile yeah."
        ta "Well maybe that’s just another power of mine, drawing out the time in the name of fun."
        pl "You’re having fun right now?"
        ta "I’m not all pranks and chaos. I have my downtime, I enjoy talking to people just like the next guy. Albeit, I do enjoy it in probably smaller amounts than the average person."
        ta "It’s easier to talk at a club room than to a specific person, but you are quite an easy person to talk to [name]."
        pl "Well thank you, I try."
        ta "Hmm, I am curious though…"
        pl "About what?"
        ta "A lot of things to be fair, but right now, I will say that I may be most curious about you."
        "Taylor leans a bit closer to me, her eyes scrutinizing."
        pl "What about me?"
        ta "Well I don’t know. What is your deal [name]?"
        pl "My deal?"
        ta "Beyond the fact that you’ve reverted to a parrot, yes, your deal. You come into the club, make friends with everyone, you’ve fallen in like a puzzle piece. Like you belonged here the whole time."
        pl "Thank you…?"
        ta "It wasn’t completely meant as a compliment. What I’m asking I guess is - what’s your endgame? What do you want to get out of the Forum? Friends and memories? Games and Fun? A place to chill out and nothing more?"
        pl "Are all those mutually exclusive?"
        "She eyes me for another moment, not saying anything right away."
        ta "The forum is the oldest club on campus. It’s unique in the fact that it basically has a vast array of alumni who are basically dedicated to it after graduation, probably more than they should be."
        ta "They come visit, they have support groups for each other - hell, a former forumite passed away last year and they left the club money in their will."
        pl "That is a lot of passion for the club."
        ta "So, when you come in, so smoothly slipping yourself into its folds, I’m inclined to ask… what’s brought you here?"

        menu:
            "I want to meet people like you.":
                jump taylordatepos

            "I want to have fun like you.":
                jump taylordateneg

        label taylordatepos:

            $ updateHearts("TAYLOR", 1)

            pl "I joined because I want to meet people like you Taylor."
            "Her eyes widen and she suddenly falls back into her seat as if I knocked her down. A moment passes before she seems to process what I said."
            "Her hand suddenly reaches and smacks me upside the head."
            ta "You idiot! What are you trying to do with a smooth line with that?!"
            "I look up at her, her expression actually embarrassed as she blushes and pouts at me."
            pl "Well I just-"
            ta "Just nothing, what do you take me for?"
            pl "Cute?"
            "She lets out a groan of exasperation."
            ta "Stop that!"
            pl "Stop what?"
            ta "Stop- fu- aah! Stop complimenting me!"
            pl "Do you not like getting complimented?"
            ta "No, I don’t like it when people pull smooth one-liners or try to call me cute or anything like that. If anything I should be the one trying to pull the flirty one-liners!"
            pl "You want to try flirting with me?"
            "What she just said seems to hit her and she waves her arms around."
            ta "Nope, nope forget it, I am burying you at dawn, they’re going to find you under one of the trees in the forests around Tabler."

            jump taylordateend

        label taylordateneg:

            pl "I want to have fun like you do in the forum."
            ta "Ah, I see. I guess I should have realized that much."
            "She leans back from me with a sigh, seeming more tired than before."
            pl "Is there something wrong with that?"
            ta "Hm? Oh no, nothing wrong with that. A lot of people just join to fuck around, I won’t diss them."
            pl "That’s what you do isn’t it? Just fuck around and do your mischief thing?"
            ta "Yeah. Just one dyejob short of going full Manic Pixie Dream Girl I guess. You don’t seem like the brooding, soulful type though."
            pl "Well, you’re not just some flat character, you do have a whole life around you."
            ta "I guess."

            jump taylordateend

    label taylordateend:

        play music "<loop 3.5>music/spooky.oga" volume 0.6

        "She doesn’t even seem like she believes what she’s saying, but as she stands up the monitor walks back in, apologizing for the delay."
        ta "Ah my knack for perfect timing kicks in one more, great!"
        pl "Are you-"
        ta "Yes I’m going again. I am going to stab these blocks with light sabers one more time before you go and it’s not up for debate."
        "Taylor slips the headset back on and starts another level before I have the chance to protest and I watch her twirl and slam through the blocks to the beat of the song."
        "Even though I’m sitting still, I feel a wave of nausea go over me as Ned suddenly looks over and comments on the time."
        "Pulling out my phone, I jolt to sit up as I realized how much time had passed. I was going to be late for my next class! I jump to my feet but feel the nausea and dizziness only intensify."
        pl "Shit, I need to run Taylor, I got to g-"
        "Looking up, I realize my mistake too late as I stumble forward and Taylor’s controller-bearing fist collides with my nose."
        ta "Oh shit!"
        "Immediately, she pulls the headset and controller off and the monitor jumps up as well."
        ta "Ned, tissues!"
        "She’s handed tissues which she hands to me as I smack my lips tasting blood."
        pl "..Ow."
        ta "Shit, I’m sorry dude, I didn’t realize you’d stood up, are you alright? How many fingers am I holding up?"
        pl "Thero."
        "I stop."
        pl "Thero. What? I’m trying to thay thero… oh no."
        "Taylor winces as the game over sounds play from the still-running game around us. She lightly presses the tissues to my face."
        ta "Maybe let’s not try talking for now. Come on, we have a proper first aid kit in the forum, we can probably get a compress or… something. We have a Jolee in the forum, we can ask her to fix it."
        "She leans over, grabbing her stuff and mine instantly, sighing as she stands."
        ta "Jesus you have a lot of books. Come on, let’s get to the forum before these packs drag me to the center of the earth, hold the tissues to your… nose-mouth region."
        "I silently oblige, not trusting my own speaking ability as Taylor carefully guides me out of the room."
        ta "Late to your morning class and then you get decked by me… not your lucky day [name], is it?"
        "We head out of the center and off to the forum."

        jump friday

    label friday:

        scene friday
        play music "<loop 26.766>music/forum.oga" volume 0.6
        "..."

        scene forummainclapcheeks

        "The GBM is uneventful honestly."

        show jolee

        jo "If there’s nothing else anyone has to add then I think we can mark this GBM as over!"
        jo "Thanks again to Alex for stepping in as temporary secretary while ours is studying abroad."
        jo "And hopefully our President will be able to be back here soon when he gets out of the hospital from his broken femur!"

        show taylor at left

        "Taylor walks in almost immediately after the meeting ends."
        ta "What a shame that only one bone broke."

        show thomas at right

        th "Dare I ask if you were involved?"
        ta "Dare you involve yourself with my answer?"
        th "Touche. Come on, let’s get our stuff, we got class."
        "Everyone mills about for a moment and I watch Alex, Taylor, Jolee and Thomas get their stuff."
        pl "All of you have class now?"

        hide jolee
        show alex

        al "Yeah, somehow all our schedules lined up to have class after meeting."
        ta "Me and Jolee are in the same SBC! The other two nerds have normal classes though."
        th "As normal as physics could be considered."
        "As I watch them all move to leave, I feel a pain in my chest. Like I’m about to miss a chance."
        mv "Don’t…"
        "Valentine’s day is Sunday… maybe I can be lucky this year?"
        pl "Hey wait up-!"

        hide alex
        hide thomas
        hide taylor

        python:
            chosen_date = renpy.display_menu([("Alex","ALEX"),("Jolee","JOLEE"),("Taylor","TAYLOR"), ("Thomas","THOMAS")])
            renpy.jump(findDate(chosen_date))


    # Beginning of endings
    label alex_gpa_rock_end:
        show alex
        pl "Hey wait up Alex!"
        "Alex pauses, looking back at me curiously."
        al "Yeah, what’s up?"
        pl "Can I… talk to you for a minute? Alone?"
        al "Oh uh, sure. You guys can go ahead without me, I’ll catch up."
        "He waves to the others before stopping out in the hall. I realize we’re both under the cherry blossom they made and my heart skips a beat."
        al "What is it [name]?"

        menu:
            "I like you.":
                jump alexahead

        label alexahead:

            al "Y-you what?"
            pl "I like you and I wanted to know if you wanted to go out together on sunday for Valentine’s day?"
            al "[name]... I’m flattered but I kind of like someone else in the club."
            pl "Oh..who?"
            al "I actually planned on confessing later. To Jolee. I’m sorry dude. But I just don’t like you like that. We can still be friends though?"
            pl "Yeah. I get it…"
            "Alex winces at my response but waves."
            al "I got to go to class...later."
            pl "Later."
            "I stand there in dejected silence as Alex heads up the stairs and out of the basement, unsure of what to do next. Then suddenly I hear it."
            hide alex
            show gpa_rock
            play music "<loop 3.5>music/spooky.oga" volume 0.6

            gpa "I’ll go out with you [name]!"
            pl "The GPA rock!?"
            gpa "I must confess to you [name], I’ve been hopelessly in love with you ever since I laid my keychains on you!"
            pl "You’re… you’re a rock! Rocks don’t have brains or rights, you shouldn’t even be talking to me right now!"
            gpa "The power of love has animated me! Now I am here to resolve your relationship woes and end this sad attempt at a plot!"
            pl "Plot? What plot!?"
            gpa "Hush my love, you’re safe now. Now we can end this all with a kiss!"
            pl "What the hell? What are you talking about? What plot, what’s going on?"
            pl "No don’t get closer, stay back!"
            pl "Don’t pull the chainmail off no!"
            pl "No!"
            pl "NOOOOOOOOOOOOOOOOO!"

            "Ending C: Unlucky Valentine."
            return

    label jolee_gpa_rock_end:
        show jolee
        pl "Hey wait up Jolee!"
        "Jolee pauses, looking back at me curiously."
        jo "Yeah, what’s up?"
        pl "Can I… talk to you for a minute? Alone?"
        jo "Oh uh, sure. You guys can go ahead without me, I’ll catch up."
        "She waves to the others before stopping out in the hall. I realize we’re both under the cherry blossom they made and my heart skips a beat."
        jo "What is it [name]?"

        menu:
            "I like you.":
                jump joleeahead

        label joleeahead:

            jo "Y-you what?"
            pl "I like you and I wanted to know if you wanted to go out togejoer on sunday for Valentine’s day?"
            jo "[name]... I’m flattered but I kind of like someone else in joe club."
            pl "Oh..who?"
            jo "I actually planned on confessing later. To Thomas. I’m sorry dude. But I just don’t like you like joat. We can still be friends joough?"
            pl "Yeah. I get it…"
            "Jolee winces at my response but waves."
            jo "I got to go to class...later."
            pl "Later."
            "I stand there in dejected silence as Jolee heads up joe stairs and out of joe basement, unsure of what to do next. joen suddenly I hear it."
            hide jolee
            show gpa_rock
            play music "<loop 3.5>music/spooky.oga" volume 0.6

            gpa "I’ll go out with you [name]!"
            pl "The GPA rock!?"
            gpa "I must confess to you [name], I’ve been hopelessly in love with you ever since I laid my keychains on you!"
            pl "You’re… you’re a rock! Rocks don’t have brains or rights, you shouldn’t even be talking to me right now!"
            gpa "The power of love has animated me! Now I am here to resolve your relationship woes and end this sad attempt at a plot!"
            pl "Plot? What plot!?"
            gpa "Hush my love, you’re safe now. Now we can end this all with a kiss!"
            pl "What the hell? What are you talking about? What plot, what’s going on?"
            pl "No don’t get closer, stay back!"
            pl "Don’t pull the chainmail off no!"
            pl "No!"
            pl "NOOOOOOOOOOOOOOOOO!"

            "Ending C: Unlucky Valentine."
            return

    label taylor_gpa_rock_end:
        show taylor
        pl "Hey wait up Taylor!"
        "Taylor pauses, looking back at me curiously."
        ta "Yeah, what’s up?"
        pl "Can I… talk to you for a minute? Alone?"
        ta "Oh uh, sure. You guys can go ahead without me, I’ll catch up."
        "She waves to the others before stopping out in the hall. I realize we’re both under the cherry blossom they made and my heart skips a beat."
        ta "What is it [name]?"

        menu:
            "I like you.":
                jump taylorahead

        label taylorahead:

            pl "I like you and I wanted to know if you wanted to go out together on sunday for Valentine’s day?"
            ta "[name]... I’m flattered but I kind of like someone else in the club."
            pl "Oh..who?"
            ta "I actually planned on confessing later. To Alex. I’m sorry dude. But I just don’t like you like that. We can still be friends though?"
            pl "Yeah. I get it…"
            "Taylor winces at my response but waves."
            ta "I got to go to class...later."
            pl "Later."
            "I stand there in dejected silence as Taylor heads up the stairs and out of the basement, unsure of what to do next. Then suddenly I hear it."
            hide taylor
            show gpa_rock
            play music "<loop 3.5>music/spooky.oga" volume 0.6

            gpa "I’ll go out with you [name]!"
            pl "The GPA rock!?"
            gpa "I must confess to you [name], I’ve been hopelessly in love with you ever since I laid my keychains on you!"
            pl "You’re… you’re a rock! Rocks don’t have brains or rights, you shouldn’t even be talking to me right now!"
            gpa "The power of love has animated me! Now I am here to resolve your relationship woes and end this sad attempt at a plot!"
            pl "Plot? What plot!?"
            gpa "Hush my love, you’re safe now. Now we can end this all with a kiss!"
            pl "What the hell? What are you talking about? What plot, what’s going on?"
            pl "No don’t get closer, stay back!"
            pl "Don’t pull the chainmail off no!"
            pl "No!"
            pl "NOOOOOOOOOOOOOOOOO!"

            "Ending C: Unlucky Valentine."
            return

    label thomas_gpa_rock_end:
        show thomas
        pl "Hey wait up Thomas!"
        "Thomas pauses, looking back at me curiously."
        th "Yeah, what’s up?"
        pl "Can I… talk to you for a minute? Alone?"
        th "Oh uh, sure. You guys can go ahead without me, I’ll catch up."
        "He waves to the others before stopping out in the hall. I realize we’re both under the cherry blossom they made and my heart skips a beat."
        th "What is it [name]?"

        menu:
            "I like you.":
                jump thomasahead

        label thomasahead:

            th "Y-you what?"
            pl "I like you and I wanted to know if you wanted to go out together on sunday for Valentine’s day?"
            th "[name]... I’m flattered but I kind of like someone else in the club."
            pl "Oh..who?"
            th "I actually planned on confessing later. To Taylor. I’m sorry dude. But I just don’t like you like that. We can still be friends though?"
            pl "Yeah. I get it…"
            "Thomas winces at my response but waves."
            th "I got to go to class...later."
            pl "Later."
            "I stand there in dejected silence as Thomas heads up the stairs and out of the basement, unsure of what to do next. Then suddenly I hear it."
            hide thomas
            show gpa_rock
            play music "<loop 3.5>music/spooky.oga" volume 0.6

            gpa "I’ll go out with you [name]!"
            pl "The GPA rock!?"
            gpa "I must confess to you [name], I’ve been hopelessly in love with you ever since I laid my keychains on you!"
            pl "You’re… you’re a rock! Rocks don’t have brains or rights, you shouldn’t even be talking to me right now!"
            gpa "The power of love has animated me! Now I am here to resolve your relationship woes and end this sad attempt at a plot!"
            pl "Plot? What plot!?"
            gpa "Hush my love, you’re safe now. Now we can end this all with a kiss!"
            pl "What the hell? What are you talking about? What plot, what’s going on?"
            pl "No don’t get closer, stay back!"
            pl "Don’t pull the chainmail off no!"
            pl "No!"
            pl "NOOOOOOOOOOOOOOOOO!"

            "Ending C: Unlucky Valentine."
            return

    label alex_end:

        pl "Hey wait up Alex!"

        show alex

        "Alex pauses, looking back at me curiously."
        al "Yeah, what’s up?"
        pl "Can I… talk to you for a minute? Alone?"
        al "Oh uh, sure. You guys can go ahead without me, I’ll catch up."

        hide alex
        scene hallwaysakura
        show alex

        "He waves to the others before stopping out in the hall. I realize we’re both under the cherry blossom they made and my heart skips a beat."
        al "What is it [name]?"

        menu:
            "I like you.":
                jump alexendcon

        label alexendcon:

        al "Y-you what?"
        pl "I like you and I wanted to know if you wanted to go out together on sunday for Valentine’s day?"
        al "I-"

        # First Rewind begins
        hide alex
        scene bwhallwaysakura

        pl "{cps=200}I like you and I wanted to know if you wanted to go out together on sunday for Valentine’s day?{/cps}{nw}"
        al "{cps=200}Y-you what?{/cps}{nw}"
        pl "{cps=200}I like you.{/cps}{nw}"
        al "{cps=200}What is it [name]?{/cps}{nw}"

        scene bwforummainclapcheeks

        al "{cps=200}Oh uh, sure. You guys can go ahead without me, I’ll catch up.{/cps}{nw}"
        pl "{cps=200}Can I… talk to you for a minute? Alone?{/cps}{nw}"
        al "{cps=200}Yeah, what’s up?{/cps}{nw}"
        pl "{cps=200}Hey wait up Alex!{/cps}{nw}"
        th "{cps=200}As normal as physics could be considered.{/cps}{nw}"
        ta "{cps=200}Me and Jolee are in the same SBC! The other two nerds have normal classes though.{/cps}{nw}"
        al "{cps=200}Yeah, somehow all our schedules lined up to have class after meeting.{/cps}{nw}"
        pl "{cps=200}All of you have class now?{/cps}{nw}"
        th "{cps=200}Touche. Come on, let’s get our stuff, we got class.{/cps}{nw}"
        ta "{cps=200}Dare you involve yourself with my answer?{/cps}{nw}"
        th "{cps=200}Dare I ask if you were involved?{/cps}{nw}"
        ta "{cps=200}What a shame that only one bone broke.{/cps}{nw}"

        # First Rewind Ends

        scene forummainclapcheeks
        play music "<loop 26.766>music/forum.oga" volume 0.6

        show jolee

        jo "If there’s nothing else anyone has to add then I think we can mark this GBM as over!"
        "Wait…"
        jo "Thanks again to Alex for stepping in as temporary secretary while ours is studying abroad."
        "Wait we just did this, didn’t we?"
        jo "And hopefully our President will be able to be back here soon when he gets out of the hospital from his broken femur!"
        pl "What the…"

        show taylor at left

        ta "What the what?"
        "Taylor walks in almost immediately after the meeting ends like before."
        ta "More like what a shame that only one bone broke."

        show thomas at right

        th "Dare I ask if you were involved?"
        ta "Dare you involve yourself with my answer?"
        th "Touche. Come on, let’s get our stuff, we got class."
        "Everyone mills about for a moment and I watch Alex, Taylor, Jolee and Thomas get their stuff again. They’re just...going through the motions again."
        "What is this groundhog day?"
        pl "You guys all have class together…"

        hide jolee
        show alex

        al "Yeah, somehow all our schedules lined up to have class after meeting."
        ta "Me and Jolee are in-"
        pl "In the same SBC."
        ta "Yeah, how’d you guess?"
        pl "You uh.. Mentioned it before."
        "As I watch them all move to leave, I feel a pain in my chest. It’s stronger than before. Maybe I did something wrong. I never heard their answer."
        mv "Don’t…!"
        "They’re all going to leave again."
        "I refuse to let this be the end of it."
        pl "Hey wait up-!"

        hide alex
        hide thomas
        hide taylor

        # Rewind Two Begins

        scene bwforummainclapcheeks

        pl "{cps=200}Hey wait up-!{/cps}{nw}"
        pl "{cps=200}You uh.. Mentioned it before.{/cps}{nw}"
        ta "{cps=200}Yeah, how’d you guess?{/cps}{nw}"
        pl "{cps=200}In the same SBC.{/cps}{nw}"
        ta "{cps=200}Me and Jolee are in-{/cps}{nw}"
        al "{cps=200}Yeah, somehow all our schedules lined up to have class after meeting.{/cps}{nw}"
        pl "{cps=200}You guys all have class together…{/cps}{nw}"
        th "{cps=200}Touche. Come on, let’s get our stuff, we got class.{/cps}{nw}"
        ta "{cps=200}Dare you involve yourself with my answer?{/cps}{nw}"
        th "{cps=200}Dare I ask if you were involved?{/cps}{nw}"
        ta "{cps=200}More like what a shame that only one bone broke.{/cps}{nw}"
        ta "{cps=200}What the what?{/cps}{nw}"
        pl "{cps=200}What the…{/cps}{nw}"

        # Rewind Two Ends
        play music "<loop 3.5>music/spooky.oga" volume 0.6

        pl "FUCK!"
        "I slam my hand into the shelf next to me, looking around to see that no one reactions to my outrage."
        "No one reacts at all. They’re just.. Frozen."
        mv "...Stop trying to get a happy ending."
        pl "What the hell? Who are you? Show yourself! I know I heard you before in the bathroom!"
        mv "Yes, I am the voice in the bathroom. I am the reason your little spontaneous dates ended poorly. I am the reason you even exist to be quite honest. Please spare me the monologue of realization, I haven’t got the patience."
        mv "There was an error in the system, you’re supposed to be a side character, not the main character of this story - you don’t get a love interest. You’re supposed to be nameless."
        pl "What are you talking about, what do you mean a side character?"
        mv "I mean a side character. A nobody. A blank slate. A faceless part of the crowd who exists only to move the plot forward."
        pl "You’re talking like this is a story."
        mv "Well it is a story. And somehow, you found yourself lucky enough to slip through the cracks and put yourself at the forefront of this tale."
        pl "Then if this is all a story, who are you?"
        mv "I am…"

        show gwee

        mv "Something beyond your comprehension."
        pl "You’re a sharkpuppy."
        mv "No! I mean, yes I’m a shark puppy currently, but my form is unimportant-"
        pl "Kind of an edgelord with that hood too."
        mv "No! My hood is my uniform, you don’t see me insult your all grey appearance and lack of eyes!"
        pl "I’m not all grey I’m (insert skin color) with (insert eye color) eyes!"
        mv "...Right."
        pl "So are you a blue Kyube-"
        mv "No! Don’t even joke about that, even extradimensional beings are scared of copyright!"
        mv "I am what is best translated into your language as the ‘Narrator’."
        mv "I am the dictator of your world, not in that I rule it but that I dictate all that happens. I am the one who determines everything from the tweet of the birds to the turning of the Earth. I may loose the arrows of love or break the hearts of fools."
        pl "So… Cupid?"
        mv "...You are really annoying the one person that can remove you from existence."
        pl "I feel like if you could do that, you would have already."
        mv "Cute."
        pl "So what is the point of all this? Freezing and rewinding time, using the force or whatever it is you do to interrupt my life - what’s the end goal?"
        mv "Originally, it was to simply redirect you away and back into your proper place but despite my jinxing, you managed to still make something of it all."
        pl "I’m just trying to live my life man-"
        mv "First off I am no ‘man’, and second off, you don’t get a say in that. It is my story, you are my character and you need to know your place. The characters I create are made lucky, born for everything to go their way. You are lucky to have been made at all."
        al "Normally I'd say, 'say your prayers,' but nobody's coming to help you. How ironic."

        show alex at left
        play music "<loop 10.0>music/alex.oga" volume 0.6

        "I look past the entity to see a beautiful sight of an infuriated Alex pulling a bat out from behind one of the shelves."
        pl "Alex!"
        mv "How are you not frozen!?"
        al "Don’t know, don’t care, go fuck yourself."
        al "This is our story, not yours and whether or not you started it, we’ll be the ones ending it - lucky or unlucky."
        "Alex starts to come towards me, but the ‘Narrator’ turns and tries to swipe him with his tail."
        mv "You insolent child!"
        "I try to dash forward as Alex ducks. One of the ‘Narrator’s’ grubby little hands grabs onto Alex’s hoodie, tightening the strings around his neck. He gasps for air."
        al "[name]!"
        "His bat clatters to the ground."
        mv "You fail to realize that you are alone here you useless character! There is only darkness and death if you try to fight the very being that gives you life!"
        "I resist the urge to charge into it as Alex’s frantic hand points to the knife on the ground, going towards the weapon instead."
        mv "Can you feel your heart burning? Can you feel the struggle within? The fear within me is beyond anything your soul can make."
        "Grabbing the ground, I whip it around and slam it into the strange entity. It lets Alex go and I quickly grab his arm, pulling him back as he coughs, struggling to catch his breath."
        "It’s head slowly turns to look at us."
        mv "You cannot kill me in a way that matters. No matter how strong you are, I am beyond strength."
        "The knife seems to be absorbed into its skin as it takes a short breath in and lets a long breath out."
        mv "I may have lost my temper."
        al "What the fuck is wrong with you!?"
        mv "You try watching your life’s work crumble around you and you tell me it’s fun!"
        mv "I can’t bring myself to care about this trainwreck of a story anymore… I’ll just have to write a new, better one, and hope neither of you interrupt. I can’t hold back the tide of your bad decisions anymore."
        pl "What the hell does that mean?"
        mv "It means say your last goodbyes, this world is about to be no more."
        al "No more?"

        hide gwee
        play music "music/end.oga" noloop volume 0.6
        "The entity says nothing more, turning away from us and this time, disappearing with the motion."

        hide alex
        show alex

        al "Hey! Hey come back!"
        "Alex slams a fist into the ground."
        al "God...damn it."
        "He goes quiet and I sit next to him."
        pl "Alex. Alex, look at me."
        "He doesn’t respond and I lean a bit closer to him, putting a hand on his shoulder."
        pl "Alex, I know this looks pretty bad-"
        al "Pretty bad?! PRETTY BAD!? The apparent equivalent to fucking God just busted in here, said the world’s about to end because you came to the forum, and you think it’s only pretty bad!?"
        pl "Alright its apocalyptically bad, what do you want me to say?"
        al "I want you to say that you regret coming to the forum! That you regret meeting us, that you, that you-"
        al "That-..."
        "His angry expression breaks as tears pool up in his eyes."
        pl "Alex. This isn’t ending because I walked into the forum. This is because I met you and decided I wanted to try something more."
        al "Since when have I been worth the end of life as we know it?"
        pl "Since I met you and realized there was something about you that seemed different from the others… though to be honest, even if it was every instinct in my body screaming to run the other way, I don’t regret it."
        al "...this sucks."
        "Alex leans down and I outstretch my arms. He hugs onto me and we sit there for a moment. The world frozen around us. The warmth of his body against mine. I wrap my fingers around his."
        al "...How long will it take?"
        pl "For the world to end?"
        al "Yeah."
        pl "If it’s a story, I guess it goes by as fast as whoever is reading it."
        al "I mean, if this is the story that ‘God’ has abandoned, who's reading it?"
        pl "Does it matter?"
        al "...Guess not."
        pl "Don’t dwell on it too much."
        al "How can I not?"
        pl "I don’t want your last moments to be spent crying. The only thing that matters is right now, this moment. This one, spectacular moment."
        al "...How are you so positive? How are you so sure it’s worth it?"
        pl "Maybe it’s because I can’t go back on it. Maybe it’s because I was told I did the impossible. Something that ‘Narrator’ said has stuck with me."
        al "What?"
        pl "Well… the ‘Narrator’ said you all were born lucky right?"
        al "Right."
        pl "Well what’s better. To be born lucky or to overcome the odds through your own effort?"
        al "...I’d call you pretty lucky considering that you just faced a god who said he couldn’t even stop you without interfering directly."
        pl "True, true…"
        "Another moment passes."
        pl "Alex?"
        al "Yeah?"

        menu:
            "Whether or not I’m lucky, would you be my Valentine?":
                jump alexlove

        label alexlove:

            al "..."
            al "Of course."

        "Ending D: Gun-DAMN."
        return

    label jolee_end:

        show jolee

        pl "Hey wait up Jolee!"
        "Jolee pauses, looking back at me curiously."
        jo "Yeah, what’s up?"
        pl "Can I… talk to you for a minute? Alone?"
        jo "Oh uh, sure. You guys can go ahead without me, I’ll catch up."

        scene hallwaysakura

        "She waves to the others before stopping out in the hall. I realize we’re both under the cherry blossom they made and my heart skips a beat."
        jo "What is it [name]?"

        menu:
            "I like you.":
                jump joleeendcon

    label joleeendcon:

        jo "Y-you what?"
        pl "I like you and I wanted to know if you wanted to go out together on sunday for Valentine’s day?"
        jo "I-"

        #Rewind One Starts
        scene bwhallwaysakura
        pl "{cps=200}I like you and I wanted to know if you wanted to go out together on sunday for Valentine’s day?{/cps}{nw}"
        jo "{cps=200}Y-you what?{/cps}{nw}"
        pl "{cps=200}I like you.{/cps}{nw}"
        jo "{cps=200}What is it [name]?{/cps}{nw}"

        scene bwforummainclapcheeks

        jo "{cps=200}Oh uh, sure. You guys can go ahead without me, I’ll catch up.{/cps}{nw}"
        pl "{cps=200}Can I… talk to you for a minute? Alone?{/cps}{nw}"
        jo "{cps=200}Yeah, what’s up?{/cps}{nw}"
        pl "{cps=200}Hey wait up Jolee!{/cps}{nw}"
        th "{cps=200}As normal as physics could be considered.{/cps}{nw}"
        ta "{cps=200}Me and Jolee are in the same SBC! The other two nerds have normal classes though.{/cps}{nw}"
        al "{cps=200}Yeah, somehow all our schedules lined up to have class after meeting.{/cps}{nw}"
        pl "{cps=200}All of you have class now?{/cps}{nw}"
        th "{cps=200}Touche. Come on, let’s get our stuff, we got class.{/cps}{nw}"
        ta "{cps=200}Dare you involve yourself with my answer?{/cps}{nw}"
        th "{cps=200}Dare I ask if you were involved?{/cps}{nw}"
        ta "{cps=200}What a shame that only one bone broke.{/cps}{nw}"
        #Rewind One Ends

        scene forummainclapcheeks
        play music "<loop 26.766>music/forum.oga" volume 0.6

        show jolee

        jo "If there’s nothing else anyone has to add then I think we can mark this GBM as over!"
        "Wait…"
        jo "Thanks again to Alex for stepping in as temporary secretary while ours is studying abroad."
        "Wait we just did this, didn’t we?"
        jo "And hopefully our President will be able to be back here soon when he gets out of the hospital from his broken femur!"
        pl "What the…"

        show taylor at left

        ta "What the what?"
        "Taylor walks in almost immediately after the meeting ends like before."
        ta "More like what a shame that only one bone broke."

        show thomas at right

        th "Dare I ask if you were involved?"
        ta "Dare you involve yourself with my answer?"
        th "Touche. Come on, let’s get our stuff, we got class."
        "Everyone mills about for a moment and I watch Alex, Taylor, Jolee and Thomas get their stuff again. They’re just...going through the motions again."
        "What is this groundhog day?"
        pl "You guys all have class together…"

        hide jolee
        show alex

        al "Yeah, somehow all our schedules lined up to have class after meeting."
        ta "Me and Jolee are in-"
        pl "In the same SBC."
        ta "Yeah, how’d you guess?"
        pl "You uh.. Mentioned it before."
        "As I watch them all move to leave, I feel a pain in my chest. It’s stronger than before. Maybe I did something wrong. I never heard their answer."
        mv "Don’t…!"
        "They’re all going to leave again."
        "I refuse to let this be the end of it."
        pl "Hey wait up-!"

        # Rewind Two Begins

        scene bwforummainclapcheeks

        pl "{cps=200}Hey wait up-!{/cps}{nw}"
        pl "{cps=200}You uh.. Mentioned it before.{/cps}{nw}"
        ta "{cps=200}Yeah, how’d you guess?{/cps}{nw}"
        pl "{cps=200}In the same SBC.{/cps}{nw}"
        ta "{cps=200}Me and Jolee are in-{/cps}{nw}"
        al "{cps=200}Yeah, somehow all our schedules lined up to have class after meeting.{/cps}{nw}"
        pl "{cps=200}You guys all have class together…{/cps}{nw}"
        th "{cps=200}Touche. Come on, let’s get our stuff, we got class.{/cps}{nw}"
        ta "{cps=200}Dare you involve yourself with my answer?{/cps}{nw}"
        th "{cps=200}Dare I ask if you were involved?{/cps}{nw}"
        ta "{cps=200}More like what a shame that only one bone broke.{/cps}{nw}"
        ta "{cps=200}What the what?{/cps}{nw}"
        pl "{cps=200}What the…{/cps}{nw}"

        # Rewind Two Ends
        play music "<loop 3.5>music/spooky.oga" volume 0.6
        pl "FUCK!"
        "I slam my hand into the shelf next to me, looking around to see that no one reactions to my outrage."
        "No one reacts at all. They’re just.. Frozen."
        mv "...Stop trying to get a happy ending."
        pl "What the hell? Who are you? Show yourself! I know I heard you before in the bathroom!"
        mv "Yes, I am the voice in the bathroom. I am the reason your little spontaneous dates ended poorly. I am the reason you even exist to be quite honest. Please spare me the monologue of realization, I haven’t got the patience."
        mv "There was an error in the system, you’re supposed to be a side character, not the main character of this story - you don’t get a love interest. You’re supposed to be nameless."
        pl "What are you talking about, what do you mean a side character?"
        mv "I mean a side character. A nobody. A blank slate. A faceless part of the crowd who exists only to move the plot forward."
        pl "You’re talking like this is a story."
        mv "Well it is a story. And somehow, you found yourself lucky enough to slip through the cracks and put yourself at the forefront of this tale."
        pl "Then if this is all a story, who are you?"
        mv "I am…"

        show gwee


        mv "Something beyond your comprehension."
        pl "You’re a sharkpuppy."
        mv "No! I mean, yes I’m a shark puppy currently, but my form is unimportant-"
        pl "Kind of an edgelord with that hood too."
        mv "No! My hood is my uniform, you don’t see me insult your all grey appearance and lack of eyes!"
        pl "I’m not all grey I’m (insert skin color) with (insert eye color) eyes!"
        mv "...Right."
        pl "So are you a blue Kyube-"
        mv "No! Don’t even joke about that, even extradimensional beings are scared of copyright!"
        mv "I am what is best translated into your language as the ‘Narrator’."
        mv "I am the dictator of your world, not in that I rule it but that I dictate all that happens. I am the one who determines everything from the tweet of the birds to the turning of the Earth. I may loose the arrows of love or break the hearts of fools."
        pl "So… Cupid?"
        mv "...You are really annoying the one person that can remove you from existence."
        pl "I feel like if you could do that, you would have already."
        mv "Cute."
        pl "So what is the point of all this? Freezing and rewinding time, using the force or whatever it is you do to interrupt my life - what’s the end goal?"
        mv "Originally, it was to simply redirect you away and back into your proper place but despite my jinxing, you managed to still make something of it all."
        pl "I’m just trying to live my life man-"
        mv "First off I am no ‘man’, and second off, you don’t get a say in that. It is my story, you are my character and you need to know your place. The characters I create are made lucky, born for everything to go their way. You are lucky to have been made at all."

        show jolee at left
        play music "<loop 4.0>music/jolee.oga" volume 0.6

        jo "Leave them alone!"
        "I look past the entity to see a beautiful sight of an infuriated Jolee."
        pl "Jolee!"
        mv "How are you not frozen?!"
        jo "I don’t know and I don’t care, but you need to let us go! I don’t care if you started all this, this is our story to end, no luck or unluck about it!"
        "The entity looks at Jolee pointing up at him and laughs."
        mv "Or what?!"
        "I try to dash forward as one of his grubby little hands grabs onto her hoodie, tightening the strings around her neck. She gasps for air."
        jo "[name]!"
        "He slams her into the tv and a cascade of glass, plastic and wires fall to the ground around them. She raises her hands and digs her nails into its skin, a thin line of black, oil-like ‘blood’ leaking out of it. As the ‘blood’ hits the ground, it twinkles like there’s a star in every drop."
        mv "You fail to realize that you are alone here you useless character! There is only darkness and death if you try to fight the very being that gives you life!"
        "I resist the urge to charge into it as Jolee’s frantic hand points to the shards on the ground, going towards them instead."
        mv "Can you feel your heart burning? Can you feel the struggle within? The fear within me is beyond anything your soul can make."
        "Grabbing a large shard, I whip it around and slam it into the strange entity. It lets Jolee go and I quickly grab her arm, pulling her back as she coughs, struggling to catch her breath."
        "It’s head slowly turns to look at us."
        mv "You cannot kill me in a way that matters. No matter how strong you are, I am beyond strength."
        "The shard seems to be absorbed into its skin as it takes a short breath in and lets a long breath out."
        mv "I may have lost my temper."
        jo "What is wrong with you!?"
        mv "You try watching your life’s work crumble around you and you tell me it’s fun!"
        mv "I can’t bring myself to care about this trainwreck of a story anymore… I’ll just have to write a new, better one, and hope neither of you interrupt. I can’t hold back the tide of your bad decisions anymore."
        pl "What the hell does that mean?"
        mv "It means say your last goodbyes, this world is about to be no more."
        jo "No more?"

        hide gwee
        play music "music/end.oga" noloop volume 0.6
        "The entity says nothing more, turning away from us and this time, disappearing with the motion."

        hide jolee
        show jolee

        "Jolee tries to jump forward but I hold her back."
        pl "Hey, hey, the apparent creator of life just tried to choke you out, I’d rather not see it happen again."
        jo "But I- it-"
        "She sighs."
        jo "God...damn it."
        "She goes quiet and I sit next to her."
        pl "Jolee. Jolee look at me."
        jo "..."
        "Silently, Jolee lifts her head up and I see tears pool up in her eyes. I hold out my arms and she all but throws herself into them, hugging onto me."
        jo "We… we just invited you in. Tried to make friends. And what, now the world is… is ENDING because of it?"
        pl "The world is ending because I decided to try to become something more than friends."
        "Jolee looks up at me in shock again and I can’t help but laugh."
        pl "You always seem so surprised whenever I try to say something nice."
        jo "It’s… not really a common thing."
        pl "Well I’m not try to follow the crowd, I’m trying to follow my heart."
        "She hides her face again, quietly muttering something about me being a smooth-talker."
        pl "Heh, I guess I try my best sometimes."
        "We sit there for a moment, the world frozen around us and her body leaning on mine. I wrap my fingers around hers."
        pl "...I think this was worth it."
        "She laughs."
        jo "The world’s ending!"
        pl "Well, I never thought the apocalypse was supposed to be much fun. But I’m pretty happy right now."
        jo "...How long do you think it’ll take?"
        pl "For this to all just disappear?"
        jo "Yeah. I don’t know if it’s instant or.."
        pl "Well, apparently this is all a story. I guess it goes by as fast as whoever is reading it."
        jo "I mean, if this is the story that ‘God’ has abandoned, who's reading it?"
        pl "Does it matter?"
        jo "I… I guess not."
        "Jolee sits up slightly, still using my chest as a pillow as I feel my shirt grow a bit damp from her tears."
        pl "You want to know why I think this is worth it?"
        "She looks up at me."
        jo "Because you ‘got the girl’?"
        pl "Heh, not just that. It’s because of what that thing said."
        jo "Which part?"
        pl "Well… the ‘Narrator’ said you all were born lucky right?"
        jo "Right."
        pl "Is it better to be born lucky or to overcome the odds through your own effort?"
        jo "...I’d call you pretty lucky considering that you just faced a god who said he couldn’t even stop you without interfering directly."
        pl "True, true…"
        "Another moment passes."
        pl "Jolee?"
        jo "Yeah?"

        menu:
            "Whether or not I'm lucky, would you be my Valentine?":
                jump joleelove

        label joleelove:

            jo "..."
            jo "Of course."

            "Ending E: Blinded by Love."
            return

    label taylor_end:
        pl "Hey wait up Taylor!"
        "Taylor pauses, looking back at me curiously."
        ta "Yeah, what’s up?"
        pl "Can I… talk to you for a minute? Alone?"
        ta "Oh uh, sure. You guys can go ahead without me, I’ll catch up."

        scene hallwaysakura

        "She waves to the others before stopping out in the hall. I realize we’re both under the cherry blossom they made and my heart skips a beat."
        ta "What is it [name]?"

        menu:
            "I like you.":
                jump taylorendcon

        label taylorendcon:

        ta "Y-you what?"
        pl "I like you and I wanted to know if you wanted to go out together on sunday for Valentine’s day?"

        # Rewind One Begins

        scene bwhallwaysakura

        pl "{cps=150}I like you and I wanted to know if you wanted to go out together on sunday for Valentine’s day?{/cps}{nw}"
        ta "{cps=150}Y-you what?{/cps}{nw}"
        pl "{cps=150}I like you.{/cps}{nw}"
        ta "{cps=150}What is it [name]?{/cps}{nw}"

        scene bwforummainclapcheeks

        ta "{cps=150}Oh uh, sure. You guys can go ahead without me, I’ll catch up.{/cps}{nw}"
        pl "{cps=150}Can I… talk to you for a minute? Alone?{/cps}{nw}"
        ta "{cps=150}Yeah, what’s up?{/cps}{nw}"
        pl "{cps=150}Hey wait up Taylor!{/cps}{nw}"
        th "{cps=150}As normal as physics could be considered.{/cps}{nw}"
        ta "{cps=150}Me and Jolee are in the same SBC! The other two nerds have normal classes though.{/cps}{nw}"
        al "{cps=150}Yeah, somehow all our schedules lined up to have class after meeting.{/cps}{nw}"
        pl "{cps=150}All of you have class now?{/cps}{nw}"
        th "{cps=150}Touche. Come on, let’s get our stuff, we got class.{/cps}{nw}"
        ta "{cps=150}Dare you involve yourself with my answer?{/cps}{nw}"
        th "{cps=150}Dare I ask if you were involved?{/cps}{nw}"
        ta "{cps=150}What a shame that only one bone broke.{/cps}{nw}"

        #Rewind One Ends

        scene forummainclapcheeks
        play music "<loop 26.766>music/forum.oga" volume 0.6

        show jolee

        jo "If there’s nothing else anyone has to add then I think we can mark this GBM as over!"
        "Wait…"
        jo "Thanks again to Alex for stepping in as temporary secretary while ours is studying abroad."
        "Wait we just did this, didn’t we?"
        jo "And hopefully our President will be able to be back here soon when he gets out of the hospital from his broken femur!"
        pl "What the…"

        show taylor at left

        ta "What the what?"
        "Taylor walks in almost immediately after the meeting ends like before."
        ta "More like what a shame that only one bone broke."

        show thomas at right

        th "Dare I ask if you were involved?"
        ta "Dare you involve yourself with my answer?"
        th "Touche. Come on, let’s get our stuff, we got class."
        "Everyone mills about for a moment and I watch Alex, Taylor, Jolee and Thomas get their stuff again. They’re just...going through the motions again."
        "What is this groundhog day?"
        pl "You guys all have class together…"

        hide jolee
        show alex

        al "Yeah, somehow all our schedules lined up to have class after meeting."
        ta "Me and Jolee are in-"
        pl "In the same SBC."
        ta "Yeah, how’d you guess?"
        pl "You uh.. Mentioned it before."
        "As I watch them all move to leave, I feel a pain in my chest. It’s stronger than before. Maybe I did something wrong. I never heard their answer."
        mv "Don’t…!"
        "They’re all going to leave again."
        "I refuse to let this be the end of it."
        pl "Hey wait up-!"

        # Rewind Two Begins

        scene bwforummainclapcheeks

        pl "{cps=200}Hey wait up-!{/cps}{nw}"
        pl "{cps=200}You uh.. Mentioned it before.{/cps}{nw}"
        ta "{cps=200}Yeah, how’d you guess?{/cps}{nw}"
        pl "{cps=200}In the same SBC.{/cps}{nw}"
        ta "{cps=200}Me and Jolee are in-{/cps}{nw}"
        al "{cps=200}Yeah, somehow all our schedules lined up to have class after meeting.{/cps}{nw}"
        pl "{cps=200}You guys all have class together…{/cps}{nw}"
        th "{cps=200}Touche. Come on, let’s get our stuff, we got class.{/cps}{nw}"
        ta "{cps=200}Dare you involve yourself with my answer?{/cps}{nw}"
        th "{cps=200}Dare I ask if you were involved?{/cps}{nw}"
        ta "{cps=200}More like what a shame that only one bone broke.{/cps}{nw}"
        ta "{cps=200}What the what?{/cps}{nw}"
        pl "{cps=200}What the…{/cps}{nw}"

        # Rewind Two Ends

        play music "<loop 3.5>music/spooky.oga" volume 0.6

        pl "FUCK!"
        "I slam my hand into the shelf next to me, looking around to see that no one reactions to my outrage."
        "No one reacts at all. They’re just.. Frozen."
        mv "...Stop trying to get a happy ending."
        pl "What the hell? Who are you? Show yourself! I know I heard you before in the bathroom!"
        mv "Yes, I am the voice in the bathroom. I am the reason your little spontaneous dates ended poorly. I am the reason you even exist to be quite honest. Please spare me the monologue of realization, I haven’t got the patience."
        mv "There was an error in the system, you’re supposed to be a side character, not the main character of this story - you don’t get a love interest. You’re supposed to be nameless."
        pl "What are you talking about, what do you mean a side character?"
        mv "I mean a side character. A nobody. A blank slate. A faceless part of the crowd who exists only to move the plot forward."
        pl "You’re talking like this is a story."
        mv "Well it is a story. And somehow, you found yourself lucky enough to slip through the cracks and put yourself at the forefront of this tale."
        pl "Then if this is all a story, who are you?"
        mv "I am…"

        show gwee


        mv "Something beyond your comprehension."
        pl "You’re a sharkpuppy."
        mv "No! I mean, yes I’m a shark puppy currently, but my form is unimportant-"
        pl "Kind of an edgelord with that hood too."
        mv "No! My hood is my uniform, you don’t see me insult your all grey appearance and lack of eyes!"
        pl "I’m not all grey I’m (insert skin color) with (insert eye color) eyes!"
        mv "...Right."
        pl "So are you a blue Kyube-"
        mv "No! Don’t even joke about that, even extradimensional beings are scared of copyright!"
        mv "I am what is best translated into your language as the ‘Narrator’."
        mv "I am the dictator of your world, not in that I rule it but that I dictate all that happens. I am the one who determines everything from the tweet of the birds to the turning of the Earth. I may loose the arrows of love or break the hearts of fools."
        pl "So… Cupid?"
        mv "...You are really annoying the one person that can remove you from existence."
        pl "I feel like if you could do that, you would have already."
        mv "Cute."
        pl "So what is the point of all this? Freezing and rewinding time, using the force or whatever it is you do to interrupt my life - what’s the end goal?"
        mv "Originally, it was to simply redirect you away and back into your proper place but despite my jinxing, you managed to still make something of it all."
        pl "I’m just trying to live my life man-"
        mv "First off I am no ‘man’, and second off, you don’t get a say in that. It is my story, you are my character and you need to know your place. The characters I create are made lucky, born for everything to go their way. You are lucky to have been made at all."

        show taylor at left
        play music "<loop 6.5>music/taylor.oga" volume 0.6

        ta "You are lucky I don’t send this pocket knife into the back of your head you dog-sushi piece of shit."
        "I look past the entity to see a beautiful sight of an infuriated Taylor wielding a long pocket knife."
        pl "Taylor!"
        mv "How are you not-"
        ta "Fuck you that’s how."
        ta "I don’t give a fuck if you’re this world’s version of God or Zeus or Karma or Fate or whatever the hell we’ll call it. But I hope to make one thing crystal fucking clear."
        ta "You may have started this story. But we decide how to finish it. No luck or unluck about it."
        "The ‘Narrator’ turns and I see Taylor duck out of the wave of his swinging tail."
        mv "You insolent child!"
        "I try to dash forward as one of his grubby little hands grabs onto her hoodie, tightening the strings around her neck. She gasps for air."
        ta "[name]!"
        "Her pocket knife clatters to the ground."
        mv "You fail to realize that you are alone here you useless character! There is only darkness and death if you try to fight the very being that gives you life!"
        "I resist the urge to charge into it as Taylor’s frantic hand points to the knife on the ground, going towards the weapon instead."
        mv "Can you feel your heart burning? Can you feel the struggle within? The fear within me is beyond anything your soul can make."
        "Grabbing the knife, I whip it around and slam it into the strange entity. It lets Taylor go and I quickly grab her arm, pulling her back as she coughs, struggling to catch her breath."
        "It’s head slowly turns to look at us."
        mv "You cannot kill me in a way that matters. No matter how strong you are, I am beyond strength."
        "The knife seems to be absorbed into its skin as it takes a short breath in and lets a long breath out."
        mv "I may have lost my temper."
        ta "What the fuck is wrong with you!?"
        mv "You try watching your life’s work crumble around you and you tell me it’s fun!"
        mv "I can’t bring myself to care about this trainwreck of a story anymore… I’ll just have to write a new, better one, and hope neither of you interrupt. I can’t hold back the tide of your bad decisions anymore."
        pl "What the hell does that mean?"
        mv "It means say your last goodbyes, this world is about to be no more."
        ta "No more?"

        hide gwee
        play music "music/end.oga" noloop volume 0.6
        "The entity says nothing more, turning away from us and this time, disappearing with the motion."

        hide taylor
        show taylor

        ta "Hey! Hey come back!"
        "Taylor slams a fist into the ground."
        ta "God...damn it."
        "She goes quiet and I sit next to her. I hear wheezing coming from her chest with every breath as she palms her pocket for a moment. A small blue inhaler comes out and she presses it silently to her lips."
        pl "Taylor. Taylor look at me."
        ta "What?"
        "She looks up at me with a bitter expression as she rips the inhaler away from her mouth and chucks it across the room."
        ta "The world’s apparently about to end now just because, what? You came into the forum. You became friends with all of us. You…"
        pl "I met you and decided I wanted to try something more?"
        ta "Shut up…"
        "Her words are half-hearted as she leans to the side and lets her head hit my shoulder."
        ta "...This blows."
        pl "I never thought the apocalypse was supposed to be much fun."
        ta "How long do you think it’ll take?"
        pl "If it’s a story, I guess it goes by as fast as whoever is reading it."
        ta "I mean, if this is the story that ‘God’ has abandoned, who's reading it?"
        pl "Does it matter?"
        ta "...Guess not."
        "We sit there for a moment, the world still frozen around us and her body leaning on mine. I wrap my fingers around hers."
        pl "...I think this was worth it."
        "She laughs."
        ta "Worth it? Apparently the fact that you tried to be a ‘main character’ and chase after me is what just caused all this."
        pl "Well… the ‘Narrator’ said you all were born lucky right?"
        ta "Yeah."
        pl "Well what’s better. To be born lucky or to overcome the odds through your own effort?"
        ta "...I’d call you pretty lucky considering that you just faced a god who said he couldn’t even stop you without interfering directly."
        pl "True, true…"
        "Another moment passes."
        pl "Taylor?"
        ta "Yeah?"

        menu:
            "Whether or not I’m lucky, would you be my Valentine?":
                jump taylorlove

        label taylorlove:

        ta "..."
        ta "Of course."

        "Ending F: Love Hurts."
        return

    label thomas_end:
        pl "Hey wait up Thomas!"
        "Thomas pauses, looking back at me curiously."
        th "Yeah, what’s up?"
        pl "Can I… talk to you for a minute? Alone?"
        th "Oh uh, sure. You guys can go ahead without me, I’ll catch up."

        scene hallwaysakura

        "He waves to the others before stopping out in the hall. I realize we’re both under the cherry blossom they made and my heart skips a beat."
        th "What is it [name]?"

        menu:
            "I like you.":
                jump thomasendcon

        label thomasendcon:

            th "Y-you what?"
            pl "I like you and I wanted to know if you wanted to go out together on sunday for Valentine’s day?"

        # Rewind One Starts here

            scene bwhallwaysakura

            pl "{cps=200}I like you and I wanted to know if you wanted to go out together on sunday for Valentine’s day?{/cps}{nw}"
            th "{cps=200}Y-you what?{/cps}{nw}"
            pl "{cps=200}I like you.{/cps}{nw}"
            th "{cps=200}What is it [name]?{/cps}{nw}"

            scene bwforummainclapcheeks

            th "{cps=200}Oh uh, sure. You guys can go ahead without me, I’ll catch up.{/cps}{nw}"
            pl "{cps=200}Can I… talk to you for a minute? Alone?{/cps}{nw}"
            th "{cps=200}Yeah, what’s up?{/cps}{nw}"
            pl "{cps=200}Hey wait up Thomas!{/cps}{nw}"
            th "{cps=200}As normal as physics could be considered.{/cps}{nw}"
            ta "{cps=200}Me and Jolee are in the same SBC! The other two nerds have normal classes though.{/cps}{nw}"
            al "{cps=200}Yeah, somehow all our schedules lined up to have class after meeting.{/cps}{nw}"
            pl "{cps=200}All of you have class now?{/cps}{nw}"
            th "{cps=200}Touche. Come on, let’s get our stuff, we got class.{/cps}{nw}"
            ta "{cps=200}Dare you involve yourself with my answer?{/cps}{nw}"
            th "{cps=200}Dare I ask if you were involved?{/cps}{nw}"
            ta "{cps=200}What a shame that only one bone broke.{/cps}{nw}"


            #Rewind One Ends

            scene forummainclapcheeks
            play music "<loop 26.766>music/forum.oga" volume 0.6
            show jolee

            jo "If there’s nothing else anyone has to add then I think we can mark this GBM as over!"
            "Wait…"
            jo "Thanks again to Alex for stepping in as temporary secretary while ours is studying abroad."
            "Wait we just did this, didn’t we?"
            jo "And hopefully our President will be able to be back here soon when he gets out of the hospital from his broken femur!"
            pl "What the…"

            show taylor at left

            ta "What the what?"
            "Taylor walks in almost immediately after the meeting ends like before."
            ta "More like what a shame that only one bone broke."

            show thomas at right

            th "Dare I ask if you were involved?"
            ta "Dare you involve yourself with my answer?"
            th "Touche. Come on, let’s get our stuff, we got class."
            "Everyone mills about for a moment and I watch Alex, Taylor, Jolee and Thomas get their stuff again. They’re just...going through the motions again."
            "What is this groundhog day?"
            pl "You guys all have class together…"

            hide jolee
            show alex

            al "Yeah, somehow all our schedules lined up to have class after meeting."
            ta "Me and Jolee are in-"
            pl "In the same SBC."
            ta "Yeah, how’d you guess?"
            pl "You uh.. Mentioned it before."
            "As I watch them all move to leave, I feel a pain in my chest. It’s stronger than before. Maybe I did something wrong. I never heard their answer."
            mv "Don’t…!"
            "They’re all going to leave again."
            "I refuse to let this be the end of it."
            pl "Hey wait up-!"

            # Rewind Two Begins

            scene bwforummainclapcheeks

            pl "{cps=200}Hey wait up-!{/cps}{nw}"
            pl "{cps=200}You uh.. Mentioned it before.{/cps}{nw}"
            ta "{cps=200}Yeah, how’d you guess?{/cps}{nw}"
            pl "{cps=200}In the same SBC.{/cps}{nw}"
            ta "{cps=200}Me and Jolee are in-{/cps}{nw}"
            al "{cps=200}Yeah, somehow all our schedules lined up to have class after meeting.{/cps}{nw}"
            pl "{cps=200}You guys all have class together…{/cps}{nw}"
            th "{cps=200}Touche. Come on, let’s get our stuff, we got class.{/cps}{nw}"
            ta "{cps=200}Dare you involve yourself with my answer?{/cps}{nw}"
            th "{cps=200}Dare I ask if you were involved?{/cps}{nw}"
            ta "{cps=200}More like what a shame that only one bone broke.{/cps}{nw}"
            ta "{cps=200}What the what?{/cps}{nw}"
            pl "{cps=200}What the…{/cps}{nw}"

            # Rewind Two Ends
            play music "<loop 3.5>music/spooky.oga" volume 0.6

            pl "FUCK!"
            "I slam my hand into the shelf next to me, looking around to see that no one reactions to my outrage."
            "No one reacts at all. They’re just.. Frozen."
            mv "...Stop trying to get a happy ending."
            pl "What the hell? Who are you? Show yourself! I know I heard you before in the bathroom!"
            mv "Yes, I am the voice in the bathroom. I am the reason your little spontaneous dates ended poorly. I am the reason you even exist to be quite honest. Please spare me the monologue of realization, I haven’t got the patience."
            mv "There was an error in the system, you’re supposed to be a side character, not the main character of this story - you don’t get a love interest. You’re supposed to be nameless."
            pl "What are you talking about, what do you mean a side character?"
            mv "I mean a side character. A nobody. A blank slate. A faceless part of the crowd who exists only to move the plot forward."
            pl "You’re talking like this is a story."
            mv "Well it is a story. And somehow, you found yourself lucky enough to slip through the cracks and put yourself at the forefront of this tale."
            pl "Then if this is all a story, who are you?"
            mv "I am…"

            show gwee


            mv "Something beyond your comprehension."
            pl "You’re a sharkpuppy."
            mv "No! I mean, yes I’m a shark puppy currently, but my form is unimportant-"
            pl "Kind of an edgelord with that hood too."
            mv "No! My hood is my uniform, you don’t see me insult your all grey appearance and lack of eyes!"
            pl "I’m not all grey I’m (insert skin color) with (insert eye color) eyes!"
            mv "...Right."
            pl "So are you a blue Kyube-"
            mv "No! Don’t even joke about that, even extradimensional beings are scared of copyright!"
            mv "I am what is best translated into your language as the ‘Narrator’."
            mv "I am the dictator of your world, not in that I rule it but that I dictate all that happens. I am the one who determines everything from the tweet of the birds to the turning of the Earth. I may loose the arrows of love or break the hearts of fools."
            pl "So… Cupid?"
            mv "...You are really annoying the one person that can remove you from existence."
            pl "I feel like if you could do that, you would have already."
            mv "Cute."
            pl "So what is the point of all this? Freezing and rewinding time, using the force or whatever it is you do to interrupt my life - what’s the end goal?"
            mv "Originally, it was to simply redirect you away and back into your proper place but despite my jinxing, you managed to still make something of it all."
            pl "I’m just trying to live my life man-"
            mv "First off I am no ‘man’, and second off, you don’t get a say in that. It is my story, you are my character and you need to know your place. The characters I create are made lucky, born for everything to go their way. You are lucky to have been made at all."
            th "I didn't expect to face a god today, huh. Fate is weird isn't it."

            show thomas at left
            play music "<loop 0.5>music/thomas.oga" volume 0.6

            "I look past the entity to see a beautiful sight of an infuriated Taylor wielding a small pocket knife."
            pl "Thomas!"
            mv "How are you not-"
            th "Fuck you that’s how."
            th "I could care less what deity you are, but whether or not you made this story, we’ll be deciding how it finishes, lucky or unlucky."
            "The ‘Narrator’ turns and I see Thomas duck out of the wave of his swinging tail, trying to slash it with his knife."
            mv "You insolent child!"
            "I try to dash forward as one of his grubby little hands grabs onto Thomas’s hoodie, tightening the strings around her neck. He gasps for air."
            th "[name]!"
            "His pocket knife clatters to the ground."
            mv "You fail to realize that you are alone here you useless character! There is only darkness and death if you try to fight the very being that gives you life!"
            "I resist the urge to charge into it as Thomas’s frantic hand points to the knife on the ground, going towards the weapon instead."
            mv "Can you feel your heart burning? Can you feel the struggle within? The fear within me is beyond anything your soul can make."
            "Grabbing the ground, I whip it around and slam it into the strange entity. It lets Thomas go and I quickly grab his arm, pulling him back as he coughs, struggling to catch his breath."
            "It’s head slowly turns to look at us."
            mv "You cannot kill me in a way that matters. No matter how strong you are, I am beyond strength."
            "The knife seems to be absorbed into its skin as it takes a short breath in and lets a long breath out."
            mv "I may have lost my temper."
            th "What the fuck is wrong with you!?"
            mv "You try watching your life’s work crumble around you and you tell me it’s fun!"
            mv "I can’t bring myself to care about this trainwreck of a story anymore… I’ll just have to write a new, better one, and hope neither of you interrupt. I can’t hold back the tide of your bad decisions anymore."
            pl "What the hell does that mean?"
            mv "It means say your last goodbyes, this world is about to be no more."
            th "No more?"

            hide gwee
            play music "music/end.oga" noloop volume 0.6
            "The entity says nothing more, turning away from us and this time, disappearing with the motion."

            hide thomas
            show thomas

            th "God...damn."
            "Thomas stays on the ground for a moment, staring at the space where the Narrator disappeared. I sit next to him."
            pl "Thomas. Thomas look at me."
            th "...What?"
            "There’s nothing but shock and pain in his eyes as they meet mine."
            th "The world’s apparently about to end now just because, what? You came into the forum. You became friends with all of us. You…"
            pl "I met you and decided I wanted to try something more?"
            th "Shut up…"
            "His words are half-hearted as he leans to the side and lets his head hit my shoulder."
            th "There’s no way any of this or us, are worth this high of a price."
            pl "As the one who was told to pay, I think it’s fine."
            th "...How long do you think it’ll take?"
            pl "If it’s a story, I guess it goes by as fast as whoever is reading it."
            th "I mean, if this is the story that ‘God’ has abandoned, who's reading it?"
            pl "Does it matter?"
            th "...Guess not."
            "We sit there for a moment, the world still frozen around us and his body leaning on mine. I wrap my fingers around his."
            th "Why are you so sure this was worth it? Apparently the fact that you tried to be a ‘main character’ and chase after me is what just caused all this."
            pl "Well… the ‘Narrator’ said you all were born lucky right?"
            th "Yeah."
            pl "Well what’s better. To be born lucky or to overcome the odds through your own effort?"
            th "...I’d call you pretty lucky considering that you just faced a god who said he couldn’t even stop you without interfering directly."
            pl "True, true…"
            "Another moment passes."
            pl "Thomas?"
            th "Yeah?"

            menu:
                "Whether or not I’m lucky, would you be my Valentine?":
                    jump thomaslove

            label thomaslove:

            th "..."
            th "Of course."

            "Ending G: Honk if you're in love."
            return

# This ends the game.
    return


# Don't enter club
    label endinga:
        "I watch as the guy stands in the way of a nearby student and begins expound on how he’s president of the club and made it great again or something."
        "It’s probably for the best that I just leave it be… right?"
        "Time to wait another 15 minutes for this stupid cotton candy…"

        "Ending A: What if?"
    return

# Uncover the gpa rock

    label endingb:
        $ name = "test"
        show 4pspread
        pl "Well, it’s just a rock, it can’t actually be cursed right?"
        "I reach forward to pull off the chainmail as Thomas reels back. Alex completely stands up from the couch, moving further back into the room."
        "Pulling it off I’m just faced with… a rock."
        "It’s a mix of brown and grey mostly and is cool to the touch."
        pl "Hey, for a cursed rock, it seems pretty normal."
        al "That’s how it gets you."
        jo "It was nice knowing you."
        ta "Tell me [name]... how do you feel?"
        "I think for a moment as I pull the chainmail back over the rock."
        pl "I mean, I feel a bit hungry but besides that, fine."
        ta "And if I was to propose showing you this ascension game I mentioned?"
        "I look between everyone’s concerned faces and laugh."
        pl "Guys, I swear I’m fine."
        pl "And if you want to show me a new game, I won’t object."
        ta "Okaaay, grab that silver box from the shelf next to you and come over here then…"
        jo "Taylor, you’re the real agent of the rock at this point."
        ta "Hush, it’s fine for them to accept their fate."

        scene timeskip

        "I learned how to play Ascension that day."

        scene sbuoutside
        play music "<loop 3.5>music/spooky.oga" volume 0.6

        "We played and played and played until I realized I had missed class and almost was going to miss the train home."
        "Thomas thankfully drove me to the station so I’d get there in time, but it was the first of many days like that."
        "I thought it was just a fluke, I didn’t forget about my classes the next day, or the day after that, or after that."
        "But soon as I hung out at the forum more, meeting more of its members and playing more of its games…"
        "I started willingly skipping classes to stay in this warm, friendly place."
        "It was only when finals week came and I realized I needed to get perfect scores in so many of my classes to secure passing grades that it dawned on me."
        "Maybe that rock was cursed."
        "And maybe Jolee wasn’t wrong that its members were just agents of the rock."

        "Ending B: Death of a GPA."
        return

    label exit:
        return
