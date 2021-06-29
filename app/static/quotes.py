import random, logging

logging.basicConfig(level=logging.INFO)

luke_taunts = ["Just like beggar's canyon back home", "You should've bargained, that's the last mistake you'll ever make.", "You failed, your highness.", "Your overconfidence is your weakness.","You'll Find I'm Full Of Surprises.","The Force Is Strong In My Family.","Your Thoughts Betray You.", "This is not going to go the way you think","I warn you not to underestimate my powers.","Your thoughts betray you","I'm Luke Skywalker, I'm here to rescue you.","You're gravely mistaken"
]
leia_taunts = ["Someone has to save our skins", "Why, you stuck-up, half-witted, scruffy-looking nerf herder!", "Into the garbage chute, flyboy", "I'd just as soon kiss a wookie", "You have your moments. Not many of them, but you do have them.", "I hope you know what you're doing.", "We have powerful friends, you're going to regret this.", "May the force be with you."]

logging.info(random.choice(luke_taunts))