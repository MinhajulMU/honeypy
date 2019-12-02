
#!usr/bin/env python

##################################################################
# setup.py                                                       #
# description: for running the web server honeypot               #
# author: @shipcod3                                              #
# greetz: ROOTCON goons and baby jim trevor                      #
##################################################################

import sys, SimpleHTTPServer, SocketServer, cgi, logging
import telegram
import json
from telegram.ext import Updater, CommandHandler

chat_ids = [282504451]
chat_id = []
bot = telegram.Bot(token='920749265:AAFVpTsf8LdsrSlXSYL8e5MymABfcFfj4KI')

def start(bot, update):
#    update.message.reply_text(update.message.chat.id)
    chat_id.append(update.message.chat.id)
    update.message.reply_text("Selamat ! anda sudah terdaftar dalam bot, sekarang anda sudah mulai bisa menerima notifikasi dari kami ")
print """
  _  _                   ___
 | || |___ _ _  ___ _  _| _ \_  _
 | __ / _ \ ' \/ -_) || |  _/ || |
 |_||_\___/_||_\___|\_, |_|  \_, |
                    |__/     |__/  by @shipcod3
"""
class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        bot.send_message(282504451,'Halo Kak, ada akses baru nih')
        #print(self.headers)
        #print(self.client_address[0])
        bot.send_message(282504451,'IP Address'+self.client_address[0])

        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
#        logging.error(self.headers)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        for item in form.list:
            print(item)
            #bot.send_message(282504451,json.dumps(item))
        user = form.getvalue('user', 0)
        password = form.getvalue('password', 0)
        bot.send_message(282504451,"user yang diinput: "+ user)
        bot.send_message(282504451,"password yang diinput: "+ password)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

def usage():
    print("USAGE: python setup.py <port>")

def main(argv):
    if len(argv) < 2:
        return usage()
    updater = Updater('920749265:AAFVpTsf8LdsrSlXSYL8e5MymABfcFfj4KI')
    
    PORT = int(sys.argv[1])
    PORT2 = PORT+1
    Handler = ServerHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print "\n [***] Honeypot Web Server is running at port", PORT
    #updater.start_webhook()
    
    start_handler = CommandHandler('start',start)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(start_handler)
    httpd.serve_forever()
#    updater.idle()
    updater.start_webhook(listen="0.0.0.0",
                       port=PORT,
                       url_path="920749265:AAFVpTsf8LdsrSlXSYL8e5MymABfcFfj4KI")
    
    updater.bot.setWebhook("https://e1ee869f.ngrok.io/"+"920749265:AAFVpTsf8LdsrSlXSYL8e5MymABfcFfj4KI")
    updater.idle()
    


if __name__ == "__main__":
    try:
        main(sys.argv)
        
    except KeyboardInterrupt:
        print "\n HoneyPy has been stopped :("
        pass
