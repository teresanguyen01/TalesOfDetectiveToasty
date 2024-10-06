

screen lib_trans(): ##TODO CHECK SIZES & SIDES
    # add "images/backgrounds/bg library.png"
    if not spoken:
        imagebutton:
            idle im.Scale("images/sprites/dan/d chat.png", 700, 800)
            hover im.Scale("images/sprites/dan/d pixel.png", 700, 800)
            pos(1000, 300)
            action Return(1)
    if spoken:
        add "images/sprites/dan/d pixel.png" at dan_soze, 
    # if spoken: 
        # im.Scale("images/sprites/dan/d pixel.png", 450, 600)
    imagebutton:
            idle im.Scale("images/sprites/sugar/s chat.png", 600, 800)
            hover im.Scale("images/sprites/sugar/s pixel.png", 600, 800)
            pos(400, 300)
            action Return(2)

screen hall_trans():

    if not spoken:
        imagebutton:
                idle im.Scale("images/sprites/haidi/h chat.png", 800, 800)
                hover im.Scale("images/sprites/haidi/h pixel.png", 800, 800)
                pos(1100, 300)
                action Return(1)
    if spoken:
        add "images/sprites/haidi/h pixel.png" at h_soze

    if not spoken1:
        imagebutton:
                idle im.Scale("images/sprites/frank/f chat.png", 800, 800)
                hover im.Scale("images/sprites/frank/f pixel.png", 800, 800)
                pos(600, 300)
                action Return(3)
    
    if spoken1:
        add "images/sprites/frank/f pixel.png" at f_soze
    imagebutton:
            idle im.Scale("images/sprites/sugar/s chat.png", 600, 800)
            hover im.Scale("images/sprites/sugar/s pixel.png", 600, 800)
            pos(100, 300)
            action Return(2)
    
screen kitchen_trans():
    # add "images/backgrounds/bg library.png"
    # add "images/sprites/john/j pixel.png" at j_soze

    if not spoken:
        imagebutton:
                idle im.Scale("images/sprites/john/j chat.png", 620, 800)
                hover im.Scale("images/sprites/john/j pixel.png", 620, 800)
                pos(1050, 300)
                action Return(1)
    if spoken:
        add "images/sprites/john/j pixel.png" at j_soze
    # if spoken:
        # im.Scale("images/sprites/dan/d pixel.png", 450, 600)
    imagebutton:
            idle im.Scale("images/sprites/sugar/s chat.png", 600, 800)
            hover im.Scale("images/sprites/sugar/s pixel.png", 600, 800)
            pos(500, 300)
            action Return(2)

#Library, Hall, Kitchen 