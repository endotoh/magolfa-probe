# Installation

git clone git@github.com:endotoh/magolfa-probe.git

cd magolfa-probe

python3 -m venv venv

source venv/bin/activate

pip3 install requests

or

pip install requests

chmod a+x probe.py

# Usage

source venv/bin/activate  # only needed in a new terminal

./probe.py username passwordfile server_ip_address login_failure_match_string

eg

./probe.py user rockyou.txt 192.168.1.5 "o errati"

Press Ctrl-C to abort execution