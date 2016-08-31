import random

SPOCK_QUOTES = ["Live long and prosper.",
                "I have been and ever shall be your friend.",
                "I am Spock.",
                "If you eliminate the impossible, whatever remains, however improbable, must be the truth.",
                "It was logical to cultivate multiple options.",
                "...if crew morale is better served by my roaming the halls weeping, I will gladly defer to your medical expertise.",
                "What if I told you that your transwarp theory was correct, that is is indeed possible to beam onto a ship that is traveling at warp speed?",
                "I will be back",
                "I have no comment on the matter.",
                "I am as conflicted as I once was as a child.",
                "If you are presuming that these experiences in any way impede my ability to command this ship, you are mistaken.",
                "I will not allow you to lecture me about the merits of emotion.",
                "Have you disengaged the external inertial dampener?",
                "That would be unwise."
                "Captain, what are you doing?",
                "No, not really. Not this time.",
                "The purpose is to experience fear, fear in the face of certain death, to accept that fear, and maintain control of oneself and one's crew.",
                "I would cite regulation, but I know you will simply ignore it.",
                "Out of the chair.",
                "I presume you've prepared new insults for today.",
                "This is your thirty-fifth attempt to elicit an emotional response from me.",
                "The complexities of human pranks escape me.",
                "It appears that you have been keeping important information from me.",
                "... the statistical likelihood that our plan will succeed is less than 4.3%.",
                "Thrusters on full.",
                "Fascinating!",
                "You are Montgomery Scott.",
                "I need everyone to continue performing admirably.",
                "May I say that I have not thoroughly enjoyed serving with humans? I find their illogic and foolish emotions a constant irritant.",
                "Computers make excellent and efficient servants, but I have no wish to serve under them.",
                "Insufficient facts always invite danger.",
                "In critical moments, men sometimes see exactly what they wish to see.",
                "After a time, you may find that having is not so pleasing a thing after all as wanting. It is not logical, but is often true.",
                "Without followers, evil cannot spread.",
                "The needs of the many outweigh the needs of the few.",
                "Curious how often you Humans manage to obtain that which you do not want.",
                "If there are self-made purgatories, then we all have to live in them.",
                "Vulcans never bluff.",
                "Logic is the beginning of wisdom ... not the end.",
                "When there is no emotion, there is no motive for violence.",
                "That position... would not only be unavailing but also undignified.",
                "The fact that my internal arrangement differs from yours, doctor, please me to no end.",
                "Has it occurred to you that there is a certain inefficiency in constantly questioning me on things you've already made up your mind about?",
                "Fascinating is a word I use for the unexpected; in this case, I would think interesting would suffice.",
                "The most unfortunate lack in current computer programming is that there is nothing available to immediately replace the starship's surgeon.",
                "Insults are effective only where emotion is present.",
                "Change is the essential process of all existence.",
                ]


def get_random_quote(quotes):
    """Get a random quote from a provided list of quotes."""

    return random.choice(quotes)
