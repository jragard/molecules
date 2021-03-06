import itertools
import argparse
import sys


def find(string, char):
    return [i for i, letter in enumerate(string) if letter == char]

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

# def crossings(horizontal, vertical, (width, height)):

#     horizontal_lst = []
#     vertical_lst = []
#     final_lst = []

#     max_horizontal_index = (len(horizontal) - 3) - width
#     max_vertical_index = (len(vertical) - 3) - height

    

#     for horizontal_index, char in enumerate(horizontal):
#         if horizontal_index > max_horizontal_index:
#             break
#         else:
#             if char in vertical:
#                 if horizontal_index != 0 and horizontal_index <= max_horizontal_index:
#                     matching_chars_in_vertical = find(vertical, char)
#                     for vertical_index in matching_chars_in_vertical:
#                         if vertical_index != 0 and vertical_index <= max_vertical_index:
#                     # if vertical.index(char) != 0 and vertical.index(char) <= max_vertical_index:
#                             horizontal_lst.append((char, horizontal_index, vertical_index))

#     for vertical_index, char in enumerate(vertical):
#         if vertical_index > max_vertical_index:
#             break
#         else:
#             if char in horizontal:
#                 if vertical_index != 0 and vertical_index <= max_vertical_index:
#                     matching_chars_in_horizontal = find(horizontal, char)
#                     for horizontal_index in matching_chars_in_horizontal:
#                         if horizontal_index != 0 and horizontal_index <= max_horizontal_index:

#                     # if horizontal.index(char) != 0 and horizontal.index(char) <= max_horizontal_index:
#                             vertical_lst.append((char, vertical_index, horizontal_index))

#     for x in horizontal_lst:
#         final_lst.append(x)

#     for x in vertical_lst:
#         final_lst.append(x)
#     set_list = list(set(final_lst))
#     # x = 1
#     # return list(set(final_lst))
#     return vertical_lst
#     # return set_list


def rectangles():
    lst = [(i, y) for i in range(1, 9) for y in range(i, 9)]
    return sorted(lst, key=lambda(x, y): x*y, reverse=True)

def rectangles2():
    lst = [(y, i) for i in range(1, 9) for y in range(i, 9)]
    return sorted(lst, key=lambda(x, y): x*y, reverse=True)

def permutations():
    final_list = []

    for tup in rectangles():
        if tup not in final_list:
            final_list.append(tup)
    
    for tup in rectangles2():
        if tup not in final_list:
            final_list.append(tup)
    return final_list


def possible_molecules(first_vertical, first_horizontal, second_vertical, second_horizontal, poss_area):
    
    area_width = poss_area[0]
    area_height = poss_area[1]

    areas = []

    possible_crossings = crossings(first_horizontal, first_vertical,
                                   (area_width, area_height))
    match = False

    try:
        for crossing in possible_crossings:

            horizontal = crossing[1]
            vertical = crossing[2]
            second_horiz_crossing = first_horizontal[horizontal + area_width + 1]

            if second_horiz_crossing in second_vertical:
                if second_vertical.index(second_horiz_crossing) != 0 and second_vertical.index(second_horiz_crossing) + area_height + 1 != 11:
                    index_of_possible_bottom_crossing = second_vertical.index(second_horiz_crossing) + area_height + 1
                    index_of_possible_top_crossing = second_vertical.index(second_horiz_crossing)
                    if second_vertical[index_of_possible_top_crossing] == second_horiz_crossing:
                        if second_vertical[index_of_possible_bottom_crossing] in second_horizontal and first_vertical[vertical + area_height + 1] in second_horizontal:

                            for index, char in enumerate(second_horizontal):
                                if index != 0 and index != 11:
                                    if char == first_vertical[vertical + area_height + 1] and second_horizontal[index + area_width + 1] == second_vertical[index_of_possible_bottom_crossing]:
                                        if (index + area_width + 1) != 11:
                                            match = True
                                            break
    except Exception:
        return 0

    if match:
        areas.append(area_width*area_height)

    if areas:
        return areas
    else:
        return 0


def open_file(filename):

    file_object = open(filename, 'r')
    file_text = file_object.read().split('\n')
    tup_list = []
    original_length = len(file_text) - 1

    while len(tup_list) < (original_length / 4) + 1:
        tup_list.append((file_text[0:4]))
        file_text = file_text[4:]

    return tup_list


def create_parser():
    """Create an argument parser object"""
    parser = argparse.ArgumentParser()
    parser.add_argument('textfile', help='text file with molecule blocks')

    return parser


def main(args):

    parser = create_parser()

    if not args:
        parser.print_usage()
        sys.exit(1)

    parsed_args = parser.parse_args(args)

    molecules_list = open_file(parsed_args.textfile)
    

    area_lst = []

    if parsed_args.textfile:
        # x = possible_molecules('AKEDDDCPGBMG', 'DNLDNDAPMEDF', 'MCPNACAFAAIN', 'CJEEJGMNAOOK', (2, 4))
        # print x
        perms = permutations()
        for group in molecules_list:
        
            if len(group) > 1:
                for tup in perms:
                    i = itertools.permutations(group)
                    
                    for a, b, c, d in i:
                        
                        x = possible_molecules(a, b, c, d, tup)
                        if x:
                            
                            # area_lst.append([x, a, b, c, d, tup])
                            area_lst.append(x)
                            break
                if area_lst:
                    
                    print max(area_lst)[0]
                    # print area_lst
                    area_lst = []
                else:
                    print 0
            else:
                break
        print ""
    else:
        parser.print_usage()
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv[1:])
