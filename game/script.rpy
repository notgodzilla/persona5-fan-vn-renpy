# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Ann")
image ann blush = "images/ann/ann_blush.png"
image bg classroom = "images/bgs/school.jpg"


init python:
    player_likes_cats = False 
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg classroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ann blush:
        xalign 0.0
        yalign 1.0
        
    # These display lines of dialogue.

    a "Hello, world!"

    a "Hey! Do you like cats?"
    
    menu:
        "Yes":
            $ player_likes_cats = True
            jump like_cats 
        "No":
            jump dislike_cats
   
label dislike_cats:
        a  "Wow lame"
        
        return
        
label like_cats:
        a "Oh, me too! They're sooooo cute!"

        return
        

