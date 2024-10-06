label library: 
    default spoken = False
    $ spoken = False
    jump library0
    play music "audio/Melancholic Walk.mp3"
label library0:
    scene bg library at bg_size
    with fade
    "The library... What should I do next?"
    menu:
        "Move to the next room"if spoken:
            #TODO transition
            t "Let's move on."
            stop music
            jump kitchen
            
        "Continue looking here" :
            t "There's still more here..."

    call screen lib_trans
    if _return == 1:
        $ spoken = True
        t "I'll go talk to Danson."
        jump libraryA
    if _return == 2:
        t "I'll go discuss with Sugar."
        jump libraryB
        
    transform half_size:
        zoom 0.47
        xalign 0.5
        yalign 0.5
    transform half_center_sizeSUGAR:
        zoom 0.5
        xalign 0.5
        yalign 0.5
    
    transform dan_soze:
        zoom 0.7
        xalign .84
        yalign 1.0
    transform j_soze:
        zoom 0.7
        xalign 0.84
        yalign 0.999
    transform h_soze:
        zoom 0.7
        xalign 0.9
        yalign 0.999
    transform bg_size:
        zoom 1.5
        xalign 0.5
        yalign 0.5
    transform f_soze:
        zoom 0.7
        xalign 0.54
        yalign 0.999
    
    
    # show normal
label libraryA: 
    show d sleepy at half_size, right
    with dissolve
    show t normal at half_size, left
    with dissolve
    d "…zzz…"
    t "Are you okay?"
    "(There’s a pause as Danson Han doesn’t respond, his head bobbing forward slightly. Detective Toasty leans in closer.)"
    show t suprised at half_size, left
    t "Hello?"
    show d suprised at half_size, right
    "Danson Han suddenly jolts awake, blinking sleepily. He takes a moment to orient himself before lazily looking up at Detective Toasty."
    show d sleepy at half_size, right
    show t normal at half_size, left
    d "Oh… Hello, Detective."
    t "Hello. I introduced myself to you earlier, but we haven’t had a chance to talk properly. Who are you?"
    "(Danson Han rubs his eyes, yawning slightly before responding in his slow, sleepy voice.)"
    scene danson at bg_size
    with fade
    d "I’m Danson Han, but… uh… you can just call me Dan. I’m a student… at Kale University. Studying mechanical engineering. You know… gears, machines, that sort of thing. It’s… uhh… …pretty interesting stuff, I guess."
    t "Mechanical engineering, huh? That’s impressive. And… how is your day going so far, Dan?"
    "(Dan yawns again, looking like he could easily drift back to sleep at any moment, but he makes an effort to answer.)"
    scene bg library at bg_size
    with fade
    show t thinking at half_size, left, with dissolve
    show d suprised at half_size, right, with dissolve
    d  "Uh… well, you know… Just trying to stay awake, mostly. My day’s been kinda weird… kinda confusing. I didn’t expect to be here… not really my idea of fun. But… uh… I guess it’s alright… for now. How’s your day, Detective?"
    show t normal at half_size, left
    t "I’m managing, thanks for asking. But I’m more interested in hearing about you. Tell me more, Dan. What brought you here?"
    "(Dan looks off to the side, thinking for a moment. He seems to be trying to recall the details, though his exhaustion makes his responses slow.)"
    d "Well… I got this letter, right? I thought it was about… some engineering competition or scholarship thing. Sounded like it could be… good for my career, you know? So I figured… why not check it out? But then…"
    d "I don’t really remember much after that. I was at the dock… then… poof. Here I am. Guess I fell asleep somewhere in between. Can’t say I’m the best at staying awake for… uh… long periods of time."
    show t thinking at half_size, left
    t "You don’t remember much before waking up here? Did you notice anything unusual at the dock? Anyone suspicious?"
    "(Dan’s eyes droop for a second as he considers the question, then he shakes his head slowly.)"
    d "No… not really. I was kinda just… focused on getting through the day. I wasn’t really paying attention, to be honest… I’m usually pretty wrapped up in my own head. But now that you mention it… there might have been…"
    d "...someone standing near me? I dunno… everything’s kinda foggy."
    show t normal at half_size, left
    t "That’s alright. Just let me know if you remember anything more. Even the smallest detail could help."
    d "Yeah… sure… If I remember something, I’ll let you know. But, uh… right now, I think I’m just gonna… take a quick nap…"
    t "Try not to sleep too long, Dan. We’re in the middle of a mystery here."
    show d sleepy at half_size, right
    d "Yeah… yeah, I know… Just a few minutes… zzz…"
    hide d sleepy with dissolve
    hide t normal with dissolve
    jump library0
label libraryB: 
    show s normal at half_center_sizeSUGAR
    default Responded = False
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

    jump library0
# Investigation: 

# Click on the bookshelves: 
# Sugar: Wow! They have rare editions of Agatha Christie and Holmes here! That’s amazing! 
