import itertools


chain1 = 'OIMDIHEIAFNL'
chain2 = 'CHJDBJMHPJKD'
chain3 = 'LCBJOJGIEKBO'
chain4 = 'KAINLHLOLBEJ'


def compare_chains(string1, string2):
    lst = []
    for index, char in enumerate(string1):
        if char in string2:
            lst.append((char, index, string2.index(char)))
    
    return lst



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
                                  
    for x in one_two:
        if 0 in x or 11 in x:
            continue
        else:
            x_horiz_width = x[2]
            x_vert_height = x[1]
            for tuple1 in two_three:
                if 0 in tuple1 or 11 in tuple1:
                    continue
                else:
                    tuple1_horiz_width = tuple1[1]
                    tuple1_vert_height = tuple1[2]
                    if tuple1_horiz_width == area_width + x_horiz_width + 1:
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
                                                tuple3_horiz_width = tuple3[2]
                                                tuple3_vert_height = tuple3[1]
                                      
                                                if tuple3_vert_height == tuple2_vert_height and tuple2_horiz_width - tuple3_horiz_width == area_width + 1:
                                                    match = True
                                                    

                    
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

# print possible_molecules('OIMDIHEIAFNL', 'CHJDBJMHPJKD', 'LCBJOJGIEKBO', 'KAINLHLOLBEJ', (2, 5))

# print possible_molecules('ABAAAAAAAABA', 'CBCCCCCCCCBC', 'DBDDDDDDDDBD', 'EBEEEEEEEEBE', (8,8))

area_lst = []

for dimensions in rectangles():
    i = itertools.permutations([chain1, chain2, chain3, chain4])
    for a,b,c,d in i:
        x = possible_molecules(a,b,c,d, dimensions)
        # print x
        if x != 0:
            area_lst.append(x)
            break
if area_lst:        
    print max(area_lst)
else:
    print 0

print area_lst


# CDBADCBBEFEF
# DACCBADAFEAB
# EFBDCAADBDCD
# ABCDABCDABCD