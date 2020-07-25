"""
Algoritm: 
    1. consider the first element ot be sorted and the rest to be unsorted
    2. take the first element in the unsorted part(u1) and compare it with sorted part elements(s1)
    3. if u1<s1 then insert u1 in the correct index, else leave as is
    4. take the next element in the unsorted part and compare with sorted elements
    5. repeat step 3 and step 4 until all elements are sorted
   - Good for small lists 
"""