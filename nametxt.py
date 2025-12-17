with open("names.txt", "w") as file:
    for i in range(3):
        name = input("Enter a name: ")
        file.write(name + "\n")

print("Names saved to names.txt")

print("\n Saved names...")
with open("names.txt") as file:
    for line in file:
        print(line.strip())