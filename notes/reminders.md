
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


## Help function
1. Send a help message that shows how to use all the commands in the service

## Create reminder
This will create a meeting reminder in the service database. We'll just use sqlite3 as a simple start. No need to use anything fancy yet. The reminder will just hold information about the date and title of the meeting. We need validation if the reminder fails or if not enough arguments are passed. 

1. Reminder will be stored in sqlite3 with data model above
2. Check if all the proper arguments are supplied in the request
	* Check for title
	* Validate the date format
	* Check that the duration argument has been passed
	* Check role of the user creating a reminder (This feature is for E-board only)
3. Alert user if the reminder is successfully created


## View reminder
This is the command for viewing all the reminders that have been created. It displays sorted by date and upcoming events. 

1. View reminders in the database
2. Reminders should be sorted by date, view upcoming events
3. If we have "too many" reminders
	* Create an argument for limiting results to a certain number


## Delete reminder
1. Specify reminder id and delete the object
2. Delete the reminder from the database
3. Alert user if reminder delete was successful or not

## Update reminder
1. Specify reminder id that we want to update
2. Specify fields that we want to change
3. Commit changes to the database

## Attach Message
This feature is for attaching a message to a reminder from the database. The message is what will be sent when the date is closer to the reminder time. The message has the roles that are tagged and the message content. 

1. Create message model for DB. Link reminder ID to message model
2. Attach message to reminder using reminder id as parameter
3. Create message using message data model above
4. Attach role to message (Role will contain the users that the message will be sent to)
5. Commit changes to the database

## View reminder message
This is for previewing or viewing the message for a reminder and what will be sent out prior to the date. 

1. Pass in reminder id and send message back to user
2. This shows the current reminder message set for the meeting


## Scheduler for reminders in the database
This is going to be a function that checks the database everyday to see if any reminders need to be sent out. It will check if the date for the reminders matches the current day/hour and then send the reminder message to the discord server. 








