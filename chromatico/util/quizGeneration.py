#A set of useful tools for quiz generation
import random

#TODO: Make a list that contains either the frequencies of a note or the letter of the note. The frequencies looks cooler and make it harder to hack, harder to cheat.
#References 440hz version of the chromatic scale, the most used scale in music. A drawback is that it only uses the 0th octave, the lowest frequency on the scale we can hear.
#However, it is only used for reference. The pitches of the notes vary on the 10 octaves, so they all have the potential to be used.
#TODO: Make a function that chooses which type of quiz will be generated: audio snippet or play-it-on-the-virtual-piano.
#TODO: Then make a final function that will randomly select the two functions and return them for later use.

all_freq = {"C" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/261.mp3",
            "C#" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/277.mp3",
            18.354 : "D", 19.445 : "D#",
            20.602 : "E", 21.827 : "F", 23.125 : "F#", 24.500 : "G",
            25.957 : "G#",  27.500 : "A",  29.135 : "A#",  30.868 : "B"}

major_freq = {16.352 : "C", 18.354 : "D", 20.602 : "E", 21.827 : "F", 24.500 : "G", 27.500 : "A", 30.868 : "B"}


minor_freq = {17.324 : "C#", 19.445 : "D#", 23.125 : "F#", 25.957 : "G#",  29.135 : "A#"}

#All the values of the frequencies
all_f_ls = ls = list(all_freq.keys())
major_f_ls = ls = list(major_freq.keys())
minor_f_ls = list(minor_freq.keys())

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

def getAudio(note):
    if note == "C":
        return all_freq.get(note)
    elif note == "C#":
        return "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/277.mp3"



    #TODO: Get a random audio file out of somewhere from a song, frequency or piano noise, return that link for use in the template
