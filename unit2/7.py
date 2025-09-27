"""Problem 7: Minimum Number of Steps to Match Treasure Maps
Captain Blackbeard has two treasure maps represented by two strings of the same 
ength map1 and map2. In one step, you can choose any character of map2 and replace 
it with another character.

Return the minimum number of steps to make map2 an anagram of map1.

An Anagram of a string is a string that contains the same characters with a different 
(or the same) ordering."""

def min_steps_to_match_maps(map1, map2):
    freq = {}

    for ch in map1:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    total = 0
    for ch in map2:
        if ch in freq:
            freq[ch] -= 1
        else:
            total += 1
        
    return (total + sum([abs(x) for x in freq.values()])) // 2

map1_1 = "bab"
map2_1 = "aba"
map1_2 = "treasure"
map2_2 = "huntgold"
map1_3 = "anagram"
map2_3 = "mangaar"

print(min_steps_to_match_maps(map1_1, map2_1))
print(min_steps_to_match_maps(map1_2, map2_2))
print(min_steps_to_match_maps(map1_3, map2_3))

