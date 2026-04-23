data = [78, 90, 65, 97, 882, 360, 21, 9, 1, 36, 67, 99, 420, 510, 443, 38, 505, 123, 404, 45, 5, 300, 250, 220, 15, 5, 33, 256, 10, 20, 44,
        421, 234, 42, 32, 37, 80, 0, 54, 14, 71, 19, 121, 96, 126, 84, 155, 110, 18, 76, 166, 2, 6, 51, 31, 59, 98, 55, 99, 280, 303, 16, 25, 321]

print("Sebelum di sort :", data)
print()

#Radix Sort
print("---- Radix Sort ----")
radixArray = [[], [], [], [], [], [], [], [], [], []]
maxVal = max(data)
exp = 1

while maxVal // exp > 0:

  while len(data) > 0:
    val = data.pop()
    radixIndex = (val // exp) % 10
    radixArray[radixIndex].append(val)

  for bucket in radixArray:
    while len(bucket) > 0:
      val = bucket.pop()
      data.append(val)

  exp *= 10

print("Sesudah di radix sort :", data)
print()

#Merge Sort
print("---- Merge Sort ----")
def mergeSort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  leftHalf = arr[:mid]
  rightHalf = arr[mid:]

  sortedLeft = mergeSort(leftHalf)
  sortedRight = mergeSort(rightHalf)

  return merge(sortedLeft, sortedRight)

def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

mysortedlist = mergeSort(data)
print("Sesudah di merge sort :", mysortedlist)
print()

#Linear Search & Binary Search
def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

angka = int(input("\nMasukkan angka yang ingin dicari: "))
print()

print("---- Linear Search ----")
linear_result = linearSearch(data, angka)
if linear_result != -1:
    print(f"Elemen ditemukan pada index: {linear_result}, Value: {data[linear_result]}")
else:
    print("tidak ada")
print()

print("---- Binary Search ----")
binary_result = binarySearch(data, angka)
if binary_result != -1:
    print(f"Elemen ditemukan pada index: {binary_result}, Value: {data[binary_result]}")
else:
    print("tidak ada")