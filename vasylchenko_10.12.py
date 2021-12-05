n, m = [int(i) for i in input().split()]



for i in range(1, n * m + 1):
    print(i, end=" ")
    if i % m == 0:
        print()
A = [[0 for x in range(m)] for x in range(n)]

student_num = 1
for i in range(n):
    for j in range(m):
        A[i][j] = student_num
        student_num += 1

same_place_counter = 0
new_student_num = 1
for j in range(m):
    for i in range(n):
        if A[i][j] == new_student_num:
            same_place_counter += 1
        new_student_num += 1

# Output
print(same_place_counter)
