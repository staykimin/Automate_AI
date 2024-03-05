import requests, time
url = "http://127.0.0.1:3000/chat/gpt"
data = {"text":f"Halo Apakah Bisa Membantu Saya Dalam Bahasa Indonesia"}
start = time.time()
respon = requests.post(url, data=data)
print(respon.text)
print(f"Respon Time : {time.time() - start} Detik")