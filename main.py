if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # di ubah ke set dulu untuk menghilangkan angka duplikat
    # di ubah ke list supaya bisa di urutkan menggunakan fungsi sorted
    print(sorted(list(set(arr)))[-2]) 
