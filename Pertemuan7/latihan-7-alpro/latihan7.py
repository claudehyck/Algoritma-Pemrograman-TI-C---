def hitung_panjang(arr):
    count = 0
    for _ in arr:
        count += 1
    return count

def salin_list(arr):
    copy_list = []
    for item in arr:
        copy_list += [item]
    return copy_list

def bubble_sort(arr):
    n = hitung_panjang(arr)
    data = salin_list(arr)
    swap_count = 0
    
    i = 0
    while i < n:
        swapped = False
        j = 0
        while j < (n - i - 1):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp
                
                swap_count += 1
                swapped = True
            j += 1
        
        if not swapped:
            break
        i += 1
            
    return data, swap_count

def selection_sort_descending(arr):
    n = hitung_panjang(arr)
    data = salin_list(arr)
    swap_count = 0
    
    i = 0
    while i < n:
        max_idx = i
        j = i + 1
        while j < n:
            if data[j] > data[max_idx]:
                max_idx = j
            j += 1
            
        if max_idx != i:
            temp = data[i]
            data[i] = data[max_idx]
            data[max_idx] = temp
            swap_count += 1
        i += 1
            
    return data, swap_count

data_original = [
    290, 1012, 731, 801, 992, 1395, 367, 519, 795, 1385, 274, 154, 219, 1410, 83, 589, 553, 362, 594, 851, 173,
    657, 581, 397, 543, 791, 226, 81, 1459, 126, 941, 491, 1207, 1093, 1473, 951, 267, 1371, 864, 953, 1119, 212, 1266,
    120, 723, 643, 205, 130, 9, 16, 1053, 507, 1381, 1122, 1323, 758, 713, 1219, 375, 951, 98, 1011, 642, 1099, 1098, 453, 7, 1137, 53, 1352, 553, 380, 1324, 473, 519, 923, 13, 592, 10, 546, 65, 1440, 1002, 1444, 510, 1266, 901, 1444, 691, 650, 373, 896, 681, 916, 943, 323, 783, 1385, 891, 621, 687, 1384, 268, 211, 708, 1067, 736, 1223, 990, 1145, 448, 731, 486, 381, 1441, 312, 181, 785, 157, 793, 1029, 1273, 846, 1473, 57, 785, 588, 582, 920, 808, 644, 1182, 1101, 579, 623, 556, 858, 59, 163, 1236, 310, 1308, 962, 356, 1005, 883, 582, 786, 958, 321
]

sorted_bubble, swaps_bubble = bubble_sort(data_original)
print("Hasil Bubble Sort (Ascending):")
print(sorted_bubble)
print("Total Swap Bubble Sort:", swaps_bubble)

print()

sorted_selection, swaps_selection = selection_sort_descending(data_original)
print("Hasil Selection Sort (Descending):")
print(sorted_selection)
print("Total Swap Selection Sort:", swaps_selection)