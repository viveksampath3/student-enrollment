import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\x88\x85K\x08\xe1.\xe7\x9e\x190\x0eo3\xbeR\x08'
    
    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment', 'host':'mongodb://localhost:27017/UTA_Enrollment'}