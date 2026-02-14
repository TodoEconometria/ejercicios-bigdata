# Tools Installation﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌‌​​​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​‌‌​​‌​‌‍​​‌‌‌​​​﻿

This guide will walk you through the installation of all the tools needed for the course, step by step.﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌‌​​​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​‌‌​​‌​‌‍​​‌‌‌​​​﻿

## System Requirements

!!! info "Minimum Requirements"
    - **RAM:** 8GB
    - **Disk space:** 20GB
    - **Processor:** i5 or equivalent
    - **Operating System:** Windows 10+, macOS 10.14+, or Linux (Ubuntu 20.04+)

!!! success "Recommended Requirements"
    - **RAM:** 16GB
    - **Disk space:** 50GB SSD
    - **Processor:** i7 or equivalent
    - **Operating System:** Latest available operating system

---

## Step 1: Install Git

Git is the version control system we will use to manage our code.

=== "Windows"

    ### Option A: With winget (Recommended)

    ```bash
    # Open PowerShell or CMD as Administrator
    winget install Git.Git
    ```

    ### Option B: Graphical installer

    1. Download from [git-scm.com](https://git-scm.com/download/win)
    2. Run the installer
    3. Use the default settings (Next, Next, Next...)

    ### Verify installation

    ```bash
    git --version
    # Should show: git version 2.x.x
    ```

=== "macOS"

    ### Option A: With Homebrew (Recommended)

    ```bash
    # If you don't have Homebrew, install it first:
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    # Install Git
    brew install git
    ```

    ### Option B: With Xcode Command Line Tools

    ```bash
    xcode-select --install
    ```

    ### Verify installation

    ```bash
    git --version
    # Should show: git version 2.x.x
    ```

=== "Linux"

    ### Ubuntu/Debian

    ```bash
    sudo apt-get update
    sudo apt-get install git
    ```

    ### Fedora

    ```bash
    sudo dnf install git
    ```

    ### Arch Linux

    ```bash
    sudo pacman -S git
    ```

    ### Verify installation

    ```bash
    git --version
    # Should show: git version 2.x.x
    ```

---

## Step 2: Configure Git

Once Git is installed, we need to configure it with your information:

```bash
# Set your name (use your real name)
git config --global user.name "Your Full Name"

# Set your email (use the same email as GitHub)
git config --global user.email "your@email.com"

# Verify configuration
git config --list
```

!!! tip "Tip"
    The name and email you set will appear on all your commits, so use your real name and the email you will use on GitHub.

---

## Step 3: Create a GitHub Account

GitHub is the platform where we will host our code.

1. Go to [github.com](https://github.com)
2. Click on **"Sign Up"**
3. Fill in the form:
    - Username: Choose a professional name (e.g.: `juan-garcia`, not `kitty123`)
    - Email: Use the same one you configured in Git
    - Password: Use a strong password
4. Verify your email
5. Complete your profile (photo, bio optional)

!!! warning "Important"
    Use the **same email** you configured in Git. This links your commits with your GitHub account.

---

## Step 4: Install Python

We need Python 3.11 or higher.

=== "Windows"

    ### Option A: With winget (Recommended)

    ```bash
    winget install Python.Python.3.11
    ```

    ### Option B: Graphical installer

    1. Download from [python.org](https://www.python.org/downloads/)
    2. **IMPORTANT:** Check "Add Python to PATH"
    3. Run the installer
    4. Click on "Install Now"

    ### Verify installation

    ```bash
    python --version
    # Should show: Python 3.11.x

    pip --version
    # Should show: pip 23.x.x
    ```

=== "macOS"

    ### With Homebrew (Recommended)

    ```bash
    brew install python@3.11
    ```

    ### Verify installation

    ```bash
    python3 --version
    # Should show: Python 3.11.x

    pip3 --version
    # Should show: pip 23.x.x
    ```

=== "Linux"

    ### Ubuntu/Debian

    ```bash
    sudo apt-get update
    sudo apt-get install python3.11 python3-pip
    ```

    ### Fedora

    ```bash
    sudo dnf install python3.11 python3-pip
    ```

    ### Verify installation

    ```bash
    python3 --version
    # Should show: Python 3.11.x

    pip3 --version
    # Should show: pip 23.x.x
    ```

!!! warning "Note for macOS/Linux"
    On macOS and Linux, use `python3` and `pip3` instead of `python` and `pip`.

---

## Step 5: Install PyCharm (Optional but Recommended)

PyCharm is the IDE we recommend for the course.

### PyCharm Community Edition (Free)

=== "Windows"

    1. Download from [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/download/)
    2. Choose **"Community Edition"** (free)
    3. Run the installer
    4. Follow the installer steps

=== "macOS"

    ```bash
    brew install --cask pycharm-ce
    ```

    Or download from [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/download/)

=== "Linux"

    Download from [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/download/)

    Or use Snap:

    ```bash
    sudo snap install pycharm-community --classic
    ```

### Alternatives to PyCharm

If you prefer another editor:

- **Visual Studio Code:** Lightweight and extensible ([code.visualstudio.com](https://code.visualstudio.com))
- **Jupyter Lab:** For working with notebooks ([jupyter.org](https://jupyter.org))
- **Sublime Text:** Advanced text editor ([sublimetext.com](https://www.sublimetext.com))

---

## Step 6: Clone the Repository

Now that you have everything installed, clone your fork of the repository:

!!! warning "Important"
    First you must **Fork** the repository on GitHub. Go to the [Fork and Clone guide](../git-github/fork-clone.md) for more details.

```bash
# Navigate to the folder where you want to save the project
cd Documents  # or whichever folder you prefer

# Clone YOUR fork (replace YOUR_USERNAME)
git clone https://github.com/YOUR_USERNAME/ejercicios-bigdata.git

# Enter the folder
cd ejercicios-bigdata

# Connect to the original repository (upstream)
git remote add upstream https://github.com/TodoEconometria/ejercicios-bigdata.git

# Verify that everything is set up correctly
git remote -v
```

You should see something like this:

```
origin    https://github.com/YOUR_USERNAME/ejercicios-bigdata.git (fetch)
origin    https://github.com/YOUR_USERNAME/ejercicios-bigdata.git (push)
upstream  https://github.com/TodoEconometria/ejercicios-bigdata.git (fetch)
upstream  https://github.com/TodoEconometria/ejercicios-bigdata.git (push)
```

---

## Step 7: Create a Virtual Environment

It is a good practice to use virtual environments for each project:

```bash
# Make sure you are in the project folder
cd ejercicios-bigdata

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate

# macOS/Linux:
source .venv/bin/activate

# You should see (.venv) at the beginning of your terminal
```

!!! tip "Tip"
    Always activate the virtual environment before working on the project.

---

## Step 8: Install Dependencies

With the virtual environment activated, install the project dependencies:

```bash
# Upgrade pip
pip install --upgrade pip

# Install project dependencies
pip install -r requirements.txt

# Verify that everything was installed correctly
python -c "import pandas, dask, sqlite3; print('All OK!')"
```

If you see **"All OK!"**, you are ready to get started.

---

## Final Verification

Run these commands to verify that everything is installed correctly:

```bash
# Git
git --version

# Python
python --version

# Pip
pip --version

# Verify libraries
python -c "import pandas; print(f'Pandas {pandas.__version__}')"
python -c "import dask; print(f'Dask {dask.__version__}')"
```

!!! success "Installation Complete"
    If all the commands above worked, you are ready to start with [Your First Exercise](primer-ejercicio.md)!

---

## Common Issues

??? question "Error: 'python' is not recognized as a command"

    **Windows:** Python is not in the PATH.

    Solution:

    1. Reinstall Python
    2. Check the **"Add Python to PATH"** option
    3. Restart the terminal

    **macOS/Linux:** Use `python3` instead of `python`

??? question "Error: Permission denied when installing with pip"

    **Cause:** Attempting to install packages globally without permissions.

    **Solution:** Use a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # macOS/Linux
    .venv\Scripts\activate      # Windows
    pip install -r requirements.txt
    ```

??? question "Git says 'fatal: not a git repository'"

    **Cause:** You are not in the project folder.

    **Solution:**

    ```bash
    # Navigate to the correct folder
    cd path/to/ejercicios-bigdata

    # Verify you are in the correct folder
    ls -la  # You should see a .git/ folder
    ```

??? question "PyCharm does not detect the Python interpreter"

    **Solution:**

    1. Open PyCharm
    2. File → Settings (Windows/Linux) or PyCharm → Preferences (macOS)
    3. Project → Python Interpreter
    4. Click on the gear icon → Add
    5. Select "Existing environment"
    6. Browse to `.venv/Scripts/python.exe` (Windows) or `.venv/bin/python` (macOS/Linux)

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌‌​​​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​‌‌​​‌​‌‍​​‌‌‌​​​﻿---

## Next Steps

Now that you have everything installed, continue with:

- [Your First Exercise](primer-ejercicio.md) - Learn the basic workflow
- [Fork and Clone](../git-github/fork-clone.md) - Understand how to work with Git and GitHub
- [Course Roadmap](roadmap.md) - See all available exercises
