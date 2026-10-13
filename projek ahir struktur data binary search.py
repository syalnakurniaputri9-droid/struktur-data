# Fungsi Insertion Sort
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

# Fungsi Binary Search
def binary_search(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid  # Ditemukan, kembalikan index
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Tidak ditemukan

# Program utama
data = [25, 10, 35, 5, 50]
print("Data sebelum diurutkan:", data)

# Urutkan data dengan Insertion Sort
sorted_data = insertion_sort(data)
print("Data setelah diurutkan:", sorted_data)

# Cari data dengan Binary Search
target = int(input("Masukkan angka yang ingin dicari: "))
hasil = binary_search(sorted_data, target)

# Output hasil pencarian
if hasil != -1:
    print(f"Data {target} ditemukan di index ke-{hasil}")
else:
    print(f"Data {target} tidak ditemukan.")
