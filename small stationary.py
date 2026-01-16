import os
def manage_items():
    item = input("Enter the name of the new stationery item: ")

    filename = "items.txt"
    if not os.path.exists(filename):

        with open(filename, "w") as f:
            f.write(item + "\n")
    else:
        with open(filename, "a") as f:
            f.write(item + "\n")
    print("\nFull list of items:")
    with open(filename, "r") as f:
        for line in f:
            print(line.strip())
manage_items()