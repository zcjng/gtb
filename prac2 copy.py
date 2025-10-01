synonyms = {
    "big": "large",
    "small": "tiny",
    "fast": "quick",
    "slow": "sluggish",
    "happy": "joyful",
    "sad": "unhappy",
    "angry": "furious",
    "good": "great",
    "bad": "awful",
    "hot": "warm",
    "cold": "chilly",
    "smart": "clever",
    "stupid": "dumb",
    "easy": "simple",
    "hard": "difficult",
    "friend": "buddy",
    "enemy": "foe",
    "child": "kid",
    "dog": "puppy",
    "cat": "kitten"
}

texts = input()
text = texts.split()

new = []

for i in text:
    sss = synonyms.get(i)
    new.append(sss)

newlen = len(new)

for i in range(newlen):
    if new[i] == None:
        new[i] = text[i]
    
print(' '.join(new))
