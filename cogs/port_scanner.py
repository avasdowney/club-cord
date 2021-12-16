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

	
	def scanHost(self, ip, startPort, endPort):
		""" Starts a TCP scan on a given IP address """

		# Begin TCP scan on host
		results = self.tcp_scan(ip, startPort, endPort)
		return results

	
	def scanRange(self, network, startPort, endPort):
		""" Starts a TCP scan on a given IP address range """

		# Iterate over a range of host IP addresses and scan each target
		for host in range(1, 255):
			ip = network + '.' + str(host)
			self.tcp_scan(ip, startPort, endPort)


	def tcp_scan(self, ip, startPort, endPort):
		""" Creates a TCP socket and attempts to connect via supplied ports """
		msg = "**PORT SCANNER RESULTS** for *{}* \n\n".format(ip)
		for port in range(startPort, endPort + 1):
			try:
				# Create a new socket
				tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
				# Print if the port is open
				if not tcp.connect_ex((ip, port)):
					value = '*OPEN*:  __{}/TCP__ \n'.format(port)
					msg += value
					tcp.close()
				
			except Exception:
				pass

		return msg
	
	
	@commands.command()
	async def port_scan(self,ctx, hostname: str, startPort, endPort):
		socket.setdefaulttimeout(0.01)
		results = self.scanHost(hostname, int(startPort), int(endPort))
		await ctx.send(results)

def setup(client):
	client.add_cog(PortScanner(client))
