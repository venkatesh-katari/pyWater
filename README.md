# Water Reminder

### Screenshot
![Screenshot](/screenshot.png)


### Setup

    git clone https://github.com/venkatesh-katari/pyWater.git
    cd pyWater
    ./run.sh # this will install dependencies and run water.py

### Create cron 

    0 10 * * * <path to shell script>/run.sh #run every day at 10 am


### Update run.sh
```sh
#assumes brew is present
brew install terminal-notifier

#### update this
cd <path to code folder>

export WATER_VENV_PATH=/tmp/waterR

python3 -m venv ${WATER_VENV_PATH}

source  ${WATER_VENV_PATH}/bin/activate

pip3 install -r requirements.txt

python water.py

deactivate
```

### run

```sh
cd <path-to-git-repo>
./run.sh
```
