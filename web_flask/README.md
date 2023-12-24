<a name="top"></a>
# Your README Title

<!-- Content of your README -->
Certainly! Here's a modified version of the information to resemble the structure you'd typically find in a README.md file on GitHub:

---

# AirBnB Clone - Web Framework Project

## Table of Contents
- [Introduction](#introduction)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
  - [Python Scripts](#python-scripts)
  - [HTML/CSS Files](#htmlcss-files)
- [Installation](#installation)
- [Manual QA Review](#manual-qa-review)
- [Video Library](#video-library)
- [Tasks](#tasks)
  - [Task 0: Hello Flask!](#0-hello-flask)
  - [Task 1: HBNB](#1-hbnb)
  - [Task 2: C is fun!](#2-c-is-fun)
  - [Task 3: Python is cool!](#3-python-is-cool)
- [GitHub Repository](#github-repository)
- [Conclusion](#conclusion)

## Introduction
This project involves creating an AirBnB clone using the Flask web framework in Python. The project is managed by Guillaume, the CTO at Holberton School, and is scheduled to start on December 21, 2023, at 4:00 AM, with a deadline of January 2, 2024, at 4:00 AM.

## Learning Objectives
By the end of this project, you are expected to understand the following concepts:

### General
- What is a Web Framework?
- How to build a web framework with Flask.
- How to define routes in Flask.
- Handling variables in a route.
- Working with templates and creating HTML responses in Flask.
- Creating dynamic templates with loops and conditions.
- Displaying data from a MySQL database in HTML.

### Copyright - Plagiarism
- Strict guidelines against plagiarism.
- Independent problem-solving and code creation.

## Requirements
### Python Scripts
- Use Python 3.4.3 on Ubuntu 20.04 LTS.
- Use PEP 8 style (version 1.7).
- All files must be executable.
- Documentation for modules, classes, and functions.

### HTML/CSS Files
- W3C compliant code.
- CSS files in the styles folder, images in the images folder.
- No use of `!important` or id (#...) in the CSS file.
- All tags must be in uppercase.

## Installation
To install Flask, use the following command:
```bash
$ pip3 install Flask
```

## Manual QA Review
Request a review from a peer before the project's deadline. If no peers are available, request a review from a TA or staff member.

## Video Library
A recommended YouTube playlist titled "Python: Flask the web framework" is suggested to get you started.

## Tasks
### 0. Hello Flask!
- Write a script that starts a Flask web application.
- The application should listen on `0.0.0.0`, port `5000`.
- Define a route `/` that displays "Hello HBNB!"
- Use the option `strict_slashes=False` in your route definition.
``
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
guillaume@ubuntu:~$ 
``

### 1. HBNB
- Write a script that starts a Flask web application.
- The application should listen on `0.0.0.0`, port `5000`.
- Define routes `/` and `/hbnb` that display "Hello HBNB!" and "HBNB" respectively.
- Use the option `strict_slashes=False` in your route definition.
``
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.1-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
HBNB$
guillaume@ubuntu:~$ 
``

### 2. C is fun!
- Write a script that starts a Flask web application.
- The application should listen on `0.0.0.0`, port `5000`.
- Define routes `/`, `/hbnb`, and `/c/<text>` that display "Hello HBNB!", "HBNB", "C " followed by the value of the text variable, replacing underscores with spaces.
- Use the option `strict_slashes=False` in your route definition.
``
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.2-c_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
C is fun$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
C cool$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 
``

### 3. Python is cool!
- Write a script that starts a Flask web application.
- The application should listen on `0.0.0.0`, port `5000`.
- Define routes `/`, `/hbnb`, `/c/<text>`, and `/python/<text>` that display "Hello HBNB!", "HBNB", "C " followed by the value of the text variable (replace underscores with spaces), and "Python " followed by the value of the text variable (replace underscores with spaces).
- The default value of text for `/python` is "is cool".
- Use the option `strict_slashes=False` in your route definition.

``
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.3-python_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/is_magic ; echo "" | cat -e
Python is magic$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$
``

## GitHub Repository
- [AirBnB_clone_v2](https://github.com/username/AirBnB_clone_v2)
- Directory: web_flask
- Files: 0-hello_route.py, 1-hbnb_route.py, 2-c_route.py, 3-python_route.py, __init__.py

## Conclusion
This project focuses on developing a Flask web application for an AirBnB clone, emphasizing independent problem-solving and adherence to coding standards. Each task contributes to the overall learning objectives, and successful completion requires a deep understanding of web frameworks, Flask, and related concepts.

--- 

Feel free to customize it further based on your preferences!

[Return to Top](#top)

