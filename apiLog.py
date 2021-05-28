from pymongo import MongoClient
from models.modelLog import database as db
import json, lasio
from bson import ObjectId

db = db()

def objIdToStr(obj):
  return str(obj["_id"])

def insertLAS(document):
  las = lasio.read(document)
  try:
    wellData = [{
      "mnemonic": well.mnemonic,
      "desc": well.desc,
      "unit": well.unit,
      "value": well.value}
      for well in las.well]

    curveData = [{
      "mnemonic": curve.mnemonic,
      "desc": curve.descr,
      "unit": curve.unit,
      "data": curve.data.shape}
      for curve in las.curves]

    log_titles = [curve.mnemonic for curve in las.curves]
    logData = [{
      "version": las.version[0].descr,
      "data" : {}
    }]
    for n in range(len(las.data)):
      id_ = str(n)
      log_values = las.data[n]
      log_data =  dict(zip(log_titles, log_values))
      data[id_]=log_data

    db.insertData(wellData, curveData, logData)
  
  except Exception as e:
    print(e)


