from datetime import datetime
import requests

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S");

def get_city_weather(city):
    url=f"https://wttr.in/{city}?format=3"
    response=requests.get(url, timeout=10)
    return response.text

def get_city():
    return "Mumbai";

tools=[
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description" : "Return current date time in string format",
            "parameters": {
                "type": "object",
                "properties":{}
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_city_weather",
            "description": "Return weather of any city in string format",
            "parameters": {
                "type": "object",
                "properties": {
                    "city" :{
                        "type": "string",
                        "description" : "City to get the weather"
                    }
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name" :"get_city",
            "description" : "Return current city in string format",
            "parameters": {
                "type" :"object",
                "properties" : {}
            }
        }
    }
]

FUCNTION_NAME_TO_FUNCTION_MAP={
    "get_current_time" : get_current_time,
    "get_city_weather": get_city_weather,
    "get_city": get_city
}
