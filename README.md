# Flask environment files setup
Managing environment files in Flask, spanning from development to production.

In this example, we'll be loading:
- Either the development `.env.dev` or production `.env.prod` environment file, determined by the debug mode of the application.

# Prerequisites
- Familiarity with setting up virtual environments
- Basic understanding of creating Flask applications
- Understanding of environment file usage

# Steps to run the application
- Clone the repository

- Create virtual environment using the following command
```
virtualenv <environment-name>
```
_Note: Replace `<environment-name>` with your actual environment name_

- Activate the environment using following command
```
.\<environment-name>\Scripts\activate.ps1
```
_Note: Replace `<environment-name>` with your actual environment name_

- Install the required packages using following command
```
pip install -r .\src\utils\requirements.txt
```

- Run the flask application
```
python .\src\app\main.py
```

- The result will be visible on the specified PORT_NUMBER.

# Points to remember
- If you modify your application's debug mode, you need to restart the application to reflect the changes.