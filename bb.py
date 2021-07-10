def degreeofArray(arr):
    list = arr
    dictionary = []
    degrees = []
    position_list = []

    number = {}
    for i in list:
        if i in number:

            number[i] += 1
            # print(number)
        else:
            number[i] = 1
            # print(number)

    for value in number:
        dictionary.append(value)
    for value in number.values():
        degrees.append(value)

    # print(dictionary)
    # print(degrees)

    maximum = max(degrees)
    position = degrees.index(maximum)
    position_list.append(dictionary[position])
    degrees.remove(degrees[position])
    dictionary.remove(dictionary[position])

    retrieving = True

    while retrieving:
        new_max = max(degrees)
        if new_max == maximum:
            new_position = degrees.index(new_max)
            position_list.append(dictionary[new_position])
            degrees.remove(degrees[new_position])
            dictionary.remove(dictionary[new_position])
        else:
            retrieving = False

    # print(position_list)
    # print(maximum)


    compar_list = None

    for value in position_list:
        sub_array_list = []
        checker = maximum
        for comparision in list:
            if comparision == value:
                position = list.index(comparision)


        keep_adding = True
        start = list[position]
        while keep_adding:
            if checker == 0:
                keep_adding = False
            else:
                if  start == value:
                    checker -= 1

                sub_array_list.append(start)
                try:
                    position += 1
                    start = list[position]
                except:
                    pass

        if compar_list == None:
            compar_list = sub_array_list
        elif len(compar_list) > len(sub_array_list):
            compar_list = sub_array_list


    final_value = len(compar_list)
    return final_value













value = degreeofArray(arr=[1,3,2,3,1,1,3,3])
print(f'final value is {value}')



# diction = {3:5,5:6}
#
# if 3 in diction:
#     diction[6] = 2
#     print(diction)
#     diction[3] += 1
#     print(diction)



