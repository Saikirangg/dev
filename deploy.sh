sudo kill -9 $(lsof -t -i:8000)
cd /home/ubuntu/crm/
unzip -o code_master.zip
rm code_master.zip
pip3 install -r requirements.txt
nohup python3 manage.py runserver 0.0.0.0:8000 &>/dev/null &
