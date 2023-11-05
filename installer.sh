git clone https://github.com/SebAndBlocks/TabbieOS /tabbie
cd /tabbie
python3 -m venv .venv
. .venv/bin/activate
pip3 install flask
chmod +x /tabbie/tabbie-startup.sh
crontab -e @reboot /tabbie/tabbie-startup.sh