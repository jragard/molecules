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
    
    area_width = poss_area[0]
    area_height = poss_area[1]
    
    areas = []
    
    one_two = compare_chains(first_vertical, first_horizontal)
    two_three = compare_chains(first_horizontal, second_vertical)
    one_four = compare_chains(first_vertical, second_horizontal)
    three_four = compare_chains(second_vertical, second_horizontal)
    match = False
    
    # print 'one_two', one_two
    # print '-------------'
    # print 'two_three', two_three
    # print '-----------'
    # print 'one_four', one_four
    # print '------------'
    # print 'three_four', three_four
                                  
    for x in one_two:
        if 0 in x or 11 in x:
            continue
        else:
            x_horiz_width = x[1]
            x_vert_height = x[2]
            for tuple in two_three:
                if 0 in tuple or 11 in tuple:
                    continue
                else:
                    tuple_horiz_width = tuple[1]
                    tuple_vert_height = tuple[2]
                    if tuple_horiz_width == area_width + x_horiz_width + 1:
                        for tuple2 in three_four:
                            if 0 in tuple2 or 11 in tuple2:
                                continue
                            else:
                                tuple2_horiz_width = tuple2[2]
                                tuple2_vert_height = tuple2[1]
                                if tuple2_vert_height == area_height + x_vert_height + 1:
                                      
                                      for tuple3 in one_four:
                                            if 0 in tuple3 or 11 in tuple3:
                                                continue
                                            else:
                                                tuple3_horiz_width = tuple3[1]
                                                tuple3_vert_height = tuple3[2]
                                      
                                                if (tuple3_vert_height == area_height + x_vert_height + 1) and (tuple2_horiz_width - tuple3_horiz_width == area_width + 1):
                                                    match = True
    
    # area_width = 5
    # area_height = 6
    # x = ('D', 3, 3)
    # tuple = ('J', 9, 3)
    # tuple2 = ('B', 10, 9)
    # tuple3 = ('N', 3, 10)
    
    # x_horiz_width = x[1]
    # x_vert_height = x[2]
    
    # tuple_horiz_width = tuple[1]
    # tuple_vert_height = tuple[2]
    
    # tuple2_horiz_width = tuple2[2]
    # tuple2_vert_height = tuple2[1]
    
    # tuple3_horiz_width = tuple3[1]
    # tuple3_vert_height = tuple3[2]
    
    # if tuple_horiz_width == area_width + x_horiz_width + 1:
    #     print 'yay1'
    #     if tuple2_vert_height == area_height + x_vert_height + 1:
    #         print 'yay2'
    #         if (tuple3_vert_height == area_height + x_vert_height + 1) and (tuple2_horiz_width - tuple3_horiz_width == area_width + 1):
    #               return 'yes'
    #         else:
    #             print area_width
                
                        
                                
    if match:
        areas.append(poss_area[0]*poss_area[1])
        print chain1, chain2, chain3, chain4, poss_area
        match = False
    
    if areas:
        return areas
    else:
        return 0


# print possible_molecules(chain1, chain2, chain3, chain4, (5, 6))                
    
# print possible_molecules('CHJDBJMHPJKD', 'OIMDIHEIAFNL', 'KAINLHLOLBEJ', 'LCBJOJGIEKBO',  (6, 6))

# print possible_molecules('OIMDIHEIAFNL', 'CHJDBJMHPJKD', 'LCBJOJGIEKBO', 'KAINLHLOLBEJ', (5, 7))

area_lst = []

for tuple in rectangles():
    i = itertools.permutations([chain1, chain2, chain3, chain4])
    for each in i:
        x = possible_molecules(each[0], each[1], each[2], each[3], tuple)
        if x != 0:
            area_lst.append(x)
            break
            
print area_lst