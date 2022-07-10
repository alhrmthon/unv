import telebot,random,os,pyrogram
from telebot import types
import py_compile,json,base64, marshal, zlib,os
botf = True

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
token = os.environ.get("TOKEN")
app = Client("tag", bot_token=token, api_id = api_id, api_hash = api_hash)


data_json = {

	"base64": "#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n# ---------------------\n# Telegram : @VR_LA , @APP_YOUTUBE , \n# Coded by virus\n#---------------------\nimport base64\nexec(base64.b64decode(",
	
	"base16": "#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n# ---------------------\n# Telegram : @VR_LA , @APP_YOUTUBE , \n# Coded by virus\n# ---------------------\nimport base64\nexec(base64.b16decode(",

	"base32": "#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n# ---------------------\n# Telegram : @VR_LA , @APP_YOUTUBE , \n# Coded by virus\n# ---------------------\nimport base64\nexec(base64.b32decode(",	
	
	"marshal":"#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n# ---------------------\n# Telegram : @VR_LA , @APP_YOUTUBE , \n# Coded by virus\n# ---------------------\nimport marshal\nexec(marshal.loads(",
	
	"zlib":"#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n# ---------------------\n# Telegram : @VR_LA , @APP_YOUTUBE ,\n# Coded by virus\n#---------------------\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b64decode(",
	
	"lambda":"#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n# ---------------------\n# Telegram : @VR_LA , @APP_YOUTUBE ,  \n# Coded by virus\n# ---------------------\nexec((lambda _____, ______ : ______(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(_____),'<https://t.me/APP_YOUTUBE,'exec'))("
            }
''
class en():
    def mr(name_file):
        file = open(name_file, "r").read()
        print(file)
        en = compile(file, '<virus>', 'exec')
        enc = marshal.dumps(en)
        da = str(data_json["marshal"])
        data = (f"{da}{enc}))")
        return data
    def b64(name_file):
        file = open(name_file, "r").read()
        Enc = base64.b64encode(file.encode('UTF-8')).decode('ascii')
        da = str(data_json["base64"])
        data = (f"{da}'{Enc}'))")
        return data
    def lambdaS(name_file):
        file = open(name_file, "r").read()
        print(file)
        en=repr(zlib.compress(file.encode('utf-8')))
        da = str(data_json["lambda"])
        cmb=(f"{da}{en},compile))")
        return cmb
    def zi(name_file):
        file = open(name_file, "r").read()
        co=compile(file,"ru",'exec')
        mr=marshal.dumps(co)
        zl = zlib.compress(mr)
        enc = str(base64.b64encode(zl))
        da = str(data_json["zlib"])
        data = (f"{da}{enc}))))")
        return data



@bot.message_handler(commands=['start'])
def stagrt(message): 
    name_user = message.chat.first_name
    text=f"""
* مرحبأ  {name_user} *
- - - - - - - - - - - - - -
انا بوت تشفير ادوات البايثون بكل سهوله .
للتشفير اضغط امر التشفير : 
  /encode
 - - - - - - - - - - - - - -
coded : virus
DEV : @VR_LA

"""
    bot.send_message(message.chat.id, text =f"*{text}*",parse_mode="markdown")


@bot.message_handler(commands=['encode'])
def start_encode(message):
    call1 = types.InlineKeyboardButton(text = "base64 🔐", callback_data = 'base64')
    call2 = types.InlineKeyboardButton(text = "lambda 🔐", callback_data = 'lambda')
    call3 = types.InlineKeyboardButton(text = "marshal 🔐", callback_data = 'marshal')
    call4 = types.InlineKeyboardButton(text = "zlib 🔐", callback_data = 'zlib')
    call6 = types.InlineKeyboardButton(text = "<\> Developer channel <\>", url= "https://t.me/APP_YOUTUBE")
    Keyy = types.InlineKeyboardMarkup()
    Keyy.row_width = 1
    Keyy.add(call1,call2,call3,call4,call6)
    bot.send_message(message.chat.id, text=f"*اختر نوع التشفير \n\n  Choose the type of encryption ,🔥*",parse_mode="markdown",reply_markup=Keyy)
    
@bot.callback_query_handler(func=lambda call: True)
def virus_call(call):
    if call.data =="base64":
        virus_en(call.message)
    elif call.data == "lambda":
        virus_cc(call.message)
    elif call.data == "marshal":
        virus_er(call.message)
    elif call.data == "zlib":
        virus_et(call.message)


def virus_en(message):
    bot.send_message(message.chat.id, text ="*Send file in base64 : *",parse_mode="markdown")
    @bot.message_handler(content_types=['document'])
    def save(message):
        chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        ran = 'a'+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
        name_file = str(ran+'.py')
        with open(name_file, 'wb') as new_file:
            new_file.write(downloaded_file)
            new_file.close()
            msg = message.text
            Encs = en.b64(name_file)
            path_y=str(name_file.split(".")[0])
            name_file_tele = str(path_y+"virus.py")
            with open(name_file_tele, 'a') as x:
                x.write(f"{Encs}")
            doc = open(name_file_tele,'rb') 
            bot.send_document(message.chat.id,doc)
            os.system(f"rm -f {name_file}") 
            os.system(f"rm -f {name_file_tele}") 
                

def virus_cc(message):
    bot.send_message(message.chat.id, text ="*Send file in lambda : *",parse_mode="markdown")
    @bot.message_handler(content_types=['document'])
    def save(message):
        chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        ran = 'a'+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
        name_file = str(ran+'.py')
        with open(name_file, 'wb') as new_file:
            new_file.write(downloaded_file)
            new_file.close()
            msg = message.text
            Encs = en.lambdaS(name_file)
            path_y=str(name_file.split(".")[0])
            name_file_tele = str(path_y+"virus.py")
            with open(name_file_tele, 'a') as x:
                x.write(f"{Encs}")
            doc = open(name_file_tele,'rb') 
            bot.send_document(message.chat.id,doc)
            os.system(f"rm -f {name_file}") 
            os.system(f"rm -f {name_file_tele}") 

def virus_er(message):
    bot.send_message(message.chat.id, text ="*Send file in marshal : *",parse_mode="markdown")
    @bot.message_handler(content_types=['document'])
    def save(message):
        chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        ran = 'a'+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
        name_file = str(ran+'.py')
        with open(name_file, 'wb') as new_file:
            new_file.write(downloaded_file)
            new_file.close()
            msg = message.text
            Encs = en.mr(name_file)
            path_y=str(name_file.split(".")[0])
            name_file_tele = str(path_y+"virus.py")
            with open(name_file_tele, 'a') as x:
                x.write(f"{Encs}")
            doc = open(name_file_tele,'rb') 
            bot.send_document(message.chat.id,doc)
            os.system(f"rm -f {name_file}") 
            os.system(f"rm -f {name_file_tele}") 


def virus_et(message):
    bot.send_message(message.chat.id, text ="*Send file in zlib : *",parse_mode="markdown")
    @bot.message_handler(content_types=['document'])
    def save(message):
        chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        ran = 'a'+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
        name_file = str(ran+'.py')
        with open(name_file, 'wb') as new_file:
            new_file.write(downloaded_file)
            new_file.close()
            msg = message.text
            Encs = en.zi(name_file)
            path_y=str(name_file.split(".")[0])
            name_file_tele = str(path_y+"virus.py")
            with open(name_file_tele, 'a') as x:
                x.write(f"{Encs}")
            doc = open(name_file_tele,'rb') 
            bot.send_document(message.chat.id,doc)
            os.system(f"rm -f {name_file}") 
            os.system(f"rm -f {name_file_tele}") 
bot.polling(False)

