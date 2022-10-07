# pyvo-bot

A bot 🤖 which reminds people that the [Pyvo](https://pyvo.cz) meetup 🍻 is coming! 

## Usage

Currently, the bot supports only [Telegram](https://telegram.org/) and can be found at https://t.me/pyvo_bot. The bot runs once per day here using the [CircleCI build](https://circleci.com/gh/honzajavorek/pyvo_bot). It loads iCalendar feed of Pyvo Praha and checks when is the next meetup. If it's about to be soon, it notifies the [Pyvo Praha](https://t.me/pyvopraha) Telegram channel.

## Development

Initial setup:
```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

Run the code:
```bash
python3 main.py 
```

## To Do

* refactor code (functions could be more decoupled)
* write tests

Contributions are welcomed. 

## Credits

Inspired by [honzajavorek/pyvo_bot](https://github.com/honzajavorek/pyvo_bot).

## License

[MIT](LICENSE)