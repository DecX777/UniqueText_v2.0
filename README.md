UniqueText_v2.0
=============
Program for automatic translation and uniqueness text.

Installation
------------
To install the requirements, enter a console:

    pip install -r requirements.txt 
    
Getting api_id and api_hash
------------
Go to https://my.telegram.org/auth and then create 3 environmental variable `api_id`, `api_hash`, `session_file`

Running
------------
Open terminal `python3 main.py`.

Compilation
------------
    pip install pyinstaller
    pyinstaller -w main.py --onefile
