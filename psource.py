#!/usr/bin/env python3

# Print source code, easy for ChatGPT to digest. Place as executable inside ~/./local/bin/psource, and then it is callable from the command-line.

import os
import sys
from pathlib import Path

def print_files(file_path):
    with open(file_path, "r") as file:
        print(f"\033[1m{file_path}:\033[0m")
        print(file.read())
        print()

def print_help():
    print("Usage: printSource [OPTIONS] [FILES]")
    print("Recursively print the content of files in the current working directory.")
    print("\nOptions:")
    print("  -h, --help    Show this help message and exit.")
    print("\nArguments:")
    print("  FILES         A list of files to print (whitelist). If not provided,")
    print("                the script will print all files except those in the")
    print("                default blacklist (e.g., .env).")

def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print_help()
        sys.exit(0)

    current_directory = Path.cwd()
    default_blacklist = {".env", ".gitignore", ".gitmodules", ".gitattributes"}
    blacklisted_dirs = {".git"}
    whitelist = set(arg for arg in sys.argv[1:] if arg not in ["--help", "-h"])

    for root, _, files in os.walk(current_directory):
        if any(blacklisted_dir in str(Path(root).relative_to(current_directory)) for blacklisted_dir in blacklisted_dirs):
            continue

        for file in files:
            file_path = Path(root) / file
            file_name = file_path.name

            if whitelist:
                if any(whitelisted_file in str(file_path) for whitelisted_file in whitelist):
                    print_files(file_path)
            else:
                if file_name not in default_blacklist:
                    print_files(file_path)

if __name__ == "__main__":
    main()
