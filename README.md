# pocket-color-bot

## Description
Twitter bot to generate random webcolors alongside information about the color.

Built using Python3, [webcolors](https://github.com/ubernostrum/webcolors), [Pillow](https://github.com/python-pillow/Pillow/blob/0f44136e720cd3b2db72bdf29614897b7aa3e868/docs/index.rst), and the [Twitter API](https://developer.twitter.com/en/docs/twitter-api).

Enter the virtual environment with `source venv/bin/activate`.

Leave the virtual environment with `deactivate`.



To initialize for use:
* `git clone https://github.com/colelewis/pocket-color-bot.git && cd pocket-color-bot`
* `source venv/bin/activate`
* You will need to provide your API tokens into `twitter_secrets.py` as specified in the file.
* `python3 main.py`

Use the `--save` flag to save the image and text contents of the tweet in the project's `/data` directory.

## Demonstration

[@pocketcolorbot](https://twitter.com/pocketcolorbot)

## Notes
You will need to provide your API tokens into `twitter_secrets.py` as specified in the file.


![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/colelewis/pocket-color-bot)