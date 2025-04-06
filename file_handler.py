def file_read_write_challenge():
    """Handles file reading, modification, and writing to a new file with error handling"""
    try:
        # Ask user for input filename
        input_filename = input("Enter the name of the file to read: ")
        
        # Read the original file
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Create output filename
        output_filename = f"modified_{input_filename}"
        
        # Write the modified content to a new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"File successfully modified and saved as {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: You don't have permission to read '{input_filename}'.")
    except IsADirectoryError:
        print(f"Error: '{input_filename}' is a directory, not a file.")
    except UnicodeDecodeError:
        print(f"Error: Could not decode the file '{input_filename}'. It might be a binary file.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def main():
    print("File Handling and Exception Handling Program")
    print("-------------------------------------------")
    file_read_write_challenge()

if __name__ == "__main__":
    main()