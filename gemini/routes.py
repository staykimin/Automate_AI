from flask import render_template, request, session, url_for, redirect, session, abort, send_from_directory
from kimin.core_selenium import Driver

import json, time, os, atexit

gemini = []
def Gemini(**parameter):
	hasil = ""
	if parameter['driver'].Fill_XPATH('//div[@role="textbox"]', f"{parameter['text']}\n"):
		elemen1 = f'//div[@id="chat-history"]/infinite-scroller/div[{gemini.index(gemini[-1])+1}]'
		while True:
			cek = parameter['driver'].Get_Elemen(elemen1)
			if not cek is None:
				elemen = f"{elemen1}/model-response"
				elem = parameter['driver'].Get_Elemen(f"{elemen}/div/div[2]")
				if not elem is None:
					parameter['driver'].Scroll_Funtion(elem)
					hasil = parameter['driver'].Extract_Text(f"{elemen}/div/response-container")
					if not hasil.find("\nshare\n") == -1:
						hasil = hasil.split("\n")
						hasil = "\n".join(hasil[2:-3])
						break
				
			elem = parameter['driver'].Get_Elemen('//body')
			parameter['driver'].Send_END(elem)
			time.sleep(0.5)
		
	return hasil

def CHAT(mode):
	text = request.form['text']
	if mode == 'gemini':
		hasil = Gemini(driver=sin, text=text)
		gemini.append(hasil)
	return hasil

def On_Close(sin):
	sin.Exit()

config = "kimin/cfg.min"
with open(config, 'r', encoding='UTF-8') as dataku:
	config = json.loads(dataku.read())

path = os.path.abspath(f"{config['folder_profile']}/Profile_2")
config['browser_config'].append(f'--user-data-dir={path}')
	
path = os.path.abspath(f"{config['folder_profile']}/Profile_2")
config['browser_config'].append(f'--user-data-dir={path}')
if not os.path.exists(path):
	os.makedirs(path)

sin = Driver(config)
sin.Visit("https://gemini.google.com/app")
atexit.register(On_Close, sin)