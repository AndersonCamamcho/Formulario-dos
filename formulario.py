import datetime

# Variables:
nombre = []
apellido = []
edad = []
fecha_nacimiento = []
fecha_actual = datetime.datetime.now()
bandera = 0
terminar_app = False


# Inicio del programa

while True:
    bandera += 1
# Validar nuevo registro
    if bandera > 1:
        while True:
            agregar_formulario = input(" ¿Desea crear otro registro? SI/NO: ")

            if agregar_formulario == "SI":
                break
            elif agregar_formulario == "NO":
                terminar_app = True
                break
            else:
                print("Respuesta no valida, responda SI, si desea continuar y NO si no desea hacerlo.")



    if terminar_app:
        print("Registro esxitoso, gracias su participación.")
        break


# Inicio obtención de nombre para el formulario:

    while True:

        nombre_recibido = input(" » Ingrese aqui un nombre, no mayor a 50 caracteres: ")
        validar_nombre = len(nombre_recibido)
        if validar_nombre <= 50 and not nombre_recibido[0].isspace():
            nombre.append(nombre_recibido)
            break
        else:
            print("Entrada incorrecta.")




# Inicio obtención de apellido para el formulario:

    while True:

        apellido_recibido = input(" » Ingrese aqui apellidos, no mayor a 50 caracteres: ")
        validar_apellido = len(apellido_recibido)
        if validar_apellido <= 50 and not apellido_recibido[0].isspace():
            apellido.append(apellido_recibido)
            break
        else:
            print("Entrada incorrecta.")


    # Inicio obtención de edad para el formulario:

    while True:
        try:
            edad_formulario = int(input(" » Ingrese aqui su edad: "))
            if 18 <= edad_formulario <= 100:
                edad.append(edad_formulario)
                break
            else:
                print("Recuerde que la edad debe estar entre 18 y 100 años, por favor intente de nuevo.")
        except ValueError:
            print("No esta ingresando numeros enteros, por favor intente de nuevo.")



    # Inicio obtención de fecha de expeidción para el formulario:

    while True:
        try:
            fecha_ingresada = input(
                " » Ingrese aqui su fecha de nacimiento con el siguiente formato: dia/mes/año(completo):   ")
            fecha_formulario = datetime.datetime.strptime(fecha_ingresada, "%d/%m/%Y")

            fecha_por_validar = fecha_actual.year - fecha_formulario.year
            if 0 <= fecha_por_validar <= 100:
                fecha_nacimiento.append(fecha_formulario)
                break
            else:
                print("La fecha ingresada no debe ser mayor a 100, ni menor a 0 años, intente de nuevo.")


        except ValueError:
            print("Esta ingresando un formato incorrecto, recuerde que debe ser: dia/mes/año(completo)")