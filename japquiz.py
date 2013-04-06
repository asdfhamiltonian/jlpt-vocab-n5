#!/usr/bin/env python3
# -*- coding: utf8 -*-

import random
import re
import os
import sys
"""
Reads a file named 'formatted' in the current directory that has Q&A pairs in the following format

{<QUESTION>#<ANSWER>}

And then rattles questions and 4 random answers (as choices) 

Keeps track of correct and wrong answers in a file named "progress" with the format:
"10 10"
The first number is correct answers.

This program takes one argument: the number of questions to ask per loop
"""

def tryRemovePronunciation(s):
    if "\\" in s:
        return s.split("\\")[1]
    else:
        return s

#def tryRemovePronunciation(s):
#    return s

inp = open(os.path.dirname(os.path.realpath(__file__)) + "/formatted")
# qna =  [ [ re.split(r'[#{}]', line)[1] ] + [ re.split(r'[#{}]', line)[2].replace("\\n","\n") ] for line in inp.readlines() ] 
qna =  [ [ re.split(r'[#{}]', line)[1] ] + [ re.split(r'[#{}]', line)[2].replace("\\n","\\") ] for line in inp.readlines() ] 
inp.close()

print(len(qna[0]))

repetitions = int(sys.argv[1])
isContinuing = True

while isContinuing:
    for aaaaa in range(repetitions):
        # Print the question
        i = random.randint(0, len(qna))
        print ( qna[i][0] + "\n" )

        # Pick 3 random answers as choices
        choices = []
        for j in range(3):
            k = random.randint(0, len(qna))
            while k == i:    
                k = random.randint(0, len(qna))
            #choices.append(tryRemovePronunciation(qna[k][1]))
            choices.append(qna[k][1])

        # The actual answer
        # Now choices is 4 elements long
        choices.append(qna[i][1])

        # Shuffle choices
        random.shuffle(choices)

        answerNumber = choices.index(qna[i][1]) + 1

        # Print the choices
        for j in range(0,4):
            print(str(j+1) + ": " + tryRemovePronunciation(choices[j]))

        print("Enter which number is correct.")
        
        progressFile = open(os.path.dirname(os.path.realpath(__file__)) + "/progress","r")
        l = [int(x) for x in progressFile.readline().split()]
        corrects = l[0]
        wrongs = l[1]
        progressFile.close()
        
        guess = int(input())
        progressFile = open(os.path.dirname(os.path.realpath(__file__)) + "/progress","w")
        if guess == answerNumber:
            print("Correct!")
            corrects += 1
        else:
            print("Wrong!")
            wrongs += 1

        progressFile.write(str(corrects) + " " + str(wrongs))
        progressFile.close()

        print ("The correct answer was: " + qna[i][1] )
        print("Your correct-to-wrong ratio is {}%".format(float(corrects)/(corrects + wrongs) * 100))

    print("Try again? [n]")
    a = input().lower()
    isContinuing = a == "y" or a == "yes"
