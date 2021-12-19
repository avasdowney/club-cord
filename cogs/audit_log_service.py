
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
	async def filter_log_by_user(self, ctx, username, log_limit):
		
		result_dict = {}
		result_dict[username] = []

		for server in self.client.guilds:
			async for entry in server.audit_logs(limit=int(log_limit)):
				if username in str(entry.user.name):

					data_obj = {}
					data_obj["username"] = str(entry.user.name)
					data_obj["target"] = str(entry.target)	
					data_obj["action"] = str(entry.action)
					result_dict[username].append(data_obj)

		pprint(result_dict)


	@commands.command()
	async def filter_log_by_action(self, ctx, log_action, log_limit):
		
		result_dict = {}
		action_filter = "AuditLogAction.{}".format(log_action)
		result_dict[action_filter] = []

		for server in self.client.guilds:
			async for entry in server.audit_logs(limit=int(log_limit)):
				if action_filter in str(entry.action):

					data_obj = {}
					data_obj["username"] = str(entry.user.name)
					data_obj["target"] = str(entry.target)
					data_obj["action"] = str(entry.action)
					result_dict[action_filter].append(data_obj)

		pprint(result_dict)

	
	@commands.command()
	async def audit_log_report_user(self, ctx, username, log_limit):
		
		count = 0
		action_count = {}
		
		for server in self.client.guilds:
			async for entry in server.audit_logs(limit=int(log_limit)):
				action_filter = str(entry.action) not in action_count.keys()
				user_filter = username in str(entry.user.name)

				if user_filter:
					if action_filter:
						action_count[str(entry.action)] = 1 
					else:
						action_count[str(entry.action)] += 1

				
		msg = "AUDIT LOG REPORT for {} LIMIT {} \n\n".format(username, log_limit)
		for item in action_count:
			msg += "__{}__  : **{}** \n".format(item, action_count[item])

		await ctx.send(msg)
		

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
