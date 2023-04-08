def compare_list_by_content(list1, list2):
    """Compares two lists by content. If the lists have
    the same number of elements and the same contents
    regardless of order, returns True. Else, returns False.""" 
    if len(list1) == len(list2):
        for i in list1:
            if i in list2:
                pass
            else:
                return False
    else:
        return False
    return True
