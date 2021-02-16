# The script of the game goes in this file.
# Ideally id make a class for characters and their variables

define al = Character('Alex', color="#FFFF32")
define jo = Character('Jolee', color="#FFAE19")
define ta = Character('Taylor', color="#E50000")
define th = Character('Thomas', color="#66B2FF")
define pl = Character("[name]")
define rj = Character('Egotistical Student', color="#FFFFFF")

# Initialize placeholder values for characters for ease of use
define gpa_rock = "GPA_ROCK"
define alex = "ALEX"
define jolee = "JOLEE"
define taylor = "TAYLOR"
define thomas = "THOMAS"
define jmp = "JMP"
define msg = "MSG"
define scn = "SCN"
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

define place1 = int(0) # placeholder "points" variable
define place2 = int(0) # placeholder "points" variable

# Go backwards wheeeee
init python:
    # Stack to store messages
    stack = []

    # Method to do action based on object type
    def run_action(action):
        # Check type of message stored
        if action[0] == "MSG":
            renpy.say(action[1], action[2])
        elif action[0] == "SCN":
            renpy.scene()
            renpy.show(action[1])
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

# Bookmark for where taylor left off the dialogue work
    label neatnerd:

        pl "I guess History is just... pretty neat?"

    label neatchad:

        pl "Taylor didn't write this yet because it's 2am and she should sleep."

    # Two choices code
    label finalChoices:
        $ updateHearts("THOMAS", 1)
        $ updateHearts("TAYLOR", 3)
        python:
            # Grab two options
            options = findDates()
            choiceOne = options[0].capitalize()
            choiceTwo = options[1].capitalize()
            # Show menu with options
            charChosen = renpy.display_menu([("[choiceOne]", options[0]), ("[choiceTwo]",options[1])])
            # Jump to appropriate label
            jumpToDate(charChosen, "")

    # Beginning of after choice options
    label gpa_rock:
        rj "GPA Rock"
        jump after_choice

    label alex:
        al "Alex"
        jump after_choice

    label jolee:
        jo "Jolee"
        jump after_choice

    label taylor:
        ta "Taylor"
        jump after_choice

    label thomas:
        th "Thomas"
        jump after_choice

    label after_choice:
        "You made your choice"

    # Beginning of endings
    label gpa_rock_end:
        rj "GPA ROCK"
        return

    label alex_end:
        al "Alex"
        return

    label jolee_end:
        jo "Jolee"
        return

    label taylor_end:
        ta "Taylor"
        return

    label thomas_end:
        th "Thomas"
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
        $ store_action(jmp, "testing")
        $ store_action(msg, taylor, "Lorem ipsum dolor sit amet,")
        $ store_action(msg, thomas, "consectetur adipiscing elit,")
        $ store_action(msg, jolee, "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
        $ store_action(scn, "hallwaysakura")
        $ store_action(msg, alex, "Ut enim ad minim veniam,")
        $ store_action(msg, taylor, "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
        $ store_action(msg, thomas, "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")
        $ store_action(msg, jolee, "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        $ store_action(scn, "forumhallway")
        if has_rewinded:
            jump exit
            return
        else:
            $ has_rewinded = True
            $ rewind()
            "Shouldn't reach this"
    label exit:
        return
