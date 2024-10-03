import sys
import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def display_tool_name():
    # Tool name
    tool_name = "Bug Bounty Tool"
    
    # Get the length of the tool name for centering
    name_length = len(tool_name)
    
    # Create a decorative line
    line_length = 60
    print(Fore.CYAN + "=" * line_length)
    
    # Center the tool name
    print(Fore.CYAN + tool_name.center(line_length))
    
    print(Fore.CYAN + "=" * line_length)
    print(Style.RESET_ALL)  # Reset styles

def main():
    display_tool_name()
    # Simulate some processing time
    time.sleep(1)
    
    # Your tool logic here
    print("Running the tool...")  # Replace with your actual tool logic

if __name__ == "__main__":
    main()
