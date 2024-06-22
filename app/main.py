from fastapi import FastAPI, File, UploadFile
from PIL import Image
from app.model.model import sentiment_classifier, speech_to_text

app = FastAPI()

@app.get("/")
def home():
    return {"health_check": "OK"}

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    file.filename = "voice.mp3"
    try:
        contents = await file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception as e:
        return {"message": f"Error uploading or processing image: {str(e)}"}
    finally:
        file.file.close()

    return {"filename": file.filename}

@app.get("/predict")
def predict():

    file_path = "voice.mp3"
    text = speech_to_text(file_path)
    label = sentiment_classifier(text[0].text)
    return {"message": f" label: {label}"}
