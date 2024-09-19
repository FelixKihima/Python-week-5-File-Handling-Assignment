def create_file(filename):
    """Create a file and write initial content."""
    try:
        with open(filename, 'w') as file:
            file.write("Hello, this is my file.\n")
            file.write("Here is a number: 42\n")
            file.write("Let's store some text and numbers together.\n")
        print(f"File '{filename}' created and initial content written.")
    except (PermissionError, IOError) as e:
        print(f"Error occurred while creating/writing to the file: {e}")

def read_file(filename):
    """Read the content of the file and display it."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("Reading contents of the file:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except (PermissionError, IOError) as e:
        print(f"Error occurred while reading the file: {e}")

def append_to_file(filename):
    """Append additional content to the file."""
    try:
        with open(filename, 'a') as file:
            file.write("This is an additional line 1.\n")
            file.write("This is an additional line 2: 100.\n")
            file.write("This is an additional line 3.\n")
        print(f"Added new content to '{filename}'.")
    except (PermissionError, IOError) as e:
        print(f"Error occurred while appending to the file: {e}")

def main():
    filename = "my_file.txt"
    
    # Create the file and write initial content
    create_file(filename)
    
    # Read the file contents
    read_file(filename)
    
    # Append additional content to the file
    append_to_file(filename)
    
    # Read the file contents again to display the updated content
    read_file(filename)

if __name__ == "__main__":
    main()

