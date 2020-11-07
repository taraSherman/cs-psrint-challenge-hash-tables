def intersection(arrays):
    # create cache
    cache = {}
    # create empty array
    result = []
    # now to populate cache:
    # for each sub_array
    for sub_arrays in arrays:
        # for each item in sub_arrays (nested loop)
        for num in sub_arrays:
            # if item is in sub_arrays but not in cache...
            if num not in cache:
                # add it
                cache[num] = 1
            # otherwise
            else:
                # iterate
                cache[num] += 1
    # with cache populated,
    # iterate over it and,
    for i in cache:
        # if there is more than one item in cache,
        if cache[i] > 1:
            # add to the end of result array
            result.append(i)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
'''
Using terms like arrays and lists might be too confusing here. Using cache instead.
Maybe use sub_array for each stored array?
Lists can be dictionaries where the key is the item (in this case num) and the value is truthy
Because sub_arrays are nested, have to use a nested loop to iterate over each sub_array
'''
