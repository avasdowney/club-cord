# club-cord
This a discord bot is for people that run clubs/organizations and need a tool to keep their membership organized. This bot allows you to create reminder messages, generate reports for audit logs, channels and users. As the bot continues to grow, I hope to implement a analytics service for data visualizations and reinforcement learning. The discord server can be viewed as a environment for an agent to learn and optimize/perform desired actions to increase membership on the server. 

## Help and how the bot works
The bot is divided into multiple services. There is a designated service for "reminders", "Audit log mining" and "Channel data mining". 


### Reminders service
Service for creating messages that can be sent at certain times.

| command | what it does |
|---------|--------------|
| `!create_reminder <Meeting Title> <Day> <Time> <Occurence> <Duration>` | Creates a reminder for the server |
| `!view_reminders`| Views all the reminders in the database |
| `!attach_message <Reminder_ID> <Message Content>` | Attaches a message to the reminder using the reminder id as a param |
| `!view_reminder_message <Reminder_ID>` | Views the preview message for the reminder using the reminder id |
| `!delete_reminder <Reminder_ID>` | Deletes a reminder in the database |


### Audit log service
Service for mining audit logs and detect abnormalities in the server. 

| command | what it does |
|---------|--------------|
| `!audit_log_report_user <username> <log_limit>` | Shows a report of all the audit logs from a users, can limit the results |
| `!audit_log_report_action_users <log_action> <log_limit>`| Shows a general report of all the audit logs done by users |
| `!audit_log_report` | General audit log report for the whole server. |


### Channel mining service

| command | what it does |
|---------|--------------|
| `!channelstats` | displays a graph of how many messages people have posted in the general channel  |
| `!channel_actvity_report`| Creates a general report of the channel activity for the server. |


### Port Scanner
Service for finding open ports on IPS and Domains. 

| command | what it does |
|---------|--------------|
| `!port_scan  <HOST> <START_PORT> <END_PORT>` | performs port scan and returns result of open ports |

## Getting started
If you want to deploy the bot on your server, follow the instructions below. 

1. Start by creating a file called "credentials.conf" and paste in the following. You can retrieve the bot token by asking an E-board member or contact shsingh@hartford.edu. 

```

[clubcord]

# note -- do not use any quotes...

#
# api access id - ENTER API ACCESS ID
#
bot_token = <TOKEN GOES HERE>

```

Then save the file (MAKE SURE it's called credentials.conf)


## Want to contribute?
1. Fork the repo and clone locally. You can follow [this guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) using [gitbash](https://git-scm.com/downloads) if you do not know how to do so.
2. Install all required packages using `pip install -r requirements.txt` in a terminal such as gitbash
3. In the terminal, run `python3 bot.py` which will allow you to test your commands in the devops channel of the discord server. Press ctrl c or cmnd c to exit when you are done testing.
4. Push your changes to your repo, then submit a pull request to the main repo. Here is a good [guide](https://stackoverflow.com/questions/7036193/how-to-push-my-changes-back-to-the-source-code-in-git) on what to do if you do not know. As long as there are no issues, your change will become a part of club-cord!
5. Read through the notes folder to understand how the code was created if you want to add functions to the existing services. 





