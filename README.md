# flask-env-setup
Managing environment files in Flask, spanning from development to production.

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

# Points to remember
- If you modify your application's debug mode, you need to restart the application to reflect the changes.