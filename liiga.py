from icalendar import Calendar
from datetime import datetime

def giev_liigai():

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
  return "No hockey for you!"
 else:
  separateGames = ', '.join(gamesToday)
  gamesToPrint = ''.join(separateGames)
  games = announcement + gamesToPrint
  return games

def command_liiga(bot, user, channel, args):
 return bot.say(channel, giev_liiga())
