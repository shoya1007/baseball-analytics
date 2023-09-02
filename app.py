import io

import uvicorn
from fastapi import FastAPI, Response

from analytics import Analytics
from data_collector import DataCollector

app = FastAPI()


@app.get("/pitch_movement_stats")
def get_pitch_movement_data(player_first_name, player_last_name, start_date, end_date):
    collector = DataCollector(player_first_name, player_last_name, start_date, end_date)
    csv_data = collector.create_pitching_stats_csv()
    buffer = io.BytesIO()
    a = Analytics(buffer)
    a.get_pitch_movement_data(csv_data)
    return Response(content=buffer.getvalue(), media_type="image/png")


@app.get("/pitch_plate")
def get_pitch_plate(player_first_name, player_last_name, start_date, end_date):
    collector = DataCollector(player_first_name, player_last_name, start_date, end_date)
    csv_data = collector.create_pitching_stats_csv()
    buffer = io.BytesIO()
    a = Analytics(buffer)
    a.get_pitch_plate(csv_data)
    return Response(content=buffer.getvalue(), media_type="image/png")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
