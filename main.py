import itertools

chain1 = 'OIMDIHEIAFNL'
chain2 = 'CHJDBJMHPJKD'
chain3 = 'LCBJOJGIEKBO'
chain4 = 'KAINLHLOLBEJ'

def delete_zeros(lst):
    for index, tuple in enumerate(lst):
        if 0 in tuple:
            del lst[index]
    return lst
            
            
def delete_elevens(lst):
    for index, tuple in enumerate(lst):
        if 11 in tuple:
            del lst[index]
    return lst

def compare_chains(string1, string2):
    lst = []
    for index, char in enumerate(string1):
        if char in string2:
            lst.append((char, index, string2.index(char)))
    
    for index, char in enumerate(string2):
        if char in string1:
            lst.append((char, index, string1.index(char)))
            
    # delete_elevens(lst)
    # delete_zeros(lst)
    
    return list(set(lst))
    
def lowest_index(lst):
    return sorted(lst, key=lambda(x,y,z): abs(y-z))[0]
    
def highest_index(lst):
    return sorted(lst, key=lambda(x,y,z): abs(y-z), reverse=True)
    
            
def rectangles():
    lst = [(i, y) for i in range(1, 9) for y in range(i, 9)]  
    return sorted(lst, key=lambda(x,y): x*y, reverse=True)
    
    
    
    
    
    
    
def possible_molecules(first_vertical, first_horizontal, second_vertical, second_horizontal, poss_area):
    
    areas = []
    one_two = compare_chains(first_vertical, first_horizontal)
    two_three = compare_chains(first_horizontal, second_vertical)
    one_four = compare_chains(first_vertical, second_horizontal)
    three_four = compare_chains(second_vertical, second_horizontal)
    # match = False
    
  
    delete_elevens(one_two)
    delete_zeros(one_two)
    delete_elevens(two_three)
    delete_zeros(two_three)
    delete_elevens(one_four)
    delete_zeros(one_four)
    delete_elevens(three_four)
    delete_zeros(three_four)
    
    for tuple in two_three:
        if tuple[1] == poss_area[0] + lowest_index(one_two)[1] + 1:
            for tuple2 in three_four:
                if tuple2[1] == poss_area[1] + tuple[2] + 1:
                      for tuple3 in one_four:
                            if tuple3[2] == lowest_index(one_two)[2] + poss_area[1] + 1:
                                print 'these are the possible areas'
                                return poss_area[0]*poss_area[1]
                                
                                
    # if match:
    #     areas.append(poss_area[0]*poss_area[1])
    
    # if len(areas) > 0:
    #     return areas[0]
    # else:
    #     pass
                
    
    
    # print 'one_two', one_two
    # print 'two_three', two_three
    # print '-----------'
    # print 'one_four', one_four
    # print 'three_four', three_four
    # print 'poss_area', poss_area
    
    

# print possible_molecules('OIMDIHEIAFNL', 'CHJDBJMHPJKD', 'LCBJOJGIEKBO', 'KAINLHLOLBEJ', (5, 6))



for tuple in rectangles():
    i = itertools.permutations([chain1, chain2, chain3, chain4])
    for each in i:
        print possible_molecules(each[0], each[1], each[2], each[3], tuple)