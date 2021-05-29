from re import search
from fastapi import APIRouter
from fastapi.datastructures import UploadFile
from fastapi import APIRouter, File, UploadFile
from fastapi.encoders import jsonable_encoder
from apiLog import *
import os, json

router = APIRouter()

@router.post("/upload-las/")
async def upload_las(las: UploadFile = File(...)):
  print(las.file)
  try:
    os.chdir("fileLAS")
    file_name = las.filename.replace(" ","-")
    #with open(file_name,'wb+') as f:
    #  content = las.file.read()
    #  f.write(content)
    new_las = insertLAS(file_name)
    return {"output": new_las}
    
  except Exception as e:
    print(e)
    return {"error": str(e)}

@router.get("/well-information")
async def view_search_data_wellInfo():
  result = search_data_wellInfo()
  return result

@router.post("/well-information/search")
async def view_search_data_wellInfo_by_mnemonic(params:dict):
  result = search_data_wellInfo_by_mnemonic(**params)
  return result

@router.get("/log-information")
async def view_search_data_logInfo():
  result = search_data_logInfo()
  return result

@router.get("/log-data")
async def view_search_data_logData():
  result = search_data_logData()
  return result