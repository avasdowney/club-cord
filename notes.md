
## Metrics
Useful metrics we could add to the stats wrapper

# General stats
1. Number of members in the server
2. Number of members offline/online (Seperate counts)
	* Use 0 to represent offline, 1 to represent online


# Audit logging
Mine audit logging data (View Later)
1. Create a general report for audit logs (Done)
2. Filter audit logs by action
3. Filter audit logs by date/time
4. Filter audit logs by username/member

# New Members
Visualize server growth with filtered time frames. 
1. View new members that have joined on a weekly, monthly and yearly basis. 
2. Figure out how to get the join date of all the members

# Channels
Stats related to channels
1. Use simple text summarization technique from NLTK to get specific keywords in the channel
2. Get members that talk the most in that channel

# Reminder Service
Service for scheduling meetings/events. 

## Model
**Name**: Name of meeting/event
**Time**: Time that the meeting starts
**Duration**: How long the meeting will be
**Occurrence Time**: (Weekly, BI-Weekly, Monthly)
**User**: User that created the reminder


1. Create/Read/Update/Delete reminder model
2. Send message reminder 4 HR's before meeting
3. Store all info in a sqlite3 database
4. Have a function that checks the DB everyday and see if a meeting is occuring the day before

