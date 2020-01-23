from pync import Notifier
import time
import os
import random
import atexit

START = time.time()
DURATION =  3600 * 9 # 9 hours
FREQUENCY = 1800 #every 30 mins
QUOTES = ["Drinking water is like washing out your insides. The water will cleanse the system, fill you up, decrease your caloric load and improve the function of all your tissues.","If there is magic on this planet, it is contained in water.","Water is life's matter and matrix, mother and medium. There is no life without water.","In time and with water, everything changes.","I believe that water is the only drink for a wise man.","Water is the soul of the Earth.","Water is the best of all things.","Anyone who can solve the problems of water will be worthy of two Nobel prizes - one for peace and one for science.","Thousands have lived without love, not one without water.","We forget that the water cycle and the life cycle are one.","Wanna lose 1200 Calories a month? Drink a liter of ice water a day. You burn the energy just raising the water to body temp.","Whiskey is for drinking; water is for fighting over.","I fear the man who drinks water and so remembers this morning what the rest of us said last night","It's funny, I do try to maintain health. I started doing Bikram yoga which is that hothouse yoga, the 105 degrees yoga for 90 minutes. It's great, you purge out all the sweat and you're drinking water.","The health of our waters is the principle measure of how we live on the land.","Thirst drove me down to the water\nwhere I drank the moon's reflection.","The world needs water. For every bottle of wine you drink you contribute to conserving the drinking water reserves.","At the moment there are 1 in 8 people who have no access to clear drinking water, about a billion people worldwide, which can make you feel quite overwhelmed.","Water is the one substance from which the earth can conceal nothing; it sucks out its innermost secrets and brings them to our very lips.","Water is one of the most basic of all needs - we cannot live for more than a few days without it. And yet, most people take water for granted. We waste water needlessly and don't realize that clean water is a very limited resource. More than 1 billion people around the world have no access to safe, clean drinking water, and over 2.5 billion do not have adequate sanitation service. Over 2 million people die each year because of unsafe water - and most of them are children!","We think of our land and water and human resources not as static and sterile possessions but as life giving assets to be directed by wise provisions for future days.","For many of us, water simply flows from a faucet, and we think little about it beyond this point of contact. We have lost a sense of respect for the wild river, for the complex workings of a wetland, for the intricate web of life that water supports.","What makes the desert beautiful is that somewhere it hides a well.","The true practice to meditation is to sit as if you where drinking water when you are thirsty.","Water, water, everywhere, And all the boards did shrink; Water, water, everywhere, Nor any drop to drink."]

def exit_handler():
    print("Exiting pyWater")
    Notifier.remove(os.getpid())


atexit.register(exit_handler)

def main():
    while True:
        if START + DURATION < time.time():
            exit()
        quote = QUOTES[random.randint(0, len(QUOTES)-1)]
        Notifier.notify(quote, sound='default', title="Drink Water 😃", appIcon='rain.png')
        time.sleep(FREQUENCY)
        

if __name__ == '__main__':
    main()
