# Secure File-sharing System

## Description
The goal is to create a secure file-sharing system between two types of users: Operation Users (Ops Users) and Client Users. This system will be implemented using REST APIs to perform various actions. Below is an overview of the actions that each type of user can perform.

### Ops User (Operation User):

- #### Login:
    Ops Users will be able to log in securely using their credentials.

- #### Upload File:
    Ops Users are allowed to upload files, but only files with specific types (pptx, docx, xlsx) are allowed.
    The system should enforce that only these file types are accepted during the upload process.

### Client User:

- #### Sign Up:
    Client Users can sign up for the system, and the system should return an encrypted URL.
    This URL may be used for further verification or to complete the registration process.

- #### Email Verify:
    After signing up, a verification email with otp will be sent to the user's registered email address.
    The user needs to verify their email by sharing otp on the link.

- #### Login:
     Client Users will be able to log in securely using their credentials.

- #### Download File:
    Client Users can download files that have been uploaded by Ops Users.
    The system should ensure secure and authorized access to the files.

- #### List all uploaded files:
    Client Users can view a list of all files that have been uploaded by Ops Users.
    This list may include information such as file names, types, and upload dates.
## Getting Started

### Dependencies

* Prerequisites
  * Docker
  * Python 
  
* Libraries 
  * Fastapi 
  * Boto3
  * Sqlite3

### Installing

* Clone Repository
```commandline

```

### Setup


* Install required libraries
```commandline
pip install -r requirements.txt
```
* Setup Docker Container
```
docker-compose up -d
```

* Run ```main.py``` 


## Authors

[@Varun_Bainsla](https://www.linkedin.com/in/varun-b-8424a1141/)

