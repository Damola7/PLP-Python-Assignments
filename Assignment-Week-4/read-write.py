import os

def read_and_write_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content (converting to uppercase in this case)
        modified_content = content.upper()

        # Open the output file for writing the modified content
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Content from {input_filename} has been modified and saved to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except IOError:
        print(f"Error: Unable to read or write to file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
input_file = 'input.txt'  # Ensure it's in the correct path
output_file = 'output.txt'
read_and_write_file(input_file, output_file)
