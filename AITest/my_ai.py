from aip import AipSpeech, AipNlp
import os

APP_ID = '15221232'
API_KEY = 'mekMUt6nem2O5M9HHUlAAGqF'
SECRET_KEY = 'kukGiDvX5eNO2CLiiNjHF1mtTFm0VPw2'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
nlp_client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

res = client.synthesis('兰兰，你喜不喜欢杨真贤？杨真贤很喜欢你呢，她放不下你，咋办？', 'zh', 1, {
    "per": 4,
    "pit": 8,
    "spd": 4,
    "vol": 5,
})

if not isinstance(res, dict):
    with open("voice.mp3", "wb") as f:
        f.write(res)


# 下面展示语音识别

def get_file_content(file_path):
    os.system(f"ffmpeg -y -i {file_path} -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {file_path}.pcm")
    with open(f"{file_path}.pcm", 'rb') as fp:
        return fp.read()


# 识别本地文件
result = client.asr(get_file_content('voice.mp3'), 'pcm', 16000, {
    'dev_pid': 1536
})

questions = result.get("result")[0]
print(questions)

# if nlp_client.simnet(questions, "")
