# Space Telegram

The program downloads photos on specified dates from the resources of Spacex and Nasa, and then publishes them in the telegram channel.

### Software environment and installation:

Python3 should already be installed.

### Program installation:

Download the code: [https://github.com/VAChess777/Lesson4-web-servises-API-Devman](https://github.com/VAChess777/Lesson4-web-servises-API-Devman), or clone the `git` repository to a local folder:
```
git clone https://github.com/VAChess777/Lesson4-web-servises-API-Devman.git
```

### Installing dependencies:
 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```bach
pip install -r requirements.txt
```

### About environment variables:

For the program to work, you will need `API tokens`, which you will then place in the 
environment variables.  The values of which you will put in the `.env` file.

For the work of the program `fetch_nasa_epic_picture.py`, you will need an `API token` from the resource
by the link [https://api.nasa.gov/#epic](https://api.nasa.gov/#epic). 

When you receive the token, put its value in the `.env` file.
For example: 'NASA_API_KEY_EPIC'='zwtGhK6qmLM...........'.

Then put this value in an environment variable in the program.
For example: nasa_api_key_epic = os.environ['NASA_API_KEY_EPIC'].

For the work of the program `fetch_nasa_astronomy_image_day.py`, you will need an `API token` from the resource
by the link [https://api.nasa.gov/](https://api.nasa.gov/).

When you receive the token, put its value in the `.env` file.
For example: 'NASA_API_KEY'='zwtGhK6qmLM...........'.

Then put this value in an environment variable in the program.
For example: nasa_api_key_epic = os.environ['NASA_API_KEY'].

For the work of the program `fetch_nasa_astronomy_image_day.py`, you will need an `API token` from `@botfather`
bot in `telegram`. You will need to open your telegram channel, and get the `Chat ID` of this channel.
The `Chat ID` of the channel is a link to it, for example: `@dvmn_flood`.

When you receive the token, put its value in the `.env` file.
For example: 'TELEGRAM_BOT_TOKEN'='zwtGhK6qmLM...........'.
And put the value `Chat ID` in the `.env` file.
For example: 'TELEGRAM_CHAT_ID'=`@dvmn_flood`.

Then put this value in an environment variables in the program.
For example: 
'TELEGRAM_BOT_TOKEN'='78536960203:nYNc41OAe..........'.
'TELEGRAM_CHAT_ID'='@dvmn_flood'.

To use all of the above environment variables in programs, use the `load_dotenv()` module.

### How to run the program:

Run the script ```fetch_spacex_launch_images.py``` with the command:
```bach
$ python fetch_spacex_launch_images.py {id}
'Where id - is the flight_number of the launch of interest'
```
Run the script ```fetch_nasa_epic_picture.py``` with the command:
```bach
$ python fetch_nasa_epic_picture.py -d(--date) {YYYY-mm-dd}
'Where YYYY-mm-dd - is the start date for the download epic image day from NASA. '
'if you do not enter -s(--start_date), then default = today'
```
Run the script ```fetch_nasa_astronomy_image_day.py``` with the command:
```bach
$ python fetch_nasa_astronomy_image_day.py -s(--start_date) {YYYY-mm-dd}
'Where YYYY-mm-dd - is the start date for the download astronomy image day from NASA. '
'if you do not enter -s(--start_date), then default = today'
```
Run the script ```images_nasa_telegram_bot.py``` with the command:
```bach
$ python images_nasa_telegram_bot.py -t(--time) {value in seconds(at least 15 seconds)}
'Where {value in seconds} this is the value in seconds of the frequency '
'of sending images to the channel by the bot'
' If you do not enter, then the default value is 14400 seconds(4 hours) '
```

### How the program works:

The program consists of 4 scripts:

```fetch_spacex_launch_images.py``` - 'The program downloads photos of Spacex launches by launch number (id).'
```fetch_nasa_epic_picture.py``` - 'The program downloads an epic image of the Earth of the day from a NASA server.'
```fetch_nasa_astronomy_image_day.py``` -  'The program downloads astronomical images of the day from the NASA server.'
```images_nasa_telegram_bot.py``` - 'The program edits the images to the required size and sends the images to the telegram channel.'
            
### Features works of the program:

The `fetch_spacex_launch_images.py` program contains the functions:

* The `get_pictures_latest_launch` function - checks and downloads photos from the last launch from the SpaceX server.
* The `get_pictures_by_launch_id` function - checks and downloads photos from the SpaceX server for the date.
* The `create_parser` function - parser function.
* The `def main():` main function.

The `fetch_nasa_epic_picture.py` program contains the functions:

* The `get_epic_picture_numbers` function - gets the numbers of the required pictures from the server response.
* The `get_epic_picture_urls` function - gets the necessary links to photos based on picture numbers.
* The `download_epic_pictures` function - downloads images from the NASA server.
* The `create_parser` function - parser function.
* The `def main():` main function.

The `fetch_nasa_astronomy_image_day.py` program contains the functions:

* The `get_astronomy_pictures_day` function - downloads images from the NASA server on dates of interest.
* The `create_parser` function - parser function.
* The `def main():` main function.

The `images_nasa_telegram_bot.py` program contains the functions:

* The `get_all_pictures` function - gets all downloaded images from directories using the above scripts.
* The `change_size_pictures_for_telegram` function - changes the size of the images to suitable for placement in the telegram.
* The `create_parser` function - parser function.
* The `def main():` main function.

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).