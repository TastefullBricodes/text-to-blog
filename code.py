import os
paragraphcount = 0
title = ""
subtitle = ""
author = ""
output = ""

title = input("What is the title of your blog? ")
subtitle = input("What is the subtitle of your blog? ")
author = input("What is your name? ")
output += "<h1>" + title + "</h1>"
output += "<h2>" + subtitle + "</h2>"
output += "<h3>By " + author + "</h3>"
paragraphcount = int(input("How many paragraphs do you want to add? "))

for i in range(paragraphcount):
    paragraph = input("Enter paragraph " + str(i + 1) + ": ")
    output += "<p>" + paragraph + "</p>"

# clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

print(output)
