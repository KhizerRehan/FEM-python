# FEM-python
This repo is to learn python

# Install Python 
- version: 3.7 or > 3.7

# Install Missing Dependencies 
- sudo apt-get update \
    && apt-get install -y python3-pip python3-dev build-essential python3-setuptools python3-venv \
    && apt-get install -y python-dev pkg-config


# Create Virtual Environment
python3 -m venv env1
source env1/bin/activate
deactivate

# Lock packages files:
- pip freeze > requirements.txt

Note: This can create a lock file of depdencies inside a virtual environment
      it is local `depdencies` w.r.t to environment not the global depdencies
      install in your system (Global Dependencies may vary from user system to system).



