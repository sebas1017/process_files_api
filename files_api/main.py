from fastapi import FastAPI, File, UploadFile, Form
import uvicorn
import shutil
import logging
import traceback

app = FastAPI()

logger = logging.getLogger()
logger.setLevel(logging.INFO)


@app.post("/post_file_server")
async def post_file_server(file: UploadFile = File(...), case_param: str = Form(...), aditional_param: int = Form(...)):
    try:
        file_path = f"/mnt/{file.filename}"  # Ruta de destino en /mnt
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        form_data = {
            "file_name": file.filename,
            "case_param": case_param,
            "aditional_param": aditional_param,
            "file_path": file_path
        }
        return form_data
    except Exception as error:
        logger.error(f"error in endpoint post_file_server -> {error}")
        logger.error(traceback.format_exc())



@app.get("/test_message")
async def test_message():
    return "Welcome to post_file_server API REST"



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3333, reload=True)