# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define t = Character("Detective Toasty")
# define h = Character("Haini Poly")
# define l = Character("Lemoor Frank")

# The game starts here.
transform half_center_sizeVS: 
    zoom 0.5 # Adjust to show the character at half size centered
    xalign 0.5
    yalign 0.5

transform half_center_size: 
    zoom 0.5 # Adjust to show the character at half size centered
    xalign 0.5
    yalign 0.5

transform bg_size: 
    zoom 1.5
    xalign 0.5
    yalign 0.5

label grandroom:
    default spoken1 = False
    $ spoken = False
    jump grandroom0
    play music "audio/Melancholic Walk.mp3"

label grandroom0:
    scene grandroom at bg_size
    with fade 
    "The grand hall... What should I do next?"
    menu:
        "Move to the next room" if spoken and spoken1:
            # jump Finalscene
            t "Let's move on."
            stop music
            jump FinalScene
           
        "Continue looking here":
            t "There's still more here..."

    call screen hall_trans
    if _return == 1:
        $ spoken = True
        t "I'll go talk to Haini."
        jump grandroomA
    if _return == 2:
        t "I'll go discuss with Sugar."
        jump grandroomB
    if _return == 3:
        $ spoken1 = True
        t "I'll go discuss with Frank."
        jump grandroomC
    # These display lines of dialogue.
label grandroomA:
    show h crying at half_center_size, right
    with dissolve
    show t normal at half_center_size, left
    with dissolve

    play music "/audio/Melancholic Walk.mp3" 
    h "Detective Toasty… do you really think you'll be able to get us out of here?"

    h "I mean, what if… what if something terrible happens?"

    t "I’ll try my best to keep you all safe. No one's getting left behind on my watch."

    show t thinking at half_center_size, left
    
    t "By the way, I don’t think we’ve been properly introduced. Who are you?"

    show h suprised at half_center_size, right

    h "Oh, darling, where are my manners?"

    scene haini at bg_size
    with fade

    h "My name is Haini Poly, and I am a professional actor! You may have heard of me… I’ve starred in several productions—big ones! Well, at least, important to me."

    h "I’ve always been the leading lady in everything I do."

    scene grandroom at bg_size
    with fade

    show h thinking at half_center_size, right
    with dissolve

    show t thinking at half_center_size, left
    with dissolve

    "(She pauses dramatically, placing a hand on her chest as if preparing for an award speech.)"

    h "Honestly, I’m a bit out of my element here."
    h "I mean, I’m used to bright lights, glamorous red carpets, and adoring fans—not creepy cruises and potential murder mysteries."

    show h crying at half_center_size, right

    h "I never thought I’d end up in a real-life thriller."

    show t normal at half_center_size, left

    "(Detective Toasty watches her, unimpressed but maintaining his composure.)"

    t "Right. A professional actor… And what exactly brought you here, Haini?"

    show h thinking at half_center_size, right

    h "Well… I was supposed to be at this fabulous charity gala, but I received this strange letter."

    h "It said that an ‘exclusive event’ was being hosted here, and it’d be a perfect opportunity for networking… you know, rubbing shoulders with the rich and famous."

    h "But then, everything went dark, and now I’m stuck here with you all. Not exactly the glamour I was promised."

    show h crying at half_center_size, right

    h "But seriously… Detective, do you think we’ll be okay? This is like a bad movie plot—except it’s real."

    show t thinking at half_center_size, left

    t "..."
    t "We’ll be alright if we stick together and stay focused. No one’s going to harm you as long as we remain vigilant. We’ll figure out who’s behind this."

    "(Haini nods, her usual confident demeanor faltering just a bit as she bites her lip nervously.)"

    h "I hope so… I don’t want to be the tragic victim in this story."

    hide h crying
    with dissolve
    hide t thinking
    with dissolve
    jump grandroom0
label grandroomC:
    show t normal at half_center_size, left
    with dissolve
    show f normal at half_center_size, right
    with dissolve

    stop music
    play music "audio/Hello, it's Me!.mp3"

    l "Detective Toasty! So glad you’re here to save us!"
    l "I have seen you all over the news! I’m so happy to meet such an amazing detective."

    show t thinking at half_center_size, left

    t "Oh you are too kind. Wait I think I recognize you too. You’re Lemoor Frank right? The famous investment banker?"

    "(Lemoor chuckles, a modest smile playing on his lips as he nods.)"

    scene frank at bg_size
    with fade

    l "Guilty as charged. It’s a little strange being recognized outside of my usual circles, but hey, I guess that’s what happens when you move big money around."

    l "I've been part of some pretty high-profile deals over the years."

    l "But I’ve gotta admit, this whole situation? Completely outside my wheelhouse. I’m used to volatile markets, but this…? "

    l "..."

    l "This is something else."

    scene grandroom at bg_size
    with fade 

    show f normal at half_center_size, right
    with dissolve

    show t normal at half_center_size, left
    with dissolve

    t "I imagine it’s a bit of a change of pace for you. Less stock market volatility, more… well, life or death. Though, honestly, I’m starting to think someone has a pretty dark sense of humor setting this all up."

    l "Yeah, no kidding. But, you know, there’s something about this that still feels… calculated. Like in finance, right? There’s always a strategy. "
    l "This feels like a high-stakes game, and someone’s playing us for their own reasons. Just wish I knew what the hell the rules were."

    show t thinking at half_center_size, left

    l "You’re probably right. Whoever brought us here went to a lot of trouble."
    l "They had a plan, and the letters they sent were clearly part of it. I’m just trying to figure out what their endgame is—and why they chose us."

    show f suprised at half_center_size, right

    l "Yeah… I got this letter about some exclusive event. Big opportunity, sounded too good to pass up. I figured it was some kind of insider deal or investment gathering."

    show f thinking at half_center_size, right 

    l "But when I got to the dock, everything went dark. Next thing I knew, I woke up here."

    l "But what I can’t wrap my head around is why someone would go through all this effort. What could they possibly want from us? Money? Leverage? Revenge?"

    t "It’s hard to say for sure right now. But the fact that they’ve gathered a group of people from different walks of life—people with different talents, connections, and reputations—it tells me they’re after something specific."

    t "We just don’t know what it is yet."

    show f normal at half_center_size, right

    l "Well, whatever it is, they’ve picked the wrong people if they think we’re just going to sit around and wait for answers."

    l "I might not be a detective, but I’m not the kind of guy who stays passive when there’s something at stake."

    show f suprised at half_center_size, right

    l "If you need anything, Detective, I’m here to help. I’ve got a knack for reading people, and I know how to stay calm under pressure."

    "(Detective Toasty nods appreciatively, acknowledging Lemoor’s offer of help.)"

    show t normal at half_center_size, left

    t "That’s good to know. We’re going to need all hands on deck if we want to get to the bottom of this. Keep your eyes open, and if you notice anything out of place, let me know."

    show f normal at half_center_size, right

    "(Lemoor smirks, giving a confident nod.)"

    l "Count on it. I’m already sizing everyone up. Someone here knows more than they’re letting on. And I’m not going to miss a single tell."

    hide t normal 
    hide f normal
    jump grandroom0
    # This ends the game.

label grandroomB:
    show s thinking at half_center_sizeVS
    $ Responded = False
    python:
        apikey = "sk-jRh4hzPEwwlX_6b7G4FW0RrYZ9As45Pq1JHGprNB8CT3BlbkFJmSlvOXyNhYGQixxbIgCEYCKUS77ZPUBLGOynxl_TsA"

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

    jump grandroom0