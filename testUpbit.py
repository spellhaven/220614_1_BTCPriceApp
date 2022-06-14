#https://docs.upbit.com/reference/ticker%ED%98%84%EC%9E%AC%EA%B0%80-%EB%82%B4%EC%97%AD
# pyupbit 모듈을 가져오는 건 쉽고 이렇게 API를 가져오는 건 어렵다.
#만남은 쉽고~~~~ 이별은 어려워~~~~~~~

import requests

url = "https://api.upbit.com/v1/ticker"
param = {"markets":"KRW-BTC"}

headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers, params = param)
print(response)

result = response.json()
#print(result)
print(result[0]['trade_date'])


