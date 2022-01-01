from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import PIL.ImageTk
import webbrowser
import PIL.Image
import shutil
import json
import os


class FileOrganizer:
    def __init__(self):
        self.window = Tk()
        
        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()
        
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.resizable(False, False)
        self.window.title("File Organizer")
        self.window.iconbitmap("icon.ico")
        self.window.attributes("-alpha", 1)
        self.window.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.dictExtensions = {
            'Audio Files': ('.mp3', '.m4a', '.wav', '.flac'),
            'Video Files': ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
            'Document Files': ('.doc', '.pdf', '.txt')
        }

        self.questionsList = [
            "Forgot Question",
            "Favourite Food",
            "Birth Place",
            "Best Friend",
            "First Pet Name",
            "School Name",
            "Home Town"
        ]

        self.username_1 = StringVar()
        self.password_1 = StringVar()
        self.rememberUser_1 = BooleanVar()

        self.username_2 = StringVar()
        self.password_2 = StringVar()

        self.question_1 = StringVar()
        self.answer_1 = StringVar()

        self.username_3 = StringVar()
        self.question_2 = StringVar()
        self.answer_2 = StringVar()

        self.folderPath_1 = StringVar()

        self.oldPassword_1 = StringVar()
        self.newPassword_1 = StringVar()
        self.confirmPassword_1 = StringVar()

        self.backgroundImage = PIL.Image.open(r"lib\background.jpg")
        self.backgroundImage = self.backgroundImage.resize((self.width, self.height))
        self.backgroundImage = PIL.ImageTk.PhotoImage(self.backgroundImage)

        self.userImage = PIL.Image.open(r"lib\user.png")
        self.userImage = self.userImage.resize((50, 50))
        self.userImage = PIL.ImageTk.PhotoImage(self.userImage)

        self.passwordImage = PIL.Image.open(r"lib\password.png")
        self.passwordImage = self.passwordImage.resize((50, 50))
        self.passwordImage = PIL.ImageTk.PhotoImage(self.passwordImage)

        self.questionImage = PIL.Image.open(r"lib\question.png")
        self.questionImage = self.questionImage.resize((50, 50))
        self.questionImage = PIL.ImageTk.PhotoImage(self.questionImage)

        self.answerImage = PIL.Image.open(r"lib\answer.png")
        self.answerImage = self.answerImage.resize((50, 50))
        self.answerImage = PIL.ImageTk.PhotoImage(self.answerImage)

        self.folderImage = PIL.Image.open(r"lib\folder.png")
        self.folderImage = self.folderImage.resize((50, 50))
        self.folderImage = PIL.ImageTk.PhotoImage(self.folderImage)

        self.facebookImage = PIL.Image.open(r"lib\facebook.png")
        self.facebookImage = self.facebookImage.resize((40, 40))
        self.facebookImage = PIL.ImageTk.PhotoImage(self.facebookImage)

        self.twitterImage = PIL.Image.open(r"lib\facebook.png")
        self.twitterImage = self.twitterImage.resize((40, 40))
        self.twitterImage = PIL.ImageTk.PhotoImage(self.twitterImage)

        self.youtubeImage = PIL.Image.open(r"lib\youtube.png")
        self.youtubeImage = self.youtubeImage.resize((40, 40))
        self.youtubeImage = PIL.ImageTk.PhotoImage(self.youtubeImage)

        self.instagramImage = PIL.Image.open(r"lib\instagram.png")
        self.instagramImage = self.instagramImage.resize((40, 40))
        self.instagramImage = PIL.ImageTk.PhotoImage(self.instagramImage)

        self.backgroundLabel = Label(self.window, image=self.backgroundImage)
        self.backgroundLabel.image = self.backgroundImage
        self.backgroundLabel.pack()

        self.setMainWindowFrames()

        self.window.mainloop()

    def setMainWindowFrames(self):
        self.setMainWindowLoginFrame()
        self.setMainWindowSideFrame()

    def setMainWindowLoginFrame(self):
        self.loginFrame_1 = Frame(self.window, width=650, height=550, bg="#aaaac6", bd=0)
        self.loginFrame_1.place(x=250, y=170)

        self.loginLabel_1 = Label(self.loginFrame_1, text="LOGIN FORM", bg="#aaaac6", font=("fira code", 30, "bold"), bd=0)
        self.loginLabel_1.place(x=0, y=30, relwidth=1)

        self.usernameLabel_1 = Label(self.loginFrame_1, text="Username", bg="#aaaac6", font=("fira code", 22, "bold"), image=self.userImage, compound=LEFT, padx=10, bd=0)
        self.usernameLabel_1.image = self.userImage
        self.usernameLabel_1.place(x=30, y=130)

        self.usernameEntry_1 = Entry(self.loginFrame_1, width=20, font=("fira code", 18, "bold"), textvariable=self.username_1, bd=0)
        self.usernameEntry_1.place(x=300, y=140)
        self.usernameEntry_1.focus_set()

        self.passwordLabel_1 = Label(self.loginFrame_1, text="Password", bg="#aaaac6", font=("fira code", 22, "bold"), image=self.passwordImage, compound=LEFT, padx=10, bd=0)
        self.passwordLabel_1.image = self.passwordImage
        self.passwordLabel_1.place(x=30, y=230)

        self.passwordEntry_1 = Entry(self.loginFrame_1, width=20, font=("fira code", 18, "bold"), textvariable=self.password_1, bd=0, show="*")
        self.passwordEntry_1.place(x=300, y=240)

        self.rememberCheckButton_1 = Checkbutton(self.loginFrame_1, text="Remember me", font=("fira code", 18, "bold"), bg="#aaaac6", variable=self.rememberUser_1)
        self.rememberCheckButton_1.place(x=300, y=300)

        self.loginButton_1 = Button(self.loginFrame_1, width=20, text="LOGIN", font=("fira code", 18, "bold"), bg="#36802d", bd=0, command=self.loginUser)
        self.loginButton_1.place(x=300, y=400)

        self.window.bind("<Tab>", self.autoFillPassword)
        self.window.bind("<Return>", self.loginUser)

        self.usernameEntry_1.bind("<Enter>", self.hoverEnter)
        self.usernameEntry_1.bind("<Leave>", self.hoverLeave)

        self.passwordEntry_1.bind("<Enter>", self.hoverEnter)
        self.passwordEntry_1.bind("<Leave>", self.hoverLeave)

        self.rememberCheckButton_1.bind("<Enter>", self.hoverEnter)
        self.rememberCheckButton_1.bind("<Leave>", self.hoverLeave)

        self.loginButton_1.bind("<Enter>", self.hoverEnter)
        self.loginButton_1.bind("<Leave>", self.hoverLeave)

    def setMainWindowSideFrame(self):
        self.sideFrame_1 = Frame(self.window, width=350, height=550, bd=0)
        self.sideFrame_1.place(x=900, y=170)

        self.accountLabel_1 = Label(self.sideFrame_1, text="CREATE NEW ACCOUNT", font=("fira code", 16, "bold"), bd=0)
        self.accountLabel_1.place(x=0, y=30, relwidth=1)

        self.loginButton_2 = Button(self.sideFrame_1, width=17, text="LOG IN", font=("fira code", 16, "bold"), bg="#36802d", bd=0, command=self.setMainWindowLoginFrame)
        self.loginButton_2.place(x=50, y=100)

        self.signupButton_1 = Button(self.sideFrame_1, width=17, text="SIGN UP", font=("fira code", 16, "bold"), bg="#00FFFF", bd=0, command=self.setMainWindowSignupFrame)
        self.signupButton_1.place(x=50, y=200)

        self.forgotPasswordButton_1 = Button(self.sideFrame_1, width=17, text="FORGOT PASSWORD", font=("fira code", 16, "bold"), bg="#FFA500", bd=0, command=self.setMainWindowForgotPasswordFrame)
        self.forgotPasswordButton_1.place(x=50, y=300)

        self.followUsLabel_1 = Label(self.sideFrame_1, text="FOLLOW US ON", font=("fira code", 16, "bold"), fg="red", bd=0)
        self.followUsLabel_1.place(x=0, y=400, relwidth=1)

        self.facebookButton_1 = Button(self.sideFrame_1, image=self.facebookImage, bd=0, command=self.facebook)
        self.facebookButton_1.image = self.facebookImage
        self.facebookButton_1.place(x=30, y=470)

        self.twitterButton_1 = Button(self.sideFrame_1, image=self.twitterImage, bd=0, command=self.twitter)
        self.twitterButton_1.image = self.twitterImage
        self.twitterButton_1.place(x=110, y=470)

        self.youtubeButton_1 = Button(self.sideFrame_1, image=self.youtubeImage, bd=0, command=self.youtube)
        self.youtubeButton_1.image = self.youtubeImage
        self.youtubeButton_1.place(x=190, y=470)

        self.instagramButton_1 = Button(self.sideFrame_1, image=self.instagramImage, bd=0, command=self.instagram)
        self.instagramButton_1.image = self.instagramImage
        self.instagramButton_1.place(x=280, y=470)

    def setMainWindowSignupFrame(self):
        self.signupFrame_1 = Frame(self.window, width=650, height=550, bg="#aaaac6", bd=0)
        self.signupFrame_1.place(x=250, y=170)

        self.signupLabel_1 = Label(self.signupFrame_1, text="SIGNUP FORM", bg="#aaaac6", font=("fira code", 30, "bold"), bd=0)
        self.signupLabel_1.place(x=0, y=30, relwidth=1)

        self.usernameLabel_2 = Label(self.signupFrame_1, text="Username", bg="#aaaac6", font=("fira code", 22, "bold"), image=self.userImage, compound=LEFT, padx=10, bd=0)
        self.usernameLabel_2.image = self.userImage
        self.usernameLabel_2.place(x=30, y=130)

        self.usernameEntry_2 = Entry(self.signupFrame_1, width=20, font=("fira code", 18, "bold"), textvariable=self.username_2, bd=0)
        self.usernameEntry_2.place(x=300, y=140)
        self.usernameEntry_2.focus_set()

        self.passwordLabel_2 = Label(self.signupFrame_1, text="Password", bg="#aaaac6", font=("fira code", 22, "bold"), image=self.passwordImage, compound=LEFT, padx=10, bd=0)
        self.passwordLabel_2.image = self.passwordImage
        self.passwordLabel_2.place(x=30, y=230)

        self.passwordEntry_2 = Entry(self.signupFrame_1, width=20, font=("fira code", 18, "bold"), textvariable=self.password_2, bd=0, show="*")
        self.passwordEntry_2.place(x=300, y=240)

        self.questionsCombobox_1 = ttk.Combobox(self.signupFrame_1, width=16, values=self.questionsList, font=("fira code", 14, "bold"), textvariable=self.question_1)
        self.questionsCombobox_1.place(x=40, y=340)
        self.questionsCombobox_1.current(0)

        self.answerEntry_1 = Entry(self.signupFrame_1, width=20, font=("fira code", 18, "bold"), textvariable=self.answer_1, bd=0)
        self.answerEntry_1.place(x=300, y=340)

        self.signupButton_2 = Button(self.signupFrame_1, width=20, text="SIGNUP", font=("fira code", 18, "bold"), bg="#00FFFF", bd=0, command=self.registerUser)
        self.signupButton_2.place(x=300, y=440)

        self.window.bind("<Return>", self.registerUser)

    def setMainWindowForgotPasswordFrame(self):
        self.forgotPasswordFrame_1 = Frame(self.window, width=650, height=550, bg="#aaaac6", bd=0)
        self.forgotPasswordFrame_1.place(x=250, y=170)

        self.forgotPasswordLabel_1 = Label(self.forgotPasswordFrame_1, text="FORGOT PASSWORD FORM", bg="#aaaac6", font=("fira code", 30, "bold"), bd=0)
        self.forgotPasswordLabel_1.place(x=0, y=30, relwidth=1)

        self.usernameLabel_3 = Label(self.forgotPasswordFrame_1, text="Username", bg="#aaaac6", font=("fira code", 22, "bold"), image=self.userImage, compound=LEFT, padx=10, bd=0)
        self.usernameLabel_3.image = self.userImage
        self.usernameLabel_3.place(x=30, y=130)

        self.usernameEntry_3 = Entry(self.forgotPasswordFrame_1, width=20, font=("fira code", 18, "bold"), textvariable=self.username_3, bd=0)
        self.usernameEntry_3.place(x=300, y=140)
        self.usernameEntry_3.focus_set()

        self.questionLabel_1 = Label(self.forgotPasswordFrame_1, text="Question", bg="#aaaac6", font=("fira code", 22, "bold"), image=self.questionImage, compound=LEFT, padx=10, bd=0)
        self.questionLabel_1.image = self.questionImage
        self.questionLabel_1.place(x=30, y=230)

        self.questionsCombobox_2 = ttk.Combobox(self.forgotPasswordFrame_1, width=20, values=self.questionsList, font=("fira code", 16, "bold"), textvariable=self.question_2)
        self.questionsCombobox_2.place(x=300, y=240)
        self.questionsCombobox_2.current(0)

        self.answerLabel_1 = Label(self.forgotPasswordFrame_1, text="Answer", bg="#aaaac6", font=("fira code", 22, "bold"), image=self.answerImage, compound=LEFT, padx=10, bd=0)
        self.answerLabel_1.image = self.answerImage
        self.answerLabel_1.place(x=30, y=330)

        self.answerEntry_2 = Entry(self.forgotPasswordFrame_1, width=20, font=("fira code", 18, "bold"), textvariable=self.answer_2, bd=0)
        self.answerEntry_2.place(x=300, y=340)

        self.forgotPasswordButton_2 = Button(self.forgotPasswordFrame_1, width=20, text="SUBMIT", font=("fira code", 18, "bold"), bg="#FFA500", bd=0, command=self.retrievePassword)
        self.forgotPasswordButton_2.place(x=300, y=440)

        self.window.bind("<Return>", self.retrievePassword)

    def setOrganizerFrames(self):
        self.setOrganizerLeftFrame()
        self.setOrganizerRightFrame()

    def setOrganizerLeftFrame(self):
        self.organizerLeftFrame_1 = Frame(self.window, width=650, height=550, bg="#aaaac6", bd=0)
        self.organizerLeftFrame_1.place(x=250, y=170)

        self.organizeFilesLabel_2 = Label(self.organizerLeftFrame_1, text="ORGANIZE FILES", bg="#aaaac6", font=("fira code", 30, "bold"), bd=0)
        self.organizeFilesLabel_2.place(x=0, y=30, relwidth=1)

        self.pathLabel_1 = Label(self.organizerLeftFrame_1, text="Folder Path", bg="#aaaac6", font=("fira code", 16, "bold"), image=self.folderImage, compound=LEFT, padx=10, bd=0)
        self.pathLabel_1.image = self.folderImage
        self.pathLabel_1.place(x=30, y=130)

        self.pathEntry_1 = Entry(self.organizerLeftFrame_1, width=20, font=("fira code", 18, "bold"), textvariable=self.folderPath_1, bd=0)
        self.pathEntry_1.place(x=300, y=140)
        self.pathEntry_1.focus_set()

        self.changePasswordButton_1 = Button(self.organizerLeftFrame_1, text="Change Password", font=("fira code", 16, "bold"), bg="#aaaac6", bd=0, fg="blue", command=self.setChangePasswordFrame)
        self.changePasswordButton_1.place(x=300, y=200)

        self.organizeButton_1 = Button(self.organizerLeftFrame_1, width=20, text="Organize", font=("fira code", 18, "bold"), bg="#36802d", bd=0, command=self.organizeFiles)
        self.organizeButton_1.place(x=300, y=300)

        self.window.bind("<Return>", self.organizeFiles)

    def setChangePasswordFrame(self):
        self.changePasswordFrame_1 = Frame(self.window, width=650, height=550, bg="#aaaac6", bd=0)
        self.changePasswordFrame_1.place(x=250, y=170)

        self.changePasswordLabel_1 = Label(self.changePasswordFrame_1, text="Change Password", bg="#aaaac6", font=("fira code", 30, "bold"), bd=0)
        self.changePasswordLabel_1.place(x=0, y=30, relwidth=1)

        self.oldPasswordLabel_1 = Label(self.changePasswordFrame_1, text="Old Password", bg="#aaaac6", font=("fira code", 14, "bold"), image=self.passwordImage, compound=LEFT, padx=10, bd=0)
        self.oldPasswordLabel_1.image = self.passwordImage
        self.oldPasswordLabel_1.place(x=30, y=130)

        self.oldPasswordEntry_1 = Entry(self.changePasswordFrame_1, width=20, font=("fira code", 18, "bold"), textvariable=self.oldPassword_1, bd=0)
        self.oldPasswordEntry_1.place(x=300, y=140)
        self.oldPasswordEntry_1.focus_set()

        self.newPasswordLabel_1 = Label(self.changePasswordFrame_1, text="New Password", bg="#aaaac6", font=("fira code", 14, "bold"), image=self.passwordImage, compound=LEFT, padx=10, bd=0)
        self.newPasswordLabel_1.image = self.passwordImage
        self.newPasswordLabel_1.place(x=30, y=210)

        self.newPasswordEntry_1 = Entry(self.changePasswordFrame_1, width=20, font=("fira code", 18, "bold"), textvariable=self.newPassword_1, bd=0)
        self.newPasswordEntry_1.place(x=300, y=220)

        self.confirmPasswordLabel_1 = Label(self.changePasswordFrame_1, text="Confirm Password", bg="#aaaac6", font=("fira code", 14, "bold"), image=self.passwordImage, compound=LEFT, padx=10, bd=0)
        self.confirmPasswordLabel_1.image = self.passwordImage
        self.confirmPasswordLabel_1.place(x=30, y=290)

        self.confirmPasswordEntry_1 = Entry(self.changePasswordFrame_1, width=20, font=("fira code", 18, "bold"), textvariable=self.confirmPassword_1, bd=0)
        self.confirmPasswordEntry_1.place(x=300, y=300)

        self.changePasswordButton_2 = Button(self.changePasswordFrame_1, width=20, text="Change Password", font=("fira code", 18, "bold"), bg="#FFA500", bd=0, command=self.changePassword)
        self.changePasswordButton_2.place(x=300, y=400)

        self.window.bind("<Return>", self.changePassword)

    def setHistoryFrame(self):
        self.historyFrame_1 = Frame(self.window, width=650, height=550, bg="#aaaac6", bd=0)
        self.historyFrame_1.place(x=250, y=170)

        self.historyLabel_1 = Label(self.historyFrame_1, text="History", bg="#aaaac6", font=("fira code", 30, "bold"), bd=0)
        self.historyLabel_1.place(x=0, y=30, relwidth=1)

        self.historyFrame_2 = Frame(self.historyFrame_1, bg="#aaaac6", bd=0)
        self.historyFrame_2.place(x=0, y=150)
        
        self.historyScroll_1 = Scrollbar(self.historyFrame_2)
        self.historyScroll_1.pack(side=RIGHT, fill=Y)

        self.historyScroll_2 = Scrollbar(self.historyFrame_2, orient=HORIZONTAL)
        self.historyScroll_2.pack(side=BOTTOM, fill=X)

        self.historyText_1 = Text(self.historyFrame_2, height=10, width=57, bg="#aaaac6", fg="green", font=("fira code", 12, "bold"), bd=0, yscrollcommand=self.historyScroll_1.set, xscrollcommand=self.historyScroll_2.set, wrap=WORD)
        self.historyText_1.pack(expand=0, side=LEFT, fill=BOTH)

        self.historyScroll_2.config(command=self.historyText_1.xview)
        self.historyScroll_1.config(command=self.historyText_1.yview)

        self.deleteHistoryButton_1 = Button(self.historyFrame_1, text="Delete History", width=18, bd=0, font=("fira code", 14, "bold"), bg="#FFA500", pady=10, command=self.deleteHistory)
        self.deleteHistoryButton_1.place(x=50, y=450)

        self.deleteAccountButton_1 = Button(self.historyFrame_1, text="Delete Account", width=18, bd=0, font=("fira code", 14, "bold"), bg="#FFA500", pady=10, command=self.deleteAccount)
        self.deleteAccountButton_1.place(x=380, y=450)

        self.userDataFolder = "Users/" + self.usernameLogin + "/"
        self.userDataFile = self.usernameLogin + ".json"
        self.userDataFilePath = self.userDataFolder + self.userDataFile

        if os.path.exists(self.userDataFilePath):
            self.userDataFileObject = open(self.userDataFilePath, "r")
            self.loadedUserData = json.load(self.userDataFileObject)

            self.pathsList = self.loadedUserData["Paths"]

            for self.path in self.pathsList:
                self.historyText_1.insert(END, self.path + "\n")

            self.historyText_1.configure(state=DISABLED)
            self.userDataFileObject.close()

    def setOrganizerRightFrame(self):
        self.organizerRightFrame_1 = Frame(self.window, width=350, height=550, bd=0)
        self.organizerRightFrame_1.place(x=900, y=170)

        self.organizeFilesLabel_1 = Label(self.organizerRightFrame_1, text="ORGANIZE YOUR FILES", font=("fira code", 16, "bold"), bd=0)
        self.organizeFilesLabel_1.place(x=0, y=30, relwidth=1)

        self.organizeButton_1 = Button(self.organizerRightFrame_1, width=17, text="Organize", font=("fira code", 16, "bold"), bg="#36802d", bd=0, command=self.setOrganizerLeftFrame)
        self.organizeButton_1.place(x=50, y=100)

        self.historyButton_1 = Button(self.organizerRightFrame_1, width=17, text="History", font=("fira code", 16, "bold"), bg="#00FFFF", bd=0, command=self.setHistoryFrame)
        self.historyButton_1.place(x=50, y=200)

        self.logoutButton_1 = Button(self.organizerRightFrame_1, width=17, text="Log Out", font=("fira code", 16, "bold"), bg="#FFA500", bd=0, command=self.logoutUser)
        self.logoutButton_1.place(x=50, y=300)

        self.followUsLabel_2 = Label(self.organizerRightFrame_1, text="FOLLOW US ON", font=("fira code", 16, "bold"), fg="red", bd=0)
        self.followUsLabel_2.place(x=0, y=400, relwidth=1)

        self.facebookButton_2 = Button(self.organizerRightFrame_1, image=self.facebookImage, bd=0)
        self.facebookButton_2.image = self.facebookImage
        self.facebookButton_2.place(x=30, y=470)

        self.twitterButton_2 = Button(self.organizerRightFrame_1, image=self.twitterImage, bd=0)
        self.twitterButton_2.image = self.twitterImage
        self.twitterButton_2.place(x=110, y=470)

        self.youtubeButton_2 = Button(self.organizerRightFrame_1, image=self.youtubeImage, bd=0)
        self.youtubeButton_2.image = self.youtubeImage
        self.youtubeButton_2.place(x=190, y=470)

        self.instagramButton_2 = Button(self.organizerRightFrame_1, image=self.instagramImage, bd=0)
        self.instagramButton_2.image = self.instagramImage
        self.instagramButton_2.place(x=280, y=470)

    def registerUser(self, event=None):
        self.usernameRegister = self.username_2.get()
        self.passwordRegister = self.password_2.get()
        self.questionRegister = self.question_1.get()
        self.answerRegister = self.answer_1.get()

        if self.usernameRegister and self.passwordRegister and self.questionRegister and self.answerRegister:
            if self.questionRegister != "Forgot Question":
                self.userDataFolder = "Users/" + self.usernameRegister + "/"
                self.userDataFile = self.usernameRegister + ".json"
                self.userDataFilePath = self.userDataFolder + self.userDataFile

                if not os.path.exists(self.userDataFolder):
                    os.mkdir(self.userDataFolder)

                if not os.path.exists(self.userDataFilePath):
                    self.userData = {
                        'Username': self.usernameRegister,
                        'Password': self.passwordRegister,
                        'Question': self.questionRegister,
                        self.questionRegister: self.answerRegister,
                        'Remember': False,
                        'Paths': []
                    }

                    self.userDataFileObject = open(self.userDataFilePath, "w")
                    json.dump(self.userData, self.userDataFileObject)
                    self.userDataFileObject.close()

                    if os.path.exists(self.userDataFilePath):
                        messagebox.showinfo("Success", "Registration successful.")

                        self.usernameEntry_2.delete(0, END)
                        self.passwordEntry_2.delete(0, END)
                        self.questionsCombobox_1.current(0)
                        self.answerEntry_1.delete(0, END)

                        self.setMainWindowLoginFrame()

                    else:
                        messagebox.showerror("Error", "Unexpected error.")

                else:
                    messagebox.showwarning("Warning", "User already exists.")

            else:
                messagebox.showwarning("Warning", "Invalid question.")

        else:
            messagebox.showwarning("Warning", "All fields are required.")

    def loginUser(self, event=None):
        self.usernameLogin = self.username_1.get()
        self.passwordLogin = self.password_1.get()
        self.rememberUserLogin = self.rememberUser_1.get()

        if self.usernameLogin and self.passwordLogin:
            self.userDataFolder = "Users/" + self.usernameLogin + "/"
            self.userDataFile = self.usernameLogin + ".json"
            self.userDataFilePath = self.userDataFolder + self.userDataFile

            if os.path.exists(self.userDataFilePath):
                self.userDataFileObject = open(self.userDataFilePath, "r")
                self.loadedUserData = json.load(self.userDataFileObject)

                if self.loadedUserData["Password"] == self.passwordLogin:
                    self.loadedUserData["Remember"] = self.rememberUserLogin

                    self.userDataFileObject = open(self.userDataFilePath, "w")
                    json.dump(self.loadedUserData, self.userDataFileObject)
                    self.userDataFileObject.close()

                    messagebox.showinfo("Success", "Login successful.")

                    self.usernameEntry_1.delete(0, END)
                    self.passwordEntry_1.delete(0, END)
                    self.rememberUser_1.set(False)

                    self.userDataFileObject.close()
                    self.setOrganizerFrames()

                else:
                    messagebox.showwarning("Warning", "Incorrect password.")

            else:
                messagebox.showwarning("Warning", "User not found.")

        else:
            messagebox.showwarning("Warning", "All fields are required.")

    def retrievePassword(self, event=None):
        self.usernameForgot = self.username_3.get()
        self.questionForgot = self.question_2.get()
        self.answerForgot = self.answer_2.get()

        if self.usernameForgot and self.questionForgot and self.answerForgot:
            self.userDataFolder = "Users/" + self.usernameForgot + "/"
            self.userDataFile = self.usernameForgot + ".json"
            self.userDataFilePath = self.userDataFolder + self.userDataFile

            if os.path.exists(self.userDataFilePath):
                self.userDataFileObject = open(self.userDataFilePath, "r")
                self.loadedUserData = json.load(self.userDataFileObject)

                if self.loadedUserData["Question"] == self.questionForgot:
                    if self.loadedUserData[self.questionForgot] == self.answerForgot:
                        messagebox.showinfo("Success", f"Your password : {self.loadedUserData['Password']}")

                        self.usernameEntry_3.delete(0, END)
                        self.questionsCombobox_2.current(0)
                        self.answerEntry_2.delete(0, END)

                        self.setMainWindowLoginFrame()

                    else:
                        messagebox.showwarning("Warning", "Incorrect answer.")

                else:
                    messagebox.showwarning("Warning", "Question not registered.")

            else:
                messagebox.showwarning("Warning", "User not found.")

        else:
            messagebox.showwarning("Warning", "All fields are required.")

    def changePassword(self, event=None):
        self.oldPassword_2 = self.oldPassword_1.get()
        self.newPassword_2 = self.newPassword_1.get()
        self.confirmPassword_2 = self.confirmPassword_1.get()

        if self.oldPassword_2 and self.newPassword_2 and self.confirmPassword_2:
            if self.newPassword_2 == self.confirmPassword_2:
                self.userDataFolder = "Users/" + self.usernameLogin + "/"
                self.userDataFile = self.usernameLogin + ".json"
                self.userDataFilePath = self.userDataFolder + self.userDataFile

                if os.path.exists(self.userDataFilePath):
                    self.userDataFileObject = open(self.userDataFilePath, "r")
                    self.loadedUserData = json.load(self.userDataFileObject)

                    if self.loadedUserData["Password"] == self.oldPassword_2:
                        self.loadedUserData["Password"] = self.newPassword_2

                        self.userDataFileObject = open(self.userDataFilePath, "w")
                        json.dump(self.loadedUserData, self.userDataFileObject)
                        self.userDataFileObject.close()

                        messagebox.showinfo("Success", "Your password has been successfully changed.")

                        self.oldPasswordEntry_1.delete(0, END)
                        self.newPasswordEntry_1.delete(0, END)
                        self.confirmPasswordEntry_1.delete(0, END)

                        self.setMainWindowFrames()

                    else:
                        messagebox.showwarning("Warning", "Incorrect password.")

                else:
                    messagebox.showwarning("Warning", "User not found.")

            else:
                messagebox.showwarning("Warning", "Password doesn't match.")

        else:
            messagebox.showwarning("Warning", "All fields are required.")

    def autoFillPassword(self, event):
        self.usernameLogin = self.username_1.get()

        if self.usernameLogin:
            self.userDataFolder = "Users/" + self.usernameLogin + "/"
            self.userDataFile = self.usernameLogin + ".json"
            self.userDataFilePath = self.userDataFolder + self.userDataFile

            if os.path.exists(self.userDataFilePath):
                self.userDataFileObject = open(self.userDataFilePath, "r")
                self.loadedUserData = json.load(self.userDataFileObject)

                if self.loadedUserData["Remember"]:
                    self.passwordEntry_1.insert(END, self.loadedUserData["Password"])
                    self.rememberUser_1.set(True)

                else:
                    self.passwordEntry_1.focus_set()
                    self.rememberUser_1.set(False)

            else:
                self.usernameEntry_1.focus_set()

        else:
            self.usernameEntry_1.focus_set()

    @staticmethod
    def filesFinder(path, tuple_extensions):
        return [file for file in os.listdir(path) for extension in tuple_extensions if file.endswith(extension)]

    def organizeFiles(self, event=None):
        self.folderPath_2 = self.folderPath_1.get()

        if self.folderPath_2:
            for folder_name, tuple_extensions in self.dictExtensions.items():
                folder_path = os.path.join(self.folderPath_2, folder_name)

                for item in (self.filesFinder(self.folderPath_2, tuple_extensions)):
                    item_path = os.path.join(self.folderPath_2, item)
                    item_new_path = os.path.join(folder_path, item)

                    if not os.path.exists(folder_path):
                        os.mkdir(folder_path)

                    shutil.move(item_path, item_new_path)

            messagebox.showinfo("Success", "Your files are successfully organized.")

            self.pathEntry_1.delete(0, END)

            self.userDataFolder = "Users/" + self.usernameLogin + "/"
            self.userDataFile = self.usernameLogin + ".json"
            self.userDataFilePath = self.userDataFolder + self.userDataFile

            if os.path.exists(self.userDataFilePath):
                self.userDataFileObject = open(self.userDataFilePath, "r")
                self.loadedUserData = json.load(self.userDataFileObject)

                if self.folderPath_2 not in self.loadedUserData["Paths"]:
                    self.loadedUserData["Paths"].append(self.folderPath_2)

                self.userDataFileObject = open(self.userDataFilePath, "w")
                json.dump(self.loadedUserData, self.userDataFileObject)
                self.userDataFileObject.close()

        else:
            messagebox.showwarning("Warning", "All fields are required.")

    def deleteHistory(self):
        self.userDataFolder = "Users/" + self.usernameLogin + "/"
        self.userDataFile = self.usernameLogin + ".json"
        self.userDataFilePath = self.userDataFolder + self.userDataFile

        if os.path.exists(self.userDataFilePath):
            self.userDataFileObject = open(self.userDataFilePath, "r")
            self.loadedUserData = json.load(self.userDataFileObject)

            if self.loadedUserData["Paths"]:
                self.loadedUserData["Paths"].clear()

                self.userDataFileObject = open(self.userDataFilePath, "w")
                json.dump(self.loadedUserData, self.userDataFileObject)
                self.userDataFileObject.close()

                messagebox.showinfo("Success", "Your history has been successfully deleted.")

                self.setOrganizerFrames()

            else:
                messagebox.showwarning("Warning", "History not found.")

        else:
            messagebox.showwarning("Warning", "User not found.")

    def deleteAccount(self):
        self.userDataFolder = "Users/" + self.usernameLogin + "/"

        if os.path.exists(self.userDataFilePath):
            shutil.rmtree(self.userDataFolder)
            messagebox.showinfo("Success", "Your account has been successfully deleted.")
            self.setMainWindowFrames()

        else:
            messagebox.showwarning("Warning", "Not found.")

    @staticmethod
    def hoverEnter(event):
        event.widget.config(bd=2)

    @staticmethod
    def hoverLeave(event):
        event.widget.config(bd=0)

    @staticmethod
    def facebook():
        webbrowser.open(r"https://www.facebook.com/")

    @staticmethod
    def twitter():
        webbrowser.open(r"https://www.twitter.com/")

    @staticmethod
    def youtube():
        webbrowser.open(r"https://www.youtube.com/")

    @staticmethod
    def instagram():
        webbrowser.open(r"https://www.instagram.com/")

    def logoutUser(self):
        if messagebox.askyesno("Logout", "Are you sure you want to logout"):
            self.setMainWindowFrames()

            self.usernameEntry_1.delete(0, END)
            self.passwordEntry_1.delete(0, END)
            self.rememberUser_1.set(False)

    def closeWindow(self):
        if messagebox.askyesnocancel("Quit", "Are you sure you want to quit?"):
            self.window.destroy()


if __name__ == '__main__':
    organizer = FileOrganizer()