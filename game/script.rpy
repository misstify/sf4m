# The script of the game goes in this file.
# Ideally id make a class for characters and their variables

define al = Character('Alex', color="#FFFF32")
define jo = Character('Jolee', color="#FFAE19")
define ta = Character('Taylor', color="#E50000")
define th = Character('Thomas', color="#66B2FF")
define pl = Character("[name]")
define rj = Character('Egotistical Student', color="#FFFFFF")
define mv = Character('Mysterious Voice', color="#FFFFFF")

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

    # Jump to appropriate label, gpa_rock if invalid input given
    def jumpToDate(char_name, label_end):
        if char_name == "GPA_ROCK":
            renpy.jump("gpa_rock" + label_end)
        elif char_name == "ALEX":
            renpy.jump("alex" + label_end)
        elif char_name == "JOLEE":
            renpy.jump("jolee" + label_end)
        elif char_name == "TAYLOR":
            renpy.jump("taylor" + label_end)
        elif char_name == "THOMAS":
            renpy.jump("thomas" + label_end)
        else:
            renpy.jump("gpa_rock" + label_end)

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

    # Nates testing cheaty jump
    jump testing

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
        # play music "illurock.ogg" fadeout 1.0 fadein 1.0
        # play sound "oof"

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

        ta "So which do you prefer, Netflix or Hulu?"

    menu:
        "Hulu or bust":
            jump hulu

        "Netflix all the way":
            jump netflix
    # needs close statement here

    label hulu:

            show alex at right

            al "A-ha! Take that, 'nerd'!"
            "The tired boy seems invigorated as the girl gives me an annoyed glare before she just grabs a pillow off of the couch."
            ta "I'm hitting one of you with this, choose wisely fools."
            al "Ha, I'll happily tae the blow to protect the new member actually being cultured."

            hide alex
            hide taylor

            jump split
    # needs close statement here

    label netflix:

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
        th "[name] was it? Nice to meet you. I’m Thomas."
        jo "Oh, and I’m Jolee! Over there is Taylor and Alex."
        al "Hiya."
        pl "Nice to meet you all."
        jo "This is just an open room, so feel free to sit and relax or go and come back later."
        al "Maybe if you go and come back, there will actually be something on the TV by then."
        pl "It’s alright, I don’t have class for a bit anyway."
        ta "Are you a resident or commuter?"
        pl "Commuter. Take the train here. Getting a car on campus seems like a lot honestly."
        th "Ah, it kind of is but if you need help I can walk you through it. I just moved my truck to one of the other parking lots earlier."
        pl "You had to move parking lots…?"
        th "Yeah, all in the name of not getting tickets."
        ta "Imagine not going into copious amounts of debt to stay in a dirty little room with someone else."
        jo "You are here on basically full scholarship and you’re the reason our dorm is dirty."
        ta "...I plead the fifth."
        "As Taylor and Jolee begin to banter, I look and see Alex trying to lean over and take a controller off from the table."
        "Taylor seems to follow my gaze and suddenly hits Alex with a pillow."
        ta "Don’t try to grab the remote when I’m not looking, you’re not sneaking anything on!"
        al "The silence is deafening and I’m shiftholder so I can overrule you."
        ta "That insinuates I respect your authority."
        "The two of them start bickering again, Jolee offering me an apologetic smile before she goes back to talking to Thomas about the papers they seem to be writing on."
        "Maybe I should go talk to one of these pairs."

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
        "Jolee goes over to the couch as Thomas shrugs."
        th "Club’s a bit empty because of all this but, it’s home, y’know?"
        pl "I definitely can see why people don’t stick around, but I can see plenty of reasons why I’d want to stick around though."
        th "Heh, glad you’re enjoying our insanity."
        ta "I will not yield!"
        jo "I will buy you ramen if you do."
        ta "...I have been bribed."
        al "Really, you accept her bribes but not mine?!"
        th "Care to watch the movie?"
        pl "Huh?"
        "I look away from the chaotic scene to look back over at Thomas who seems to be looking at me with an almost analytical eye."
        th "Me and Jolee have to fill out the rest of this paperwork for the events, just thought you’d have a better view of the movie from on the couch."
        pl "Oh uh, I guess. You guys don’t need any more help?"
        th "Nah, once we get past our stubbornness, we can get things done pretty quickly around here."
        pl "I’ll take your word for it."
        "Jolee groans as she sits back down at the table."
        jo "Children, all of you are children."
        th "Yes, children who need to be advertised to if we plan on having either of these events be a success. Let’s get these event applications done."
        jo "Right, right."
        pl "I’ll talk to you guys later then."
        jo "Oh, see ya [name]."
        th "Later."
        "I go over to the couch to join the movie screening."

        scene forumalt

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
        ta "Huh, what, morning already?"
        al "Phone call?"
        "I lean forward to check and my eyes bulge at the time."
        pl "Shit, that’s my alarm for class, I should go."
        al "Ah, definitely don’t want to be late for that, see you dude."
        ta "Hmm.. yeah, bye…"
        "I look away from Alex and the half-awake Taylor to wave to the still-working Jolee and Thomas."
        pl "Bye guys!"
        jo "Have fun in class!"
        th "Later."
        "I jog out of the forum… I might stop by again tomorrow."

# Beginning of Day 2

    label tuesday:

        scene sbuoutside
        with dissolve

        "Dawn of the Second Day… or at least the afternoon of it."
        "I walk out of the SAC cafeteria, stomach full of mediocre food and an hour left before my next class starts."
        "As I go to leave the building, I pause for a moment."
        "Rather than go sit in the library and play on my phone there is a different place I could go…"
        "Turning away from the outside world, I head downstairs to the basement of the SAC, popping my head into the forum."

        scene forummainclapcheeks
        with dissolve

        ta "...and then I’ll change his profile picture to a catgirl so if he wants to try and get his account access back from me, he’ll have to admit that his tinder account is the one advertising itself as a catgirl."
        jo "...’owo’?"
        ta "Yes, ‘owo’."
        pl "Am I interrupting something?"
        ta "Oh hey [name]! Nah, nothing besides the usual plans for world domination."
        "Taylor and Jolee are sitting together at the back tables. Thomas silently looks up and nods to me while Alex waves from the couch."
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

        pl "...I get depressed around this time every year honestly."
        jo "Don’t enjoy being reminded about how single you are?"
        ta "Well at least he doesn’t have to see Angela and Ken being lovey-dovey this time around, the lovebirds are studying abroad together!"
        al "Don’t worry [name], I get you."
        "I look over to find Alex completely turned on the couch, nodding to me with an understanding expression."
        al "Valentine’s day has never exactly been the happiest time of the year for me either."
        pl "Did something bad happen when you were younger?"
        al "Ah… story for another time."
        ta "Well, you can get the joys of experiencing it with us."
        th "That isn’t exactly going to be making him any happy memories Taylor."
        ta "Well it makes me happy to see you all suffer so I say we should open the forum on the weekend."
        jo "You don’t get up before 3 on the weekend Taylor."
        ta "When I said ‘we should open the forum’, I meant all of you do and I come watch later."
        "I catch Alex’s eye as he looks from everyone else over to me from his spot on the couch. His usually tired expression seems to perk up for a moment as he grins at me before looking back at the others."
        th "This is why you don’t have a room key."
        ta "You all are just afraid of me growing too powerful."
        al "Ah yes, that’s it and not you skipping every GBM meeting."
        ta "GBM meeting is a redundant phrase so your point is invalid, hush."

        jump prehistory

    label valex:

        $ updateHearts("ALEX", 1)

        pl "...I get depressed around this time every year honestly."
        jo "Don’t enjoy being reminded about how single you are?"
        ta "Well at least he doesn’t have to see Angela and Ken being lovey-dovey this time around, the lovebirds are studying abroad together!"
        al "Don’t worry [name], I get you."
        "I look over to find Alex completely turned on the couch, nodding to me with an understanding expression."
        al "Valentine’s day has never exactly been the happiest time of the year for me either."
        pl "Did something bad happen when you were younger?"
        al "Ah… story for another time."
        ta "Well, you can get the joys of experiencing it with us."
        th "That isn’t exactly going to be making him any happy memories Taylor."
        ta "Well it makes me happy to see you all suffer so I say we should open the forum on the weekend."
        jo "You don’t get up before 3 on the weekend Taylor."
        ta "When I said ‘we should open the forum’, I meant all of you do and I come watch later."
        "I catch Alex’s eye as he looks from everyone else over to me from his spot on the couch. His usually tired expression seems to perk up for a moment as he grins at me before looking back at the others."
        th "This is why you don’t have a room key."
        ta "You all are just afraid of me growing too powerful."
        al "Ah yes, that’s it and not you skipping every GBM meeting."
        ta "GBM meeting is a redundant phrase so your point is invalid, hush."

        jump prehistory

    label vnone:

        pl "...I’m honestly hoping for love this year. I don’t know, I’m feeling optimistic."
        th "Nothing wrong with optimism I guess."
        ta "If you get crushed by whoever you plan on confessing to dude, I will happily take whatever chocolate you buy for them on their behalf."
        "I look between everyone only to find that no one seems to agree with my perspective on this."
        jo "It’s alright [Name], if you have someone you care about and want to confess to, I’d say get it over with and do it quickly."
        jo "A lot of people have anxiety about it, but… I mean, it helps to not dwell on it."
        ta "That’s too wholesome for me, change the channel on that one Jolee."
        jo "Go grab the remote and put something on yourself."
        ta "But laaaaazy."
        jo "Not my problem."
        "Taylor groans as she sinks into her chair, looking at her laptop screen."

        jump prehistory

    label vtom:

        $ updateHearts("THOMAS", 1)

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
        ta "My dude!"
        pl "I look over at Taylor immediately holds up her hand for a high-five towards me, smacking her hand on instinct as she laughs."
        ta "Forget the romance, this is a holiday of sugar highs and money lows!"
        al "Your money is always ‘low’."
        ta "Hence why I’m currently figuring out how to blackmail RJ by holding his discord account ransom until he gives me some chocolate."
        jo "Damn Taylor, if you want someone to confess to you that badly, there’s a whole anime club down the hall that would love to have a female member."
        ta "Oh shut up, I’m in this for the food."
        "Taylor’s cheeks turn slightly red as she turns away from Jolee to look at me."
        ta "[name], you said you had a car right?"
        pl "I do but I take the train to campus."
        ta "Dammit! My quest for chocolate continues…"
        "She turns to look at Thomas."
        th "...No."
        "She pouts and turns away."

        jump prehistory

# Conversation between Vday choice and Forum History Choice
    label prehistory:

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

        pl "I’d like to know more about this Fahrenheit 451 book and the fire you mentioned."
        pl "This copy of it does look like it’s been burnt, did you guys set it on fire or something?"
        th "Ah, that. Well this wasn’t us, this is something that happened back in the 1980s."
        th "You see, long ago, the four elements lived in harmony-"
        ta "Thomas, I can’t use THAT in my article-!"
        th "But everything changed when the forum fire happened."
        th "Back in 1986, the forum wasn’t in this room but was being run out of one of the dorms."
        th "Suffice to say, one idiot student later, and the dorm had a giant fire."
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

        jump choiceloop

    label raftenberg:

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
        ta "Yeah, if you look in the cabinet, one of those old newspapers has the article about it. I scoped it out, it’s not even a wives’ tale."
        th "He was steamed alive for 18 seconds and his parents were paid restitution in $18,000 - $1,000 for each second he suffered."
        ta "That part I’m less sure about, but I mean, I wouldn’t put it past Stony Brook."
        pl "How does this all connect to White Castle though?"
        th "The tradition to remember Sherman was that they would make a pilgrimage to White Castle and purchase burgers there as they are… steamed."
        ta "Old forumites are crazier than we are honestly, I just leave some wrapped around or draw a burger on the white board, those guys went hard though."
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
        al "Would it be wrong of me to say I’m hungry now?"
        ta "I’d say no, but I know Jolee will disagree with me."
        jo "Yup."

        jump choiceloop

    label rockstory:

        pl "I have to ask, what is up with this rock?"
        th "Yeah, so as you’ve noticed, we have this giant rock here."
        th "A long time ago, in a Stony Brook building far, far away, a forumite brought a rock into the forum."
        th "We don’t know where he got it. We don’t know how he was able to move it."
        th "What we do know is that somehow it ended up in the forum and every since then, we’ve just… moved it to every following location of the forum."
        al "It’s basically part of the family now."
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
        jo "Taylor, why are you trying to kill his GPA, he just got here."
        ta "Well I mean, I could show him Ascension and get the same effect by getting him addicted to that game."
        pl "What’s Ascension?"
        th "A board game that killed the GPA of the last historian and forced him to leave the club."
        ta "It’s fun but dangerous. That old historian was one of the few people who have uncovered the GPA rock so I maintain that the rock did it and Ascension was just the curse kicking in."
        al "Still though, leave their GPA alone."
        ta "Well I think that’s up to them to decide, no?"

# Endings stored at the bottom of the script
        menu:
            "Uncover the GPA Rock":
                jump endingb

            "Leave it be":
                jump refusal

        label refusal:

            pl "Nah, I’m good. I’d rather not tempt fate like that."
            jo "Smart move."
            ta "Aww, and here I was hoping to induct him into the Ascension cult."
            pl "Maybe later?"
            al "Don’t encourage her, she really isn’t kidding."
            ta "Blood for the blood god, cards for the card throne!"

            jump choiceloop

# Release from the forum history loop
    label loopend:

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

        menu:
            "History is neat.":
                jump neatnerd

            "I'd rather make history.":
                jump neatchad

# Opinion on History
    label neatnerd:

        pl "I guess History is just… pretty neat?"
        pl "I like learning about all this, not really sure how to elaborate on it besides that."
        "Thomas nods approvingly as he pats the cabinet."
        th "I can appreciate it, it’s fun to learn about all these different things."
        ta "You can learn about me when I do something like rob fort knox and end up in your textbooks."

        jump classwalkja

    label neatchad:

        pl "History is cool and all, but I’d rather make history than learn it."
        ta "Oh? Do I hear the sounds of a getaway driver?"
        "Taylor perks up and looks at me with an expression that concerns me and my jail-less life."
        pl "Not trying to become the next Billy the Kid."
        ta "Boo, no fun. You’ll be the alibi then though."

        jump classwalkja

# Leaving for Class with Jolee and Alex

    label classwalkja:

        "I stop as my phone begins to go off, forming a chorus as Jolee and Alex’s ping along as well."
        ta "Oh, all of you have class now, neat. Guess I’m in charge!"
        th "No, I’m staying in here as well."
        ta "Damn, worth a try."
        jo "Come on you two, let’s grab our stuff, doesn’t help to be late. Taylor, no killing Thomas."
        ta "No promises!"
        "We all stand, putting away our laptops and grabbing our backpacks."
        "Taylor and Thomas wave as we head out of the room and up the stairs, pausing as we reach the door outside."
        al "[name], which way are you heading? I’m going by Harriman, Jolee is going near Life Sciences."

        menu:
            "Jolee is going my way.":
                jump joleewalk

            "Alex is going my way.":
                jump alexwalk

    label joleewalk:

        pl "Oh, I’m going Jolee’s way then."
        jo "Nice, let’s walk together!"
        al "Alright, then I’ll catch you two later."

        scene sbuoutside

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

        scene timeskip

        "The night passes..."

        scene forumhallway

        "Wednesday is here, and after sleeping on the long train ride onto campus, I make my way towards the Student Activities Center."

        scene forummainclapcheeks

        "The basement is surprisingly quiet as I approach, but it’s obviously why when I enter to find just Jolee, Thomas and Alex all sitting at the back table with their laptops."
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

            "Taylor seems confident as she looks at me, it has to be her, right?"
            "I throw my batman card on the table and point to her."
            pl "Do you have the joker?"
            "She cackles and shakes her head."
            ta "Nah, I was just baiting you to waste your cards honestly."

            jump taylorturn

        # J'accuse Jolee
        label lljolee:

            "Jolee seems nervous, it has to be her right?"
            "I throw my batman card on the table and point to her."
            pl "Do you have the joker?"
            jo "Huh? Me? Oh no, sorry."
            pl "Dang, you looked like you were worried about something."
            jo "Oh I’m just always stressed like this, don’t mind it."

            jump taylorturn

        # J'accuse Thomas
        label llthomas:

            "Thomas has a perfect poker face right now, maybe it’s him?"
            "I throw my batman card on the table and point to him."
            pl "Do you have the joker?"
            th "Nah."
            "He just shrugs at me and I sigh, letting my extended arm fall."

            jump taylorturn

        # J'accurse Alex
        label llalex:

            "Alex seems confused despite being so excited earlier. Maybe it’s him?"
            "I throw my batman card on the table and point to him."
            pl "Do you have the joker?"
            al "I uh.. I do."
            pl "Nice!"
            al "But I somehow have two of them."

            jump llcontinue

        # If Alex isn't accused, proceeds to Taylor's turn
        label taylorturn:

            "Taylor draws a card happily."
            ta "My turn~!"
            "She looks between all of us for a moment before suddenly pointing at Alex."
            ta "I play Catwoman, let me look at your cards nerd."
            al "If you insist."
            "The two of them lean in, Alex letting her peek at his cards. Almost immediately, her expression grows as confused as him."
            jo "What is it?"
            ta "Alex, how the hell do you have two jokers?"

            jump llcontinue

# All the choices of the love letter game reconverge
    label llcontinue:

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

    # Two choices code
    label dualScene:
        $ updateHearts(taylor, 3)
        $ updateHearts(thomas, 4)
        # Jump to label for appropriate scene
        $ findDates()

    # Beginning of after choice options
    label ALEXJOLEE:
        "I walk in to find Jolee and Alex sitting at the tables alone, each cutting shapes out of pink construction paper."
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

            "I kind of want to go out in the hall with Jolee to tape parts of this up. Hand’s kind of getting sore too."
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
        "I walk in to find Jolee and Alex sitting at the tables alone, each cutting shapes out of pink construction paper."
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

        jump thursdayjolee


    label alexhallway:
        scene forumhallway

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
    # NATE - Turn this following monologue up to like 500 characters per second and autoplay.
    # This is being written in monologue mode so I don't have to write 'al "text"' a million times.

        al """
        Gundam is a massively popular giant robot franchise from Japan that's been running since the late 70s and defined the mecha genre as we know it with the original series Mobile Suit Gundam from 1979 which was a show that was hard science-fiction for the most part. It lasted 43 episodes and wasn't particularly successful at the time, facing cancellation but allowed to finish its story, it only became popular through the compilation film trilogy that succeeded it which trimmed about 10 hours of fat from the original series in total. Nowadays it's recognized, along with other Gundam series as phenomenal examples of anti-war narratives with shows that despite the spectacle of giant robots are about people, the hopes for the growth of humanity, and a reflection of the hell people are capable of. Getting into an old anime series is rough for a lot of people, and the '79 TV series has definite signs of aging, so I wouldn't recommend it for newcomers. I'd personally suggest Mobile Suit Gundam: Iron-Blooded Orphans from 2015, which is the series I started with. It's a complete standalone so you don't need to worry about any of the other Gundam works to be released over the years. Also, as a franchise over 40 years old now, it's a franchise that's been highly malleable, whether you want hard sci-fi anti-war or basically Street Fighter with robots like Mobile Fighter G Gundam, Gundam has something for you. If you wanna see the upcoming Gundam movie, you'd have to watch a good amount of the 'Universal Century' timeline. Gundam has multiple different continuities and Universal Century is the largest one, it includes the original '79 series among others. To watch the new movie, you'd have to watch a bare minimum of Gundam '79, Zeta Gundam, Gundam ZZ, Gundam CCA, Gundam Unicorn, and maybe Gundam NT to get the big picture of what's going on in this movie. If you get really into the series, there's the plastic model kits based on robots from the show known as gunpla, which come in-
        """

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

        jump thursdayalex

    label thomashallway:

        scene forumhallway

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

        jump thursdaythomas

    label taylorhallway:

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

        jump thursdaytaylor

    # Beginning of Thursday - Different Version for each route
    label thursdayjolee:
        "Yeet"

    label thursdayalex:
        "Yeet"

    label thursdaythomas:
        "Yeet"

    label thursdaytaylor:
        "Yeet"

    # Beginning of endings
    label gpa_rock_end:
        rj "GPA ROCK"

        "Ending C: Unlucky Valentine."
        return

    label alex_end:
        al "Alex"

        "Ending D: Gun-DAMN."
        return

    label jolee_end:
        jo "Jolee"

        "Ending E: Blinded by Love."
        return

    label taylor_end:
        ta "Taylor"

        "Ending F: Love Hurts."
        return

    label thomas_end:
        th "Thomas"

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

        "We played and played and played until I realized I had missed class and almost was going to miss the train home."
        "Thomas thankfully drove me to the station so I’d get there in time, but it was the first of many days like that."
        "I thought it was just a fluke, I didn’t forget about my classes the next day, or the day after that, or after that."
        "But soon as I hung out at the forum more, meeting more of its members and playing more of its games…"
        "I started willingly skipping classes to stay in this warm, friendly place."
        "It was only when finals week came and I realized I needed to get perfect scores in so many of my classes to secure passing grades that it dawned on me."
        "Maybe that rock was cursed."
        "And maybe Jolee wasn’t wrong that its members were just agents of the rock."

        "Ending B: Death of a GPA."

    label testing:
        $ store_action(jmp, "exit")
        scene bg hallwaysakura
        show ta at right
        $ store_action(msg, taylor, "Lorem ipsum dolor sit amet,")
        show th at center
        $ store_action(msg, thomas, "consectetur adipiscing elit,")
        show jo at left
        $ store_action(msg, jolee, "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
        hide ta
        hide th
        hide jo
        $ store_action(scn, "hallwaysakura")
        scene bg forumhallway
        show al
        $ store_action(msg, alex, "Ut enim ad minim veniam,")
        hide al
        show ta
        $ store_action(msg, taylor, "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
        hide ta
        show th
        $ store_action(msg, thomas, "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")
        hide th
        show jo
        $ store_action(msg, jolee, "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        hide jo
        $ store_action(scn, "forumhallway")
        $ rewind()

    label exit:
        return
