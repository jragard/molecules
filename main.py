import itertools
import math

chain1 = 'OIMDIHEIAFNL'
chain2 = 'CHJDBJMHPJKD'
chain3 = 'LCBJOJGIEKBO'
chain4 = 'KAINLHLOLBEJ'
    
def crossings(horizontal, vertical, (width, height)):
  
    horizontal_lst = []
    vertical_lst = []
    final_lst = []
    
    max_horizontal_index = (len(horizontal) - 3) - width
    max_vertical_index = (len(vertical) - 3) - height
    
    for index, char in enumerate(horizontal):
        if index > max_horizontal_index:
            break
        else:
            if char in vertical:
                if index != 0 and index <= max_horizontal_index:
                    if vertical.index(char) != 0 and vertical.index(char) <= max_vertical_index:
                        horizontal_lst.append((char, index, vertical.index(char)))
                        
    for index, char in enumerate(vertical):
        if index > max_vertical_index:
            break
        else:
            if char in horizontal:
                if index != 0 and index <= max_vertical_index:
                    if horizontal.index(char) != 0 and horizontal.index(char) <= max_horizontal_index:
                        vertical_lst.append((char, horizontal.index(char), index))
                        
    for x in horizontal_lst:
        final_lst.append(x)
        
    for x in vertical_lst:
        final_lst.append(x)
                   
    return list(set(final_lst))
    

def rectangles():
    lst = [(i, y) for i in range(1, 9) for y in range(i, 9)]  
    return sorted(lst, key=lambda(x,y): x*y, reverse=True)
    
    
def possible_molecules(first_vertical, first_horizontal, second_vertical, second_horizontal, poss_area):
    
    area_width = poss_area[0]
    area_height = poss_area[1]
    
    areas = []
    
    possible_crossings = crossings(first_horizontal, first_vertical, (area_width, area_height))
    match = False
    
    try:
        for crossing in possible_crossings:
            horizontal = crossing[1]
            vertical = crossing[2]
            second_horiz_crossing = first_horizontal[horizontal + area_width + 1]
            second_vert_crossing = second_vertical[vertical]
            if first_horizontal[horizontal + area_width + 1] == second_vertical[vertical]:
                bottom_vert_crossing = second_vertical[vertical + area_height + 1]
                bottom_second_horiz = second_horizontal[horizontal + area_width + 1]
                # if second_vertical[vertical + area_height + 1] == second_horizontal[horizontal + area_width + 1]:
                if second_vertical[vertical + area_height + 1] in second_horizontal and first_vertical[vertical + area_height + 1] in second_horizontal:
                    # x = second_horizontal[index + area_width + 1]
                    # y = second_vertical[vertical + area_height + 1]
                    final_vert_crossing = first_vertical[vertical + area_height + 1]
                    for index, char in enumerate(second_horizontal):
                        if char == first_vertical[vertical + area_height + 1] and second_horizontal[index + area_width + 1] == second_vertical[vertical + area_height + 1]:
                    # if second_horizontal[horizontal] == first_vertical[vertical + area_height + 1]:
                            match = True
                            break
    except:
        return 0
    
    
    if match:
        areas.append(area_width*area_height)
        print first_vertical, first_horizontal, second_vertical, second_horizontal, poss_area
        
    
    if areas:
        # print areas
        return areas
    else:
        return 0


# print possible_molecules('ABAAAAAAAABA', 'CBCCCCCCCCBC', 'DBDDDDDDDDBD', 'EBEEEEEEEEBE', (8, 8))                

area_lst = []

for tup in rectangles():
    # i = itertools.permutations(['CDBADCBBEFEF', 'DACCBADAFEAB', 'EFBDCAADBDCD', 'ABCDABCDABCD'])
    # i = itertools.permutations(['DACCBADAFEAB', 'EFBDCAADBDCD', 'ABCDABCDABCD', 'CDBADCBBEFEF'])
    # i = itertools.permutations(['ABABABABABAB', 'CDCDCDCDCDCD', 'EEEEEEEEEEEE', 'FFFFFFFFFFFF'])
    # i = itertools.permutations(['ABAAAAAAAABA', 'CBCCCCCCCCBC', 'DBDDDDDDDDBD', 'EBEEEEEEEEBE'])
    # i = itertools.permutations(['ABBBBBBBBBBA', 'ACCCCCCCCCCA', 'ADDDDDDDDDDA', 'AEEEEEEEEEEA'])
    # i = itertools.permutations(['BBBABBBABBBB', 'CCACCCACCCCC', 'DDDDADDADDDD', 'EEAEEAEEEEEE'])
    # i = itertools.permutations([chain1, chain2, chain3, chain4])
    for a,b,c,d in i:
        x = possible_molecules(a, b, c, d, tup)
        # print x
        if x:
            area_lst.append(x)
            break
            
print area_lst