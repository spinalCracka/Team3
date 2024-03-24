import subprocess
import os
from openai import OpenAI
import chef1
import chef2
import chef3


import settings
settings.init()

#ask 1st script for 1st option
#ask 2nd script 
# 1. Experiment passing a list of ingredients for one script, 
# 2. then ask another script for a recipe for that dish, 
# 3. and then criticize the recipe given by the last script with a third script

#memory = []

while True:
    print("\n")
    print ("memory length is:"+ str( len(settings.memory) ) )
    #print ("some_num is" + str(settings.some_num))
    #print ("some_str is" + str(settings.some_str))
    chef_picker_input = input("Type chef1, chef2, chef3, or chef4 to ask a question to the respective chef:\n")
    if(chef_picker_input=="chef1"):
        chef1.run()
    elif(chef_picker_input=="chef2"):
        chef2.run()
    elif(chef_picker_input=="chef3"):
        chef3.run()
    #subprocess.run(['python',  chef_picker_input +'.py'])
    #os.system("python "+ chef_picker_input +".py")
    