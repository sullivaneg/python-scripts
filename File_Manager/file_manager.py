# This is just an independent project I came up with to tie together all the functions I created
# in the lab. NOTE: I'm going to copy and paste the functions instead of referencing the module
# because this script is getting copied to my personal script folder so I can use it!

import os
import re
import shutil


def cat(file_path):
    """Reads content of a file and prints its contents."""
    try:
        if os.path.splitext(file_path)[1] == '.txt':
            path = open(file_path, "r")  # 'r' is read
            content = path.read()
            path.close()
            print(content)
        elif os.path.splitext(file_path)[1] == '.txt':
            with open(file_path, "rb") as bin_file:
                data = bin_file.read()
                bin_file.close()
                print(data)
        else:
            print("File not supported")
    except FileNotFoundError:
        print("File not found")

def word_count(file_name):
    """Counts the number of words in a file."""
    try:
        if os.path.splitext(file_name)[1] == '.txt':
            with open(file_name, "r") as file:
                text = file.read()
                file.close()
                words = re.split(r"\s+", text)
                num_words = len(words)
        elif os.path.splitext(file_name)[1] == '.bin':
            with open(file_name, "rb") as bin_file:
                data = bin_file.read()
                bin_file.close()
                words = re.split(r"\s+", data)
                num_words = len(words)
        else:
            print("File not supported")

        print(f'The number of words in your file {file_name} is: {num_words}')
    except FileNotFoundError:
        print("File not found")


def character_count(file_name):
    """Counts the number of characters in a file."""
    try:
        if os.path.splitext(file_name)[1] == '.txt':
            with open(file_name, "r") as file:
                text = file.read()
                file.close()
                characters = re.findall(r".", text)
        elif os.path.splitext(file_name)[1] == '.bin':
            with open(file_name, "rb") as bin_file:
                data = str(bin_file.read())
                bin_file.close()
                characters = re.findall(r".", data)
        else:
            print("File not supported")

        print(f'The number of characters in your file {file_name} is: {len(characters)}')
    except FileNotFoundError:
        print("File not found")

def count_string(file_name, string):
    """Counts the number of occurrences of a string in a file."""
    try:
        if os.path.splitext(file_name)[1] == '.txt':
            with open(file_name, "r") as file:
                count = 0
                for l_no, line in enumerate(file):
                    if string in line:
                        count += 1
                    else:
                        continue
                print(f'The number of occurrences of {string} in {file_name} is: {count}')
        else:
            print("File not supported")
    except FileNotFoundError:
        print("File not found")

def find_string(file_name, string):
    """Finds all the occurrences of a string in a file."""
    try:
        if os.path.splitext(file_name)[1] == '.txt':
            with open(file_name, "r") as file:
                for l_no, line in enumerate(file):
                    if string in line:
                        print(f'String found in {file_name}, line {l_no}')
                        print(f'Line {l_no}: {line}\n')
                    else:
                        continue
        else:
            print("File not supported")
    except FileNotFoundError:
        print("File not found")

def text_append(text, file_name):
    """Appends text to an existing file."""
    try:
        if os.path.splitext(file_name)[1] == '.txt':
            with open(file_name, "a") as file:
                file.write(text)
        elif os.path.splitext(file_name)[1] == '.bin':
            with open(file_name, "ab") as file:
                file.write(text)
        else:
            print("File not supported")
    except FileNotFoundError:
        print("File not found")

def copy_paste(source, destination):
    """Copies a file from source to destination."""
    try:
        if os.path.splitext(source)[1] == ".txt":
            shutil.copy(source, destination)
        elif os.path.splitext(source)[1] == ".bin":
            with open(source, "rb") as source_file:
                binary_data = source_file.read()
            with open(destination, "wb") as destination_file:
                destination_file.write(binary_data)
        else:
            print("Source File not supported")
    except FileNotFoundError:
        print("Source File not found")

def write(file, content):
    """Writes content to a file."""
    try:
        if os.path.splitext(file)[1] == ".txt":
            with open(file, "w") as file:
                file.write(content)
        elif os.path.splitext(file)[1] == ".bin":
            with open(file, "wb") as bin_file:
                bin_file.write(content)
        else:
            print("File not supported")
    except FileNotFoundError:
        print("File not found")

def check_existence(file_name):
    """Checks if a file exists."""
    if os.path.exists(file_name):
        return True
    else:
        return False

def get_file_size(file_name):
    """Gets file size in bytes."""
    try:
        size = os.path.getsize(file_name)
        return size
    except FileNotFoundError:
        return None

def rename(old_name, new_name):
    """Renames a file from old name to new name."""
    try:
        os.rename(old_name, new_name)
    except FileNotFoundError:
        print("File not found")

def rm(file_name):
    """Deletes a file."""
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("File not found")

def replace(old_word, new_word, file_name):
    """Replaces a word in a file."""
    try:
        if os.path.splitext(file_name)[1] == ".txt":
            with open(file_name, "r") as file:
                text = file.read()
                edited_text = text.replace(old_word, new_word)
            with open(file_name, "w") as file:
                file.write(edited_text)
        elif os.path.splitext(file_name)[1] == ".bin":
            with open(file_name, "rb") as file:
                text = file.read()
                edited_text = text.replace(old_word, new_word)
            with open(file_name, "w") as file:
                file.write(edited_text)
        else:
            print("File not supported")
    except FileNotFoundError:
        print("File not found")

def file_checker(file_path):
    if check_existence(file_path):
        if os.path.splitext(file_path)[1] == ".txt":
            file_type = "txt"
        elif os.path.splitext(file_path)[1] == ".bin":
            file_type = "bin"
        else:
            file_type = "other"
        continue_on = True
    else:
        print("File not found")
        file_type = None
        continue_on = False
    return continue_on, file_type

def display_main_menu():
    """Displays the main menu."""
    print("\n______________________Welcome to Emma's File Manager______________________"
          "\nPlease Choose from the following options:"
          "\n1. Check File Size"
          "\n2. Delete file"
          "\n3. Rename file"
          "\n4. Copy file"
          "\n5. Text/Bin File Viewer and Editor"
          "\n6. Choose a different file"
          "\n7. Exit"
          )

def display_text_menu():
    """Displays the text menu."""
    print("\n______________________Welcome to Emma's File Manager______________________"
          "\nPlease Choose from the following options:"
          "\n1. Read File"
          "\n2. Add to File"
          "\n3. Word Count"
          "\n4. Character Count"
          "\n5. Find and Replace"
          "\n6. Find"
          "\n7. Exit"
          )

def choose():
    option = int(input("Enter your choice: "))
    return option


def interface():
    """Main function."""
    outer_break = False
    while not outer_break:
        create_file = input("Create a new file? (y/n): ")
        if create_file.lower() == "y":
            file_path = input("Enter the file name: ")
            with open(file_path, "w") as file:
                file.write('')

        file_path = input("For the rest of the menu -> Enter the file path: ")
        flag, file_type = file_checker(file_path)

        if flag:
            display = True
            while flag:

                if display:
                    display_main_menu()

                option = choose()

                if option == 1:
                    print(f'Size of file {file_path}: {get_file_size(file_path)}')
                    display = False

                elif option == 2:
                    while True:
                        error_count = 0
                        rm(file_path)
                        file_checker(file_path)
                        if not check_existence(file_path):
                            print("File Deleted")
                            break
                        else:
                            if error_count < 4:
                                print("Error Encountered: Trying again...")
                                error_count += 1
                                continue
                            else:
                                print("Error Count Exceeded: Please try again later...")
                                break
                    display = False

                elif option == 3:
                    while True:
                        new_name = input("Enter the new file name: ")
                        if check_existence(new_name):
                            print("File Already Exists")
                            continue
                        else:
                            while True:
                                rename(file_path, new_name)
                                if check_existence(new_name):
                                    print(f'File {file_path} has been renamed to {new_name}')
                                    file_path = new_name
                                    break
                                else:
                                    continue
                            break
                    display = False

                elif option == 4:
                    while True:
                        destination = input("Enter the destination file name: ")
                        if check_existence(destination):
                            print("File Already Exists")
                            continue
                        else:
                            while True:
                                copy_paste(file_path, destination)
                                if check_existence(destination):
                                    print(f'File {file_path} has been copied to {destination}')
                                    break
                                else:
                                    continue
                            break
                    display = False

                elif option == 5:
                    inner_break = False
                    display = True
                    while not inner_break:

                        if display:
                            display_text_menu()

                        option = choose()

                        if option == 1:
                            cat(file_path)
                            display = True

                        elif option == 2:
                            cat(file_path)
                            text = input("What would you like to add?")
                            text_append(text, file_path)
                            display = True

                        elif option == 3:
                            word_count(file_path)
                            display = False

                        elif option == 4:
                            character_count(file_path)
                            display = False

                        elif option == 5:
                            while True:
                                string = input("Enter the string to replace: ")
                                replacement = input("Enter the replacement string: ")
                                count_string(file_path, string)
                                replace(string, replacement, file_path)
                                print(f'All instances of {string} have been replaced to {replacement}')
                                check = input("Do you want to replace something else? (y/n): ")
                                if check.lower() == "y":
                                    continue
                                else:
                                    break
                            display = True

                        elif option == 6:
                            while True:
                                string = input("Enter the string to find: ")
                                count_string(file_path, string)
                                find_string(file_path, string)
                                check = input("\nDo you want to find something else? (y/n): ")
                                if check.lower() == "y":
                                    continue
                                else:
                                    break
                            display = True

                        elif option == 7:
                            break

                elif option == 6:
                    outer_break = False
                    break

                elif option == 7:
                    outer_break = True
                    break

                else:
                    print("Invalid choice")
                    continue
        else:
            print("File does not exist")
            continue

        if outer_break:
            break

        else:
            continue


interface()

