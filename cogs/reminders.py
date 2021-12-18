import discord
from discord.ext import commands
from datetime import datetime
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

	
	async def check_db(self):

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
                if week_day == i[2]:
                    await self.client.send_message("Test?")
        except Exception as e:
            print("Error checking db: {}".format(e))


    @commands.command()
    async def schedule_db(self, ctx):

        schedule.every().day.at("08:00:00").do(self.check_db)
        await ctx.send("Schedule DB Check: ")
        while True:
            schedule.run_pending()
            time.sleep(1)


    # prototype function for testing on shorter intervals
    @commands.command()
    async def schedule_test(self, ctx):

        schedule.every().minute.at(":17").do(check_db)
        await ctx.send("Schedule DB Check: ")
        while True:
            schedule.run_pending()
            time.sleep(1)
	
		


def setup(client):
	client.add_cog(Reminders(client))
