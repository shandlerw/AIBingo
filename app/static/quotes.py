import random, logging

logging.basicConfig(level=logging.DEBUG)

luke_taunts = ["just like beggar's canyon back home", "you should've bargained, that's the last mistake you'll ever make.", "You failed, your highness.", "Your overconfidence is your weakness.",]

logging.info(random.choice(luke_taunts))