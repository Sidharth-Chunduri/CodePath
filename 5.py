def concatenate(words):
    #for loop through the list of strings and add them together
    output = ""
    for word in words:
        output += word
    
    print(output)

words = ["vengeance", "darkness", "batman"]
concatenate(words)

words = []
concatenate(words)