# Mission 4 — How programs run

## 1. Task / objective
Run a simple Python program and compare compiled and interpreted execution.

## 2. Work completed
I created `hello.py` with `print("Hello from Python")` and ran it with Python 3. The terminal displayed `Hello from Python`.

| Point | Compiler | Interpreter |
|---|---|---|
| When translation/execution happens | Translates source code before the program runs. | Executes instructions at runtime. |
| Typical output | May create a native executable or intermediate file. | Often runs a script through a language runtime. |
| Language/tool | C with Clang | Python with CPython |
| Advantage | Can optimize ahead of time. | Supports a quick edit-and-run cycle. |

A compiler translates code before execution, while an interpreter carries out instructions as the program runs. The distinction is not absolute: CPython compiles Python source to bytecode and then runs it in its virtual machine. The `python3` command starts that runtime and runs my script.

## 3. Commands / tools used
`python3 hello.py` ran the program. I used a text editor to create the file.

## 4. My understanding
The `.py` file contains source instructions. Python runs those instructions, and `print` sends the message to the terminal as output.

## 5. Difficulties faced
Running the command from the wrong directory can make Python report that it cannot find `hello.py`.

## 6. How I resolved them
I checked the current folder and ran the command from `mission-04-programs`.

## 7. Evidence / files
`hello.py`; terminal output: `Hello from Python`.

## 8. Commit details
- Commit message: `Compare compilers and interpreters`.
- The mission commit is pushed to GitHub.
