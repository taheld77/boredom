import os

def read_first_file(path):
    """
    this function print the first file from the directory path.
    """
    print_or_not = 0
    index_file_on_dir = 0
    try:
        while print_or_not != 1:
            new_path = os.path.join(path, os.listdir(path)[index_file_on_dir])
            try:
                with open(new_path,"r") as file:
                    read_file = file.read()
                    print_or_not = 1
                    return read_file
            except PermissionError:
                index_file_on_dir += 1
            except UnicodeDecodeError:
                index_file_on_dir += 1
    except FileNotFoundError:
        return "dir not found."
    except IndexError:
        return "File not found."

def main():
    while True:
        path = input("Enter the dir path: ")
        print(read_first_file(path))

if __name__ == "__main__":
    main()

