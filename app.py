from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlmodel import Session, select
from model.models import IsuzuMotors, SQLModel
from db import engine  
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.get("/get-model")
def get_model(number: int):
    with Session(engine) as session:
        result = session.exec(
            select(IsuzuMotors).where(
                IsuzuMotors.start_number <= number,
                IsuzuMotors.end_number >= number
            )
        ).first()

        # Construct full chassis number
        chassis_number = f"{result.chassis_type}-{number}"

        # Prepare the POST payload
        payload = {
            'searchCertificate': chassis_number
        }

        # Make the POST request
        response = requests.post(
            "https://www.qisjp.co.uk/processVerifyCertificate.php",
            data=payload
        )

        # Handle response
        print("POST sent with chassisNo:", chassis_number)
        print("Status:", response.status_code)
        print("Response:")
        print(response.text)

        return result.model_dump() 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)