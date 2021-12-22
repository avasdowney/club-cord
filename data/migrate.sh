sudo rm reminders.db
touch reminders.db
cat tables.sql | sqlite3 reminders.db
