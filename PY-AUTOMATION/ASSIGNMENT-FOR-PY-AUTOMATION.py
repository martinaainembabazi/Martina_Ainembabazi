
import requests
import time

# Telegram Bot credentials
TELEGRAM_BOT_TOKEN = '8166810170:AAEuxN6K1HM95pQuK-PzZ-wRSud-wEdbIkE'
TELEGRAM_CHANNEL = '@MumbleswithMartina' 

messages = [
    "Monday: Did you know Beyoncé has won 32 Grammy Awards, the most in history? #Beyonce #MondayMotivation",
    "Tuesday: Tom Hanks is known for his kindness both on and off screen. What's your favorite Tom Hanks movie? #TomHanks #TuesdayTrivia",
    "Wednesday: Oprah Winfrey went from humble beginnings to becoming a media mogul and philanthropist. #Oprah #WisdomWednesday",
    "Thursday: Dwayne 'The Rock' Johnson started as a wrestler before becoming a Hollywood superstar! #TheRock #ThursdayThoughts",
    "Friday: Taylor Swift is the first artist to claim all top 10 spots on the Billboard Hot 100 in a single week! #TaylorSwift #FunFactFriday",
    "Saturday: Leonardo DiCaprio is not just an actor but also a passionate environmentalist. #LeonardoDiCaprio #SustainableSaturday",
    "Sunday: Zendaya made history as the youngest actress to win an Emmy for Outstanding Lead Actress in a Drama Series. #Zendaya #SundaySpotlight"
]

def post_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHANNEL,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response.json()

# Post each message with a 24-hour interval (for demo, use shorter interval)
for msg in messages:
    result = post_to_telegram(msg)
    print(f"Posted: {msg} | Result: {result}")
    time.sleep(86400)  