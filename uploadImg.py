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

@app.post("/upload_file/")
async def upload_file (file: UploadFile = File (...)):
    fileUploaded = await file.read()

    uploadToCloud = cloudinary.uploader.upload(
        fileUploaded,
        resource_type = "auto",
        public_id = file.filename
    )
    
    return { "Cloudinary URL" : uploadToCloud["secure_url"]}