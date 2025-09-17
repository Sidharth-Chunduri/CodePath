def nanana_batman(x):
    output = ""
    for i in range(x):
        output += "na"

    if x > 0:
        output += " "

    output += "batman!"

    print(output)

x = 6
nanana_batman(x)

x = 0
nanana_batman(x)