
pip3 install virtualenv
python3 -m venv salsifydemo
cd salsifydemo
source bin/activate
pip3 install Django==2.0.5
pip3 install djangorestframework==3.8.2
pip3 install python-memcached==1.59
pip3 install pytz==2018.4
pip3 install six==1.11.0
pip3 install memory-profiler==0.52.0
pip3 install psutil==5.4.5
brew install memcached
brew services start memcached
git clone https://github.com/daidaitaotao/ReadLine.git
cd ReadLine/mysite
python3 manage.py migrate
python3 manage.py shell < readLine/load_data_to_file.py