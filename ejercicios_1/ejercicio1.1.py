#promedio de duracion
otros_curso_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#diferencias de duracion
diferencia_con_min = 100 - dalto_curso / otros_curso_min * 100
diferencia_con_max = 100 - round((dalto_curso / otros_cursos_max),3) * 100
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#calculando el porcentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - round((otros_cursos_promedio / crudo_promedio),3) * 100
tiempo_vacio_dalto = 100 - round((dalto_curso / crudo_dalto),3) * 100




#mostrando las diferencias de duracion (ejercicio a)
print("--------------")
print("El curso de dalto:")
print(f'dura un {diferencia_con_min}% menos que el mas rapido')
print(f'dura un {diferencia_con_max}% menos que el mas lento')
print(f'dura un {diferencia_con_promedio}% menos que el promedio')

#mostrando la cantidad de espacios vacios removidos
print("--------------")
print(f'Un curso elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'El curso de dalto elimina un {tiempo_vacio_dalto}% de tiempo vacio')

#mostrando diferencias si los cursos duraran 10 horas
print("--------------")
print(f'Ver 10 horas del curso de dalto equivalen a ver {round((otros_cursos_promedio / dalto_curso),2) * 10} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivalen a ver {round((dalto_curso / otros_cursos_promedio),4) * 10} horas de un curso de dalto')
