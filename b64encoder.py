import base64
from tkinter.filedialog import askopenfilename
import tkinter as tk

root=tk.Tk()
root.withdraw()

file = open(askopenfilename(), 'rb')
file_content = file.read()

result = base64.b64encode(file_content).decode('ascii')

r=open("result.txt",'w+')
r.write(result)
r.close()
print('Konwersja zakończona sukcesem')