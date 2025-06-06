from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import numpy as np



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #Title
        title_lbl = Label(self.root, text=" TRAIN DATA SET ",font=("times new roman", 35, "bold"), bg="white", fg="maroon")
        title_lbl.place(x=0, y=0,width=1530,height=45)

        #Image 1
        img_top = Image.open("images/trainingimg1.png").resize((1530, 325), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl1 = Label(self.root, image=self.photoimg_top)
        f_lbl1.place(x=5, y=55, width=1530, height=325)

        #Button middle
        bt1_1 = Button(self.root , text="TRAIN DATA", command=self.train_classifier,cursor="hand2", font=("times new roman",30, "bold"), bg="tan", fg="black")
        bt1_1.place(x=0, y=380, width=1540, height=60)

        #Image 2
        img_bottom = Image.open("images/trainingimg2.png").resize((1530, 325), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl1 = Label(self.root, image=self.photoimg_bottom)
        f_lbl1.place(x=5, y=440, width=1530, height=325)

    
    #=============== train classifier function ===============

    def train_classifier(self):
        data_dir = ("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')      # gray scale image
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1) == 13
        ids=np.array(ids)

        # ======= train the classifer and save ======

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifiers.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Data Set completed. ")

        





if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()