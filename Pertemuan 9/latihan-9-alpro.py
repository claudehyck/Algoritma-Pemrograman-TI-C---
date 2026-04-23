def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        insert_index = i
        current_value = arr.pop(i)
        for j in range(i-1, -1, -1):
            if arr[j] > current_value:
                insert_index = j
            else:
                break
        arr.insert(insert_index, current_value)
    return arr

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1
    
    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1
    return arr

def get_valid_input(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val < 0:
                print("Input harus bilangan bulat non-negatif (>= 0).")
                continue
            return val
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat.")

print("=== Program Pengurutan Array ===")

n_elemen = get_valid_input("Masukkan jumlah elemen: ")

data_asli = []
for i in range(n_elemen):
    elemen = get_valid_input(f"Masukkan elemen ke-{i+1}: ")
    data_asli.append(elemen)

print(f"Data Awal: {data_asli}")

arr_insertion = data_asli.copy()
insertion_sort(arr_insertion)
print(f"Insertion Sort : {arr_insertion}")

arr_quick = data_asli.copy()
quick_sort(arr_quick, 0, len(arr_quick) - 1)
print(f"Quick Sort : {arr_quick}")


arr_counting = data_asli.copy()
counting_sort(arr_counting)
print(f"Counting Sort : {arr_counting}")