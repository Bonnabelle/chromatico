#A set of useful tools for quiz generation
import random

#TODO: Make a list that contains either the frequencies of a note or the letter of the note. The frequencies looks cooler and make it harder to hack, harder to cheat.
#References 440hz version of the chromatic scale, the most used scale in music. A drawback is that it only uses the 0th octave, the lowest frequency on the scale we can hear.
#However, it is only used for reference. The pitches of the notes vary on the 10 octaves, so they all have the potential to be used.
#TODO: Make a class(eventually) that holds four types of question generator functions: singular note, chord, 3rds and 5ths.
#TODO: Make a function that chooses which type of quiz will be generated: audio snippet or play-it-on-the-virtual-piano.
#TODO: Then make a final function that will randomly select the two functions and return them for later use.

all_freq = {16.352 : "C", 17.324 : "C#", 18.354 : "D", 19.445 : "D#",
            20.602 : "E", 21.827 : "F", 23.125 : "F#", 24.500 : "G",
            25.957 : "G#",  27.500 : "A",  29.135 : "A#",  30.868 : "B"}

major_freq = {16.352 : "C", 18.354 : "D", 20.602 : "E", 21.827 : "F", 24.500 : "G", 27.500 : "A", 30.868 : "B"}


minor_freq = {17.324 : "C#", 19.445 : "D#", 23.125 : "F#", 25.957 : "G#",  29.135 : "A#"}

#All the values of the frequencies
all_f_ls = ls = list(all_freq.values())
major_f_ls = ls = list(major_freq.values())
minor_f_ls = list(minor_freq.values())

#List to choose random frequencies from
chooser = [all_f_ls,major_f_ls,minor_f_ls]

def getNote():
    ix = chooser[random.randrange(0,2)] #Chooses index to get a note from

    #Gets random tone from random list
    if ix == all_f_ls:
        tone = all_f_ls[random.randrange(0,len(all_f_ls))]
        return tone
    elif ix == major_f_ls:
        tone = major_f_ls[random.randrange(0,len(major_f_ls))]
        return tone
    elif ix == minor_f_ls:
        tone = minor_f_ls[random.randrange(0,len(minor_f_ls))]
        return tone

def getOption(level):
    options = []

    if level == 1:
        for i in range(0,4):
            options.append(getNote())
    elif level == 2:
        for i in range(0,6):
            options.append(getNote())
    elif level == 3:
        for i in range(0,9):
            options.append(getNote())

    elif level == 4:
        for i in range(0,11):
            options.append(getNote())

    return options

#Chooses a note to be the answer out of the options list
def getAnswer(options):
    return options[random.randrange(0,len(options))]

def createAudioQ():
    note = getNote()
    pass
    #TODO: Get a random audio file out of somewhere
    #TODO: Map the audio file to the correct frequency (key)
    #TODO: return the mapped audio file, use that in the template
