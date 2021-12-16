# club-cord
A discord bot to freelance to student organizations that want statistics on their discord servers. 

## Commands
| command | what it does |
|---------|--------------|
| `$help` | displays all commands for the bot |
| `$hello`| prints out a hello message |
| `$channels` | prints out text channels |
| `$users` | prints out the people in the discords |
| `$channelmessage` | displays a graph of how many messages people have posted in the general  channel |
| `$cheer` | prints out a cheery message |

## Want to contribute?
1. Fork the repo and clone locally. You can follow [this guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) using [gitbash](https://git-scm.com/downloads) if you do not know how to do so.
1. Install all required packages using `pip install -r requirements.txt` in a terminal such as gitbash
1. In the terminal, run `python3 auth-token.py` which will allow you to test your commands in the devops channel of the discord server. Press ctrl c or cmnd c to exit when you are done testing.
1. Push your changes to your repo, then submit a pull request to the main repo. Here is a good [guide](https://stackoverflow.com/questions/7036193/how-to-push-my-changes-back-to-the-source-code-in-git) on what to do if you do not know. As long as there are no issues, your change will become a part of club-cord!


## Metrics
Useful metrics we could add to the stats wrapper

# General stats
1. Number of members in the server
2. Number of members offline/online (Seperate counts)
	* for the state vector

# Message stats
Get a birds eye view of all the messages that are being sent on certain time intervals
## Tasks
1. Daily, Weekly and monthly counts for messages in each channel. (Done)
2. Use the stats to see which channels are dead/need to be deleted
3. Possible RL implementation with reccomendations to drive membership activity. 

# Audit logging
Mine audit logging data (View Later)
1. Create a filter for certain logs (Done)

# New Members
Visualize server growth with filtered time frames. 
1. View new members that have joined on a weekly, monthly and yearly basis. 
2. Figure out how to get the join date of all the members

# Channels
Stats related to channels
2. Use simple text summarization technique from NLTK to get specific keywords in the channel
3. Get members that talk the most in that channel




