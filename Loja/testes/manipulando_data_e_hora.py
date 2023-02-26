import datetime

data = datetime.date.today()

hora = datetime.datetime.now()

print(data)
print(hora)

from tkinter import *
from time import strftime
#from tkinter.ttk import *

window = Tk()
window.title('Clock')


def retornar_tempo():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, retornar_tempo)


label = Label(window, font=('calibri', 40, 'bold'),
              background='black',
              foreground='white')
label.pack(anchor='center')
retornar_tempo()

mainloop()

# after
"""
Chama a funcao uma vez apos determinado tempo. 
-Tempo em milissegundos. 
-Funcao que deve ser chamada.
 Parâmetros adicionais são fornecidos como parâmetros para a chamada de função. 
 Identificador de retorno para cancelar o agendamento com after_cancel
 """

# strftime
'''
Converte uma tupla de tempo em uma string de acordo com uma especificação de formato. 
Consulte o manual de referência da biblioteca para códigos de formatação. 
Quando a tupla de tempo não está presente, a hora atual retornada por localtime() é usada
'''