from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from PIL import Image
import numpy as np

def loadFile():
  filenames = askopenfilename(filetypes=[("Image files", ".jpg .png .bmp")], multiple=True)
  for filename in filenames:
    if filename not in imageList.get(0,imageList.size()):
      imageList.insert("end", filename)
  l.config(text="Dodane obrazy " + str(imageList.size()))

def removeFiles():
  for idx in reversed(imageList.curselection()):
    imageList.delete(idx)
  l.config(text="Dodane obrazy " + str(imageList.size()))

def doHDR():
  imagesPaths = imageList.get(0,imageList.size())
  
  if len(imagesPaths) == 0:
    showerror(title="Error", message="Nie podano żadnych obrazów")
    return

  resultArr = 0
  print("sumowanie obrazów")
  for (path,idx) in zip(imagesPaths,range(len(imagesPaths))):
    print(idx+1,"/",len(imagesPaths))
    im = Image.open(path)
    try:
      resultArr += np.asarray(im).astype("float")
    except:
      showerror(title="Error", message="Obrazy nie są tych samych rozmiarów! Operacje anulowano")
      return
    im.close()
  resultArr = np.round(resultArr / len(imagesPaths)).astype("uint8")

  print("tworzenie nowego obrazu")
  size = (np.size(resultArr, axis=1),np.size(resultArr, axis=0))
  result = Image.frombytes("RGB",size,resultArr)

  print("wyświetlenie")
  result.show(title="hdr")

root = Tk()
root.title("HDR")
root.resizable(False, False)

l = Label(root, text="Dodane obrazy 0")
l.grid(row=0, pady=2)

imageList = Listbox(root, width=100,height=10, selectmode=MULTIPLE)
imageList.grid(row=1, pady=6)

controlsFrame = Frame(root)
controlsFrame.grid(row=2)

delButton = Button(controlsFrame, text="usuń zaznaczone obrazy", width=40, command=removeFiles)
delButton.grid(row=0,column=0,padx=10)

addButton = Button(controlsFrame, text="dodaj obrazy", width=40, command=loadFile)
addButton.grid(row=0,column=1,padx=10)

hdrButton = Button(root, text="HDR", width=40, height=3, bg="#c4e9f5", command=doHDR)
hdrButton.grid(row=3,pady=6)

root.mainloop()