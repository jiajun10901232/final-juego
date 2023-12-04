import random

class jugador():
    rondas = 4
    def __init__(self,player1,player2,player3,puntos):
        self.__player1 = player1
        self.__player2 = player2
        self.__player3 = player3
        self.__puntos = puntos

    def juego_de_dardos(self):
        print("player ")
        print(self.__player1,self.__player2,self.__player3)
        print("el puntos de cada jugador son de ", self.__puntos)
        print("los puntos que teneis se tiene que reducir a 0 o menos")
        rondas = 1
        while (True):
            
            print("ronda: ", rondas)  
            if(rondas == 4):
                print("se acaba la ronda")
                return False
            else: 
                  
                
                #jugador1
                for tiros in range(3):
                    self.__player1
                    tiros = tiros +1
                    print("tira el",self.__player1, " : " , tiros  )
                    puntajeinicial = self.__puntos
                    p1 = random.randrange(0,50)
                    p2 = random.randrange(0,50)
                    p3 = random.randrange(0,50)
                    print("primera tirada" ,p1 ,
                     "segunda tirada",p2,
                     "tercera tirada",p3 )
                    suma=p1+p2+p3
                    resultado = puntajeinicial - suma

                    if(resultado <=0):
                        print(resultado,"ha ganado el ",self.__player2 )
                        return False
                    elif(resultado > 0) :
                        print("sigue jugando")   
                    elif(resultado > 0):
                        print("nadie gana")   
                #jugador2         
                for tiros in range(3):
                    self.__player2
                    tiros = tiros +1
                    print("tira el",self.__player2, " : " , tiros  )
                    puntajeinicial = self.__puntos
                    pl1 = random.randrange(0,50)
                    pl2 = random.randrange(0,50)
                    pl3 = random.randrange(0,50)
                    print("primera tirada" ,pl1 , "segunda tirada",pl2,"tercera tirada",pl3 )
                    suma=pl1+pl2+pl3
                    resultado = puntajeinicial - suma

                    if(resultado <=0):
                        print(resultado,"ha ganado el ",self.__player2 )
                        return False
                    elif(resultado > 0) :
                        print("sigue jugando")   
                    elif(resultado > 0):
                        print("nadie gana")   
                #jugadr3        
                for tiros in range(3):
                    self.__player3
                    tiros = tiros +1
                    print("tira el",self.__player3, " : " , tiros  )
                    puntajeinicial = self.__puntos
                    pu1 = random.randrange(0,50)
                    pu2 = random.randrange(0,50)
                    pu3 = random.randrange(0,50)
                    print("primera tirada" ,pu1 , "segunda tirada",pu2,"tercera tirada",pu3 )
                    suma=pu1+pu2+pu3
                    resultado = puntajeinicial - suma

                    if(resultado <=0):
                        print(resultado,"ha ganado el ",self.__player3 )
                        return False
                    elif(resultado > 0) :
                        print("sigue jugando")   
                    elif(resultado > 0):
                        print("nadie gana")
                        
            rondas += 1                    


player1 = input(" dime tu nombre: ")
player2 = input(" dime tu nombre: ")
player3 = input(" dime tu nombre: ")

juego = jugador(player1,player2,player3,121)
juego.juego_de_dardos()
    
