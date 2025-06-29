import argparse
from app.lexer import Lexer
from app.parser import Parser

def main():
    parser = argparse.ArgumentParser(description="JSON Parser Tool")
    parser.add_argument("file", type=str, help="The JSON file to parse.")
    args = parser.parse_args()

    try:
        with open(args.file, 'r') as file:
            data = file.read()
            parsed_data = Parser(Lexer(data)).parse()
            
            print("Parsed JSON Data:", parsed_data)

    except FileNotFoundError:
        print(f"File '{args.file}' not found.")
    except Exception as e:
        print(f"An error occurred while parsing: {e}")

if __name__ == "__main__":
    main()
