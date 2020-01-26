def tremove(tuples):
    tuples = filter(None, tuples)
    return tuples


def remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples


tuples = [(), ('ram', '15', '8'), (), ('laxman', 'hanuman'),
          ('krishna', 'akbar', '45'), ('', ''), ()]
print(tremove(tuples))
print(remove(tuples))
