# Eco Discord Lazy Consensus Bot

A Discord bot that helps communities make decisions by implementing the [Lazy Consensus](https://community.apache.org/committers/lazyConsensus.html) decision-making process. It allows users to submit grant proposals and have them approved if there are no objections after a certain period of time. This approach is used by open source projects such as Apache Foundation. 

The bot is developed specifically for [Eco](https://eco.org/) Discord community. You can [join](http://discord.eco.org/) to see it in action.

To improve sustainability, the bot uses PM2. If the script or system crashes, PM2 will restore the execution and any pending proposals will be recovered from the database, preserving the timer.

## Getting Started
These instructions will get you a copy of the project up and running on your machine.

1. Clone the project and cd into it:
```
git clone https://github.com/nisnevich/eco-discord-lazy-consensus-bot

cd eco-discord-lazy-consensus-bot
```

2. Create token file with your bot's [token](https://discord.com/developers/applications) integrated with your server:

```
echo <TOKEN> > token

chmod 600 token # You should make it only readable by you
```

3. Run startup.sh to install dependencies and start the project.
```
./startup.sh # Made with Debian-based systems in mind
```

4. Use bot from Discord:
- `!grant_proposal <mention> <amount> [description]`: Submit a grant proposal. The proposal will be approved after GRANT_PROPOSAL_TIMER_SECONDS unless a L3 member reacts with a :x: emoji to the original message or the confirmation message.

5. To stop the bot, use shutdown.sh.
```
./shutdown.sh
```

### Dependencies:
- [Node.js](https://nodejs.org)
- [npm](https://www.npmjs.com)
- [PM2](https://pm2.io)
- [Python 3.6](https://www.python.org/downloads/release/python-360/) or higher
- [sqlite3](https://www.sqlite.org)

## Contributing
Contributions are welcome! Feel free to create pull requests or reach out. Also you can [buy me a coffee](https://www.buymeacoffee.com/a.nisnevich).
