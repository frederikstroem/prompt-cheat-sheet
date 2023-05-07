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
### Code changes
```plaintext
TODO
```
