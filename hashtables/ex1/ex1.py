def get_indices_of_item_weights(weights, length, limit):
    # create empty hash table
    list = {}
    # iterate through weights --> (key: value) ==> (weight: index)
    for idx in range(length):
        list[weights[idx]] = idx
    # for each item,
    for idx in range(length):
        # get ship weight by subtracting weight from limit
        ship_weight = limit - weights[idx]
        # check if the
        if ship_weight in list:
            return(max(idx, list[ship_weight]), min(idx, list[ship_weight]))
    return None


'''
Want to ship several packages but, to reduce shipping costs, want to combine items into single packages (ignore size; just dealing with weight here)
How figure out what 2 items can go in the same box because together they add up to the weight limit?
Create list of items and what they weigh (again, don't care what item, so just go by weight and index), using input example given
[
    4 lbs: item 1,
    6 lbs: item 2,
    10 lbs: item 3,
    15 lbs: item 4,
    16 lbs: item 5
]
Length of list is 5 cells (5 packages), and the weight limit is 21 lbs. So we want to first create that list of weights (list = {}). It's empty now, so iterate through the weights we've been given, thinking of (key:value) being (item weight: index).
For each item, subtract the weight (remember, the idx) from the limit of 21, to get remaining ship_weight:
ship_weight = limit - weights[idx]
So remaining ship_weight at weights[0] is 4... limit is 21... so 21-4 = 17.
Is that 17 in the list (representing another item)? No, so move to the next.
ship_weight at weights[1] (21-6=15)... is that in the list? Yes, it's at weights[3].
So we can return those 2 values, using max and min for larger and smaller values, respectively.
'''
