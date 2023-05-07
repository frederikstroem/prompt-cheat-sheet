# [Prompt cheat sheet for OpenAi's ChatGPT 4](#prompt)
## [psource](https://github.com/frederikstroem/prompt-cheat-sheet/blob/main/psource.py)
Prints the source code of files recursively in the current directory, easy for ChatGPT to digest.

### Usage
**Copy source code recursively of current directory to clipboard:**
```bash
psource | xsel -b
```
*Output can be piped to clipboard using [xsel](https://github.com/kfish/xsel) or similar tools.*

**Copy source code of two files and one directory to clipboard:**
```bash
psource file1 file2 dir1 | xsel -b
```

### Install `psource` command:
```bash
wget -O ~/.local/bin/psource https://raw.githubusercontent.com/frederikstroem/prompt-cheat-sheet/main/psource.py && chmod +x ~/.local/bin/psource
```
**Note:** psource is still very early in the development process, migration to Rust is considered.

## Prompt
### Change code
```plaintext
🤖
INPUT

First input is a description of what code changes to make, this can include refactoring, adding new code, removing code, etc. Separate different points can be added, by adding blank lines between them.
Second input comes when paths are encourted with source code following. Each source code list item first line is `$ /a/path/to/a/file` $.

OUTPUT

First output is very short description of what code changes were made.
Second output is all changes made. Each file is separated by a blank line. Each file starts with `**/path/to/a/file**`, followed by the changes made to the file, then followed by a code block (```) of the new file after changes, but only show changed lines. If multiple changes are made in the same file, they are separated by a blank line and optinally a short description of what changes were made before it's code block.
🧑‍💻


```
