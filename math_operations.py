TYPES = [int, float, list]
    
def sum(x, y=None):
    assert type(x) in TYPES, (f"x must be 'int' or 'float'. Got {type(x)}")
    
    #--------------------- Tenho Y -----------------------------------------
    if y is not None:
        if type(y) not in TYPES:
            raise TypeError(f"y must be 'int' or 'float'. Got {type(y)}")
        
        #------- y == list-------
        if type(y) is list:
            #verifica se todos os elementos da lista são 'int' ou 'float'
            y_bool = [(type(value) == int or type(value) == float) for value in y]
            if not all(y_bool):
                raise TypeError(f"list must be only 'int' or 'float'.")
            
            #------- x == list-------
            if type(x) is list:
                x_bool = [(type(value) == int or type(value) == float) for value in x]
                if not all(x_bool):
                    raise TypeError(f"list must be only 'int' or 'float'.")
                
                soma = []
                i = 0
                
                if len(x) <= len(y):
                    while i < len(x):
                        soma.append(x[i]+y[i])
                        i+=1
                
                if len(y) < len(x):
                    while i < len(y):
                        soma.append(x[i]+y[i])
                        i+=1
                return soma
            
            soma = []
            for i in y:
                soma.append(i+x)
            return soma
                
        
        #------- x and y == list-------
        if type(x) is list:
            #verifica se todos os elementos da lista são 'int' ou 'float'
            x_bool = [(type(value) == int or type(value) == float) for value in x]
            if not all(x_bool):
                raise TypeError(f"list must be only 'int' or 'float'.")
            
            soma = []
            for i in x:
                soma.append(i+y)
            return soma
            
            
        
        return x + y
    
    
    #--------------------- Não tenho o Y -----------------------------------------
    if y is None:
        #------- x == list-------
        if type(x) is list:
            
            #verifica se todos os elementos da lista são 'int' ou 'float'
            x_bool = [(type(value) == int or type(value) == float) for value in x]
            if not all(x_bool):
                raise TypeError(f"list must be only 'int' or 'float'.")
            
            #caso seja 'int' ou 'float', soma os values da lista
            soma = 0
            for i in x:
                soma += i
            return soma
        

    return x





















def multiply(x, y=None):
    assert type(x) in TYPES, (f"x must be 'int' or 'float'. Got {type(x)}")
    
    if y is not None:
        if type(y) not in TYPES:
            raise TypeError(f"y must be 'int' or 'float'. Got {type(y)}")
        
        if type(y) is list:
            #verifica se todos os elementos da lista são 'int' ou 'float'
            y_bool = [(type(value) == int or type(value) == float) for value in y]
            if not all(y_bool):
                raise TypeError(f"list must be only 'int' or 'float'.")
            
            if type(x) is list:
                x_bool = [(type(value) == int or type(value) == float) for value in x]
                if not all(x_bool):
                    raise TypeError(f"list must be only 'int' or 'float'.")
                
                
                produto = []
                i = 0
                
                if len(y) <= len(x):
                    while i < len(y):
                        produto.append(x[i] * y[i])
                        i+=1
                
                if len(x) < len(y):
                    while i < len(x):
                        produto.append(x[i] * y[i])
                        i+=1
                return produto
            
            
            
            produto = []
            for i in y:
                produto.append(i*x)
            return produto
                
        
        
        if type(x) is list:
            #verifica se todos os elementos da lista são 'int' ou 'float'
            x_bool = [(type(value) == int or type(value) == float) for value in x]
            if not all(x_bool):
                raise TypeError(f"list must be only 'int' or 'float'.")
            
            produto = []
            for i in x:
                produto.append(i*y)
            return produto
        
        
        return x*y
    
    if y is None:
        if type(x) is list:
            
            #verifica se todos os elementos da lista são 'int' ou 'float'
            x_bool = [(type(value) == int or type(value) == float) for value in x]
            if not all(x_bool):
                raise TypeError(f"list must be only 'int' or 'float'.")
            
            #caso seja 'int' ou 'float', soma os values da lista
            produto = 1
            for i in x:
                produto *= i
            return produto
    
    return x