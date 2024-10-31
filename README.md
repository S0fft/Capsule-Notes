# Capsule-Notes
#### Notes-App — Note-Taking Asynchronous-Project on FastAPI

An information platform that allows users to publish a variety of articles. 
The application is built using SSR architecture and also includes an API for managing articles.

#### Stack:
 - Pyhton
 - FastAPI
 - Jinja2 
 - SQLAlchemy 
 - SQLite
 - Pytest
 - Pytest
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
git clone https://github.com/S0fft/True-Publish-Protocol.git
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
Run the console in the root directory of the project to access application files and the database.
```bash
python
```
Afterwards, apply migrations in the Python console
```bash
app.app_context().push()
db.create_all()
```

### - Running the Server
Then, run server:
```powershell
python main.py
```
After starting the server, you can access the application by navigating to `http://127.0.0.1:5000` in your browser.

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
git clone https://github.com/S0fft/True-Publish-Protocol.git
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
Run the console in the root directory of the project to access application files and the database.
```bash
python3
```
Afterwards, apply migrations in the Python console
```bash
app.app_context().push()
db.create_all()
```

### - Running the Server
```powershell
python main.py
```
After starting the server, you can access the application by navigating to `http://127.0.0.1:5000` in your browser.

</details>
