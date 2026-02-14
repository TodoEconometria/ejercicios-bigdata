# Useful Git Commands﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌​​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​​‌‌​​​‌‍​‌‌​​​‌​‍​‌‌​​​‌​‍​‌‌​​​‌​﻿

Git command cheatsheet for daily use in the course.﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌​​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​​‌‌​​​‌‍​‌‌​​​‌​‍​‌‌​​​‌​‍​‌‌​​​‌​﻿

---

## Basic Commands

### Initial Configuration

```bash
# Configure name
git config --global user.name "Tu Nombre"

# Configure email
git config --global user.email "tu@email.com"

# View configuration
git config --list

# View specific configuration
git config user.name
```

### Clone and Update

```bash
# Clone your fork
git clone https://github.com/TU_USUARIO/ejercicios-bigdata.git

# Enter the folder
cd ejercicios-bigdata

# Add upstream (professor's repo)
git remote add upstream https://github.com/TodoEconometria/ejercicios-bigdata.git

# View configured remotes
git remote -v
```

---

## Daily Work

### Status and Changes

```bash
# View current status
git status

# View unsaved changes
git diff

# View changes in a specific file
git diff archivo.py

# View commit history
git log

# View abbreviated history
git log --oneline

# View changes of a specific commit
git show abc123d
```

### Save Changes

```bash
# Add specific file
git add archivo.py

# Add all modified files
git add .

# Add only Python files
git add *.py

# Make a commit
git commit -m "Descriptive message"

# Commit already tracked files (skip add)
git commit -am "Descriptive message"

# Amend last commit (before push)
git commit --amend -m "New message"
```

---

## Branches

### Create and Switch

```bash
# View local branches
git branch

# View all branches (including remote)
git branch -a

# Create new branch
git branch garcia-ejercicio-01

# Switch to a branch
git checkout garcia-ejercicio-01

# Create and switch in one command
git checkout -b garcia-ejercicio-01

# Switch to main
git checkout main
```

### Merge and Delete

```bash
# Merge a branch into the current one
git merge branch-name

# Delete local branch
git branch -d garcia-ejercicio-01

# Force delete (if it has unmerged changes)
git branch -D garcia-ejercicio-01

# Delete remote branch
git push origin --delete garcia-ejercicio-01
```

---

## Synchronization

### Download Changes

```bash
# Download changes from professor (upstream)
git fetch upstream

# Download and merge from your fork (origin)
git pull origin main

# View differences with upstream
git log HEAD..upstream/main

# View commits you don't have
git log HEAD..upstream/main --oneline
```

### Full Fork Sync

```bash
# Complete workflow to sync
git checkout main
git fetch upstream
git merge upstream/main
git push origin main

# Or in a single line
git checkout main && git fetch upstream && git merge upstream/main && git push origin main
```

### Upload Changes

```bash
# Push current branch to origin
git push origin branch-name

# Push main
git push origin main

# Push and set upstream (first time)
git push -u origin branch-name

# After that you only need
git push
```

---

## Troubleshooting

### Undo Changes

```bash
# Discard changes in a file (before add)
git checkout -- archivo.py

# Discard all unsaved changes
git checkout -- .

# Remove file from staging (after add, before commit)
git reset HEAD archivo.py

# Undo last commit (keeps changes)
git reset --soft HEAD~1

# Undo last commit (discards changes)
git reset --hard HEAD~1

# Go back to a specific commit
git reset --hard abc123d
```

!!! danger "Be careful with --hard"
    `git reset --hard` permanently deletes changes. Only use it if you are sure.

### Stash (Temporarily Save)

```bash
# Temporarily save changes
git stash

# Save with a message
git stash save "WIP: working on exercise 03"

# View stash list
git stash list

# Apply last stash
git stash apply

# Apply and remove last stash
git stash pop

# Apply specific stash
git stash apply stash@{1}

# Remove stash
git stash drop stash@{0}

# Remove all stashes
git stash clear
```

### Conflicts

```bash
# View files with conflicts
git status

# After resolving manually
git add resolved-file.py
git commit -m "Resolve conflict in file"

# Abort merge with conflicts
git merge --abort

# View merge tool
git mergetool
```

---

## Information and Search

### Inspect History

```bash
# View detailed history
git log --graph --decorate --all

# View who modified each line of a file
git blame archivo.py

# Search in history
git log --grep="keyword"

# View files modified in each commit
git log --stat

# View changes from a specific author
git log --author="Your Name"
```

### Search Code

```bash
# Search in tracked files
git grep "keyword"

# Search in Python files
git grep "keyword" -- "*.py"

# Search showing line number
git grep -n "keyword"
```

---

## Shortcuts and Aliases

### Configure Aliases

```bash
# Create alias for status
git config --global alias.st status

# Create alias for checkout
git config --global alias.co checkout

# Create alias for commit
git config --global alias.ci commit

# Create alias for branch
git config --global alias.br branch

# Alias for pretty log
git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```

### Use Aliases

```bash
# Instead of: git status
git st

# Instead of: git checkout main
git co main

# Instead of: git commit -m "message"
git ci -m "message"

# View pretty log
git lg
```

---

## Course Workflow

### Start a New Exercise

```bash
# 1. Update main
git checkout main
git pull origin main
git fetch upstream
git merge upstream/main

# 2. Create branch for exercise
git checkout -b garcia-ejercicio-01

# 3. Work...
# ... edit files ...

# 4. Save work
git add .
git commit -m "Implement SQLite data loading"

# 5. Push to GitHub
git push -u origin garcia-ejercicio-01
```

### Update Exercise Branch

```bash
# If the professor added changes while you were working
git checkout main
git fetch upstream
git merge upstream/main
git checkout garcia-ejercicio-01
git merge main
git push origin garcia-ejercicio-01
```

### Apply Professor's Feedback

```bash
# 1. Make sure you are on your branch
git checkout garcia-ejercicio-01

# 2. Make corrections
# ... edit files ...

# 3. Save and push
git add .
git commit -m "Apply feedback: optimize queries"
git push origin garcia-ejercicio-01

# The PR updates automatically
```

---

## Advanced Commands

### Cherry Pick

```bash
# Apply a specific commit to the current branch
git cherry-pick abc123d

# Apply without automatic commit
git cherry-pick -n abc123d
```

### Rebase

```bash
# Rebase current branch with main
git rebase main

# Interactive rebase (last 3 commits)
git rebase -i HEAD~3

# Continue rebase after resolving conflicts
git rebase --continue

# Abort rebase
git rebase --abort
```

!!! warning "Be careful with Rebase"
    Do not rebase commits that you have already pushed to GitHub (after push).

### Reflog

```bash
# View history of all actions
git reflog

# Recover a "lost" commit
git reflog
git checkout abc123d
git checkout -b recovered-branch
```

---

## Tricks and Tips

### Useful Configuration

```bash
# Colorize output
git config --global color.ui auto

# Default editor (VSCode)
git config --global core.editor "code --wait"

# Temporarily save credentials
git config --global credential.helper cache

# Permanently save credentials (Windows)
git config --global credential.helper wincred

# Ignore file permission changes
git config core.fileMode false
```

### .gitignore

Create a `.gitignore` file in the project root:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv/

# PyCharm
.idea/

# VSCode
.vscode/

# Jupyter
.ipynb_checkpoints/

# Large data files
*.csv
*.db
*.parquet
datos/grandes/

# System
.DS_Store
Thumbs.db
```

---

## Common Errors and Solutions

### "fatal: not a git repository"

```bash
# Solution: Navigate to the project folder
cd path/to/ejercicios-bigdata

# Verify you are in the correct folder
git status
```

### "Your branch is behind 'origin/main'"

```bash
# Solution: Update your local branch
git pull origin main
```

### "CONFLICT (content): Merge conflict"

```bash
# Solution:
# 1. Open the file with the conflict
# 2. Look for the markers <<<<<<< ======= >>>>>>>
# 3. Manually edit, choose which code to keep
# 4. Remove the markers
# 5. Save and commit
git add resolved-file.py
git commit -m "Resolve conflict"
```

### "Permission denied (publickey)"

```bash
# Solution: Use HTTPS instead of SSH
git remote set-url origin https://github.com/TU_USUARIO/ejercicios-bigdata.git
```

### "error: failed to push some refs"

```bash
# Cause: Your local branch is behind the remote
# Solution: Pull first
git pull origin your-branch
# Then push
git push origin your-branch
```

---

## Emergency Commands

### Recover Lost Work

```bash
# View all changes
git reflog

# Go back to a previous state
git reset --hard abc123d

# Recover a deleted file
git checkout HEAD -- archivo.py
```

### Clean Repository

```bash
# Remove untracked files (dry run)
git clean -n

# Remove untracked files (execute)
git clean -f

# Remove untracked files and folders
git clean -fd

# Include files ignored in .gitignore
git clean -fdx
```

---

## Additional Resources

### Built-in Help

```bash
# General help
git help

# Help for a specific command
git help commit
git commit --help

# Short help version
git commit -h
```

### Useful Links

- [Git Cheat Sheet (GitHub)](https://education.github.com/git-cheat-sheet-education.pdf)
- [Visualize Git](https://git-school.github.io/visualizing-git/)
- [Learn Git Branching](https://learngitbranching.js.org/)
- [Oh Shit, Git!?!](https://ohshitgit.com/)

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌​​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​​‌‌​​​‌‍​‌‌​​​‌​‍​‌‌​​​‌​‍​‌‌​​​‌​﻿---

## Next Steps

Now that you know the essential commands:

- [Fork and Clone](fork-clone.md) - Initial project setup
- [Sync Fork](sincronizar-fork.md) - Keep your fork up to date
- [Submission Guide](../entregas/guia-entregas.md) - How to submit exercises
