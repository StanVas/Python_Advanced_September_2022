def naughty_or_nice_list(*info, **checking):
    kids_list = []
    for el in info[0]:
        lst = []
        lst.append(el[0])
        lst.append(el[1])
        kids_list.append(lst)

    santa_dict = {"Nice": [], "Naughty": [], "Not found": []}

    check_list = []
    for data in info[1:]:
        number, info = [int(x) if x.isdigit() else x for x in data.split('-')]
        lst = []
        lst.append(number)
        lst.append(info)
        check_list.append(lst)

    for number, check in check_list:
        if sum(1 for num, name in kids_list if number == num) == 1:
            for element in kids_list:
                if number in element:
                    santa_dict[check].append(element[1])
                    kids_list.remove(element)

    return santa_dict
    #
    #     if sum(1 for num, name in kids_list if number == num) == 1:
    #         for element in kids_list:
    #             if number in element:
    #                 santa_dict[info].append(element[1])
    #                 kids_list.remove(element)
    # print(santa_dict)
    # print(kids_list)



    # kids_dict = {}
    # for el in info[0]:
    #     print(el)
    #     for e in el:
    #         key = e[0]
    #         value = e[1]
    #         kids_dict[key] = value
    # return kids_dict
    # santa_dict = {"Nice": [], "Naughty": [], "Not found": []}
    # for data in info[1:]:
    #     number, info = [int(x) if x.isdigit() else x for x in data.split('-')]
    #     for el in kids_lst:
    #         print(el)



    # return santa_dict



print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naugy",
    Amy="Nice",
    Katy="Naughty",
))