import discord
from discord.ext import commands, tasks
from datetime import datetime, time, timedelta, date
from termcolor import colored
import calendar
import json
import sqlite3
import asyncio
import threading
import time

class Reminders(commands.Cog):
	
	def __init__(self, client):
		self.client = client
		# start the scheduler routine
		self.scheduler().start()
	
	@commands.Cog.listener()
	async def on_ready(self):
		print(colored("[+]", "green"), colored("Reminders online ", "yellow"))

	
	def to_date_val(self, date_string):
		date_s = date_string.split(":")	
		db_date = datetime (
			int(date_s[0]), 
			int(date_s[1]), 
			int(date_s[2]), 
			int(date_s[3]),
			int(date_s[4])
		)
		return db_date

		
	@commands.command()
	async def create_reminder(self, ctx, title, date_value, duration):

		# convert date time format

		db = sqlite3.connect("data/reminders.db")
		query = "INSERT INTO reminder (title, date_value, duration) values(?,?,?);"

		values = (
			title,
			date_value, 
			duration
		)

		try:
			cur = db.cursor()
			cur.execute(query, values)
			db.commit()
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
				title = i[1]
				date_value = i[2]
				duration = i[3] 
				values = f" **{r_id}** :  {title} : {date_value} : {duration} \n"
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
			data = "**{}**\n\n".format(value[2])
			msg += data
			await ctx.send(msg)

		except Exception as e:
			print("Error viewing reminders: {} ".format(e))


	
	@commands.command()
	async def delete_reminder(self, ctx, reminder_id):
	
		db = sqlite3.connect("data/reminders.db")
		query = "DELETE FROM reminder where id=?;"
	
		try:
			cur = db.cursor()
			cur.execute(query, (reminder_id))
			db.commit()
			await ctx.send("Reminder deleted {} ".format(reminder_id))
		except Exception as e:
			print("Error deleting reminder: {}".format(e))

	
	def get_reminder_message(self, reminder_id):

		msg = ""		
		db = sqlite3.connect("data/reminders.db")
		query = "SELECT * FROM message where reminder_id=?;"
	
		try:
			cur = db.cursor()
			cur.execute(query, (reminder_id,))
			value = cur.fetchone()
			# build message template
			msg = "**MESSAGE REMINDER:**@{}\n\n".format(value[3])
			data = "**{}**\n\n".format(value[2])
			msg += data

		except Exception as e:
			print("Error viewing reminders: {} ".format(e))

		return msg


	@tasks.loop(seconds=10.0)
	async def scheduler(self, ctx):
	
		db = sqlite3.connect("data/reminders.db")
		query = "SELECT * FROM reminder;"
		curr_time = datetime.now()

		try:
			cur = db.cursor()
			cur.execute(query)
			print("Current time: ", curr_time)
			for item in cur:
				test = self.get_reminder_message(item[0])
				# reminder message for each object
				# get time delta difference
				db_date = self.to_date_val(item[2])
				time_delta = curr_time-db_date
				print("Date in DB: " , db_date)
				print("Time delta: ", time_delta)
				# if time difference is less than 6 hours, send reminder
				if time_delta < timedelta(0,0,0,0,0,8):
					await ctx.send(test)
					

	
		except Exception as e:
			print("Something went wrong: {} ".format(e))




def setup(client):
	client.add_cog(Reminders(client))
