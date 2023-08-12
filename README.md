```markdown
<p align="center">
  <img src="https://github.com/bdbaraban/AirBnB_clone/blob/master/assets/hbnb_logo.png" alt="HolbertonBnB logo">
</p>

<h1 align="center">🏠 HolbertonBnB 🏠</h1>
<p align="center">An Airbnb Clone 🏡</p>

--------------------------------------------------------------------------------------------------------------------
<h1> 🔧 0x00. Airbnb Clone - The Console 🔧 <h1>
-------------------------------------------

<h3> 📚 0x00. Table of Contents 📚 <h3>
---------------------------------

# 📌 0x01 Introduction
# 🛠️ 0x02 Environment
# 🚀 0x03 Installation
# 🧪 0x04 Testing
# 📝 0x05 Usage

<h3> 📌 0x01 Introduction 📌 <h3>
----------------------------------

Team project to build a clone of [Airbnb](https://www.airbnb.com/).

The console is a command interpreter to manage object abstractions and their storage.

For a deeper understanding of the project, refer to the Wiki.

The console will perform the following tasks:

 * Create a new object
 * Retrieve an object from a file
 * Perform operations on objects
 * Destroy an object

## Storage
-----------

All classes are managed by the Storage engine in the FileStorage Class.

<h3> 🛠️ 0x02 Environment 🛠️ <h3>
-----------------------------------

Tools used:
- Suite CRM terminal
- Python
- Git (distributed version control system)
- GitHub

Style guidelines:
- pycodestyle (version 2.8.0)
- PEP8

Development and testing were conducted on:
- Operating System: Ubuntu 20.04 LTS
- Programming Language: Python 3.8.3
- Editors: VIM 8.1.2269, VSCode 1.6.1, and Atom 1.58.0
- Version Control: Git 2.25.1.

## 🚀 0x03 Installation 🚀

```bash
git clone https://github.com/aysuarex/AirBnB_clone.git
```

Navigate to the `AirBnb` directory and run the command:

```bash
./console.py
```

### Execution

Interactive mode:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

Non-interactive mode:

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## 🧪 0x04 Testing 🧪

All tests are defined in the `tests` folder.

### Documentation

- Modules:

```python
python3 -c 'print(__import__("my_module").__doc__)'
```

- Classes:

```python
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
```

- Functions (inside and outside a class):

```python
python3 -c 'print(__import__("my_module").my_function.__doc__)'
```

and

```python
python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
```

### Python Unit Tests

- unittest module
- File extension: `.py`
- Files and folders start with `test_`
- Organization: For `models/base.py`, unit tests are in: `tests/test_models/test_base.py`
- Execution command: `python3 -m unittest discover tests`
- Or: `python3 -m unittest tests/test_models/test_base.py`

Run tests in interactive mode:

```bash
echo "python3 -m unittest discover tests" | bash
```

Run tests in non-interactive mode:

To run tests in non-interactive mode and discover all the tests, use the command:

```bash
python3 -m unittest discover tests
```

## 📝 0x05 Usage 📝

- Start the console in interactive mode:

```bash
$ ./console.py
(hbnb)
```

- Use help to see the available commands:

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

- Quit the console:

```bash
(hbnb) quit
$
```

### Commands

> The commands are displayed in the following format: *Command / Usage / Example with Output*

* Create

> *Creates a new instance of a given class. The class' ID is printed, and the instance is saved to the file `file.json`.*

```bash
create <class>
```

```bash
(hbnb) create BaseModel
6cfb47c4-a434-4da7-ac03-2122624c3762
(hbnb)
```

* Show

```bash
show <class> <id>
```

```bash
(hbnb) show BaseModel 6cfb47c4-a434-4da7-ac03-2122624c3762
[BaseModel] (a) [BaseModel] (6cfb47c4-a434-4da7-ac03-2122624c3762) {'id': '6cfb47c4-a434-4da7-ac03-2122624c3762', 'created_at': datetime.datetime(2021, 11, 14, 3, 28, 45, 571360), 'updated_at': datetime.datetime(2021, 11, 14, 3, 28, 45, 571389)}
(hbnb)
```

* Destroy

> *Deletes an instance of a given class with a given ID.*
> *Updates the `file.json`.*

```bash
(hbnb) create User
0c98d2b8-7ffa-42b7-8009-d9d54b69a472
(hbnb) destroy User 0c98d2b8-7ffa-42b7-8009-d9d54b69a472
(hbnb) show User 0c98d2b8-7ffa-42b7-8009-d9d54b69a472
** no instance found **
(hbnb)
```

* all

> *Prints string representation of all instances of a given class.*
> *If no class is passed, all classes are printed.*

```bash
(hbnb) create BaseModel
e45ddda9-eb80-4858-99a9-226d4f08a629
(hbnb) all BaseModel
["[BaseModel] (4c8f7ebc-257f-4ed1-b26b-e7aace459897) [BaseModel] (4c8f7ebc-257f
