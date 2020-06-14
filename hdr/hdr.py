from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter.messagebox import showerror, showinfo
from PIL import Image, ImageTk
import numpy as np
import os

canvasSize = (256,256)
resultImage = None

# to prevent garbage collector from deleting thumbnail after genThumbnail()
resultImageThumbnailPhotoImage = None

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
  global resultImage
  resultImage = Image.frombytes("RGB",size,resultArr)
  genThumbnail()
  savehdrButton["state"] = "normal"
  showhdrButton["state"] = "normal"

def showHDR():
  print("wyświetlanie")
  global resultImage
  resultImage.show(title="hdr")

def saveHDR():
  print("zapisywanie")
  path = asksaveasfilename(filetypes = [('JPEG', '*.jpg'),('PNG', '*.png'),('BMP', '*.bmp')],defaultextension ='.jpg')
  print("path: ",path)
  if path:
    global resultImage
    resultImage.save(path)
    showinfo(message="Zapisano")

def genThumbnail():
  global canvasSize
  global resultImage
  global resultImageThumbnailPhotoImage
  img = resultImage.copy()
  img.thumbnail(canvasSize)
  resultImageThumbnailPhotoImage = ImageTk.PhotoImage(img)
  thumbnailCanvas.delete("IMG")
  coords = ((canvasSize[0]-resultImageThumbnailPhotoImage.width())/2,(canvasSize[1]-resultImageThumbnailPhotoImage.height())/2)
  thumbnailCanvas.create_image(coords[0],coords[1],anchor=NW,image=resultImageThumbnailPhotoImage,tags="IMG")

root = Tk()
root.title("HDR")
root.resizable(False, False)

l = Label(root, text="Dodane obrazy 0")
l.grid(row=0, pady=2)

imageList = Listbox(root, width=80,height=10, selectmode=MULTIPLE)
imageList.grid(row=1, pady=6)

controlsFrame = Frame(root)
controlsFrame.grid(row=2)

delButton = Button(controlsFrame, text="usuń zaznaczone obrazy", width=30, command=removeFiles)
delButton.grid(row=0,column=0,padx=10)

addButton = Button(controlsFrame, text="dodaj obrazy", width=30, command=loadFile)
addButton.grid(row=0,column=1,padx=10)

hdrControlsFrame = Frame(root)
hdrControlsFrame.grid(row=3)

hdrButton = Button(hdrControlsFrame, text="HDR", height=10, width=7, bg="#c4e9f5", command=doHDR)
hdrButton.grid(row=0,column=0,pady=2)

thumbnailCanvas = Canvas(hdrControlsFrame, width=canvasSize[0], height=canvasSize[1])
thumbnailCanvas.grid(row=0,column=1)

showsaveButtonsFrame = Frame(hdrControlsFrame)
showsaveButtonsFrame.grid(row=0,column=2)

showhdrButton = Button(showsaveButtonsFrame, text="pokaż obraz hdr", height=2, width=20, command=showHDR)
showhdrButton.grid(row=0,pady=2)
showhdrButton["state"] = "disabled"

savehdrButton = Button(showsaveButtonsFrame, text="zapisz obraz hdr", height=2, width=20, command=saveHDR)
savehdrButton.grid(row=1,pady=2)
savehdrButton["state"] = "disabled"

root.mainloop()