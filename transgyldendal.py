import tkinter
from googletrans import Translator
import clipboard

translate = Translator()
#___________________________def's____________________________


def inoutput(string, lang):
	detect = translate.detect(string)
	translation = translate.translate(string, src=detect.lang, dest=lang)
	return translation.text


def get_translation():
	translation = inoutput(entry.get(), variable.get())
	clipboard.copy(str(translation))
	var = translate.detect(entry.get())
	text = 'Your text has been translated and copied'
	dundeal = translate.translate(text, src='en', dest=var.lang)
	textvar.set(dundeal.text)
	

#___________________________config____________________________
mainwindow = tkinter.Tk()
mainwindow.geometry('280x80')
mainwindow.config(bg='white')
mainwindow.title('Gyldendal')

mainwindow.columnconfigure(0, weight=10)
mainwindow.columnconfigure(1, weight=10)
mainwindow.columnconfigure(2, weight=5)
mainwindow.columnconfigure(3, weight=10)
mainwindow.columnconfigure(4, weight=10)

mainwindow.rowconfigure(0, weight=10)
mainwindow.rowconfigure(1, weight=10)
mainwindow.rowconfigure(2, weight=5)
mainwindow.rowconfigure(3, weight=10)
mainwindow.rowconfigure(4, weight=10)

#___________________________visual____________________________
entry = tkinter.Entry(mainwindow)
entry.grid(row=0, column=2, columnspan=2)
variable = tkinter.StringVar(mainwindow)
variable.set('fr')
langspinner = tkinter.OptionMenu(mainwindow, variable, 'fr', 'en', 'de', 'ja', 'se', 'no', 'fi', 'da')
langspinner.grid(row=3, column=2)
button = tkinter.Button(mainwindow, command=get_translation, text='Translate')
button.grid(row=3, column=3)
textvar = tkinter.StringVar()
textvar.set(' ')
label = tkinter.Label(mainwindow, textvariable=textvar)
label.grid(row=4, column=2, columnspan=2)

mainwindow.maxsize(280, 80)
mainwindow.minsize(280, 80)
mainwindow.mainloop()
