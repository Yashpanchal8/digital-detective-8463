# Mission 6 — Git and GitHub

## 1. Task / objective
Use Git status, staging, commits and history; create a branch; publish it; and use a Pull Request for review.

## 2. Work completed
### 6.1 Git workflow
| Operation | What it does |
|---|---|
| `git status` | Shows changed, staged and untracked files. |
| `git add README.md` | Selects a change for the next commit. |
| `git commit -m "message"` | Saves staged changes in local history. |
| `git log --oneline` | Displays recent commits. |

Staging selects which changes will be included. A commit records the staged changes as a new point in the repository history.

### 6.2 Branch and learning update
I created the branch `update-about`, added a “My Learning” section to the root README, committed it, and pushed the branch. The section records that I learned how the operating system manages programs, how binary place values work, and how a branch lets me prepare a change separately.

### 6.3 Pull Request
A branch is a separate line of development. A Pull Request asks for a change to be reviewed before merging it. I opened a Pull Request from `update-about` into `main` so the README change could be reviewed. Its live URL and status are recorded below after verification.

### 6.4 Git command glossary
- `git init`: begins tracking a folder with Git.
- `git status`: checks the working tree and staging area.
- `git add`: stages selected changes.
- `git commit`: records the staged snapshot.
- `git log`: shows repository history.
- `git branch`: lists or creates branches.
- `git switch`: changes the current branch.
- `git push`: publishes commits to a remote repository.
- `git pull`: retrieves and integrates remote changes.

## 3. Commands / tools used
`git status`, `git add`, `git commit`, `git log`, `git switch -c update-about`, `git push -u origin update-about`, `git switch main`, and `git pull`.

## 4. My understanding
Git records versions locally, while GitHub hosts the remote repository. A branch keeps a change separate while it is being prepared. A Pull Request gives reviewers a place to discuss and check the change before merging.

## 5. Difficulties faced
Staging and committing are easy to mix up. A staged file is selected but has not yet been saved as a commit.

## 6. How I resolved them
I checked `git status` before and after staging, then used `git log` to confirm that the commit was recorded.

## 7. Evidence / files
The “My Learning” section in the root README, the branch commit, and the Pull Request linked below.

## 8. Commit details
- Mission message: `Complete Git and GitHub collaboration mission`.
- Branch commit: `Add My Learning section to README`.
- Pull Request: [#1 — Add My Learning section to README](https://github.com/Yashpanchal8/digital-detective-8463/pull/1).
- Status: Open and unmerged; GitHub shows no merge conflicts.
