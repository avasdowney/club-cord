# Reminder Service
Service for scheduling meetings/events. 

## Data Model for Reminder

| Field          | Description                              |
|----------------|------------------------------------------|
| **Name**       | Name of meeting/event                    |
| **Time**       | Time the meeting starts                  |
| **Duration**   | How long the meeting will be             |
| **Occurrence** | Choice of occurring Weekly/Daily/Monthly |
| **Username**   | User that created the meeting reminder.  |

## Data model for message

| Field            | Description                                 |
|------------------|---------------------------------------------|
| **Reminder ID**  | Name of meeting/event                       |
| **Message Text** | Time the meeting starts                     |
| **Role**         | Tag the role the reminder should be sent to |

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
# Features
1. Scan host with parameters for port ranges
2. Create "queued" scans
	* Allow multiple scans to happen (Not at the same time)
	* Store each search in a "queue" node and perform the scans in order
3. Create a function to priortize queue's that will take less time to perform a scan
	* Can use the port ranges as an indicator for how long the search will take
	* Prioritize smaller port ranges Ex. (1, 10), (1, 255), (1, 65535)

# Audit log miner
Service for dealing with audit log data
# Features
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

# Channels Service
Service to deal with channels

# Features
1. Create a channel activity report that shows which channels are most active
	* Calculate activity using datetime timeframe
2. Create bar chart for amount of messages sent by users in a channel
3. Sort users by most messages sent with channel ID as parameter
4. For each user, show/reccomend which channels they are most active in
5. For each channel, perform some NLP algorithms 
	* Text classification
	* Extracting information from text
	* Analyze sentence structure
	* Building feature based grammars
		- Understand meaning of sentences
		- Manage linguistic data
	* Build knowledge graphs
	* Entity recognition
