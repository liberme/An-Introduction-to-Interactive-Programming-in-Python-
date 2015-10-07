print (1000 + 1000) * 0.6
print (1200 + 1200) * 0.6

print  (1 + 1) * 0.7
print  (1.4 + 1.4) * 0.7


def wumpuses(initial_number, offspring_rate):
    result = (initial_number * 2) * offspring_rate
    return result

print wumpuses(1000, 0.6)
print wumpuses(1200, 0.6)

slow = 1
fast = 0
year = 0
while slow > fast:
    if slow == 1 and fast == 0:
        slow = wumpuses(1000, 0.6)
        fast = wumpuses(1, 0.7)
    else:
        slow = wumpuses(slow, 0.6)
        fast = wumpuses(fast, 0.7)
    year += 1
print 'year:', year
print 'final slow: ', slow
print 'final fast: ', fast
     