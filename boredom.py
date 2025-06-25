import os
from os.path import join, getsize

def read_first_file():
    """
    this function print the first file from the directory path.
    :return:
    """
    while True:
        path = input("Enter the dir path: ")
        try:
            print_or_not = 0
            index_file_on_dir = 0
            while print_or_not != 1:
                new_path = os.path.join(path, os.listdir(path)[index_file_on_dir])
                try:
                    with open(new_path,"r") as file:
                        read_file = file.read()
                        print(read_file)
                        print_or_not = 1
                except PermissionError:
                    index_file_on_dir += 1
                except UnicodeDecodeError:
                    index_file_on_dir += 1
        except FileNotFoundError:
            print("dir not found.")
        except IndexError:
            print("File not found.")

def main():
    read_first_file()
    path = "C:\\Networks\\test"
    new_path = os.path.join(path,os.listdir(path)[0])
    print(new_path)
    with open(new_path, 'r') as file:
        read_file = file.read()
        print(read_file)

if __name__ == "__main__":
    main()

