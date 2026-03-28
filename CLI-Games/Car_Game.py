command = input("> ").lower()

if command == "help":
    print(f"start - to start the car")
    print(f"stop - to stop the car")
    print(f"quit - to exit")

instruct = input().lower()

if instruct == "start":
    print('Car started...Ready to go!')
    
elif instruct == "stop":
    print('Car stopped')

elif instruct == "quit":
    print('Process finished with exit code 0')

else:
    print("I don't understand that...")