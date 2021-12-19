import discord
from discord.ext import commands, tasks
from datetime import datetime, time, timedelta, date
import calendar
import json
import sqlite3
import asyncio
import threading
import time

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
	async def attach_message(self, ctx, reminder_id, message, roles):
	
		db = sqlite3.connect("data/reminders.db")
		query = "INSERT INTO message (reminder_id, message, roles) values(?,?,?);"

		values = (
			reminder_id,
			message, 
			roles
		)
	
		try:
			cur = db.cursor()
			cur.execute(query, values)
			db.commit()
			print("Added message to reminder: ")	
			await ctx.send("Added message to reminder {}: ".format(reminder_id))
	
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
	async def view_reminder_message(self, ctx, reminder_id):
	
		db = sqlite3.connect("data/reminders.db")
		query = "SELECT * FROM message where reminder_id=?;"
	
		try:
			cur = db.cursor()
			cur.execute(query, (reminder_id))
			value = cur.fetchone()

			msg = "**MESSAGE REMINDER:**@{}\n\n".format(value[3])
			data = "MESSAGE:  *{}* \n\n".format(value[2])
			msg += data
			await ctx.send(msg)

		except Exception as e:
			print("Error viewing reminders: {} ".format(e))


	
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
	

	# Task to check the DB for reminders
	async def check_db(self, ctx):

		while True:
			db = sqlite3.connect("data/reminders.db")
			query = "SELECT * FROM reminder;"

			now = datetime.now()
			today = date.today()
			current_time = now.strftime("%H:%M:%S")
			week_day = calendar.day_name[today.weekday()]

			print("Current time: {} ".format(current_time))
			print("Weekday: {} ".format(week_day))

			try:
				cur = db.cursor()
				cur.execute(query)
				for i in cur:
					# Check if today matches weekday in db
					if week_day != i[2]:
						# send reminder message			
						reminder_query = "SELECT * FROM message where reminder_id=?;"
						second_cur = db.cursor()
						second_cur.execute(query, (reminder_id))
						for j in second_cur:
							await ctx.send((j[1]))
			except Exception as e:
				print("Error checking db: {}".format(e))

			db.close()
			await asyncio.sleep(10)


	@commands.command()
	async def schedule_db(self, ctx):
	
		# start task
		self.client.loop.create_task(self.check_db(ctx))
	
		await ctx.send("Scheduled task: ")


def setup(client):
	client.add_cog(Reminders(client))
