# Reminder Service
Service for scheduling meetings/events. 

## Data Model for Reminder
**Name**: Name of meeting/event
**Time**: Time that the meeting starts
**Duration**: How long the meeting will be
**Occurrence Time**: (Weekly, BI-Weekly, Monthly)
**User**: User that created the reminder

## Data model for message
**Reminder ID**: ID of the reminder associated with it
**Message Text**: Message that will be sent for the reminder

# Features
1. Create/Read/Update/Delete reminder model
2. Reminders are stored in a sqlite3 database with the model above
3. Check the database every day to see if a reminder matches the current day
	* Send the message at 8 AM
	* Run this task every day at 8AM
4. Attach a message for a reminder in the database
	* This is the reminder message that will be sent before the meeting
5. Add users/roles/channels to a reminder
	* Should notify users/roles/channels associated with the reminder
5. Check reactions to a reminder message

# Port Scanner
Scan web/server hosts and identify open ports

# Audit log miner
1. Create a general report for audit logs (Done)
2. Filter audit logs by action, date, time and username
3. For each user, show the audit log actions they've done
	* Do UNIQUE ORDER BY query and get counts for each action
4. Create a report that sorts users by the amount of times they've done a certain action
	* Ex. Select "created role" action, show users who've done that action the most
5. Prioritize audit actions by level of severity and how dangerous it is to use
	* Create a severity ENUM that maps each audit log with a severity level
6. Filter logs by roles
	* See what actions certain roles are doing
7. Create a vector/dictionary that shows audit actions on a daily basis
	* Use it at as possible reinforcement learning environment
	* Figure out the reward, state and actions
8. Make a feature that logs server activities to a specific channel
9. Log name changing actions
	* Use this to see if everyone changed their name to first and last


# New Members
Automate activities when new members join the server.
Visualize server growth with filtered time frames. 
1. View new members that have joined on a weekly, monthly and yearly basis. 
2. Figure out how to get the join date of all the members

# Channels
Stats related to channels
1. Use simple text summarization technique from NLTK to get specific keywords in the channel
2. Get members that talk the most in that channel

# Reminder Service




