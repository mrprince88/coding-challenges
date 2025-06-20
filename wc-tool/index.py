import sys
import argparse
import locale
from typing import BinaryIO

def count_bytes(file_str):
    try:
        byte_count = len(file_str)
        return byte_count
    except Exception as e:
        print(f"An error occurred while counting bytes: {e}")
        return None

def count_lines(file_str):
    try:
        content_bytes = file_str.splitlines()
        line_count = sum(1 for _ in content_bytes)
        return line_count
    except Exception as e:
        print(f"An error occurred while counting lines: {e}")
        return None

def count_words(file_str):
    try:
        word_count = len(file_str.split())
        return word_count
    except Exception as e:
        print(f"An error occurred while counting words: {e}")
        return None

def count_characters(file_str):
    try:
        preferred_encoding = locale.getpreferredencoding(do_setlocale=False)
        char_count = len(file_str.decode(preferred_encoding,errors="replace"))
        return char_count
    except Exception as e:
        print(f"An error occurred while counting characters: {e}")
        return None
    
def print_counts(file_str, file_name, show_bytes, show_lines, show_words, show_characters):
    if show_bytes:
        byte_count = count_bytes(file_str)
        if byte_count is not None:
            print(f"{byte_count} {file_name}")
    
    elif show_lines:
        line_count = count_lines(file_str)
        if line_count is not None:
            print(f"{line_count} {file_name}")
    
    elif show_words:
        word_count = count_words(file_str)
        if word_count is not None:
            print(f"{word_count} {file_name}")
    
    elif show_characters:
        char_count = count_characters(file_str)
        if char_count is not None:
            print(f"{char_count} {file_name}")
    else:
        line_count = count_lines(file_str)
        word_count = count_words(file_str)
        byte_count = count_bytes(file_str)
        
        if line_count is not None:
            print(f"{line_count}", end=" ")
        if word_count is not None:
            print(f"{word_count}", end=" ")
        if byte_count is not None:
            print(f"{byte_count}", end=" ")
        
        print(f"{file_name}")
    

def main():
    parser=argparse.ArgumentParser(description="WC Tool")

    parser.add_argument(
        "-c",
        action="store_true",
        required=False,
        help="The number of bytes in each input file is written to the standard output.",
    )
    parser.add_argument(
        "-l",
        action="store_true",
        required=False,
        help="The number of lines in each input file is written to the standard output.",
    )
    parser.add_argument(
        "-w",
        action="store_true",
        required=False,
        help="The number of words in each input file is written to the standard output.",
    )
    parser.add_argument(
        "-m",
        action="store_true",
        required=False,
        help="The number of characters in each input file is written to the standard output.",
    )

    parser.add_argument(
        "file",
        help="File name. If no files are specified, the standard input is used and no file name is displayed.",
        nargs="*",
    )

    args = parser.parse_args()

    file_list = args.file
    
    if file_list:
        for file in file_list:
            try:
                with open(file, 'rb') as f:
                    content_bytes = f.read()
                    print_counts(content_bytes, file, args.c, args.l, args.w, args.m)
                    
            except FileNotFoundError:
                print(f"File '{file}' not found.")
            except IsADirectoryError:
                print(f"'{file}' is a directory, not a file.")
    else:
        content_bytes = sys.stdin.buffer.read()
        print_counts(content_bytes, "", args.c, args.l, args.w, args.m)
            
if __name__ == "__main__":
    main()

