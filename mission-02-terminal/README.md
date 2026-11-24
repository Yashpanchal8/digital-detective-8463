# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
Use Terminal to inspect folders, create and manage files safely, understand flags and pipes, and explain package managers.

## 2. Work completed
I used `mission-02-terminal/terminal-practice`.

### 2.1 Command reference
| Operation | Command | What it does | Observation |
|---|---|---|---|
| Show current folder | `pwd` | Prints the current path. | It showed the `terminal-practice` folder. |
| List entries | `ls` | Lists visible files and folders. | It showed the notes files. |
| Detailed list | `ls -l` | Shows permissions, owner, size and date. | It showed file permissions and sizes. |
| Move to parent | `cd ..` | Moves up one folder. | The displayed path changed to `mission-02-terminal`. |
| Create directory | `mkdir terminal-practice` | Creates a folder. | The folder appeared in the listing. |
| Create empty file | `touch empty.txt` | Creates an empty file. | Its size was 0 bytes. |
| Copy file | `cp notes.txt backup-copy.txt` | Makes a separate copy. | Both files remained. |
| Rename file | `mv backup-copy.txt renamed-backup.txt` | Renames or moves a file. | The new name appeared. |
| Display file | `cat notes.txt` | Prints file contents. | It displayed both saved lines. |

### 2.2 File changes
The file contains `First line` and `Second line`. Using `>` writes/replaces the file; using `>>` appends to the end. Copying leaves the original in place, while moving relocates or renames the file. `pwd` tells me where a relative command will act, and `ls` helps me inspect that location first.

### 2.3 Flags and pipes
`ls -lah` gives a detailed listing, includes hidden entries, and prints readable sizes. `ls -lah | head -n 5` sends the listing through a pipe to `head`, which displays only the first five lines. The left command produces text, the pipe passes it onward, and the right command selects the part to display.

### 2.4 Package managers
Homebrew was available. `brew --version` returned Homebrew 7.0.9. `brew list` displays installed packages; it was not necessary to install or remove anything. A package manager organizes software installation and updates and can handle dependencies. It also makes software setup repeatable.

## 3. Commands / tools used
`pwd`, `ls`, `ls -l`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`, `printf`, `ls -lah`, `head -n 5`, `brew --version`, and `brew list`.

## 4. My understanding
The current directory determines how relative paths are interpreted. Listing before a file change helps me check that I am working in the right place. Flags change command behavior, and a pipe passes one command's output as another command's input.

## 5. Difficulties faced
Using `>` when I meant to add text would replace the existing contents.

## 6. How I resolved them
I used `>>` for the second line and checked the result with `cat`. I kept all file creation and renaming in the mission folder.

## 7. Evidence / files
`terminal-practice/notes.txt`, `terminal-practice/notes-backup.txt`, `terminal-practice/renamed-backup.txt`, and `terminal-practice/empty.txt`.

## 8. Commit details
- Commit message: `Complete Terminal and file management mission`.
- The mission commit is pushed to GitHub.
