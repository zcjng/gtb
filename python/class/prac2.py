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

text = input()
texts = text.split()

total = []

for i in texts:
    sss = synonyms.get(i)
    total.append(sss)

totallen = len(total)

for i in range(totallen):
    if total[i] == None:
        total[i] = texts[i]

print(' '.join(total))

