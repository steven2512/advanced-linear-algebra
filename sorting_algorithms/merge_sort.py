def merge_sort(self, array: list):
        #Use merge sorts run in O(NlogN)
        if len(array) >1:
            mid = len(array)//2
            left_array = merge_sort(array[:mid+1])
            right_array = merge_sort(array[mid+1:])
        else:
            return array
        
        sorted_list = merge(left_array, right_array)
        return sorted_list

def merge(self, left_array: list, right_array: list):
    merged_list = []
    i, j = 0,0
    while i < len(left_array) or j<len(right_array):
        if i < len(left_array) and j<len(right_array):
            if left_array[i]<right_array[j]:
                merged_list.append(left_array[i])
                i+=1
            elif left_array[j]<right_array[i]:
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