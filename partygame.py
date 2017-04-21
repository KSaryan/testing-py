from random import choice

fake_gifts = {"Bob": "silly-string", 
            "isabelle": "cat", 
            "ivy": "a shoe", 
            "Balloonicorn": "Unicorn Frap"}

def play_white_elephant(people_gifts):
    """ Returns a dictionary of which gifts people received

    Input is a dictionary of which gifts people brought.
    People cannot receive the gift that they brought
    """


    # Dictionary for gifts received
    white_elephant = {}

    # List of tuples of people and their gifts brough
    people_items = people_gifts.items() 
    
    # Loop through each party goer and give them the next partygoers gift
    # if last partygoer, get first partygoers gift
    for i in range (len(people_items)):
        if i == len(people_items)-1:
            white_elephant[people_items[i][0]]= people_items[0][1]
        else:
            white_elephant[people_items[i][0]]= people_items[i+1][1]

    return white_elephant



