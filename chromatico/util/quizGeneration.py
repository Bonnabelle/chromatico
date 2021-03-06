#A set of useful tools for quiz generation
import random

#References 440hz version of the chromatic scale, the most used scale in music. A drawback is that it only uses the 0th octave, the lowest frequency on the scale we can hear.
#However, it is only used for reference. The pitches of the notes vary on the 10 octaves, so they all have the potential to be used.

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
all_f_ls = list(all_freq.keys())
major_f_ls = list(major_freq.keys())
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

#TODO: Fix the bug that puts the same note in a list multiple times
def getTextOption(level):
    options = set()

    if level == 1:
        while len(options) < 4:
            options.add(getNote(all_f_ls))
    elif level == 2:
        while len(options) < 6:
            options.add(getNote(all_f_ls))
    elif level == 3:
        while len(options) < 9:
            options.add(getNote(all_f_ls))
    elif level == 4:
        while len(options) < 11:
            options.add(getNote(all_f_ls))

    return list(options)

def getAudioOption(level):
    options = set()

    if level == 1:
        while len(options) < 4:
            options.add(all_freq.get(getNote(all_f_ls)))
    elif level == 2:
        while len(options) < 6:
            options.add(all_freq.get(getNote(all_f_ls)))
    elif level == 3:
        while len(options) < 9:
            options.add(all_freq.get(getNote(all_f_ls)))
    elif level == 4:
        while len(options) < 11:
            options.add(all_freq.get(getNote(all_freq)))

    return list(options)


def getPianoOption(level):
    return getTextOption(level) # In the end, they need the same thing. In random, the getRandomOption determines type.

def getRandomOption(level,boo):
    if boo == 1:
        return getAudioOption(level)
    elif boo == 2:
        return getPianoOption(level)
    return getTextOption(level)

#Chooses a note to be the answer out of the options list
def getAnswer(options,typ):
    if typ != "Audio" or typ == 0:
        return options[random.randrange(0,len(options))]

    answer = options[random.randrange(0,len(options))]
    for note in all_freq.keys():
        if all_freq.get(note) == answer:
            return note

def getAudio(note):
    if all_freq.has_key(note):
        return all_freq.get(note)
    return ""
