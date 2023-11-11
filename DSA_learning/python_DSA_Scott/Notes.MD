# Big O
- Best case scenario (Time complexity) -> Ω
- Average case scenario (Time complexity) -> θ
- Worst case scenario (Time complexity) -> O (big O)
- O(n) -> Iteration trough all list items (N times). O(n) is always a straight line on  graph. It is called proportional
---

### Example code of O(n)
```
def print_items(n):
    for i in range(n):
        print(i)
```
---

### Example of Constant dropping:
```
def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
```
#### n + n = O(2n) -> we can simplify by dropping the constant (2)

### Example code of O(n^2) (Not efficient time complexity)
```
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
```
---
### Example of Constant dropping:
#### O (n^2 + n), we remove the non-dominant (since n^2 > n^1) we remove n^1

---
### Example code of O(1) (flat line)
```
def add_items(n):
    return n + n
```

---
### Example code of O(log n) (binary search algorithm, cut into half) (quite flat on graph)
```
# 2^3 = 8 | log2(8) = 3 (2 to the what power == 8)
def add_items(n):
    return n + n
```
---
### Different terms for input
```
def print_items(a, b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)
```
#### This is equal to O(a + b). If we have nested loops will be O(a * b)
---
### Big O Resources
- https://www.bigocheatsheet.com/
---

# Linked list
- Have two variables - head and tail.
- Head points to the first node (element) of linked list, tail points to the last.
- Every node inside linked list is connected x->y->z, where x is head, z is tail
- Node of LL is made of value and pointer (can related to dictionary):
```
{
    "value": 4,
    "next": None,
}
```
### Big O for methods of linked list (LL)
- append node to the last element - O(1)
- remove last element from node - O(n)
- append at the beginning - O(n)
- removing first element - O(n)
- adding element - O(n)
- removeing element - O(n)
- lookup item - O(n)
---