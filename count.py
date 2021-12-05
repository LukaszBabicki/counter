ent_string = input(str("Enter a string: "))
    
print("Duplicate characters is: ");  
for i in range(0, len(ent_string)):  
    count = 1;  
    for j in range(i+1, len(ent_string)):  
        if(ent_string[i] == ent_string[j] and ent_string[i] != ' '):  
            count = count + 1;  
            ent_string = ent_string[:j] + '0' + ent_string[j+1:];  
    
    if(count > 1 and ent_string[i] != '0'):  
        print(ent_string[i]," - ",count);