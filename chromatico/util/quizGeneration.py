#A set of useful tools for quiz generation
import random

#TODO: Make a list that contains either the frequencies of a note or the letter of the note. The frequencies looks cooler and make it harder to hack, harder to cheat.
#References 440hz version of the chromatic scale, the most used scale in music. A drawback is that it only uses the 0th octave, the lowest frequency on the scale we can hear.
#However, it is only used for reference. The pitches of the notes vary on the 10 octaves, so they all have the potential to be used.
#TODO: Make a function that chooses which type of quiz will be generated: audio snippet or play-it-on-the-virtual-piano.
#TODO: Then make a final function that will randomly select the two functions and return them for later use.

all_freq = {"C" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/261.mp3",
            "C#" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/277.mp3",
            "D" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/293.mp3",
            "D#" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/311.mp3",
            "E" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/329.mp3",
            "F" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/349.mp3",
            "F#" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/369.mp3",
            "G" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/392.mp3",
            "G#" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/415.mp3",
            "A" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/440.mp3",
            "A#" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/466.mp3",
            "B" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/493.mp3"}

major_freq = {"C" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/261.mp3",
              "D" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/293.mp3",
              "E" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/329.mp3",
              "F" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/349.mp3",
              "G" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/392.mp3",
              "A" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/440.mp3",
              "B" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/493.mp3"}


minor_freq = {"C#" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/277.mp3",
              "D#" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/311.mp3",
              "F#" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/369.mp3",
              "G#" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/415.mp3",
              "A#" : "https://raw.githubusercontent.com/Bonnabelle/chromatico/master/chromatico/sounds/466.mp3"}

#All the values of the frequencies
all_f_ls = ls = list(all_freq.keys())
major_f_ls = ls = list(major_freq.keys())
minor_f_ls = list(minor_freq.keys())

def getNote(ix):
    #Gets random tone from corresponding list
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
            options.append(getNote(all_f_ls))
    elif level == 2:
        for i in range(0,6):
            options.append(getNote(all_f_ls))
    elif level == 3:
        for i in range(0,9):
            options.append(getNote(all_f_ls))
    elif level == 4:
        for i in range(0,11):
            options.append(getNote(all_freq))

    return options

#Chooses a note to be the answer out of the options list
def getAnswer(options):
    return options[random.randrange(0,len(options))]

def getAudio(note):
    if all_freq.has_key(note):
        return all_freq.get(note)
    else:
        return ""
