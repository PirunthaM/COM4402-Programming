command: input("choose a command create, read, update, delete, list: ")

match command.strip().lower():
    case "create":
        print("Creating new file...")
    case "read":
        print("Reading file contents...")
    case "update":
        print("Updating file...")
    case "delete":
        print("Deleting file...")
    case "list":
        print("Files: file1.txt, file2.py")
    case _ if command.startswith("help"):
        print("Available: create, read, update, delete, list")
    case _:
        print("Unknown command. Type 'help'")