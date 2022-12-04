import string
import collections

# codex of the alphabet (lower and upper case). the index is the position of each letter in the alphabet
codex = list(string.ascii_lowercase) + list(string.ascii_uppercase)

# Part 1
def getPriorities(rucksacks):
    priorities = 0
    for rucksack in rucksacks:
        middle = int(len(rucksack)/2)
        
        # Slice the rucksacks in two
        subString1 = rucksack[slice(middle)]
        subString2 = rucksack[slice(middle, len(rucksack))]
        
        # Create a dictionary for each half, with the number of occurrence of each character
        dic1 = collections.defaultdict(int)
        for c in subString1:
            dic1[c] += 1
            
        dic2 = collections.defaultdict(int)
        for c in subString2:
            dic2[c] += 1
        
        # Merge the two dictionaries in one, recovering the number of occurrence from each dictionaries and append them in a list
        merged_dic = collections.defaultdict(list)
        dics = [dic1, dic2]
        for dic in dics:
            for key, val in dic.items():
                merged_dic[key].append(val)
        
        # Find the character with a list of shared occurrences greater than 1 (i.e the character was in both halves)
        for e in merged_dic:
            if (len(merged_dic[e]) > 1):
                # Retrieve the position of the character in the codex
                priorities += codex.index(e) + 1
                break 
    return priorities

# Part 2
def getBadges(rucksacks):
    badges = 0
    
    for i in range(0, len(rucksacks), 3):
        # Create a dictionary for 3 consecutive rucksacks, with the number of occurrence of each character
        dicA = collections.defaultdict(int)
        for c in rucksacks[i]:
            dicA[c] += 1
            
        dicB = collections.defaultdict(int)
        for c in rucksacks[i+1]:
            dicB[c] += 1
            
        dicC = collections.defaultdict(int)
        for c in rucksacks[i+2]:
            dicC[c] += 1
    
        # Merge the dictionaries in one, recovering the number of occurrence from each dictionaries and append them in a list
        merged_dic = collections.defaultdict(list)     
        dics = [dicA, dicB, dicC]
        for dic in dics:
            for key, val in dic.items():
                merged_dic[key].append(val)
    
        # Find the character with a list of shared occurrences greater than 2 (i.e the character was in the 3 consecutive rucksacks)
        for e in merged_dic:
            if (len(merged_dic[e]) > 2):
                # Retrieve the position of the character in the codex
                badges += codex.index(e) + 1
                break 
    return badges

with open("2022/03/input.txt", "r") as f:
    lines = []
    for line in f:
        lines.append(line)
                
        
print("Priorities of items:", getPriorities(lines))
print("Priorities of badges:", getBadges(lines))