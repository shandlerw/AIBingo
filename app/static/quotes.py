import random, logging

logging.basicConfig(level=logging.INFO)

luke_taunts = ["Just like beggar's canyon back home", "You should've bargained, that's the last mistake you'll ever make.", "You failed, your highness.", "Your overconfidence is your weakness.","You'll Find I'm Full Of Surprises.","The Force Is Strong In My Family.","Your Thoughts Betray You.", "This is not going to go the way you think","I warn you not to underestimate my powers.","Your thoughts betray you","I'm Luke Skywalker, I'm here to rescue you.","You're gravely mistaken"]

leia_taunts = ["Someone has to save our skins", "Why, you stuck-up, half-witted, scruffy-looking nerf herder!", "Into the garbage chute, flyboy", "I'd just as soon kiss a wookie", "You have your moments. Not many of them, but you do have them.", "I hope you know what you're doing.", "We have powerful friends, you're going to regret this.", "May the force be with you."]

obiwan_taunts = ["Be mindful of your thoughts, they betray you.", "The Force is what gives a Jedi his power.", "These aren't the droids you're looking for.", "The Force will be with you, always.", "If you strike me down, I shall become more powerful than you can possibly imagine.","So uncivilized","I have the high ground.", "You've taken your first step into a larger world.","Who is more foolish? The fool, or the fool who follows him?"]

yoda_taunts = ["Once you start down the dark path, forever will it dominate your destiny.","Always pass on what you have learned.","Patience you must have my young Padawan.","Powerful you have become, the dark side I sense in you.","Do or do not. There is no try.","Feel the force!","Size matters not. Look at me. Judge me by my size, do you?","Control, control, you must learn control!","Ready are you? What know you of ready?","A Jedi uses the Force for knowledge and defense, never for attack.","Adventure. Excitement. A Jedi craves not these things.","That is why you fail."]

vader_taunts = ["You don't know the power of the dark side.", "There will be no one to stop us this time.", "I find your lack of faith distrubing.","You're as clumsy as you are stupid.","This will be a day long remembered.", "I am altering the deal, pray I don't alter it any further.","Be careful not to choke on your aspirations.","You have controlled your fear. Now, release your anger.","The Emperor is not as forgiving as I am.", "All too easy.", "Join us or die.","Impressive, most impressive.", "There is no escape, don't make me destroy you.", "You are beaten, it is useless to resist.","You are unwise to lower your defenses."]

palpatine_taunts = ["Your feeble skills are no match for the power of the dark side.","You shall pay the price for your lack of vision.","Everything that has transpired has done so according to my design.","So be it... Jedi.","There is a great disturbance in the Force.","Young fool. Only now, at the end, do you understand.","You will find that it is you who are mistaken, about a great many things.","Wipe them out, all of them!","Everything is proceeding as I have foreseen.",]

mando_taunts = ["You're no good to me dead.","As you wish.","This is the way.","I can bring you in warm, or I can bring you in cold.","I like those odds.","I’m a Mandalorian. Weapons are part of my religion.","We need to talk."]

kyloren_taunts = ["I feel it again, the pull to the light.","I will finish what you started.","Don't be afraid, I feel it too.","You know I can take anything I want.","Let the past die.  Kill it if you have to.","You can't hide, not from me.","We're not done yet.","I will fulfill our destiny.","I want every gun that we have to fire on that man.","I'll show you the Dark side.","You need a teacher.  I can show you the ways of the Force.","I know what I have to do."]

logging.info(random.choice(luke_taunts))