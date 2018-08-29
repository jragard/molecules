import itertools

chain1 = 'OIMDIHEIAFNL'
chain2 = 'CHJDBJMHPJKD'
chain3 = 'LCBJOJGIEKBO'
chain4 = 'KAINLHLOLBEJ'

def delete_zeros(lst):
    'is this working'
    for index, tuple in enumerate(lst):
        if 0 in tuple:
            del lst[index]
    return lst
            
            
def delete_elevens(lst):
    print 'is this function even working'
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
  
    one_two = compare_chains(first_vertical, first_horizontal)
    two_three = compare_chains(first_horizontal, second_vertical)
    one_four = compare_chains(first_vertical, second_horizontal)
    three_four = compare_chains(second_vertical, second_horizontal)
    
    print lowest_index(one_two)
    print highest_index(two_three)
    print 'one_two', one_two
    print 'two_three', two_three
    print 'one_four', one_four
    print 'three_four', three_four
    print 'poss_area', poss_area
    
    
    
    

possible_molecules('OIMDIHEIAFNL', 'CHJDBJMHPJKD', 'LCBJOJGIEKBO', 'KAINLHLOLBEJ', (6, 5))   
# for tuple in rectangles():
#     i = itertools.permutations([chain1, chain2, chain3, chain4])
#     for each in i:
#         possible_molecules(each[0], each[1], each[2], each[3], tuple)




# chain1_chain2 = compare_chains(chain1, chain2)
# chain1_chain3 = compare_chains(chain1, chain3)
# chain1_chain4 = compare_chains(chain1, chain4)
# chain2_chain3 = compare_chains(chain2, chain3)
# chain2_chain4 = compare_chains(chain2, chain4)
# chain3_chain4 = compare_chains(chain3, chain4)
        
# delete_zeros(chain1_chain2)
# delete_zeros(chain1_chain3)
# delete_zeros(chain1_chain4)
# delete_zeros(chain2_chain3)
# delete_zeros(chain2_chain4)
# delete_zeros(chain3_chain4)

# delete_elevens(chain1_chain2)
# delete_elevens(chain1_chain3)
# delete_elevens(chain1_chain4)
# delete_elevens(chain2_chain3)
# delete_elevens(chain2_chain4)
# delete_elevens(chain3_chain4)

# print 'chain1_chain2', chain1_chain2
# print 'chain1_chain3', chain1_chain3
# print 'chain1_chain4', chain1_chain4
# print 'chain2_chain3', chain2_chain3
# print 'chain2_chain4', chain2_chain4
# print 'chain3_chain4', chain3_chain4

# print '-----------'

# srt1_2 = sorted(chain1_chain2, key=lambda(x,y,z):abs(y-z))
# srt1_3 = sorted(chain1_chain3, key=lambda(x,y,z):abs(y-z))
# srt1_4 = sorted(chain1_chain4, key=lambda(x,y,z):abs(y-z))
# srt2_3 = sorted(chain2_chain3, key=lambda(x,y,z):abs(y-z))
# srt2_4 = sorted(chain2_chain4, key=lambda(x,y,z):abs(y-z))
# srt3_4 = sorted(chain3_chain4, key=lambda(x,y,z):abs(y-z))
        
# print 'srt1_2', srt1_2
# print 'srt1_3', srt1_3
# print 'srt1_4', srt1_4
# print 'srt2_3', srt2_3
# print 'srt2_4', srt2_4
# print 'srt3_4', srt3_4