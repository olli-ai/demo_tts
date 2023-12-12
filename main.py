import uvicorn
import requests
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles


def fastapi_app() -> FastAPI:
    app = FastAPI()

    @app.post("/items/{item_id}")
    async def get_item(item_id: int, request: Request):
        # Extract user ID and S/N from request body
        body = await request.json()
        user_id = body.get("userId")
        sn = body.get("sn")

        print(f"Item ID: {item_id}, User ID: {user_id}, S/N: {sn}")

        tts = ""

        match item_id:
            case 1:
                tts = "Dạ em nghe"
            case 2:
                tts = "Em đã mở máy lạnh"
            case 3:
                tts = "Vâng ạ, em đã chỉnh nhiệt độ xuống 17 độ"
            case 4:
                tts = "Em đã mở chế độ ngủ, chúc anh ngủ ngon"
            case _:
                tts = "Xin chào"

        print({"userId": user_id, "maikaSNS": [sn], "tts": tts})
        requests.post(
            "https://smarthome.iviet.com/api/v1/gateway/notification",
            headers={"Content-Type": "application/json"},
            json={"userId": int(user_id), "maikaSNS": [sn], "tts": tts},
        )
        return {}

    app.mount("/", StaticFiles(directory="frontend", html=True), name="static")

    return app


app = fastapi_app()


if __name__ == "__main__":
    uvicorn.run(
        app, host="0.0.0.0", port=int(3010),
    )
