"""Problem 4: Booby Trap
Captain Feathersword has found another pirate's buried treasure, but they suspect 
it's booby-trapped. The treasure chest has a secret code written in pirate language,
 and Captain Feathersword believes the trap can be disarmed if the code can be 
 balanced. A balanced code is one where the frequency of every letter present 
 in the code is equal. To disable the trap, Captain Feathersword must remove 
 exactly one letter from the message. Help Captain Feathersword determine if it's 
 possible to remove one letter to balance the pirate code.

Given a 0-indexed string code consisting of only lowercase English letters, write
 a function can_make_balanced() that returns True if it's possible to remove one 
 letter so that the frequency of all remaining letters is equal, and False otherwise."""

def can_make_balanced(code):
    freq = {}

    for ch in code:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
        
    counts = set([value for value in freq.values()])
    counts = list(counts)

    return (len(counts) == 2 and abs(counts[0] - counts[1]) == 1)

code1 = "arghh"
code2 = "haha"

print(can_make_balanced(code1)) 
print(can_make_balanced(code2)) 
    


        