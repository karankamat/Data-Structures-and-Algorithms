def max_heapify(array, heap_size, index):
    l = 2*index
    r = 2*index + 1
    
    largest = index
    
    if l < heap_size and array[l] > array[index]:
        largest = l
    if r < heap_size and array[r] > array[index]:
        largest = r
        
    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        max_heapify(array, heap_size, largest)
        
def build_max_heap(array):
    heap_size = len(array)
    
    for i in range(heap_size//2, 0, -1):
        max_heapify(array, heap_size, i)
    
if __name__ == "__main__":
    a = [None, 11, 2, 5, 7 ,12, 84]
    build_max_heap(a)
    print(a[1:])