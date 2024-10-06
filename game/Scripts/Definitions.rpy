init python:
    renpy.music.register_channel("sfx1", mixer="sfx")
    renpy.music.register_channel("sfx2", mixer="sfx")
    renpy.music.register_channel("sfx3", mixer="sfx")
    renpy.music.register_channel("sfx4", mixer="sfx")
    renpy.music.register_channel("sfx5", mixer="sfx")
    renpy.music.register_channel("sfx6", mixer="sfx")
    renpy.music.register_channel("sfx7", mixer="sfx")
$ renpy.music.set_volume(0.1, channel="sfx1")
$ renpy.music.set_volume(0.1, channel="sfx2")
$ renpy.music.set_volume(0.1, channel="sfx3")
$ renpy.music.set_volume(0.1, channel="sfx4")
$ renpy.music.set_volume(0.1, channel="sfx5")
$ renpy.music.set_volume(0.1, channel="sfx6")
$ renpy.music.set_volume(0.1, channel="sfx7")
init python:
    def text_chirps4(event, **kwargs):
        if event == "show":
            renpy.sound.play("audio/dialogueblip.mp3", channel="sfx1")
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="sfx1")
    def text_chirps2(event, **kwargs):
        if event == "show":
            renpy.sound.play("audio/dialogueblip.mp3", channel="sfx2")
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="sfx2")
    def text_chirps3(event, **kwargs):
        if event == "show":
            renpy.sound.play("audio/dialogueblip.mp3", channel="sfx3")
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="sfx3")
    def text_chirps(event, **kwargs):
        if event == "show":
            renpy.sound.play("audio/dialogueblip.mp3", channel="sfx4")
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="sfx4")
    def text_chirp(event, **kwargs):
        if event == "show":
            renpy.sound.play("audio/dialogueblip copy.mp3", channel="sfx5")
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="sfx5")
    def text_chirps6(event, **kwargs):
        if event == "show":
            renpy.sound.play("audio/dialogueblip.mp3", channel="sfx6")
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="sfx6")
    def text_chirps7(event, **kwargs):
        if event == "show":
            renpy.sound.play("audio/dialogueblip.mp3", channel="sfx7")
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="sfx7")

define t = Character("Detective Toasty", color="#2A88B8", callback = text_chirp)
define s = Character("Assistant Sugar", color="#CBB4F0", callback = text_chirps2) #
define d = Character("Danson Han", color="#1463eb", callback = text_chirps3) #
define l = Character("Lemoor Frank", color="#76b576", callback = text_chirp)
define h = Character("Haini Poly", color="#E63CA2", callback = text_chirp)
define j = Character("John Harney", color="#23dcda", callback = text_chirps7) #
define q = Character("???", color="#5E585C", callback = text_chirps) #
