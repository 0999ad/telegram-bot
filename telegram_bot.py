import requests
import re
import random
import telebot

# Define your bot token as a constant
BOT_TOKEN = 'your_bot_token_goes_here' #example bot code - 0987452:AJUwhd;loihaf3flasfhpe9KLAH

bot = telebot.TeleBot(BOT_TOKEN)

# Command handler for /start and /hello
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, """Welcome to New CTI Bot
/tor (search term)
Example: /tor credit cards

Returns first 20 results from ahmia.fi - TOR 

Created By Trin.Walks
                      """)

# Command handler for /tor and /getonions
@bot.message_handler(commands=['tor', 'getonions'])
def send_links(message):
    bot.reply_to(message, "[+] Getting Links")
    data = message.text
    newdata = data.replace('/tor', '')
    links, total_links = scrape(newdata)  # Added total_links
    bot.reply_to(message, links)
    bot.reply_to(message, f"[!] TOR is Required To Access Provided Links\nTotal links available: {total_links}")

def scrape(newdata):
    myquery = newdata

    if " " in myquery:
        myquery = myquery.replace(" ", "+")
    url = "https://ahmia.fi/search/?q={}".format(myquery)
    request = requests.get(url)
    content = request.text
    regexquery = "\w+\.onion"
    grabbed_data = re.findall(regexquery, content)

    if not grabbed_data:
        return "No links have been found. Try another search or come back later", 0  # Return 0 total links if no links are found.

    n = random.randint(1, 9999)

    filename = "sites{}.txt".format(str(n))
    print("Saving to...", filename)

    grabbed_data = list(dict.fromkeys(grabbed_data))

    with open(filename, "w+") as newfile:
        for k in grabbed_data:
            k = k + "\n"
            newfile.write(k)

    print("All the files written to a text file")

    total_links = len(grabbed_data)  # Calculate total links
    if total_links > 7:
        grabbed_data = grabbed_data[:7]  # Only show the first 7 links

    try:
        with open(filename) as input_file:
            head = [next(input_file) for _ in range(20)]
            contents = '\n'.join(map(str, head))
            print(contents)
    except StopIteration:
        contents = "No links have been found! Try another search or come back later"

    return contents, total_links  # Return contents and total_links

# Start the bot's polling loop
bot.infinity_polling()
