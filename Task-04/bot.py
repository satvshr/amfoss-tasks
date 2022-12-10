
import os
import telebot
import requests
import json
import csv

# TODO: 1.1 Get your environment variables 
yourkey = 'c98889f'
bot_id = '5535013653:AAFdxG3aLevRu-0TtNXhdvbS2_OqJlz5X7k'

bot = telebot.TeleBot(bot_id)
botRunning = True
@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')

@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')



@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    global botRunning
    botRunning = True
    name_id = message.text
    z=name_id.lstrip("/movie ")
    bot.reply_to(message, 'Getting movie info...')
    # movURL="http://www.omdbapi.com/apikey="+yourkey+"&/?s="+z
    movURL = f'http://www.omdbapi.com/?apikey={yourkey}&t={z}'
    response = requests.get(movURL)
    global json62
    json62 = response.json()  
    a = "Movie Name:"+json62["Title"]+"\n"+"Movie release date:"+json62["Year"]+"\n"+"Released:"+json62["Released"]+"\n"+"Movie imdbRating:"+json62["imdbRating"]+"\n"   
    bot.send_photo(message.chat.id, json62["Poster"], caption=a)


    # TODO: 1.2 Get movie information from the API
    # TODO: 1.3 Show the movie information in the chat window
    # TODO: 2.1 Create a CSV file and dump the movie information in it

@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    #TODO: 2.2 Send downlodable CSV file to telegram chat
    fields = ["Movie", "Year", "Released", "imdbRating"]
    row = [json62["Title"], json62["Year"], json62["Released"], json62["imdbRating"]]
    filename = "movie.csv"
    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerow(row)

    with open(filename,"r") as readfile:


        bot.send_document(message.chat.id, readfile)

  #  with open(filename, 'r+') as readfile:
   #     csvreader = csv.reader(readfile)
    #    csvwriter = csv.writer(readfile)
     #   for i in csvreader: 
       #     csvwriter.writerow(i)
        #    print(i)
        #bot.send_document(message.chat.id, readfile)

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')

bot.infinity_polling()
