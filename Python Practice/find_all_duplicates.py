
def all_duplicates(arr):
    duplicates= []
    seen =set()
    for num in arr:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    
    return duplicates


arr =[4,3,2,7,8,2,3,1]
print(all_duplicates(arr))