class Bloque: 
    def __init__(self): 
        self.instrucciones = [] 
    def agregarInstruction(self, instruccion): 
        self.instrucciones.append(instruccion) 
class Si: 
    def __init__(self, condicion, entonces, si_no): 
        self.condicion = condicion 
        self.entonces = entonces 
        self.si_no = si_no 
class MientrasQue: 
    def __init__(self, condicion, bloque): 
        self.condicion = condicion 
        self.bloque = bloque 
class Mostrar: 
    def __init__(self, mensaje): 
        self.mensaje = mensaje 

mostrar_ok = Mostrar('"OK"') 
mostrar_ko = Mostrar('"KO"') 
alternativa = Si("2 + 2 == 4", mostrar_ok, mostrar_ko) 
bloque_alternativa = Bloque() 
bloque_alternativa.agregarInstruccion(alternativa) 
bucle = MientrasQue(True, bloque_alternativa) 