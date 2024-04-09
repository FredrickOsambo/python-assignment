# File Creation
def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line here\n")
        print("File 'my_file.txt' created successfully.")
    except IOError as e:
        print("Error creating file:", e)


# File Reading and Display
def read_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of 'my_file.txt':")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")
    except PermissionError:
        print("Permission denied to read file.")


# File Appending
def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1\n")
            file.write("98765\n")
            file.write("One more line appended\n")
        print("Data appended to 'my_file.txt' successfully.")
    except IOError as e:
        print("Error appending to file:", e)


# Error Handling
def main():
    create_file()
    read_file()
    append_to_file()


if __name__ == "__main__":
    main()
