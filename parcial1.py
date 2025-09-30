
class Usuario:
         def _init_ (self, nomusuario ,correo, contrasena):
            self.nomusuario= nomusuario
            self._correo = correo
            self._contrasena = contrasena

            print (f' ingresa tu correo electronico: {self._correo}')
            print (f' ingresa tu correo electronico: {self._correo}')
            print (f' ingresa la contraseña que quieres dejar: {self._contrasena} ')

class Libros:
         def _init_ (self, categoria):
            self.categoria= categoria
            
            def categoria (self,romance, ficcion, terror):
                self.romace = romance
                self.ficcion= ficcion
                self.terror= terror

            print (f' ingresa la categoria del libro: {self.categoria}')

class Nuevoslib:
         def _init_ (self, nomlibro, cantidad):
            self.nomlibro= nomlibro
            self.cantidad= cantidad

            print (f' como se llama el nuevo libro: {self.nomlibro}')
            print (f' cuantos libros son: {self.cantidad}')