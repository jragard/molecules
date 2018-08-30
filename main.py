import itertools

chain1 = 'OIMDIHEIAFNL'
chain2 = 'CHJDBJMHPJKD'
chain3 = 'LCBJOJGIEKBO'
chain4 = 'KAINLHLOLBEJ'

# chain1 = 'CDBADCBBEFEF'
# chain2 = 'DACCBADAFEAB'
# chain3 = 'EFBDCAADBDCD'
# chain4 = 'ABCDABCDABCD'

# chain1 = 'OIAGFLHMHCNH'
# chain2 = 'PNNNAOHDHMCK'
# chain3 = 'EHPLBAKAIKGN'
# chain4 = 'GNJNAGEPDCMD'



def compare_chains(string1, string2):
    lst = []
    for index, char in enumerate(string1):
        if char in string2:
            lst.append((char, index, string2.index(char)))
    
    for index, char in enumerate(string2):
        if char in string1:
            lst.append((char, index, string1.index(char)))
    
    return list(set(lst))
    

def rectangles():
    lst = [(i, y) for i in range(1, 9) for y in range(i, 9)]  
    return sorted(lst, key=lambda(x,y): x*y, reverse=True)
    
    
def possible_molecules(first_vertical, first_horizontal, second_vertical, second_horizontal, poss_area):
    
    areas = []
    
    one_two = compare_chains(first_vertical, first_horizontal)
    two_three = compare_chains(first_horizontal, second_vertical)
    one_four = compare_chains(first_vertical, second_horizontal)
    three_four = compare_chains(second_vertical, second_horizontal)
    match = False
    
    print 'one_two', one_two
    print 'two_three', two_three
    print '-----------'
    print 'one_four', one_four
    print '------------'
    print 'three_four', three_four
                                  
    for x in one_two:
        if 0 in x or 11 in x:
            continue
        else:
            for tuple in two_three:
                if 0 in tuple or 11 in tuple:
                    continue
                else:
                    if tuple[1] == poss_area[0] + x[1] + 1:
                        for tuple2 in three_four:
                            if 0 in tuple2 or 11 in tuple2:
                                continue
                            else:
                                if tuple2[1] == poss_area[1] + tuple[2] + 1:
                                      for tuple3 in one_four:
                                            if 0 in tuple3 or 11 in tuple3:
                                                continue
                                            else:
                                                if tuple3[2] == poss_area[1] + x[2] + 1:
                                                    match = True
                                                    
                                                    
                        
                                
    if match:
        print first_vertical, first_horizontal, second_vertical, second_horizontal, poss_area
        print x
        print tuple
        print tuple2
        print tuple3
        areas.append(poss_area[0]*poss_area[1])
        match = False
    
    if len(areas) > 0:
        return areas
    else:
        return 0
                
    
print possible_molecules('CHJDBJMHPJKD', 'OIMDIHEIAFNL', 'KAINLHLOLBEJ', 'LCBJOJGIEKBO',  (6, 6))

area_lst = []

# for tuple in rectangles():
#     i = itertools.permutations([chain1, chain2, chain3, chain4])
#     for each in i:
#         x = possible_molecules(each[0], each[1], each[2], each[3], tuple)
#         if x != 0:
#             area_lst.append(x)
#             break
            
# print area_lst