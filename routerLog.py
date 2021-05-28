from fastapi import APIRouter
from fastapi.datastructures import UploadFile
from fastapi import APIRouter, File, UploadFile
from apiLog import *

router = APIRouter()

@router.post("/upload-las")
async def upload_las(file: UploadFile = File(...)):
  return {"filename": file.filename}