#!/bin/bash

echo "Python3, pip3, brew, and git are all required to build the ReadLine service.  Please ensure you have them installed."

echo "Setting up the Python virtual environment"
pip3 install virtualenv
python3 -m venv salsifydemo
cd salsifydemo
source bin/activate

echo "Installing all dependencies"
pip3 install Django==2.0.5
pip3 install djangorestframework==3.8.2
pip3 install python-memcached==1.59
pip3 install pytz==2018.4
pip3 install six==1.11.0
pip3 install memory-profiler==0.52.0
pip3 install psutil==5.4.5
brew install memcached

echo "Starting dependent services"
brew services start memcached

echo "Cloning source code"
git clone https://github.com/daidaitaotao/ReadLine.git
cd ReadLine/mysite

echo "Setting up the Django database"
python3 manage.py migrate

echo "Creating a 2000-line test input file"
python3 manage.py shell < readLine/create_small_test_data_file.py

echo "Building the file index"
python3 manage.py shell < readLine/create_index_file.py