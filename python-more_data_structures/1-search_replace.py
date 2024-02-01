#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result_list = my_list[:]
    result_list = [x if x != search else replace for x in my_list]

    return (result_list)
