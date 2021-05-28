from pymongo import MongoClient
from bson.objectid import ObjectId

class database:
  def __init__(self):
    try:
      self.nosql_db = MongoClient()
      self.db = self.nosql_db.wellLog
      self.wellInfo = self.db.wellInformation
      self.logInfo = self.db.logInformation
      self.logData = self.db.logData
      print("database connected")
    except Exception as e:
      print(e)

  def showData(self):
    pass

  def insertData(self, well, log, data):
    self.wellInfo.insert_one(well)
    self.logInfo.insert_one(log)
    self.logData.insert_one(data)

  def updateDataById(self,**params):
    pass

  def deleteDataById(self, id):
    pass