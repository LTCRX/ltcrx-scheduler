## Run Locally

1.install python version

```bash
sudo apt install python3.8
```

2.create a venv

```bash
python3.8 -m venv .venv
```

3.Activate the virtual environment:

On macOS/Linux, run:

```bash
source .venv/bin/activate
```

On Windows, run:

```bash
.venv\Scripts\activate
```

4.install requirements.txt

```bash
pip install -r requirements.txt
```

5.Environment variables

- Copy the .env-dev file
- Save as .env inside irrigation_design_system_backend

6.Start the project
   To run the application

```bash
cd ./project && uvicorn main:app --reload
``` 

7.Accessing the API
   http://127.0.0.1:8000/docs#/

8.CodeChecks: 

check with flake8
```bash
flake8 .
```

check with black
```bash
black --check project
```

format with black
```bash
black .
```

9. database migrate 
create migrations
```bash
alembic revision --autogenerate -m "First commit"
```

apply migrations
```bash
alembic upgrade head
```