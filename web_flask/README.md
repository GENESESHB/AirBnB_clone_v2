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
```python
guillaume@ubuntu:~$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
guillaume@ubuntu:~$

``

guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
guillaume@ubuntu:~$ 

```

### 1. HBNB
- Write a script that starts a Flask web application.
- The application should listen on `0.0.0.0`, port `5000`.
- Define routes `/` and `/hbnb` that display "Hello HBNB!" and "HBNB" respectively.
- Use the option `strict_slashes=False` in your route definition.

```python
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.1-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
HBNB$
guillaume@ubuntu:~$ 
```

### 2. C is fun!
- Write a script that starts a Flask web application.
- The application should listen on `0.0.0.0`, port `5000`.
- Define routes `/`, `/hbnb`, and `/c/<text>` that display "Hello HBNB!", "HBNB", "C " followed by the value of the text variable, replacing underscores with spaces.
- Use the option `strict_slashes=False` in your route definition.

```python
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.2-c_route
Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
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
```

### 3. Python is cool!
- Write a script that starts a Flask web application.
- The application should listen on `0.0.0.0`, port `5000`.
- Define routes `/`, `/hbnb`, `/c/<text>`, and `/python/<text>` that display "Hello HBNB!", "HBNB", "C " followed by the value of the text variable (replace underscores with spaces), and "Python " followed by the value of the text variable (replace underscores with spaces).
- The default value of text for `/python` is "is cool".
- Use the option `strict_slashes=False` in your route definition.

```python
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.3-python_route
Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/is_magic ; echo "" | cat -e
Python is magic$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$

```

### 4. Is it a number?

Run the script `4-number_route.py` to start the Flask web application:

```bash
python3 -m web_flask.4-number_route
```

The application will be accessible at http://0.0.0.0:5000/.

#### Routes:
- `/`: Display "Hello HBNB!"
- `/hbnb`: Display "HBNB"
- `/c/<text>`: Display "C " followed by the value of the text variable (replace underscore _ symbols with a space)
- `/python/(<text>)`: Display "Python " followed by the value of the text variable (replace underscore _ symbols with a space)
- `/number/<n>`: Display "n is a number" only if n is an integer

```python
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.4-number_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/89 ; echo "" | cat -e
89 is a number$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 
```

### 5. Number template

Run the script `5-number_template.py` to start the Flask web application:

```bash
python3 -m web_flask.5-number_template
```

The application will be accessible at http://0.0.0.0:5000/.

#### Routes:
- `/`: Display "Hello HBNB!"
- `/hbnb`: Display "HBNB"
- `/c/<text>`: Display "C " followed by the value of the text variable (replace underscore _ symbols with a space)
- `/python/(<text>)`: Display "Python " followed by the value of the text variable (replace underscore _ symbols with a space)
- `/number/<n>`: Display "n is a number" only if n is an integer
- `/number_template/<n>`: Display an HTML page only if n is an integer with the H1 tag "Number: n" inside the BODY tag

```python
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.5-number_template
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 
```
### 6. Odd or even?

Run the script `6-number_odd_or_even.py` to start the Flask web application:

```bash
python3 -m web_flask.6-number_odd_or_even
```

The application will be accessible at http://0.0.0.0:5000/.

#### Routes:
- `/`: Display "Hello HBNB!"
- `/hbnb`: Display "HBNB"
- `/c/<text>`: Display "C " followed by the value of the text variable (replace underscore _ symbols with a space)
- `/python/(<text>)`: Display "Python " followed by the value of the text variable (replace underscore _ symbols with a space)
- `/number/<n>`: Display "n is a number" only if n is an integer
- `/number_template/<n>`: Display an HTML page only if n is an integer with the H1 tag "Number: n" inside the BODY tag
- `/number_odd_or_even/<n>`: Display an HTML page only if n is an integer with the H1 tag "Number: n is even|odd" inside the BODY tag

```python
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.6-number_odd_or_even
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89 is odd</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/32 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 32 is even</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 
```
Certainly! Here's a simplified README with your requested content:

---

## 7. Improve engines

### Mandatory Steps

Before using Flask to display our HBNB data, it is essential to update certain parts of our engine.

### Update FileStorage: (models/engine/file_storage.py)

- Open the `file_storage.py` file.
- Add a public method `def close(self)`: Call `reload()` method for deserializing the JSON file to objects.

### Update DBStorage: (models/engine/db_storage.py)

- Open the `db_storage.py` file.
- Add a public method `def close(self)`: Call `remove()` method on the private session attribute (`self.__session`) or `close()` on the class `Session`.

### Update State: (models/state.py) - If not already present

- If your storage engine is not `DBStorage`, add a public getter method `cities` to return the list of City objects from storage linked to the current State.

Ensure to make these changes to enhance the functionality of our engine and enable the use of Flask for displaying HBNB data.

````python
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 
>>> from models import storage
>>> from models.state import State
>>> len(storage.all(State))
5
>>> len(storage.all(State))
5
>>> # Time to insert new data!
At this moment, in another tab:

guillaume@ubuntu:~/AirBnB_v2$ echo 'INSERT INTO `states` VALUES ("421a55f1-7d82-45d9-b54c-a76916479545","2017-03-25 19:42:40","2017-03-25 19:42:40","Alabama");' | mysql -uroot -p hbnb_dev_db
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ 
And let’s go back the Python console:

>>> # Time to insert new data!
>>> len(storage.all(State))
5
>>> # normal: the SQLAlchemy didn't reload his `Session`
>>> # to force it, you must remove the current session to create a new one:
>>> storage.close()
>>> len(storage.all(State))
6
>>> # perfect!
And for the getter cities in the State model:

guillaume@ubuntu:~/AirBnB_v2$ cat main.py
#!/usr/bin/python3
"""
 Test cities access from a state
"""
from models import storage
from models.state import State
from models.city import City

"""
 Objects creations
"""
state_1 = State(name="California")
print("New state: {}".format(state_1))
state_1.save()
state_2 = State(name="Arizona")
print("New state: {}".format(state_2))
state_2.save()

city_1_1 = City(state_id=state_1.id, name="Napa")
print("New city: {} in the state: {}".format(city_1_1, state_1))
city_1_1.save()
city_1_2 = City(state_id=state_1.id, name="Sonoma")
print("New city: {} in the state: {}".format(city_1_2, state_1))
city_1_2.save()
city_2_1 = City(state_id=state_2.id, name="Page")
print("New city: {} in the state: {}".format(city_2_1, state_2))
city_2_1.save()


"""
 Verification
"""
print("")
all_states = storage.all(State)
for state_id, state in all_states.items():
    for city in state.cities:
        print("Find the city {} in the state {}".format(city, state))

guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ rm file.json ; HBNB_TYPE_STORAGE=fs ./main.py 
New state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509954), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New state: [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510256), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}
New city: [City] (e3e36ded-fe56-44f5-bf08-8a27e2b30672) {'name': 'Napa', 'id': 'e3e36ded-fe56-44f5-bf08-8a27e2b30672', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510797), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510791)} in the state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New city: [City] (12a58d70-e255-4c1e-8a68-7d5fb924d2d2) {'name': 'Sonoma', 'id': '12a58d70-e255-4c1e-8a68-7d5fb924d2d2', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511437), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511432)} in the state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New city: [City] (a693bdb9-e0ca-4521-adfd-e1a93c093b4b) {'name': 'Page', 'id': 'a693bdb9-e0ca-4521-adfd-e1a93c093b4b', 'state_id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511873), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511869)} in the state: [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510373), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}

Find the city [City] (e3e36ded-fe56-44f5-bf08-8a27e2b30672) {'name': 'Napa', 'id': 'e3e36ded-fe56-44f5-bf08-8a27e2b30672', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510953), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510791)} in the state [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
Find the city [City] (12a58d70-e255-4c1e-8a68-7d5fb924d2d2) {'name': 'Sonoma', 'id': '12a58d70-e255-4c1e-8a68-7d5fb924d2d2', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511513), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511432)} in the state [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
Find the city [City] (a693bdb9-e0ca-4521-adfd-e1a93c093b4b) {'name': 'Page', 'id': 'a693bdb9-e0ca-4521-adfd-e1a93c093b4b', 'state_id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 512073), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511869)} in the state [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510373), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}
guillaume@ubuntu:~/AirBnB_v2$ 
````
---
## Contributors
- [Your Name]
- [Contributor 1]
- [Contributor 2]

Feel free to contribute to the project by creating pull requests or reporting issues.

## GitHub Repository
- [AirBnB_clone_v2](https://github.com/username/AirBnB_clone_v2)
- Directory: web_flask
- Files: 0-hello_route.py, 1-hbnb_route.py, 2-c_route.py, 3-python_route.py, __init__.py

## Conclusion
This project focuses on developing a Flask web application for an AirBnB clone, emphasizing independent problem-solving and adherence to coding standards. Each task contributes to the overall learning objectives, and successful completion requires a deep understanding of web frameworks, Flask, and related concepts.

--- 

Feel free to customize it further based on your preferences!

[Return to Top](#top)

