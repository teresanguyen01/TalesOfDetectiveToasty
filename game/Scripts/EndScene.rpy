label FinalScene:

    transform half_size:
        zoom 0.5
        xalign 0.5
        yalign 0.5

    transform half_size22:
        zoom 0.6
        xalign 0.5
        yalign 0.5

    transform bg_size10:
        zoom 1.5
        xalign 0.5
        yalign 0.5

    scene grandroom at bg_size10, with fade
    
    "(The group finishes their investigation of the various locations on the ship and gathers back in the main hall where they initially started)" 
    "(The mood is tense but calm, everyone on edge from the strange circumstances but still trying to maintain composure.)"
    
    show s thinking at half_size22, with dissolve
    s "It looks like we’ve finished investigating everything for now. Let’s head back to where we started and see if we can make sense of all this."

    "(As the group begins to turn and head back toward the starting point, suddenly, the lights flicker, plunging the room into complete darkness.)" 
    

    hide s thinking 
    scene black with fade
    play sound "audio/screaming.mp3"
    "Ahhhhh!!!"

    play music "audio/suspense.mp3"
    play sound "audio/running.mp3"
    "(Footsteps echo in the darkness, followed by the sound of frantic running.)" 
    hide h crying
    scene grandroom at bg_size10 with fade 
    show d suprised at half_size, with dissolve
    d "W-What just happened?!" 
    d "That scream… it came from the kitchen!"

    scene black with fade
    play sound "audio/running.mp3"
    "(The group rushes to the kitchen, their hearts pounding with fear and adrenaline.)"
    scene kitchen at bg_size10, with fade
    hide d suprised
    scene deadscene with fade


    h "Oh my god! He’s… he’s dead!! John’s dead!!"

    l "What the… No… This isn’t real. It can’t be real."

    d "W-We were just talking to him… How could this…? How did this happen?!"
    
    s "Detective… what do we do now?"
    scene kitchen at bg_size10, with fade
    show t thinking at half_size, with dissolve
    t "It’s exactly what we feared… There’s a murderer on this ship."

    hide t thinking 
    show h suprised at half_size, with dissolve
    h "A murderer?! B-But… why? Why would someone kill him?!"
    hide h suprised
    show f thinking at half_size, with dissolve
    l "One of us is responsible for this. Someone here knew what they were doing. We’ve all been manipulated… played like pieces on a board."

    hide f thinking
    show d suprised at half_size, with dissolve
    d "I… I didn’t do this! I swear! I wouldn’t hurt anyone!"

    hide d suprised
    show t normal at half_size, with dissolve
    t "Everyone, listen to me. I know this is terrifying, but we can’t lose our heads. We need to stay rational. No one leaves this kitchen until we figure out what happened."

    "(The group quiets down, although the tension is thick in the air. Each person looks around at the others with a mix of fear and suspicion.)" 
    "(The gravity of the situation is sinking in—one of them is hiding something.)"

    hide t normal
    show s thinking at half_size, with dissolve
    s "Detective Toasty is right. We need to retrace our steps and find any clues we might have missed. We have to figure out who did this before anyone else gets hurt."

    hide s thinking 
    show t thinking at half_size, with dissolve
    t "The killer is among us, and they’re hoping we’ll turn on each other. But that’s not going to happen. We’re going to stay focused, and we’ll find out who’s responsible for this."

    "(The room grows even more tense as everyone exchanges wary glances.)" 
    "(The realization that the killer could be standing right next to them makes every movement feel charged with suspicion.)"
    hide t thinking 
    show h crying at half_size, with dissolve
    h "I just… I just want to go home…"

    hide h crying
    show f thinking at half_size, with dissolve
    l "We can’t let whoever did this get away with it. We have to find them. And fast."
    hide f thinking 
    show d normal at half_size, with dissolve
    d  "Y-Yeah… but… how do we even know where to start?"

    hide d normal 
    show t normal at half_size, with dissolve
    t "We start here. We search this room thoroughly, every inch of it. No one leaves until we’ve turned this place upside down. There has to be something—something that gives us a lead."

    scene black with fade
    jump Credits


label Credits:
    scene grandroom at bg_size
    with Fade(0.5, 2.0, 0.5)


    stop music fadeout 0.5
    
    # leave music for Valentina's pop song 
   
    "Thank you for playing The Tales of Detective Toasty!"
    "This project was made for Yhack 2024"
    
    "Developers: Teresa Nguyen, Isabella Campisi, Danielle Campisi"

    "Thank you for playing once again!"
    "To be continued..."
    scene bg black
    with Fade (0.5,5.0,0.5)
    return
  