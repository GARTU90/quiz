#!/usr/bin/env python3
#by gartujuan@gmail.com
#license GNU/GPL

#simple quiz

def validate_true_false(text):
	text=text.lower()
	if text=="hamburguesas" or text=="burritos" or text=="tacos" or "aguachile":
		return True
	else:
		return False

answer= False
while not answer:
	print("cual es mi comida favorita?")
	print("hamburguesas")
	print("burritos")
	print("tacos")
	print("aguachile")
	text=input("--> ")
	if validate_true_false(text):
		answer=True
		#print("respuesta valdia")
		if "hamburguesas" in text:
			print("correcto")
		else:
			print("incorrecto")
