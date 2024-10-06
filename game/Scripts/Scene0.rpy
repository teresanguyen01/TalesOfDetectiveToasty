# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    image bg road = "road.jpg"

    $ flash = Fade(.35, 0, .75, color="#fff")


# The game starts here.

label Scene0:
    stop music

    transform half_size:
        zoom 0.5
        xalign 0.5
        yalign 0.5

    transform bg_size3:
        zoom 1.25
        xalign 0.5
        yalign 0.5
    
    transform bg_size3:
        zoom 1.1
        xalign 0.5
        yalign 0.5 
    transform bg_size2:
        zoom 7
        xalign 0.5
        yalign 0.5

        
    transform bg_size5:
        zoom 1.75
        xalign 0.5
        yalign 0.5
    
    transform char_size:
        zoom 0.5
        xalign 0.5
        yalign 0.5


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    # show Images/sprites/frank/normal.png
    scene blackfade at bg_size2, with flash


    # These display lines of dialogue.

    t  "Ugh… where am I…?"

    #(Flash of blinding light, briefly illuminating the scene. A CG of all five characters flashes on screen, each frozen in shock or concern.*)

    q "Oh, he’s awake! Thank goodness. I was worried." #heidi

    q  "P-Please help us! This can’t be real!" # dan 

    q "Hey, guys, give him some space. Let's not suffocate him." #lemoor

    q "This guy better be useful. We're stuck in a mess, and I have no time for incompetence!" #john

    play music "audio/Melancholic Walk.mp3"
    scene wakeup at bg_size3, with fade
    t "What?!"
    t "Who are you people, and where exactly are we?"
   
    scene bg beginningspot at bg_size5, with fade

    show s normal at char_size, with dissolve

    s "Detective Toasty! Oh, I’m so relieved you’re finally up!" 
    #big smile* 
    show s suprised
    s "It looks like we’re on… umm… some sort of cruise, maybe?"
    
    hide s normal 
    show j angry at char_size, with dissolve

    j "No shit we’re on a cruise! What are you two, playing dumb?"

    j "Why don’t you tell us who the hell you are and what you’ve done? Did you drag us here?"

    t "No. Not exactly..."

    scene toastyreceiveletterbw at bg_size3,
    with fade
    t "I received a letter a few days ago. It warned me that a murder was going to take place on this ship."
    t "Naturally, I followed the trail, arriving at the dock as instructed." 
    t "The next thing I remember… is waking up here with all of you."

    scene bg beginningspot at bg_size5, with fade
    #(*The flashback ends, the scene shifts back to the tense room.*)
    show h suprised at char_size, with dissolve
    #gasps dramatically, hands clutching her pearls*
    h  "A murder?!! Oh no, this is just awful!" 
    show h crying at char_size
    #*tears up, her crying sprite activates* 
    h "I didn’t sign up for this! I have my own life to deal with, I can’t die here!"
    hide h crying
    #*serious, adjusting his tie* 
       
    show f thinking at char_size, with dissolve 

    l "Someone sent me a letter too. Different message, but same result. Led me right here before I blacked out."

    hide f thinking 
    show d normal at char_size, with dissolve
    d "Y-Yeah, me too… This is freaking me out. We all got tricked, right? Letters, lies, and now we’re trapped on this ship. I don’t… I don’t like this at all."

    hide d normal
    show j normal at char_size, with dissolve
    j "Tricked?! I’m a busy man! I’ve got deals to close, money on the line—this whole thing is a disaster!" 
    "(Haini starts crying louder, exaggerated tears streaming down her sprite.)"
    show j angry at char_size
    j "Who the hell is behind this?!"

    hide j angry 
    show h crying at char_size, with dissolve
    h "I just wanna go homeeeeee!"

    t "Everyone needs to calm down. Losing our heads won’t help us figure this out."

    hide h crying
    show j angry at char_size, with dissolve
    j "Calm down?! Are you out of your mind?! We’re trapped here, on a cursed cruise, with no clue what's happening!"

    hide j angry
    show f normal at char_size, with dissolve
    l  "Before we all lose it, maybe we should get some introductions out of the way. Who exactly are all of you?"

    hide f normal
    show t normal at char_size, with dissolve
    t "I’m Detective Toasty. I was brought here to prevent a murder—though it seems like there’s a lot more going on than I first expected."

    hide t normal
    show s shy_happy at char_size, with dissolve
    s "And I’m Sugar! Detective Toasty’s assistant, at your service!" #*grins brightly* 
    s "We’re here to solve this mystery and keep everyone safe."

    hide s shy_happy
    show d normal at char_size, with dissolve
    d "A detective… and his assistant? That’s actually kinda cool…" 
    d "I just hope you guys can figure this out."

    hide d normal
    show f normal at char_size, with dissolve
    l "While you were unconscious, Detective, I took a quick look around." 
    l "We’re locked in pretty tight—access seems to be restricted to just three rooms. I couldn't find a way out."

    hide f normal
    show s thinking at char_size, with dissolve
    s "Then that’s where we start!" 
    s "We’ve got three rooms, and that’s enough to begin investigating, right?"

    hide s thinking
    show t thinking at char_size, with dissolve
    t "Exactly. We need to explore every inch of this place." 
    t "Whoever brought us here wanted something, and we’ll need to figure out what that is if we want to get out in one piece."

    hide t thinking
    show j angry at char_size, with dissolve
    j "Great. Just what I needed, a scavenger hunt led by a wannabe Sherlock and his over-enthusiastic assistant."

    hide j angry 
    show h angry at char_size, with dissolve
    h "As long as we figure this out quickly… I don't wanna be stuck here longer than I have to!"

    hide h angry 
    show f normal at char_size, with dissolve
    l "We should split up and start searching. Cover more ground that way."

    hide f normal 
    show d suprised at char_size, with dissolve
    d "S-Split up? What if something happens to one of us while we’re alone?"

    hide d suprised 
    show t thinking at char_size, with dissolve
    t "We’ll stay in pairs. It’s safer that way. Let's keep our eyes open for anything out of the ordinary—and if you find anything suspicious, report back immediately."

    "(Everyone nods in agreement. The tension is palpable.)"
    hide t thinking 
    show s normal at char_size, with dissolve
    s "Alright, let’s do this! Time to crack this case wide open!" 

    #(With a determined look, the group begins to disperse, and the investigation officially starts.*)
    jump library
