txt = "The quick brown fox jumps over the lazy dog."

###############################################################################
# Done: 1. (1 pt)
#   For the following exercises, you may need to reference the material on 
#   string methods.
#
#   And again, you will reference the string at the top of this file.
#
#   Immediately below this _TODO_, write code that:
#     1. Modifies the string to be in all upper case letters, saves it to a 
#        variable called   upper   and prints its value.
#     2. Modifies the string again to be in all lower case letters, saves it to
#        a variable called   lower   and prints its vale.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
upper = txt.upper()
lower = txt.lower()
print(upper)
print(lower)
###############################################################################
# Done: 2. (1 pt)
#   Immediately below this _TODO_, write code that:
#     - Replaces the word 'brown' with a different color of your choosing.
#     - Saves the result to a variable name
#     - Prints the value of the variable
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
color_change = txt.replace('brown', 'cyan')
print(color_change)
###############################################################################
# Done: 3. (2 pts)
#   Immediately below this _TODO_, write code that:
#     - Capitalizes the first letter of each word in the string (HINT: look
#       through the methods resource in the pre-class materials that might be
#       helpful)
#     - Saves the result to a variable name
#     - Prints the value of the variable
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
title = txt.title()
print(title)