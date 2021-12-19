
import discord
from discord.ext import commands
from pprint import pprint
import datetime


class AuditLogs(commands.Cog):
	"""
	Audit Log Mining service: 
		Automate audit log activities

	"""

	def __init__(self, client):
		self.client = client
	
	@commands.Cog.listener()
	async def on_ready(self):
		print("Audit Log service is online ")

	
	@commands.command()
	async def audit_log_report(self, ctx):

		count = 0
		action_count = {}
		last_5 = []	
		for server in self.client.guilds:
			async for entry in server.audit_logs(limit=100):
				if str(entry.action) not in action_count.keys():
					action_count[str(entry.action)] = 1
				else:	
					action_count[str(entry.action)] += 1
				
				if count < 3:
					value = '*{}*  did  __{}__ '.format(entry.user.name, entry.action)
					last_5.append(value)

				count += 1

		msg = "AUDIT LOG REPORT, count of audit actions done. LIMIT 100\n\n"
		for item in action_count:
			msg += "__{}__  : **{}** \n".format(item, action_count[item])

		msg += " \n **Most recent actions:** \n"
		for item in last_5:
			msg += item + "\n"
		
		await ctx.send(msg)


def setup(client):
	client.add_cog(AuditLogs(client))
