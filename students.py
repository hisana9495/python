import os
def manage_students():
    filename = "students.txt"
    n = int(input("How many student names do you want to add? "))
    if os.path.exists(filename):
        print("\nExisting student names:")
        with open(filename, "r") as f:
            for line in f:
                print(line.strip())
    else:
        print("\nNo existing student names found. A new file will be created.")
    with open(filename, "a") as f:
        for i in range(n):
            name = input(f"Enter name {i+1}: ")
            f.write(name + "\n")
    print("\nUpdated list of all student names:")
    with open(filename, "r") as f:
        for line in f:
            print(line.strip())
manage_students()