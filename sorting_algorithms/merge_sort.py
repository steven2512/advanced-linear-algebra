def merge_sort(array: list, func = lambda a: a):
        #Use merge sorts run in O(NlogN)
        if len(array) >1:
            mid = len(array)//2
            left_array = merge_sort(array[:mid], func)
            right_array = merge_sort(array[mid:], func)
        else:
            return array
        
        sorted_list = merge(left_array, right_array, func)
        
        return sorted_list

def merge(left_array: list, right_array: list, func):
    merged_list = []
    i, j = 0,0
    while i < len(left_array) or j<len(right_array):
        if i < len(left_array) and j<len(right_array):
            if func(left_array[i])<func(right_array[j]):
                merged_list.append(left_array[i])
                i+=1
            elif func(right_array[j])<func(left_array[i]):
                merged_list.append(right_array[j])
                j+=1
            else:
                merged_list.append(left_array[i])
                merged_list.append(right_array[j])
                i+=1
                j+=1
        elif i == len(left_array):
            merged_list.append(right_array[j])
            j+=1
        else:
            merged_list.append(left_array[i])
            i+=1
    return merged_list

#Small Test Case
# print(merge_sort([42, 7, 19, 3, 88, 15, 27, 1, 63, 34]
# , lambda a: -a))