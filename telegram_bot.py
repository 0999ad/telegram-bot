import requests
import re, random
import telebot

BOT_TOKEN = 'your_bot_token_goes_here' #example bot code - 0987452:AJUwhd;loihaf3flasfhpe9KLAH

bot = telebot. TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, """Welcome to the TOR Dark Web OSINT links finder
/tor (search)
Example: /tor credit cards
Created By Trin.Walks
                            """)

@bot.message.handler(commands=['darkweb', 'getonions'])
def send_welcome(message):
    bot.reply_to(message, "[+] Getting Links")
    data = message.text
    newdata = data.replace('/darkweb', '')
    bot.reply_to(message, scrape(newdata))
    bot.reply_to(message, "[!] You Need TOR To Access Onion Links")

def scrape(newdata):
    myquery = newdata
    # myquery = "Croatia Index of"

    if " " in myquery:
        myquery = myquery.replace(" ", "+")
    url = "https://ahmia.fi/search/?q={}".format(myquery)
    request = requests.get(url)
    content = request.text
    regexquery = "\w+\.onion"
    gathereddata = re.findall(regexquery, content)

    n = random. randint(1, 9999)

    filename = "sites{}.txt".format(str(n))
    print("Saving to...", filename)
    gathereddata = list(dict.fromkeys(gathereddata))

    with open(filename, "w+") as _:
        print("")
    for k in gathereddata:
        with open(filename, "a") as newfile:
            k = k + "\n"
            newfile.write(k)
    print("All the files writen to a text file")
    with open(filename) as input_file:
        head = [next(input_file) for _ in range(7)]
        contents = '\n'.join(map(str, head))
        print(contents)

    return contents


bot.infinity_polling()
