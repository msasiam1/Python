def info():
    print("Enter ID, First Name, Last Name, Dept, Date")
    d = []
    
    
    for i in range(5):
        data = input(f"Enter field {i+1}: ")  
        d.append(data)
        
    
    print(f"{d[0]}_{d[1]}_{d[2]}_{d[3]}_{d[4]}")
    
    


info()