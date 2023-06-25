import io
from fastapi import FastAPI, Response
import uvicorn

from analytics import Analytics

app = FastAPI()

@app.get("/analytics")
def get_analytics_data():
    buffer = io.BytesIO()
    a = Analytics(buffer)
    a.get_analytiics_result()
    return Response(content=buffer.getvalue(), media_type="image/png")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
