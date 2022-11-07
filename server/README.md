# Setup

### Install pip
```
sudo apt update
sudo apt install python3-pip
```

### Use virtualenv
```
source ./venv/bin/activate
```

### Install project python requirements
```
python3 -m pip install -r requirements.txt
```

### To run the API service
```
python3 -m uvicorn main:app --reload
```
