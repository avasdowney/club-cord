import discord
from discord.ext import commands
import json
import sqlite3

class Reminders(commands.Cog):
	
	def __init__(self, client):
		self.client = client
	
	@commands.Cog.listener()
	async def on_ready(self):
		print("Reminders service is online... ")

	@commands.command()
	async def create_reminder(self, ctx, title, m_time, occurrence, duration):
	
		db = sqlite3.connect("data/reminders.db")
		query = "INSERT INTO reminder (title, time, duration, occurrence) values(?,?,?,?);"

		values = (
			title,
			m_time,
			occurrence,
			duration
		)

		try:
			cur = db.cursor()
			cur.execute(query, values)
			db.commit()
			print("Added reminder to database: ")
			await ctx.send("Added reminder to database: ")
		except Exception as e:
			print("Error in create operation: {} ".format(e))
			db.rollback()
				
		db.close()
	

		
	


def setup(client):
	client.add_cog(Reminders(client))
