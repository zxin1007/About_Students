import os


my_directory = r"C:\Users\Ariel\Desktop\About_Students\Abouts"


for root, dirname, fname in os.walk(my_directory):
    for current_file in fname:
        
        #print(current_file)
        filepath = os.path.join(root, current_file)
        with open(filepath, 'r') as file:
            try:
                for line in file:
                    print(line)
            except Exception:
                print('no go')


        
