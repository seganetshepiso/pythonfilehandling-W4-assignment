def file_processor():
    # Get input filename from user
    input_filename = input("Enter the name of the file to read: ")
    output_filename = input("Enter the name of the output file: ")
    
    try:
        # Try to open and read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            
            # Modify the content (example: convert to uppercase)
            modified_content = content.upper()
            
            # Write to the output file
            try:
                with open(output_filename, 'w') as output_file:
                    output_file.write(modified_content)
                print(f"Success! Modified content written to {output_filename}")
                
            except IOError as e:
                print(f"Error writing to output file: {e}")
                
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{input_filename}'.")
    except IOError as e:
        print(f"Error reading the file: {e}")

# Run the program
if __name__ == "__main__":
    file_processor()