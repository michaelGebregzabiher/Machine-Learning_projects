from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Ping")

@app.get("/ping") #this is the url that gets called and will return a pong response.
#note every thing we request in the internet is a url i.e we are using our browser to access it with a defined address.
#(send a get request and receive a response(html in the real world, json in our case))
def ping():
    return {"message": "This is my first fastapi app"}

if __name__ == "__main__":          #The if __name__ == "__main__": guard means the server only starts when this file is run directly (e.g., python main.py), not when it’s imported elsewhere.
    uvicorn.run(app, host="0.0.0.0", port=9696)
