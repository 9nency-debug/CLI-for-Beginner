'''
command = ""
while command.lower() != "quit":
    command = input("> ")

    if command.lower() == "start":
        print("Car started...")

    elif command.lower() == "stop":
        print("Car stopped.")
'''
# This is a bad practice if you're applying lower function multiple times; rather then you can apply it once and store input(taken from the user) in a var.

command = ""
while command != "quit": #OR can use while True:
    command = input("> ").lower()

    if command == "start":
        print("Car started...")

    elif command == "stop":
        print("Car stopped.")

    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
        # OR can use -> elif command == "quit":
        # break
else:
        print("I don't understand that...")

