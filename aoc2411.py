import math
from collections import defaultdict
input = '965842 9159 3372473 311 0 6 86213 48 '

numbers = []
number = ''
for i, char in enumerate(input):
    if char == ' ':
        numbers.append(int(number))
        number = ''
        continue
    number += char

spam = {i: 1 for i in numbers}

for i in range(75):
    afterblink = defaultdict(int)
    #print(i)
    for number, count in spam.items():
        print(number)
        if number == 0:
            afterblink[1] += count
        else:
            strnum = str(number)
            digits = int(len(strnum))
            if digits % 2 == 0:
                half = digits // 2
                afterblink[int(strnum[:half])] += count
                afterblink[int(strnum[half:])] += count
            else:
                afterblink[number * 2024] += count
    spam = afterblink 
    #print(spam)
    
print(sum(spam.values()))