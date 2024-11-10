from quart import Quart, websocket
import asyncio
import random
import json

app = Quart(__name__)

# Simulated data generator
async def send_data():
    while True:
        # Generate random temperature and humidity data
        data = {
            "temperature": round(random.uniform(20, 30), 2),
            "humidity": round(random.uniform(40, 60), 2)
        }
        # Send the data as a JSON string
        await websocket.send(json.dumps(data))
        # Wait for 2 seconds before sending the next update
        await asyncio.sleep(2)

@app.websocket('/ws/data')
async def ws_data():
    print("WebSocket connection established")
    try:
        # Keep sending data until the connection is closed
        await send_data()
    except Exception as e:
        print(f"WebSocket error: {e}")

if __name__ == '__main__':
    app.run()
