import random, logging

logging.basicConfig(level=logging.INFO)

luke_taunts = ["Just like beggar's canyon back home", "You should've bargained, that's the last mistake you'll ever make.", "You failed, your highness.", "Your overconfidence is your weakness.","You'll Find I'm Full Of Surprises.","The Force Is Strong In My Family.","Your Thoughts Betray You.", "This is not going to go the way you think","I warn you not to underestimate my powers.","Your thoughts betray you","I'm Luke Skywalker, I'm here to rescue you.","You're gravely mistaken"
]

logging.info(random.choice(luke_taunts))