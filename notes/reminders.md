
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
1. Create reminder using the data model above. All the fields are required
2. Store reminder (with model) in sqlite3 database
3. Alert user when the reminder is created
4. Alert user if the reminder creation failed

## View reminder
1. Send back reminders from db in chat

## Delete reminder
1. Specify reminder id and delete the object
2. Delete the reminder from the database
3. Alert user if reminder delete was successful or not

## Update reminder
1. Specify reminder id that we want to update
2. Specify fields that we want to change
3. Commit changes to the database

## Attach Message
1. Create message model for DB. Link reminder ID to message model
2. Attach message to reminder using reminder id as parameter
3. Create message using message data model above
4. Attach role to message (Role will contain the users that the message will be sent to)
5. Commit changes to the database

## View reminder message
1. Pass in reminder id and send message back to user
