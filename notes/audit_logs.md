# Audit log miner
Service for dealing with audit log data

# Features
1. Create a general report for audit logs (Done)
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
