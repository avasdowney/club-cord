import discord
from discord.ext import commands, tasks
from datetime import datetime
from pprint import pprint
from termcolor import colored
import socket
import sys
import queue

class PortScanner(commands.Cog):
	
	def __init__(self, client):
		self.client = client
		self.q = queue.Queue()

	@commands.Cog.listener()
	async def on_ready(self):
		print(colored("[+]", "green"), colored("Port Scanner online ", "yellow"))

	# creates a scanner object
	def create_scan(self, username, hostname, startPort, endPort):
		scan_obj = {}
		scan_obj["username"] = username
		scan_obj["hostname"] = hostname
		scan_obj["start_port"] = int(startPort) # convert
		scan_obj["end_port"] = int(endPort)
		return scan_obj
	
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
	async def run_scans(self, ctx):
		# goes through and runs all scans in queue
		for scan in list(self.q.queue):
			socket.setdefaulttimeout(0.01)
			result_msg = self.scanHost(
				scan["hostname"],
				scan["start_port"], 
				scan["end_port"]
			)

			await ctx.send(result_msg)
		

	@commands.command()
	async def view_scans(self,ctx):
		print("Viewing scans .... ")
		for scan in list(self.q.queue):
			pprint(scan)

	
	@commands.command()
	async def port_scan(self, ctx, hostname, startPort, endPort):

		scan_obj = self.create_scan("testing", hostname, startPort, endPort)
		# add scan to queue
		self.q.put(scan_obj)

		msg = "Added scan to queue, results will be sent back once scan is done... "
		await ctx.send(msg)
		

def setup(client):
	client.add_cog(PortScanner(client))
