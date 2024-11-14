def sort_array(arr):
   
    numbers = [x for x in arr if isinstance(x, (int, float))]
    characters = [x for x in arr if isinstance(x, str)]
 
    numbers.sort()
    characters.sort()
    
    sorted_arr = numbers + characters
    
    return sorted_arr

arr = [3, 'b', 1, 'a', 2, 'c', 5, 'd']
sorted_arr = sort_array(arr)
print("Sorted array:", sorted_arr)
