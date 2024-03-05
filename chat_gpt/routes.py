from flask import render_template, request, session, url_for, redirect, session, abort, send_from_directory
from kimin.core_selenium import Driver

import json, time, os, atexit

gpt = []
def GPT(**parameter):
	hasil = ""
	if parameter['driver'].Fill_XPATH('//*[@id="prompt-textarea"]', parameter['text']):
		if parameter['driver'].Click_XPATH('//button[@data-testid="send-button"]'):
			no = gpt.index(gpt[-1])+3
			elemen = f'//div[@data-testid="conversation-turn-{no}"]'
			elemen1 = f'//*[@id="__next"]/div[1]/div/main/div[1]/div[1]/div/div/div/div[{no}]/div/div/div[2]/div[2]/div[2]/div/span/button'
			parameter['driver'].delay = 1
			while True:
				cek = parameter['driver'].Elemen_Wait(elemen1)
				if cek:
					hasil = parameter['driver'].Extract_Text(elemen)
					if not hasil is None:
						hasil = hasil.split("\n")
						hasil = "\n".join(hasil[1:])
						break
				time.sleep(0.5)
				
	else:
		print("Text Area Tidak Ada")
	return hasil

def CHAT(mode):
	text = request.form['text']
	if mode == 'gpt':
		gpt.append(text)
		hasil = GPT(driver=sin, text=text)
		gpt.append(hasil)
	return hasil

def On_Close(sin):
	sin.Exit()

config = "kimin/cfg.min"
with open(config, 'r', encoding='UTF-8') as dataku:
	config = json.loads(dataku.read())

path = os.path.abspath(f"{config['folder_profile']}/Profile_1")
config['browser_config'].append(f'--user-data-dir={path}')
	
path = os.path.abspath(f"{config['folder_profile']}/Profile_1")
config['browser_config'].append(f'--user-data-dir={path}')
if not os.path.exists(path):
	os.makedirs(path)

sin = Driver(config)
sin.Visit("https://chat.openai.com")
atexit.register(On_Close, sin)