[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/arpit3018/AlgoMania-BackEnd/pulls)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

# AlgoMania-BackEnd

## About Project
A web based algorithm guessing platform where mentor/admin can post the code or algorithm and students need to guess the name of it within limited time frame. Students can track their progress on leader board and can apply filters to see weekly and monthly progress. The updation of leader board would be dynamic and would not require any third person involvement. The main aim for building this project is to make student aware about famous and important algorithm in a fun way.

## Technology Stack
* Django (Python)
* SQLite as DB

## Requirements 
* Any operating system (i.e. Linux, Windows, MacOS X)
* A little knowledge of Django. Don't worry if you are new to it, you just need knack to learn.
* Any IDE (i.e. VSCode, etc)

## Setting up the project
* Create a virtual environment in recently created directory and activate it:
```
python3 -m venv env
source env/bin/activate
```

* Clone the repository and enter to the repository:
```
git clone https://github.com/arpit3018/AlgoMania-BackEnd.git
cd algomania
```

* Next, install the dependencies using pip:
```
pip install -r requirements.txt 
```
* Once the dependencies is installed, migrate your database.
```
python3 manage.py migrate
python3 manage.py makemigrations
```

* Then create a superuser account for Django:
```
python manage.py createsuperuser
```

* Finally, you’re ready to start the development server:
```
python manage.py runserver
```
Visit [localhost:8000](http://127.0.0.1:8000/) in your browser to see how it looks.

## Contributing
You can contribute in several ways. If you know how to code or are a designer, you are welcome to contribute using pull requests.
You can also contribute by [opening issues](https://github.com/arpit3018/AlgoMania-BackEnd/issues) about defects and things that could be improved or request entirely new features that you think would help others.
