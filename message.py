import matplotlib.pyplot as plt
import numpy as np
import random

class MessageMiner:

	def __init__(self, set_messages):
		self.messages = set_messages

	# this just ranks the users that have sent the most messages in a channel
	def generate_message_stats(self):
		message_dict = {}
		for item in self.messages:
			if item.author.name in message_dict:
				message_dict[item.author.name] += 1
			else:
				message_dict[item.author.name] = 1

		return message_dict

	def generate_stats_chart(self, chart_dict):
		id_test = random.randint(1, 1000)
		x = [] 
		y = [] 
		for item in chart_dict.keys():
			x.append(item)
			y.append(chart_dict[item])

		#print(x)
		#print(y)	
		plt.figure(figsize=(15, 15))	
		plt.barh(x,y)
		plt.savefig('test.png')	
		
		
		
				

		
