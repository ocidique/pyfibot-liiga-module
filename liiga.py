import sopel.module

from icalendar import Calendar
from datetime import datetime

@sopel.module.commands('liiga', 'hokii')

def giev_liiga(bot, trigger):

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
        noGames = "No hockey for you!"
        bot.say(noGames)
    else:
        separateGames = ', '.join(gamesToday)
        gamesToPrint = ''.join(separateGames)
        games = announcement + gamesToPrint
        bot.say(games)