import os

def read_and_modify_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        modified_content = "modified_" + filename
        statement = input("What information would you like to add? ")

        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(content + "\n" + statement)
        
        print(f'File {filename} has been modified and saved as {new_filename}')

    except FileNotFoundError:
        print(f'Sorry, "{filename}" cannot be found')
    except IOError:
        print(f'Error accessing "{filename}"')

filename = input("Enter the name of the file: ")
read_and_modify_file(filename)
