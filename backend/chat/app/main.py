from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

app = FastAPI(
    title="Chat API",
    version="0.1",
    summary="Main API and backend service for Chat application domain",
    default_response_class=ORJSONResponse,
    contact={"name": "Maintainer", "email": "spdlqj011@gmail.com"},
    license_info={
        "name": "MIT License",
        "identifier": "MIT",
        "url": "https://opensource.org/license/mit",
    },
    redirect_slashes=True,
)


@app.get("/")
def landing_zone():
    return {"helloWorld": "You just landed on the Chat API!"}
