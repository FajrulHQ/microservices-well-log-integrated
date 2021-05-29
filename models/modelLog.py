from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.message import query

class database:
  def __init__(self):
    try:
      self.nosql_db = MongoClient()
      self.db = self.nosql_db.wellLog
      self.wellInfo = self.db.wellInformation
      self.logInfo = self.db.logInformation
      self.logData = self.db.logData
    except Exception as e:
      print(e)

  def show_wellInfo(self):
    result = self.wellInfo.find()
    return [item for item in result]

  def show_wellInfoByMnemonic(self,**params):
    result = self.wellInfo.find_one({"mnemonic":params['mnemonic']})
    return result

  def show_logInfo(self):
    result = self.logInfo.find()
    return [item for item in result]

  def show_logData(self):
    result = self.logData.find()
    return [item for item in result]

  def insertData(self, well, log, data):
    self.wellInfo.insert_many(well)
    self.logInfo.insert_many(log)
    self.logData.insert_many(data)

  def updateDataByMnemonic(self,data,**params):
    query_1 = {"mnemonic":params["mnemonic"]}
    query_2 = {"$set": params[data]}
    self.wellInfo.update_one(query_1, query_2)

  def deleteDataById(self, id):
    pass