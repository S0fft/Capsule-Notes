# Capsule-Notes
#### Notes-App — Note-Taking Asynchronous-Project on FastAPI

An anonymous note taking app that allows users to not only create and name notes, but also save them for later use.

#### Stack:
 - Pyhton
 - FastAPI
 - SQLAlchemy 
 - SQLite
 - Pytest
 - Jinja2 
 - Redis | Celery | Flower

Additional libraries are specified in the `requirements.txt` file.

## Project Setup on Windows

### - Installing the Stack
To begin, install: [Python](https://www.python.org/downloads/)
<br>
Links are provided to the latest version of the tools.

### - Cloning a Project from GitHub
Create a root directory on your computer, then open it in your code editor or terminal.
<br>
Next, write this command into the command line:
```powershell
git clone https://github.com/S0fft/Capsule-Notes.git .
```
You will see the project files appear in your directory.

### - Creating a Virtual Environment
Create a virtual environment:
```powershell
python -m venv .venv
```

And activate it:
```powershell
.venv\Scripts\Activate
```

### - Installing the Requirements
Next, install packages:

```powershell
python.exe -m pip install --upgrade pip
``` 
```powershell
pip install -r requirements.txt
```

 ### - Applying the Migrations
Run the following command in the terminal; this will create the folder structure and the configuration file alembic.ini:
```bash
alembic init migrations
```
Now you can create a new migration by running the following command:
```bash
alembic revision --autogenerate -m "initial migration"
```

### - Running the Server
Then, run server:
```powershell
uvicorn main:app --reload
```
After starting the server, you can access the application by navigating to `http://127.0.0.1:8000` in your browser.

<details>
<summary><h3> Project Setup on Unix-Like Systems </h3></summary>
These commands do the same thing as described above: 
<br>

### - Installing the Stack
To begin, install: [Python](https://www.python.org/downloads/)
<br>
Links are provided to the latest version of the tools.

### - Cloning a Project from GitHub
Create a root directory on your computer, then open it in your code editor or terminal.
<br>
Next, write this command into the command line:
```powershell
git clone https://github.com/S0fft/Capsule-Notes.git .
```
You will see the project files appear in your directory.

### - Creating a Virtual Environment
```bash
python3 -m pip install --upgrade pip
```

```bash
source ./venv/bin/activate
```

### - Installing the Requirements
```bash
pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

### - Applying the Migrations
Run the following command in the terminal; this will create the folder structure and the configuration file alembic.ini:
```bash
alembic init migrations
```
Now you can create a new migration by running the following command:
```bash
alembic revision --autogenerate -m "initial migration"
```

### - Running the Server
```powershell
uvicorn main:app --reload
```
After starting the server, you can access the application by navigating to `http://127.0.0.1:8000` in your browser.
</details>
