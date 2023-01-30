import sys
import os
import random

#Cookie961 Starts Here

def ending(resp):
	respdec = ''.join(chr(i) for i in resp)
	return respdec

def execute(command):
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for jj in range(len(command)):
		if (command[jj] in alphabet):
			raise TypeError("Invalid N command.")
		else:
			try:
				result = eval(command)
				return result
			except:
				raise TypeError("Invalid N command.")

#Yeah, veryyyy "clever"
def cycleinterpreter(code, counter):
	response = []
	cumm = []
	comnum = 0
	br = False
	strnum = 0
	funnum = 0
	size = 0
	cyclecode = ""
	e_exist = False
	coms = "cCokKEiIe()rR[]1234567890+-%/*"
	for jp in range(len(code)):
		if ((code[jp] in coms) == False):
			return "ProgrammError: Invalid code."
	while counter > 0 or size < 100:
		size += 1
		for i in range(len(code)):
			try:
				if (code[i] == "c"):
					counter += 1
				elif (code[i] == "C"):
					counter += 10
				elif (code[i] == "o" and counter > 0):
					counter -= 1
				elif (code[i] == "k"):
					counter *= 2
				elif (code[i] == "K"):
					counter *= 5
				elif (code[i] == "9"):
					strnum += 1
					star = "String"+":"
					stri = input(star)
					[response.append(ord(c)) for c in stri]
				elif (code[i] == "6"):
					comnum += 1
					cmar = "Command"+":"
					command = input(cmar)
					result = str(execute(command))
					[response.append(ord(pp)) for pp in result]
				elif (code[i] == "["):
					pu = i+1
					command = ""
					coderepl = code
					while coderepl[pu] != "]":
						command += coderepl[pu]
						coderepl = coderepl[:pu] + coderepl[(pu+1):]
					result = str(execute(command))
					[response.append(ord(pp)) for pp in result]
				#elif (code[i] == "1"):
				#	funstr = "Function"+":"
				#	fnar = input(funstr)
				#	result = interpreter(fnar)
				#	[response.append(ord(nn)) for nn in result]
				elif (code[i] == "1"):
					print(counter)
				elif (code[i] == "r"):
					print(random.randint(0, 500))
				elif (code[i] == "R"):
					counter += random.randint(0, 500)
				elif (code[i] == "i"):
					response.append(counter)
					counter = 0
				elif (code[i] == "I"):
					response.append(counter)
				elif (code[i] == "E"):
					counter = 0
				elif (code[i] == "e"):
					br = True
			except IndexError:
				pass
		if (size >= 100 or br == True or counter == 0):
			break
	if (len(response) > 0):
		return response
	else:
		pass
				


def interpreter(code):
	response = []
	respnum = 0
	comnum = 0
	strnum = 0
	funnum = 0
	cyclecode = ""
	e_exist = False
	coms = "cCokKEiIe()rR[]1234567890+-%/*"
	for jp in range(len(code)):
		if ((code[jp] in coms) == False):
			return "ProgrammError: Invalid code."
	for i in range(len(code)):
		try:
			if (code[i] == "c"):
				respnum += 1
			elif (code[i] == "C"):
				respnum += 10
			elif (code[i] == "o" and respnum > 0):
				respnum -= 1
			elif (code[i] == "k"):
				respnum *= 2
			elif (code[i] == "K"):
				respnum *= 5
			elif (code[i] == "9"):
				strnum += 1
				star = "String"+str(strnum)+":"
				stri = input(star)
				[response.append(ord(c)) for c in stri]
			elif (code[i] == "6"):
				comnum += 1
				cmar = "Command"+str(comnum)+":"
				command = input(cmar)
				result = str(execute(command))
				[response.append(ord(pp)) for pp in result]
			#elif (code[i] == "1"):
			#	funstr = "Function"+str(funnum)+":"
			#	fnar = input(funstr)
			#	result = interpreter(fnar)
			#	[response.append(ord(nn)) for nn in result]
			elif (code[i] == "1"):
				print(respnum)
			elif (code[i] == "r"):
				print(random.randint(0, 500))
			elif (code[i] == "R"):
				respnum += random.randint(0, 500)
			elif (code[i] == "("):
				pu = i+1
				while code[pu] != ")":
					cyclecode += code[pu]
					code = code[:pu] + code[(pu+1):]
				result = cycleinterpreter(cyclecode, respnum)
				cyclecode = ""
				try:
					for iyu in range(len(result)):
						response.append(result[iyu])
				except:
					pass
			elif (code[i] == "["):
				pu = i+1
				command = ""
				while code[pu] != "]":
					command += code[pu]
					code = code[:pu] + code[(pu+1):]
				result = str(execute(command))
				command = ""
				[response.append(ord(pp)) for pp in result]
			elif (code[i] == "i"):
				response.append(respnum)
				respnum = 0
			elif (code[i] == "I"):
				response.append(respnum)
			elif (code[i] == "E"):
				respnum = 0
			elif (code[i] == "e"):
				if (len(response) > 0):
					respdec = ending(response)
					return respdec
				else:
					return ' '
		except IndexError:
			pass
	if (e_exist == False):
		return "Programm finished."

#code = sys.argv[1]

if (len(sys.argv) == 2):
	file = sys.argv[1]
	with open(file, 'r') as f:
		if (file.endswith('.c961')):
			code = f.read()
			print(" ")
			print(interpreter(code))
			print(" ")
			print("Programm finished.")
		else:
			print("Error: Unknown file extension.")
else:
	file = input("File Name: ")
	with open(file, 'r') as f:
		if (file.endswith('.c961')):
			code = f.read()
			print(interpreter(code))
			print(" ")
			print("Programm finished.")
		else:
			print("Error: Unknown file extension.")