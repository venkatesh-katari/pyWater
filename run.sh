brew install terminal-notifier
cd /Users/vkatari/dev/tools/water
export WATER_VENV_PATH=/tmp/waterR
python3.7 -m venv ${WATER_VENV_PATH}
source ${WATER_VENV_PATH}/bin/activate
pip3 install -r requirements.txt
python water.py
deactivate