
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
