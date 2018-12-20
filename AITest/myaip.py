from aip import AipNlp

APP_ID = '15221232'
API_KEY = 'mekMUt6nem2O5M9HHUlAAGqF'
SECRET_KEY = 'kukGiDvX5eNO2CLiiNjHF1mtTFm0VPw2'

nlp_client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

text1 = "你叫什么名字"

text2 = "您怎么称呼"


res = nlp_client.simnet(text1, text2)

print(res.get("score"))