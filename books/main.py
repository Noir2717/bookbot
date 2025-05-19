def main("~/bookbot/books/frankenstein.txt")
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the contents of the file
        content = file.read()
    
    # Print the content of the file
    print(content)
