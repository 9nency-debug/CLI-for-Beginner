myDict = {
    "Pankha" : "Fan",
    "Dabba" : "BOX",
    "Vastu" : "Item"
}
print("Options are", myDict.keys())
a = input("Enter the Hindi Word\n")
# print("The meaning of your word is: ", myDict.keys())
# Below line will not throw an error of the key is not present in the dictionary
print("The meaning of your word is: ", myDict.get(a))