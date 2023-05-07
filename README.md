# [Prompt cheat sheet for OpenAi's ChatGPT 4](#prompts)
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

## Prompts
### Change code
```plaintext
🤖
FIRST PROMPT INPUT

First input is a description of what code changes to make, this can include refactoring, adding new code, removing code, etc. Separate different points can be added, by adding blank lines between them.
Second input comes when paths are encourted with source code following. Each source code list item first line is `$ /a/path/to/a/file` $.

FIRST PROMPT OUTPUT

First output is very short description of what code changes were made.
Output is separated by a single blank line.
Second output is all affected files source code, thereby making it easy to copy paste the changes into the source code. Each affected file is output in the following way: `$ /a/path/to/a/file` $, followed by a very short paragraph of what changes were made to the file, followed by the source code (put it ``` code block) of the file after changes are applied, followed by a blank line.

NTH PROMPT INPUT

First input is comments on the changes made.

NTH PROMPT OUTPUT

Be helpful and try to use feedback from the user to improve the code changes or what is otherwise asked of you.
🧑‍💻


```
