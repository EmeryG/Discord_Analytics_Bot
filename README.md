# Discord_Analytics_Bot
Python bot that uses Discord REST API, matplotlib and MySQL.

Uses Discord REST to extract Discord user data. 

Translates the data for analysis to load into SQL for records and matplotlib for data analytic chart generation. 

Bot then sends generated data analytics charts through HTTP to Discord.

Docker is used for setting up SQL server and Python package management.

Create "bot_secret", "bot_token" and "server_id" to configure the bot with your own Discord application keys and specific server ID.

Future checklist:
- Track members that leave servers
- Change database for ability to handle multiple servers
