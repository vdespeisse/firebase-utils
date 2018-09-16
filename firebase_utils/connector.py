from firebase_utils import KEYS_PATH
import json, os
import firebase_admin
from firebase_admin import db, auth
from oauth2client.service_account import ServiceAccountCredentials


class Connector(object):
  def __init__(self, project):
    self.config_path = os.path.join(KEYS_PATH,project + '.json')
    self.config = json.load(open(self.config_path))
    self.credentials = firebase_admin.credentials.Certificate(self.config_path)
    try:
      self.app = firebase_admin.initialize_app(self.credentials, {
          'databaseURL': 'https://' + self.config['project_id'] + '.firebaseio.com'
      }, project)
    except:
      self.app = firebase_admin.get_app(name=project)

  def update(self, path, data):
    if type(data) == dict:
      return db.reference(path=path,app=self.app).update(data)
    if type(data) == list:
      return db.reference(path=path,app=self.app).set(data)
    print 'Needs to be dict or list'

  def write(self, path, data):
    return db.reference(path=path,app=self.app).set(data)

  def read(self, path):
    return db.reference(path=path,app=self.app).get()


def get_access_token(project):
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
       os.path.join(KEYS_PATH,project+'.json'), 'https://www.googleapis.com/auth/firebase.messaging')
  access_token_info = credentials.get_access_token()
  return access_token_info.access_token

def get_custom_token(uid, connector):
  return auth.create_custom_token(uid, app=connector.app)
