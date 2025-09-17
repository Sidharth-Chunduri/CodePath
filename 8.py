def find_villain(crowd, villain):
	#take list of string and find the indices where we find the value
    output = []
    for i in range(len(crowd)):
        if crowd[i] == villain:
            output.append(i)
    
    print(output)

crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
villain = 'The Joker'
find_villain(crowd, villain)