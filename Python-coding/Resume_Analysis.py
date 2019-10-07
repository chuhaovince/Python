import os
import csv
import string

filepath = os.path.join("..","..","UT-TOR-DATA-PT-09-2019-U-C","Unit 3 - Python","Extra Content","01_Stu_Resume_Analysis","Unsolved","resume.md")
with open(filepath, 'r') as resume:
    words = resume.read().lower().split() #this is a list still with punctuations

#remove punctuations in string/trailing
def remove_trailing(yourlist):
    words_trailing = []
    for i in yourlist:
        words_trailing.append(i.split(",")[0].split(".")[0])
    return words_trailing

words_P = set(remove_trailing(words))

p = set(string.punctuation)

words_noP = words_P.difference(p)
words_noP_all = remove_trailing(words)
# Skills to match
required_skills = {"excel", "python", "mysql", "statistics"}
desired_skills = {"r", "git", "html", "css", "leaflet"}

match_required = required_skills.intersection(words_noP)

match_desirred = desired_skills.intersection(words_noP)

print(match_desirred)
print(match_required)

## couter the skill occurances
## can either use dict to count or to use counter() in collection library
from collections import Counter
word_count1 = Counter(words_noP_all)

'''
word_count2 = {}.fromkeys(words_noP,0)

or....
word_count2 = {key: 0 for key in words_noP}
'''
'''
for i in words_noP:
    word_count2[i] += 1
print(word_count2)
print(word_count2==word_count1)
'''

## find the first 10 skills
stop_words = {"and", "or", "with", "using", "working","in", "to","##"}
words_nostop_nop = list(words_noP.difference(stop_words))

for word in sorted(words_nostop_nop, key = word_count1.get, reverse = True)[:10]:
    print(f"Token: {word:20} Count: {word_count1[word]}")