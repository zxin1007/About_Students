import os, random


my_directory = r"C:\Users\Ariel\Desktop\About_Students\Abouts"

dict_of_abouts = {}

for root, dirname, fname in os.walk(my_directory):
    for current_file in fname:

        filepath = os.path.join(root, current_file)
        current_statement = ''
        
        with open(filepath, 'r') as file:
            for line in file:
                current_statement = "".join([current_statement, line])
        
        #you don't have to do this part.
        ##################################
        name = current_file.split('_') #this would be all that is needed if proper naming structure was used...
        if len(name) == 1:
            final_name = name[0]
        else:
            final_name = ''
            for word in name:
                if word.lower() == 'about':
                    continue
                else:
                    final_name = " ".join([final_name, word])
                    
                    
        ##################################
        
        dict_of_abouts[final_name] = current_statement

random_key = random.choice(list(dict_of_abouts.keys()))

print(random_key,":\t", dict_of_abouts[random_key], sep = '')

