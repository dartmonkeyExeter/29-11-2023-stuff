# madlibs.py
from random import randint

stories = ["The {0} {1} {2} {3} the {4} {5}.",]
types = [["adjective","adjective","animal","verb","adjective","animal"]]

def gameloop():
    which = randint(0,len(stories))
    story = stories[which]
    cur_type = ["adjective","adjective","animal","verb","adjective","animal"]
    words = []

    for i in range(len(types)):
        words.append(input(f"{types[i]}: "))

    mad_lib = story.format(*words)

    print(mad_lib)

gameloop()