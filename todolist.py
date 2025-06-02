items = []

def adding_newlist():
    newitems = input("What else would you like to add? ").lower.strip()
    items.append(newitems)
    print("Your updated to-do list is now: ", items)

def removing_list():
    remove = input("Would you like to remove something from your task list? ").lower().strip()
    if remove == "yes":
        removeditems = input("What will you remove? ").strip()
        items.remove(removeditems)
        print("Your updated to-do list is now: ", items)
    else:
        print("Nothing has been removed.")

def amount_items():
    for i in range(len(items)):
        print(i + 1, items[i])

while True:
    functions = input("Type 'see' to see tasks \n Type 'add' to add to tasks \n Type 'remove' to remove from tasks \n Else to finish type 'quit'. ").lower()
    if functions == "see":
        amount_items()
    elif functions == "add":
        adding_newlist()
    elif functions == "remove":
        removing_list()
    elif functions == "quit":
        break
    else:
        print("Looks like your option wasn't on the list.")


