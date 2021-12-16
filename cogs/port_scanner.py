import discord
from discord.ext import commands
import socket
from datetime import datetime
import sys

class PortScanner(commands.Cog):
	
	def __init__(self, client):
		self.client = client

	
	@commands.Cog.listener()
	async def on_ready(self):
		print("Port scanning service is online... ")

	
	@commands.command()
	async def start_scan(self,ctx, hostname: str):
		target = socket.gethostbyname(hostname)
		print("HOSTNAME: {} ".format(hostname))
		try:
			print("starting scan ")
			for port in range(1, 65535):
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				con = s.connect((target, port))
				if con:
					print("{} is open ".format(port))
				s.close()

		except socket.gaierror:
			print("\n Hostname Could Not Be Resolved !!!!")
		except socket.error:
			print("\ Server not responding !!!!")


def setup(client):
	client.add_cog(PortScanner(client))
