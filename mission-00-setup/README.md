# Mission 0 — Create your GitHub workspace

## 1. Task / objective
Create a correctly named repository, prepare the mission folders, check Python and Git, and document the setup.

## 2. Work completed
I created the project as `digital-detective-8463`. It contains the root README, folders `mission-00-setup` through `mission-08-final-report`, a README in each mission folder, an `evidence` folder, and the Python files needed in Missions 4 and 5. The repository is public at https://github.com/Yashpanchal8/digital-detective-8463.

## 3. Commands / tools used
- `python3 --version` — checked the installed Python version; output: Python 3.14.7.
- `git --version` — checked Git; output: git version 2.56.0.
- `git init -b main` — initialized the local repository on `main`.
- `git add` and `git commit` — staged setup files and recorded the setup commit.
- `git remote add origin` and `git push -u origin main` — connected the GitHub repository and published `main`.

## 4. My understanding
A repository is a project folder tracked by Git, which lets me save and review changes over time. Separate folders make each mission easier to find and review. Matching the local folder and GitHub repository names helps avoid confusion.

## 5. Difficulties faced
The first push attempt could not resolve GitHub from the restricted shell environment.

## 6. How I resolved them
I retried the push with the authenticated GitHub connection. GitHub then showed the repository files and commit history.

## 7. Evidence / files
Root `README.md`; this README; `mission-00-setup` through `mission-08-final-report`; and `evidence/README.md` plus `evidence/selected-output.md`.

## 8. Commit details
- Setup commit: `Set up Digital Detective mission structure`.
- Follow-up commit: `Record Mission 0 GitHub publication`.
- Both commits were pushed to the public `main` branch.
