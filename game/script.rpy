# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Narator",color="ffcccc")

define i = Character("Emily")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "house-room.png" or "house-room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "emilly-happy.png" to the images
    # directory.

    # These display lines of dialogue.

    e "So,first of all this is a beta test,so it has many bugs!"

    e "We have a website and the game is officially open source!"

    e "What means if the game is open source?"

    e "You can modify the story,the text and many others!"

    e "The source code is officially on github!"

    e "So,let's play!"

    scene house room

    show emily happy

    i "Hi! My name is Emily!"

    i "This is my story so,stay tuned!"

    # This ends the game.

    return
