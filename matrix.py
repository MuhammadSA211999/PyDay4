''''
Matrix: python e matrix hocce dui dimensional Array/List.
Matrix Array er vitor aro duita array dite hoy.
Sei Array gulu ekekta row and sei array gulur vitorer prottek property/element hocce ekekta colum.

Example:
matrix=
[
c=column
 c,c,c
[1,2,3],=> row
 c,c,c
[4,5,6] => row

]
**matrix ke row col index diye access korte hoy.
             row col
three=matrix([0],[2]) // 3
  six=matrix([1],[2]) //6
'''
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
one = (matrix[0][0])
# print(one) # 1
# nested loop and condition diye row column element gulu access kora zay.
for row in matrix:
    for element in row:
        print(element)  # // 1 2 3 4 5 6
