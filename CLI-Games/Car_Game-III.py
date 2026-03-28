# Car_Game -> to the next level -> including edge cases:

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")

    elif command == "stop":
        if not started:
            print("Car already Stopped...")
        else:
            started = False
            print("Car stopped...")

    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    else:
        print("Sorry, I don't understand")  
        break