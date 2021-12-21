import bcolors
import discord
from discord.ext import commands
from termcolor import colored
from pprint import pprint
import datetime
import asyncio




class AuditLogs(commands.Cog):

	"""
	Audit Log Mining service: 
		Automate audit log activities

	"""

	def __init__(self, client):
		self.client = client
	
	@commands.Cog.listener()
	async def on_ready(self):
		print(colored("[+]", "green"), colored("Audit logging online ", "yellow"))

	def load_log(self, username, target, action):
		
		data_obj = {}
		data_obj["username"] = str(username)
		data_obj["target"] = str(target)	
		data_obj["action"] = str(action)
	
		return data_obj


	def load_audit_log_message(result_dict, val1, val2):

		count = 0	
		msg = "AUDIT LOG REPORT for {} LIMIT {} \n\n".format(val1, val2)
		for item in result_dict:
			if count < 15:
				msg += "__{}__  : **{}** \n".format(item, result_dict[item])
			else:
				break

			count += 1

		return msg
		
		
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

						
		audit_msg = self.load_audit_log_message(result_dict, username, log_limit)
		await ctx.send(audit_msg)

	
	@commands.command()
	async def audit_log_report_action_users(self, ctx, log_action, log_limit):
		
		result_dict = {}
		action_filter = "AuditLogAction.{}".format(log_action)
		result_dict = {}
	
		for server in self.client.guilds:
			async for entry in server.audit_logs(limit=int(log_limit)):	
				if action_filter in str(entry.action):	
					key = str(entry.user.name)
					user_filter = key in result_dict.keys()
				
					if user_filter:
						result_dict[key] += 1
					else:
						result_dict[key] = 1

		
		audit_msg = self.load_audit_log_message(result_dict, log_action, log_limit)
		await ctx.send(audit_msg)


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
