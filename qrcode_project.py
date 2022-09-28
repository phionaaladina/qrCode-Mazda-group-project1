# pip install qrcode
# Importing library
import qrcode
import os

#Algorithm

#ask user to input the text/data they would like to encode
#create a folder using os module that will save our QR codes if not exists (use a try except )
#display the contents of the folder showing the codes generated so far --def displayContents():  
#use random method to select a name for the qr code or allow the user to name the qr code. 
# But we will 1st check if name exists in folder --def nameQr():
#ability of user to determine the output size and color of the generated image--def createQR(userInput, color, length, height)

#functions, modules, venv, loops, control flow, 
#comparison ops, exceptions, handle files,break,continue and pass

#create our qr folder if not exists
def createFolder():
    path = "./myqrcodes/"
    try:
        os.mkdir(path) 
        return path       
    except FileExistsError as err:
        return err
    finally:
        return path   

#returns everything in path so far
def getPath(path):
    try:
        listedfiles =os.listdir(path)
        return listedfiles
    except FileNotFoundError as fnf_err:
        return fnf_err

#used to return all QR codes in our QR code folder
def displayAllQr():
    path2 = createFolder()
    try:
        QRlist = os.listdir(path2)
        for qr in QRlist:
          print(qr)
    except FileNotFoundError as fnf_err:
        return fnf_err

#check if name of Qr already exists
def nameQR(listedFiles, userInputName): 
   for file in listedFiles:
        if userInputName+".png" in listedFiles:
            print("Oops! File already exists. choose another name")
            break
        else:
            pass

def createQR(userInput, path, name, color, size):
    data = userInput
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=size,
    border=4,
    )
    qr.add_data(data)

    img = qr.make_image(fill_color=color, back_color="white")
    img.save(path+name+'.png')
   

def main():
    menu = input("Input 1 to generate a new QR code, Input 2 to list all QR codes Or input x to exit ")
    while True:
        if menu == "1":
            path = createFolder() #create folder if it doesnot exist
            listedfiles = getPath(path) #return the folder contents

            #get user input -->data, name, color and size
            userInputdata = input("Enter data or contents of QR code: ")
            userInputName = input("Enter name of QR code: ")
            userInputColor = input("Enter color of QR code: ")
            userInputSize = input("Enter size of QR code (from size 1 to 10): ")

            #check if name to be given to QR already exists
            nameQR(listedfiles, userInputName)

            #create QR code
            createQR(userInputdata, path, userInputName, userInputColor, userInputSize)

        elif menu =="2":
            displayAllQr()
            break

        elif menu =="x":
            break

        else:
            print("You have entered an unknown menu item")
            break
    
if __name__ == '__main__':
    main()

    