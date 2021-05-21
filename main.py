def getdate():
    import datetime
    return datetime.datetime.now()

def logger(filename):
    print("Enter diet")
    details = input()
    k = str(getdate())
    filename.write(k)
    filename.write(" ")
    filename.write(details)
    filename.write("\n")

def reader(filename):
    print(filename.read)

print("press 1 if you are client1")
print("press 2 if you are client2")
print("press 3 if you are client3")
key=int(input())
if key==1:
    print("press d to enter diet log and e to enter excercise log")
    print("press dl to see diet log and el to see excercise log")
    log=input()
    if log=="d":
        with open("client1_diet", "a") as data:
            logger(data)

    elif log=="e":
        with open("client1_excercise", "a") as data:
            logger(data)

    elif log=="dl":
        with open("client1_diet", "a") as data:
            logger(data)

    elif log=="el":
        with open("client1_excercise", "a") as data:
            logger(data)

    else:
        print("invalid command")

if key == 2:
    print("press d to enter diet log and e to enter excercise log")
    print("press dl to see diet log and el to see excercise log")
    log = input()
    if log == "d":
        with open("client2_diet", "a") as data:
            logger(data)

    elif log == "e":
        with open("client2_excercise", "a") as data:
            logger(data)

    elif log == "dl":
        with open("client2_diet", "a") as data:
            logger(data)

    elif log == "el":
        with open("client2_excercise", "a") as data:
            logger(data)

    else:
        print("invalid command")

if key == 3:
    print("press d to enter diet log and e to enter excercise log")
    print("press dl to see diet log and el to see excercise log")
    log = input()
    if log == "d":
        with open("client3_diet", "a") as data:
            logger(data)
    elif log == "e":
        with open("client3_excercise", "a") as data:
            logger(data)

    elif log == "dl":
        with open("client3_diet", "a") as data:
            logger(data)

    elif log == "el":
        with open("client3_excercise", "a") as data:
            logger(data)

    else:
        print("invalid command")