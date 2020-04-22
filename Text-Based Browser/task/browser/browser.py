import os
import sys
import requests
import re
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style


blacklist = ['[document]', 'head', 'script', 'style',
             'body', 'html', 'h1', 'h2', 'h3', 'h4', 'h5',
             'h6', 'title',
             'table', 'div', 'li', 'form',
             'img', 'tr', '\n']

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here
userInput = input()
print("User input:" + userInput)
#dirName = sys.argv[1]
dirName = "./tb_tabs"

try:
    # Create target Directory
    os.mkdir(dirName)
    print("Directory ", dirName, " Created ")
except FileExistsError:
    print("Directory ", dirName, " already exists")

while (userInput != 'exit'):
    if os.path.exists(dirName + "/" + userInput + ".txt"):
        with open(dirName + "/" + userInput + ".txt") as f:
            print(f.read())
            userInput = input()
            break
    if "." not in userInput: break
    if "https://" in userInput:
        r = requests.get(userInput)
    else:
        r = requests.get("https://" + userInput)

    responce = r.content

    soup = BeautifulSoup(responce, 'html.parser')
    text = soup.find_all(text=True)




    output = ''
    for t in text:

        if t.parent.name not in blacklist:
            if(t.parent.name == 'a'):
                output +=Fore.BLUE + '{} '.format(t)

    print(output)
    fileName = userInput.split(".")
    nameOfFile = ''
    for i in range(len(fileName) - 1):
        nameOfFile += fileName[i] + "."


    with open(dirName + "/" + nameOfFile + "txt", "w+") as f:
        f.write(output)

    userInput = input()


