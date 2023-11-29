# madlibs.py
from random import randint
stories = ["The {0} {1} {2} {3} the {4} {5}.",
            "How much {0} could a {1} {2}, if a {1} could {2} {0}?",
            "{0} sells {1} on the {2}, but the value of those {1} will fall, due to the laws of supply and demand, no one wants to buy {1} when theres loads on the {3}!"]
types = [["adjective","adjective","animal","verb","adjective","animal"], ["noun", "animal", "verb"], ["pronoun","noun","place","place"]]
def gameloop():
    which = randint(0,len(stories) - 1)
    story = stories[which]
    cur_type = types[which]
    words = []
    for i in range(len(cur_type)):
        words.append(input(f"{cur_type[i]}: "))
    mad_lib = story.format(*words)
    print(mad_lib)
gameloop()
