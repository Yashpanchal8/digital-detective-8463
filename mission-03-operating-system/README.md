# Mission 3 — Understand the operating system

## 1. Task / objective
Inspect operating-system information, processes, storage, paths and permissions, then describe operating-system responsibilities.

## 2. Work completed
### 3.1 System information
| Information | What it tells me | Observation |
|---|---|---|
| OS (`sw_vers`) | Operating-system name and version | macOS 27.2.1 |
| Current account (`whoami`) | Account running the shell | Redacted in this report |
| Storage (`df -h /`) | Space used and available on the main volume | About 13 GiB used and 694 GiB available at the time checked |
| System activity | Running programs and resource use | `ps` was blocked by the restricted shell; Activity Monitor can show processes and PIDs on macOS |

### 3.2 Processes
A process is a running program. The PID is the number the operating system assigns to distinguish one process from another. A Terminal shell and a web browser are two processes that may be running. The process-list command was not available in this restricted shell, so I did not copy any PIDs.

### 3.3 Paths and permissions
An absolute path starts at the filesystem root, such as `/Users/student/digital-detective-8463/mission-03-operating-system/notes.txt`. A relative path is interpreted from the current folder, such as `mission-03-operating-system/notes.txt` when I am in the repository root.

The permission string for a text file in the Terminal activity folder was `-rw-r--r--`. The owner's letters are `rw-`: the owner can read and write the file but cannot execute it. `r` means read, `w` means write, and `x` means execute a file or traverse a directory.

### 3.4 Operating-system responsibilities
| Responsibility | Explanation | Typical situation |
|---|---|---|
| Process management | Starts, schedules and stops programs. | Shares processor time between an editor and browser. |
| Memory management | Allocates RAM and protects programs' memory. | Reserves memory for an open document. |
| Device management | Coordinates hardware through drivers and services. | Sends a print job to a printer. |
| File management | Organizes files on storage. | Opens a document by its path. |
| User interface / shell | Provides graphical or command-based control. | Finder or Terminal. |
| Security and permissions | Controls access to files and resources. | Allows the owner to edit a file. |

## 3. Commands / tools used
`sw_vers`, `whoami`, `df -h /`, `ps`, `pwd`, and `ls -l`. Activity Monitor is the graphical process viewer on macOS.

## 4. My understanding
The operating system coordinates software and hardware. It tracks running processes, manages memory and storage, and uses permissions to control access. A path locates a file, while permission letters show what users can do with it.

## 5. Difficulties faced
The restricted shell did not allow the process-list command to read the process table.

## 6. How I resolved them
I did not keep retrying the blocked command. I recorded the limitation and identified Activity Monitor as the appropriate way to inspect process names and PIDs on a Mac.

## 7. Evidence / files
This README contains the system information, privacy-safe storage observation, path and permission notes, and OS responsibility table.

## 8. Commit details
- Commit message: `Document operating system and file management`.
- The mission commit is pushed to GitHub.
