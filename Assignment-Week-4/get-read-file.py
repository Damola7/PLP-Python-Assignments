def get_filename_and_read():
    filename = input("Please enter the filename: ")
    
    try:
        # Attempt to open the file for reading
        with open(filename, 'r') as file:
            content = file.read()  # Read the entire file content
            print("File content:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except IOError:
        print(f"Error: The file {filename} could not be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Usage:
get_filename_and_read()
