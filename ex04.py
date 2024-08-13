v1 = 0
v2 = 0 
v3 = 0
v4 = 0
for i in range(4):
    opçao = input("1-Bolsonaro 2-Lula 3-Kariri 4-Padre Kelvin")
    match opçao:
        case "1":
                Bolsonaro = input("Da que eu te dou outra")
                v1+=1
        case "2":
                Lula = input("Faz o L")
                v2+=1    
        case "3": 
                kariri = input("Eu quero eu posso ")
                v3+=1
        case "4": 
                Padre_Kelvin= input("Em nome do pai")
                v4+=1
                
print(f"O candidato 1 rescebeu " +str(v1) + " votos")      
print(f"O candidato 2 rescebeu " +str(v2) + " votos")  
print(f"O candidato 3 rescebeu " +str(v3) + " votos")        
print(f"O candidato 4 rescebeu " +str(v4) + " votos")
                    

            
            

