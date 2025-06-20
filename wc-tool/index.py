import sys
import argparse
import locale

def count_bytes(file_path):
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            return len(content)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for _ in file)
            return line_count
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            return word_count
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def count_characters(file_path):
    try:
        preferred_encoding = locale.getpreferredencoding(do_setlocale=False)
        with open(file_path, 'rb') as file:
            content_bytes = file.read()
            content_text = content_bytes.decode(preferred_encoding, errors='replace')
            return len(content_text)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

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
        if args.c:
            for file in file_list:
                byte_count = count_bytes(file)
                if byte_count is not None:
                    print(f"{byte_count} {file}")
        if args.l:
            for file in file_list:
                line_count = count_lines(file)
                if line_count is not None:
                    print(f"{line_count} {file}")
        if args.w:
            for file in file_list:
                word_count = count_words(file)
                if word_count is not None:
                    print(f"{word_count} {file}")
        if args.m:
            for file in file_list:
                char_count = count_characters(file)
                if char_count is not None:
                    print(f"{char_count} {file}")
        else:
            for file in file_list:
                
                line_count = count_lines(file)
                if line_count is not None:
                    print(f"{line_count}",end=" ")
                word_count = count_words(file)

                if word_count is not None:
                    print(f"{word_count}",end=" ")
                byte_count = count_bytes(file)

                if byte_count is not None:
                    print(f"{byte_count}",end=" ")
                    
                print(f"{file}")
    else:
        if args.c:
            byte_count = count_bytes(sys.stdin)
            if byte_count is not None:
                print(f"{byte_count} <stdin>")
        if args.l:
            line_count = count_lines(sys.stdin)
            if line_count is not None:
                print(f"{line_count} <stdin>")

if __name__ == "__main__":
    main()

