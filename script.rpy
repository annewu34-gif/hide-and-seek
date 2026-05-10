default level = 0
default found = 0

# 每个外星人的独立标记
default a1_f1 = False  # Level 1, alien 1
default a1_f2 = False  # Level 1, alien 2
default a2_f1 = False
default a2_f2 = False
default a2_f3 = False
default a3_f1 = False
default a3_f2 = False
default a3_f3 = False
default a3_f4 = False

label start:
    jump main_menu

label main_menu:
    scene bg
    menu:
        "Start Game":
            $ level = 1
            $ found = 0
            jump level1
        "Quit":
            return

# -------------------- LEVEL 1 (2 aliens) --------------------
label level1:
    scene 1
    'Human met some ailnes during the travel in the space'
    'They want to be friends with human'
    'Human tought them a little game which called Hide And Seek'
    'Players need to find the aline who hides in the place!'
    "Level 1"
    "Find 2 aliens!"
    scene bg space

    # 重置标记
    $ a1_f1 = False
    $ a1_f2 = False
    $ found = 0

    screen level1_aliens():
        if not a1_f1:
            button:
                xpos 420 ypos 350
                xsize 50 ysize 50
                background "alien.png"
                action [SetVariable("a1_f1", True), SetVariable("found", found+1), Jump("check1")]
        if not a1_f2:
            button:
                xpos 1380 ypos 680
                xsize 50 ysize 50
                background "alien.png"
                action [SetVariable("a1_f2", True), SetVariable("found", found+1), Jump("check1")]

    show screen level1_aliens
    $ renpy.pause()

label check1:
    hide screen level1_aliens
    "You found an alien! Found: [found]/2"
    if found >= 2:
        "Level 1 Complete!"
        $ found = 0
        jump level2
    else:
        show screen level1_aliens
        $ renpy.pause()
        jump check1

# -------------------- LEVEL 2 (3 aliens) --------------------
label level2:
    scene bg2
    "Level 2"
    "Find 3 aliens!"

    $ a2_f1 = False
    $ a2_f2 = False
    $ a2_f3 = False
    $ found = 0

    screen level2_aliens():
        if not a2_f1:
            button:
                xpos 180 ypos 820
                xsize 50 ysize 50
                background "alien.png"
                action [SetVariable("a2_f1", True), SetVariable("found", found+1), Jump("check2")]
        if not a2_f2:
            button:
                xpos 960 ypos 180
                xsize 50 ysize 50
                background "alien.png"
                action [SetVariable("a2_f2", True), SetVariable("found", found+1), Jump("check2")]
        if not a2_f3:
            button:
                xpos 1550 ypos 750
                xsize 50 ysize 50
                background "alien.png"
                action [SetVariable("a2_f3", True), SetVariable("found", found+1), Jump("check2")]

    show screen level2_aliens
    $ renpy.pause()

label check2:
    hide screen level2_aliens
    "You found an alien! Found: [found]/3"
    if found >= 3:
        "Level 2 Complete!"
        $ found = 0
        jump level3
    else:
        show screen level2_aliens
        $ renpy.pause()
        jump check2

# -------------------- LEVEL 3 (4 aliens) --------------------
label level3:
    scene bg3
    "Level 3"
    "Find 4 aliens!"

    $ a3_f1 = False
    $ a3_f2 = False
    $ a3_f3 = False
    $ a3_f4 = False
    $ found = 0

    screen level3_aliens():
        if not a3_f1:
            button:
                xpos 120 ypos 160
                xsize 50 ysize 50
                background "alien.png"
                action [SetVariable("a3_f1", True), SetVariable("found", found+1), Jump("check3")]
        if not a3_f2:
            button:
                xpos 1700 ypos 280
                xsize 50 ysize 50
                background "alien.png"
                action [SetVariable("a3_f2", True), SetVariable("found", found+1), Jump("check3")]
        if not a3_f3:
            button:
                xpos 640 ypos 900
                xsize 50 ysize 50
                background "alien.png"
                action [SetVariable("a3_f3", True), SetVariable("found", found+1), Jump("check3")]
        if not a3_f4:
            button:
                xpos 1150 ypos 520
                xsize 50 ysize 50
                background "alien.png"
                action [SetVariable("a3_f4", True), SetVariable("found", found+1), Jump("check3")]

    show screen level3_aliens
    $ renpy.pause()

label check3:
    hide screen level3_aliens
    "You found an alien! Found: [found]/4"
    if found >= 4:
        "Level 3 Complete! You beat the game!"
        jump main_menu
    else:
        show screen level3_aliens
        $ renpy.pause()
        jump check3