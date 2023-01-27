import join

file_path_1 = input("Write the first file name here.")
file_path_2 = input("Write the second file name here.")
column1 = input("Which column from the first table do you want to merge tables through?\n").lower()
column2 = input("Which column from the second table do you want to merge tables through?\n").lower()

join.join(file_path_1, file_path_2, column1, column2)