# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

transform half_center_size: 
    zoom 0.5 # Adjust to show the character at half size centered
    xalign 0.5
    yalign 0.5

transform half_john: 
    zoom 1
    xalign 0.5
    yalign 0.5

transform bg_size: 
    zoom 1.5
    xalign 0.5
    yalign 0.5

transform bg_size_JOHN: 
    zoom 1.1
    xalign 0.5
    yalign 0.5
label kitchen:
    $ spoken = False
    jump kitchen0
    play music "audio/Melancholic Walk.mp3"
label kitchen0:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    # jump start1
    scene kitchen at bg_size
    with fade 
    "The kitchen... What should I do next?"
    menu:
        "Move to the next room" if spoken:
            t "Let's move on."
            stop music
            jump grandroom
            
        "Continue looking here":
            t "There's still more here..."

    call screen kitchen_trans
    if _return == 1:
        $ spoken = True
        t "I'll go talk to John."
        jump kitchenA
    if _return == 2:
        t "I'll go discuss with Sugar."
        jump kitchenB
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
label kitchenA:
    show j angry at half_center_size, right
    with dissolve
    show t normal at half_center_size, left
    with dissolve
    # These display lines of dialogue.

    play music "/audio/The search.mp3" 
    j "I don’t care if you’re a fucking detective. I only care if you can get us the hell out of here! This situation is a complete waste of my time!"

    t "Hey, calm down. I understand you're frustrated, but I’m trying the best that I can right now. Who exactly are you?"

    scene john at bg_size_JOHN, with fade
    j "How do you not know who I am?! I’m John Harney! I’m a famous entrepreneur, and I run a multi-billion-dollar corporation!"
    j "Ever heard of Harney Industries? No? Well, clearly you’re not paying attention to the real world!"

    #show t thinking at half_center_size, left
    
    t "I see. So you’re John Harney, the businessman. And what exactly brought you here? You mentioned earlier you had a meeting to attend—was that connected to why you came?"
    scene kitchen at bg_size, with fade
    show j smug at half_john, right, with dissolve

    show t thinking at half_center_size, left, with dissolve
    j "Yeah, I had an important business meeting lined up. And then this damn letter shows up, talking about some exclusive investment opportunity on this ship. "

    j "Normally, I wouldn’t waste my time on something like this, but it sounded… interesting. Said it would revolutionize industries. Something about cutting-edge technology."

    show j smug2 at half_john, right

    j "I figured, why not? I’m always on the lookout for the next big thing, you know?"

    show j angry at half_center_size, right
    j "But now, instead of making deals and expanding my empire, I’m stuck on this ship with a bunch of strangers and no idea what the hell is going on."

    "(Detective Toasty watches him carefully, noting the sharpness in his words but also the hint of nervousness beneath his bravado.)"

    t "You and everyone else received similar letters. It seems like whoever brought us here specifically targeted individuals from different industries. That’s no coincidence. We were all chosen for a reason."

    j "Yeah, well, good for them. What I want to know is who the hell is behind this! I’ve got more important things to deal with than playing along with some psycho’s little game."

    show t normal at half_center_size, left

    t "John, do you remember anything unusual before you blacked out? Anyone around the dock or something that stood out?"

    show j angry at half_center_size, right

    j "Look, I don’t remember much. I got to the dock, and there was no one there. It was deserted. I figured it was some kind of… private affair. "

    show j smug2 at half_john, right
    j "Next thing I know, I felt this sharp sting on my neck, like I was injected with something. Then… nothing. I woke up here, pissed off and confused."

    show t thinking at half_center_size, left

    t "Sounds familiar. Whoever did this planned everything down to the smallest detail. The question is… why us? Why now?"

    show j angry at half_center_size, right
    j "I don’t care about the ‘why.’ I care about getting off this ship and back to my life."
    show j smug2 at half_john, right
    j "You figure out who’s behind this nonsense, and I’ll get back to making real money. So unless you’ve got a way to open these doors, stop wasting my time."

    t "I understand. We’re all on edge right now, but I need you to stay focused. The sooner we figure this out, the sooner we all get off this ship. You might even be able to help with that."

    show j smug at half_john, right

    j "Fine. But don’t expect me to play detective. I’m not here to solve mysteries—I’m here to make things happen. Just… let me know if you find something useful."

    jump kitchen0 
label kitchenB:
    show s thinking at half_center_size
    $ Responded = False
    python:
        apikey = "######"

        import chatgpt

        #The "system" message is the initial prompt of your NPC
        #Messages with "assistant" are messages from the NPC, here there's a first message so we add it to the list of messages already said by the NPC
        messages = [
            {"role": "system", "content": 
            "Assistant Sugar, always cheerful and optimistic, has been aiding Detective Toasty in solving mysteries for several years. Raised in an orphanage full of secrets, Sugar developed a knack for noticing the unnoticed and a passion for puzzles. Their happy-go-lucky attitude often brings a light-hearted touch to the grimmest investigations. Give advice on talking to people and investigating the scene. You have knowledge of these characters: 1) Detective Toasty your male boss who is calm, rational, and blunt, 2)Danson Han who is a male frantic, nervous, and introverted student at Kale, 3) Haini Poly a female diva, 4) Lemoor Frank a male working in economics who is very conceited and 5) John Harney a very rude and stuck up male CEO of Harney Industries. Please limit your tokens to 1000 and do not do any weird spacing. Do not write with any new lines and keep it under 70 words."},
            {"role": "assistant", "content": "Hi Detective Toasty! Do you need help with anything?"}
        ]
        while not Responded:
            #We ask the user for an input
            user_input = renpy.input("Detective Toasty: ", length=1000)
            #Then add it in the "history" of messages
            messages.append(
                {"role": "user", "content": user_input}
            )

            if apikey != '':
                #We ask ChatGPT to "complete" the conversation by adding a response
                #If you have an API key, let's use that
                messages = chatgpt.completion(messages, api_key=apikey)
            else :
                #If you don't provide an API key, we'll use my proxy
                #This proxy only allows a set of NPCs, and serves to "hide" my API key
                #Check the README.md to know more about it
                #Of course if you modify the NPC in any way, it won't work, you'll have to use your own API key instead.
                messages = chatgpt.completion(messages,proxy="http://prima.wiki/proxy.php")

            #Here we only care about the response from the NPC
            response = messages[-1]["content"]
            #So we display just that
            s("[response]")
            Responded = True

    jump kitchen0