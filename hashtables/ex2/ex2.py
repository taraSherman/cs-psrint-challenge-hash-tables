#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # create table
    list = {}
    # set up size for route
    route = [None] * length
    
    # for each ticket:
    for ticket in tickets:
        # set source as key, destination as value
        list[ticket.source] = ticket.destination
    # like a linked list
    next = list["NONE"]
    #iterate over the length of the route 
    for i in range(0, length):
        route[i] = next
        next = list[next]
    return route


'''
set up size of memory allocated for route  = [None] * length
iterate through tickets, linking source of one ticket to destination of preceding ticket (doubly-linked list). NONE is head of list.
Iterate through route (linked tickets). Current index is next.
'''