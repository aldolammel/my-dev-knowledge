"""

FUNCTIONS: *KWARGS KEYWORD ARGUMENTS
(Funções: Argumentos nomeados):

It allows us to create a dictionary with many keys in a function.

By convention, it is called "*kwargs".

The type of args ALWAYS is a dictionary.

MORE IN THIS SECTION OF DRA. ANGELA LEE'S COURSE:
https://www.udemy.com/course/100-days-of-code/learn/lecture/20804136#overview


"""


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)
