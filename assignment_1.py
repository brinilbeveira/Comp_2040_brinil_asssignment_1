with open('input_1.txt') as file_object:
    lines = file_object.readlines()
    print(lines)
    
filename ='output_1.txt'
with open( filename, 'a') as file_object:
    file_object.write("youu are awesomeeee")