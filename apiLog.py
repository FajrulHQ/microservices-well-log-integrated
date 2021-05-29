from models.modelLog import database as db
import json, lasio
from bson import ObjectId
import pandas as pd

db = db()

def objIdToStr(obj):
  return str(obj["_id"])

def search_data_wellInfo():
  data_list = []
  for data in db.show_wellInfo():
    data["_id"] = objIdToStr(data)
    data_list.append(data)
  return data_list

def search_data_wellInfo_by_mnemonic(**params):
  data_list = []
  for data in db.show_wellInfoByMnemonic(**params):
    data["_id"] = objIdToStr(data)
    data_list.append(data)
  return data_list

def search_data_logInfo():
  data_list = []
  for data in db.show_logInfo():
    data["_id"] = objIdToStr(data)
    data_list.append(data)
  return data_list

def search_data_logData():
  data_list = []
  for data in db.show_logData():
    data["_id"] = objIdToStr(data)
    data_list.append(data)
  return data_list

def insertLAS(document):
  las = lasio.read(document)
  try:
    wellData = [{
      "filename": document,
      "mnemonic": well.mnemonic,
      "desc": well.descr,
      "unit": well.unit,
      "value": well.value}
      for well in las.well]

    curveData = [{
      "filename": document,
      "mnemonic": curve.mnemonic,
      "desc": curve.descr,
      "unit": curve.unit,
      "data_shape": curve.data.shape}
      for curve in las.curves]

    log_titles = [curve.mnemonic for curve in las.curves]
    data = dict()
    logData = [{
      "filename": document,
      "version": las.version[0].descr,
      "data" : data
    }]
    for n in range(len(las.data)):
      id_ = str(n)
      log_values = las.data[n]
      log_data =  dict(zip(log_titles, log_values))
      data[id_]=log_data
    
    db.insertData(wellData, curveData, logData)

    return {"success": "Data has been inserted"}
  
  except Exception as e:
    print(e)
    return {"error": str(e)}

#insertLAS("fileLAS\\BGN-1.las")