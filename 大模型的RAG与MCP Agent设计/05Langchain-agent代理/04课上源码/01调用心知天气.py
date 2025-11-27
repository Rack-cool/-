import requests
from pydantic import Field


# 定义心知天气API的工具类
class WeatherTool:
    city: str = Field(description="City name, include city and county")

    def __init__(self, api_key) -> None:
        self.api_key = api_key

    def run(self, city):
        city = city.split("\n")[0]  # 清除多余的换行符，避免报错
        url = f"https://api.seniverse.com/v3/weather/now.json?key={self.api_key}&location={city}&language=zh-Hans&unit=c"
        # 构建 API 请求 URL 返回结果
        response = requests.get(url)
        if response.status_code == 200:  # 请求成功
            data = response.json()  # 解析返回的JSON
            weather = data["results"][0]["now"]["text"]  # 天气信息
            tem = data["results"][0]["now"]["temperature"]  # 温度
            return f"{city}的天气是{weather}, 温度是{tem}°C"  # 返回格式化后的天气信息
        else:
            return f"无法获取{city}的天气信息。"

api_key = "S4CjQwhad-soNSc0A"
weather_tool = WeatherTool(api_key)
print(weather_tool.run("广州"))

