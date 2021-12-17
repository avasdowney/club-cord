from table2ascii import table2ascii 
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
	async def create_reminder(self, ctx, title, day, m_time, occurrence, duration):
	
		db = sqlite3.connect("data/reminders.db")
		query = "INSERT INTO reminder (title, day, time, duration, occurrence) values(?,?,?,?,?);"

		values = (
			title,
			day, 
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

	
	@commands.command()
	async def view_reminders(self, ctx):
	
		db = sqlite3.connect("data/reminders.db")
		query = "SELECT * FROM reminder;"

		msg = "**SERVER REMINDERS** \n\n"
		try:
			cur = db.cursor()
			cur.execute(query)
			for i in cur:
				r_id = i[0]
				name = i[1]
				day = i[2]
				r_time = i[3] 
				occurrence = i[4]
				duration = i[5]
				values = f" **{r_id}** :  {name} : {day} : {r_time} : {occurrence} : {duration} \n"
				msg += values
				
		except Exception as e:
			print("Error viewing reminders: {} ".format(e))


		await ctx.send(msg)

	
	@commands.command()
	async def delete_reminders(self, ctx, reminder_id):
	
		db = sqlite3.connect("data/reminders.db")
		query = "DELETE FROM reminder where id=?;"
	
		try:
			cur = db.cursor()
			cur.execute(query, (reminder_id))
			db.commit()
			await ctx.send("Reminder deleted {} ".format(reminder_id))
		except Exception as e:
			print("Error deleting reminder: {}".format(e))
	
		


def setup(client):
	client.add_cog(Reminders(client))
