from terminaltables import AsciiTable
import random


def quicksort_descending(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)

   left_num_arr = [n for n in nums if n > q]
   middle_num_arr = [q] * nums.count(q)
   right_num_arr= [n for n in nums if n < q]

   return quicksort_descending(left_num_arr) + middle_num_arr + quicksort_descending(right_num_arr)

def quicksort_ascending(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)

   left_num_arr = [n for n in nums if n < q]
   middle_num_arr = [q] * nums.count(q)
   right_num_arr = [n for n in nums if n > q]

   return quicksort_ascending(left_num_arr) + middle_num_arr + quicksort_ascending(right_num_arr)

def read_from_file(filename):
    arr = []
    try:
        with open(filename, 'r') as file: # open file with name 'file'
            for line in file.read().splitlines(): # read file line by line
                arr.append(line) # and append them to an array
        
        file.close()

    except FileNotFoundError:
        print('File wasn\'t found')
        raise SystemExit(1) # An exception will be thrown and the program will terminate

    return arr
    
def write_to_file(ascending_arr, descending_arr, filename):
    try:
        with open(filename, 'w') as file: # open file with name 'file'
            for i in range(len(ascending_arr)): # writing ascending and descending sorted array in a file
                file.write(ascending_arr[i]) # write an element from ascending sorted array
                file.write('\t') # add tabulation
                file.write(descending_arr[i]) # write an element from descending sorted array
                file.write('\n') # add new line

        file.close()
    except:
        print('Can\'t create the file')
        raise SystemExit(1) # An exception will be thrown and the program will terminate

if __name__ == '__main__':
    
    input_filename = input('Enter the absolute path to input file: ') # asking for an input filename
    print()
    str_array = read_from_file(input_filename) # reading array from file to a str_array variable

    ascending_sorted_array = quicksort_ascending(str_array) # sorting the specified array in ascending order
    descending_sorted_array = quicksort_descending(str_array) # sorting the specified array in descending order

    all_arrays = [] # initialize an array for terminal table
    all_arrays.append(['Original array', 'Ascending sorted array', 'Descending sorted array']) # adding the first line in the table

    for i in range(len(str_array)):
        all_arrays.append([str_array[i], ascending_sorted_array[i], descending_sorted_array[i]]) # adding an element from each array


    table = AsciiTable(all_arrays) # initializing Ascii table
    table.justify_columns[0] = 'center' # -----|
    table.justify_columns[1] = 'center' #      | ===> justiying all columns to center
    table.justify_columns[2] = 'center' # -----|
    print(table.table)

    output_filename = input('Enter the absolute path to output file: ') # asking for an output filename
   
    write_to_file(ascending_sorted_array, descending_sorted_array, output_filename) # writing ascending and descending sorted array in new file
