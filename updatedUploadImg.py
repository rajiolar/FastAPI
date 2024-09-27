from fastapi import  FastAPI, UploadFile, File
import cloudinary
import cloudinary.uploader

cloudinary.config( 
    cloud_name = "dzplra4wt", 
    api_key = "378195214295549", 
    api_secret = "BcbbcC38VZIA4eV6Zry7ibLNx6o",
    secure=True
)

app = FastAPI()

uploadedFiles = {}

@app.post("/upload_file/")
async def upload_file (file: UploadFile = File (...)):
    fileUploaded = await file.read()

    uploadToCloud = cloudinary.uploader.upload(
        fileUploaded,
        resource_type = "auto",
        public_id = file.filename
    )
    
    uploadedFiles[file.filename] = uploadToCloud["secure_url"]
    return { "Cloudinary URL" : uploadToCloud["secure_url"]}


@app.get("/get_upload_by_id/{upload_id}")
async def get_upload_by_id(upload_id : str):
    if upload_id not in uploadedFiles:
        {"Error": "Enter a Valid Upload ID"}
    
    return {"Here is your Uploaded Image": uploadedFiles[upload_id]}