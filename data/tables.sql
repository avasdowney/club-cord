
CREATE TABLE reminder (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT NOT NULL,
	date_value TEXT NOT NULL, 
	duration TEXT NOT NULL
);


CREATE TABLE message (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	reminder_id INTEGER NOT NULL,
	message TEXT NOT NULL, 
	roles TEXT NOT NULL
);
