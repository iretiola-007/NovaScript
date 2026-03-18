import sys


def prompt():
    files = []
    while user_input.startswith("mkdir"):
        files.append(user_input[5:])
        print(f"created {user_input[5:]}")
        break
    if user_input.startswith("rmdir"):
        list.remove[user_input[5:]]
        print(f"removed {user_input[5:]}")
    if user_input == "print files":
        print(files)
    print(files)

while True:
    user_input = input("$: ")
    prompt()


# more improvements to be made