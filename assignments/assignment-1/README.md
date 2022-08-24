# Assignment 1 - Environment Setup

## Skills Acquired/Reinforced Upon Completion

- Install Git/VCS
- Launch Git bash/Windows Command Prompt/bash shell
- Install Python3
- Create Python module
- Enter some Git commands:
  - `git config <options>`
  - `git clone <options>`
  - `git pull <options>`
  - `git add <options>`
  - `git commit <options>`
  - `git push <options>`
- Enter some gh CLI commands
  - `gh auth <options>`
  - `gh repo <options>`

___

**NOTE**: *At any time you are uncertain, ask for help rather than attempting to continue. I don't expect you to understand most of this stuff, but it is important for you to have this environment setup for ease of learning.*

## Setup

### Visual Studio Code Setup

Download and install the latest version of Visual Studio Code [here](https://code.visualstudio.com/). After the editor has finished installing; launch the program. Install the following plugins by pressing the 4 blocks on the left-hand side of the editor and searching for:

- Python
- Python Extension Pack
- Python Environment Manager
- Robot Framework Language Server
- Code Runner

### Python Environment Setup

Download and install the latest version of Python 3 [here](https://www.python.org/downloads/) for you operating system. Python 3 is the language we are going to be using in the course. In order to set up your Python3 environment, follow the instructions **below**.

```sh
# Create a virtual environment the in project directory.
python3 -m venv venv

# Activate the virtual environment using Windows command prompt.
venv\Scripts\activate

# Activate the virtual environment using OSX/Linux
./venv/bin/activate

# Import the necessary packages.
pip3 install -r requirements.txt
```

### Accessing/creating your GitHub account

We will be using GitHub as your code repository for this course. If you do not know what that is, do not worry; I will explain in class. If you do not already have an account, please visit [GitHub](https://education.github.com/pack) and in the center of the screen you should see a green button saying `Singup for Student Developer Pack`. Select `Get student benefits`

### Creating your personal access token

Once logged in, please go to the [tokens](https://github.com/settings/tokens) page. You should see a button that says "Generate new token", press that to generate a new token. Make sure that every box in is checked. Be sure to name it and to set the expiration for at least 30 days. When you are done, press "Generate token" at the bottom of the screen. Copy the token and save it someplace safe (it should look something like):

```
# THIS IS ONLY AN EXAMPLE.
ghp_kevin17MARIST9y2022SzdscMpT120ueo123
```

Remember this is a secret... **_DO NOT GIVE OUT YOUR TOKEN_**

### Git SCM installation

Download the latest version of Git [here](https://git-scm.com/). The reference manual can be found [here](https://git-scm.com/docs). Bookmark this very handy [cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf)! You will need to learn how to use this version control tool.

### GitHub CLI installation

Download and install the latest version of GitHub CLI found [here](https://cli.github.com/manual/installation). If you do not know what GitHub or a CLI is, do not worry. I will explain what they are in class. We will be using this to manage our repository. If you prefer to use Git CLI instead of GitHub CLI that is fine too.

### Forking this repository

Login into your GitHub account using the GitHub CLI...

```sh
# invoke the gh cli to log in
gh auth login

# select "Github.com"
> Github.com
  Github Enterprise Server

# only select "SSH" if you have an SSH key setup.
> HTTPS
  SSH

# select "Paste an authentication token" and then paste the token we created earlier
  Login with a web browser
> Paste an authentication token
```

### Setting up Circle CI

Now we need to login into [CircleCI](https://circleci.com/signup?return-to=https%3A%2F%2Fapp.circleci.com%2Fdashboard) which is a CI/CD tool (Continuous Integration/Continuous Delivery). On the sign-up screen, be sure to select "Sign up with GitHub" to seemlessly connect your GitHub account to your forked repository. On your projects screen, you should see your fork of `cmpt-120`. Next to you will see the link "Set Up Project"; press it. It should be pre-filled in with the existing configuration in the repo. Press "Set Up Project" and you should be all set up!

## Running Robot Framework test cases

### Running a single Robot Framework test case

In order to run a single test case execute the following:

```sh
# Run the assignment 1 test case.
python3 -m robot /assignments/assignment-1/test.robot
```

### Running all Robot Framework test cases

In order to run all of your test cases run the following command on Linux and MacOS.

```sh
# Run all of the test cases.
python3 runtests.py
```
