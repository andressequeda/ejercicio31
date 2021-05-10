distancia  =  int ( input ( "Ingrese la distancia a recorrer (en kilómetros):" ))
dias  =  int ( input ( "Ingrese los días de estancia:" ))
pasaje  =  5000  *  distancia
si  distancia  >  1000  y  dias  >  7 :
    imprimir ( pasaje  - ( pasaje  *  0.15 ))
otra cosa :
    print ( "El precio del pasaje es" , pasaje )