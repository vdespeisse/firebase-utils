# Firebase Utils

## Description
Backend utils for firebase
Authentication, DB read write ...

## Setup
```
pip install -r requirements.txt
pip install .
```

Go to firebase settings > Service accounts > Generate private key
Rename key to `<PROJECT_NAME>.json` and put it in keys folder

## Usage
### Database
```
from firebase_utils.connector import Connector
firedb = Connector(<PROJECT_NAME>)
firedb.write({'test':'whatever'})
```

### Auth
