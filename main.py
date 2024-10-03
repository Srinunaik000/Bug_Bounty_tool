import argparse
from modules.scanner import Scanner
import pyfiglet

def parse_arguments():
    parser = argparse.ArgumentParser(description="XSS Fuzzing Tool")

    # Add argument for file input
    parser.add_argument(
        '--file', '-f',
        type=str,
        help="Path to the file containing URLs"
    )

    # Add argument for a single URL input
    parser.add_argument(
        '--url', '-u',
        type=str,
        help="Single URL to test for XSS"
    )

    # Add argument for custom payloads
    parser.add_argument(
        '--payloads', '-p',
        type=str,
        help="Path to a file containing custom XSS payloads"
    )

    # Add argument for checking headers
    parser.add_argument(
        '--check-headers', 
        action='store_true',
        help="Check headers for reflected XSS"
    )

    # Add option to show only positive results
    parser.add_argument(
        '--show-positive',
        action='store_true',
        help="Only show results where payloads are reflected"
    )

    # Parse the arguments
    return parser.parse_args()

def display_tool_info():
    # Generate ASCII art for the tool name
    tool_name = pyfiglet.figlet_format("RXSS Fuzzing Tool", font="slant")
    author_info = "\nAuthor: SrinuNaik (D3V1L)\n"  # Add your name here
    print(tool_name + author_info)

def main():
    display_tool_info()  # Display the tool name and author
    args = parse_arguments()
    scanner = Scanner(args)
    scanner.run()

if __name__ == "__main__":
    main()
