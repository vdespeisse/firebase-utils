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

## Usage
### Database
```
from firebase_utils.connector import Connector
firedb = Connector(path_to_service_account_key, <PROJECT_NAME>)
firedb.write({'test':'whatever'})
```

### Auth
