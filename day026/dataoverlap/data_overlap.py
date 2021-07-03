'''Get intersection of two files'''

with open('C:/100daysofcode/day026/dataoverlap/file1.txt') as f1:
    list_1 = [int(num) for num in f1]
    with open('C:/100daysofcode/day026/dataoverlap/file2.txt') as f2:
        list_2 = [int(num) for num in f2]

intersection = [num for num in list_1 if num in list_2]
print(intersection)