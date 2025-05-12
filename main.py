from stats import(
   report
)

import sys

def get_book_text(file):
    return file.read()

def main():
    if len(sys.argv) < 2:
        print( "Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit the program with error code 1
    with open(sys.argv[1]) as f:
       book =  get_book_text(f)
       report(book)

#=========================#
main()
