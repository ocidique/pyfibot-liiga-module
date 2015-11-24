from __future__ import unicode_literals, print_function, division
from icalendar import Calendar
from datetime import datetime

def giev_liiga():

    announcement = "Liigageimit: "
    g = open('calendar.ics', 'rb')
    gcal = Calendar.from_ical(g.read())
    gamesToday = []
    
    for event in gcal.walk():
        if event.name == "VEVENT":
            game = event.get('summary')
            gameDate = event.get('dtstart').dt.date()
            dateToday = datetime.now().date()
 
            if gameDate == dateToday:
                gamesToday.append(game)

    g.close()

    if not gamesToday:
        print "No hockey for you!"
        return "No hockey for you!"
    else:
        separateGames = ', '.join(gamesToday)
        gamesToPrint = ''.join(separateGames)
        games = announcement + gamesToPrint
        print games
        return games

def command_liiga(bot, user, channel, args):
    if not args:
        return "Error!"
    return bot.say(channel, giev_liiga())

