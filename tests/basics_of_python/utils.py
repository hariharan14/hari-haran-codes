#used in day 5
def kg_to_lbs(kg):
    return kg * 0.453592

#used in day 5
def lbs_to_kg(lbs):
    return lbs / 0.453592

#used in day 5
def find_max(l):
    temp = l[0]
    for i in l:
        if i > temp:
            temp = i
    return temp

def find_max_2(list, range): # we have built-in functions with the same name so avoid naming like this
    list.sort()
    return list[range-1]