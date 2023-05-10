#!/usr/bin/env python3

# Print source code, easy for ChatGPT to digest. Place as executable inside ~/./local/bin/psource, and then it is callable from the command-line.

import os
import sys
from pathlib import Path


def remove_base_path(file_path):
    base_paths = [Path('/home/katofln/projects/'), Path('/home/katofln/')]
    for base_path in base_paths:
        try:
            return '/' + str(file_path.relative_to(base_path))
        except ValueError:
            pass
    return str(file_path)

def print_files(file_path, relative_path):
    with open(file_path, "r") as file:
        # print(f"\033[1m{relative_path}:\033[0m")
        print(f"$ {relative_path}:")
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
    default_blacklist = {".env", ".gitignore", ".gitmodules", ".gitattributes", "Cargo.lock"}
    blacklisted_dirs = {".git", "target", ".pio"}
    whitelist = set(arg for arg in sys.argv[1:] if arg not in ["--help", "-h"])

    for root, _, files in os.walk(current_directory):
        if any(blacklisted_dir in str(Path(root).relative_to(current_directory)) for blacklisted_dir in blacklisted_dirs):
            continue

        for file in files:
            file_path = Path(root) / file
            file_path_str = remove_base_path(file_path)
            file_name = file_path.name

            if whitelist:
                if any(whitelisted_file in file_path_str for whitelisted_file in whitelist):
                    print_files(file_path, file_path_str)
            else:
                if file_name not in default_blacklist:
                    print_files(file_path, file_path_str)

if __name__ == "__main__":
    main()
