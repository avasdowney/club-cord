# Audit log miner
Service for dealing with audit log data

# Features

## General Report
This is a general reporting feature that will act as main dashboard for all the audit logging actions that we've done. 

1. Shows unique counts of each audit log with a specified limit
2. Previews last 5 audit logs on the server

## User report
This will show all the most recent actions that a user has done (by searching the audit logs). 

1. Filter actions by user
2. Show unique count of all the actions that they did with a log limit as parameter

## New Members
1. Search through the audit logs and see if any new members joined
	* Find the username of the new member and send a message telling them to introduce themselves
2. Grab a report that shows stats on new members joining
	* Show membership on a monthly/weekly and yearly basis

