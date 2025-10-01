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

words = list(text.split())

reveal = []

for items in words:
    sss = synonyms.get(items)
    reveal.append(sss)


reveallen = len(reveal)

for i in range(reveallen):
    if reveal[i] == None:
        reveal[i] = words[i]


result = ' '.join(reveal)

print(f"{result}", end="\n")

