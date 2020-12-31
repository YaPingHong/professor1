class GradeSystemFunctionProfessor(object):#教授功能
    def __init__(self, master=None):
        self.root = master #定義內部變數root
        self.root.geometry('%dx%d' % (1000, 800))
        self.createPage()  
    def createPage(self):#主頁面 
        self.InputPage = InputFrame(self.root) #切換不同的頁面
        self.ProfessorOutputPage = ProfessorOutputFrame(self.root)
        self.ListCoursePage = ListCourseFrame(self.root)
        self.ListCourseStudentPage = ListCourseStudentFrame(self.root)
        self.InputPage.pack() #預設先出現的是"增加成績"的介面
        self.menu = Menu(self.root)#創建菜單
        self.menu.add_command(label='新增/修改成績', font=10,command = self.InputData)#增加命令(選項)   
        self.menu.add_command(label='列出課程成績',font=10, command = self.ProfessorOutputData)
        self.menu.add_command(label='列出課程清單',font=10,command = self.ListCourse)
        self.menu.add_command(label='列出課程學生',font=10,command = self.ListCourseStudent)
        self.menu.add_command(label='切換使用者',font=10, command = self.ChangeUser)  
        self.root['menu'] = self.menu#菜單欄位 
    def InputData(self):
        self.InputPage.pack()#讓元件出現
        self.ProfessorOutputPage.pack_forget()#讓元件消失
        self.ListCoursePage.pack_forget()
        self.ListCourseStudentPage.pack_forget()     
    def ProfessorOutputData(self):
        self.InputPage.pack_forget()  
        self.ProfessorOutputPage.pack()
        self.ListCoursePage.pack_forget()
        self.ListCourseStudentPage.pack_forget()
    def ListCourse(self):
        self.InputPage.pack_forget()  
        self.ProfessorOutputPage.pack_forget()
        self.ListCoursePage.pack()
        self.ListCourseStudentPage.pack_forget()
    def ListCourseStudent(self):
        self.InputPage.pack_forget()  
        self.ProfessorOutputPage.pack_forget()  
        self.ListCoursePage.pack_forget()
        self.ListCourseStudentPage.pack()
    def ChangeUser(self):
        self.menu.destroy()
        self.InputPage.destroy()  
        self.ProfessorOutputPage.destroy()
        self.ListCoursePage.destroy()
        self.ListCourseStudentPage.destroy()
        GradeSystemLogin(self.root)


class ProfessorOutputFrame(Frame):
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定義內部變數root
        self.E1 = Entry(self,font=10)
        self.E2 = Entry(self,font=10)
        self.E3 = Entry(self,font=10)
        self.E4 = Entry(self,font=10)
        self.E5 = Entry(self,font=10,show="*")
        self.createPage()
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, font=10, text = '學年: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=W)
        Label(self,  font=10,text = '學期: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=W)
        Label(self,  font=10,text = '課程代碼: ').grid(row=3, stick=W, pady=10)
        self.E3.grid(row=3, column=1, stick=W)
        Label(self,  font=10,text = '使用者名稱: ').grid(row=4, stick=W, pady=10)
        self.E4.grid(row=4, column=1, stick=W)
        Label(self,  font=10,text = '密碼: ').grid(row=5, stick=W, pady=10)
        self.E5.grid(row=5, column=1, stick=W)
        self.tree=ttk.Treeview(self)#表格
        self.tree["columns"]=("學號","學生姓名","成績")
        self.tree.column("學號",width=100)#表示列,不顯示
        self.tree.column("學生姓名",width=100)  
        self.tree.column("成績",width=100)
        self.tree.heading("學號",text="學號")#顯示錶頭
        self.tree.heading("學生姓名",text="學生姓名")
        self.tree.heading("成績",text="成績")
        self.tree.grid(row=6, column=1, stick=W, pady=10)
        Button(self, font=10, text='列出',command=self.search).grid(row=7, column=1, stick=E, pady=10)
    def search(self):
        x=self.tree.get_children()
        for item in x:
            self.tree.delete(item)#刪除表格內元件
        year = self.E1.get()
        semester = self.E2.get()
        num = self.E3.get()
        username = self.E4.get()
        password = self.E5.get()
        if self.spacejudge(year) or self.spacejudge(semester) or self.spacejudge(num) or self.spacejudge(username) or self.spacejudge(password):
            showinfo(title='提示', message ="任一輸入不可為空")
        else:
            self.searchInfo(year,semester,num,username,password)
    def searchInfo(self,year,semester,num,username,password):
        temp2=0
        f = open('./課程資訊.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==year and info[1] ==semester and info[2] ==num:
                temp2=1
                classname=info[3]
                proname=info[5]
                f.close()
        if temp2==0:
            showinfo(title='提示', message ="沒有此學期課程訊息")
            f.close()
            return
        else:
            f.close
        temp3=0
        f = open('./帳號密碼.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==username and info[1] ==password and info[2] =='2' and info[3]==proname:
                temp3=1
                f.close()
        if temp3==0:
            showinfo(title='錯誤', message ="身分與課程教授不符")
            f.close
            return
        else:
            f.close
        temp=0
        i=0
        f = open('./學生資訊.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==year and info[1] ==semester and info[2] ==num and info[6]=='1':
                temp=1
                self.tree.insert("",i,text=classname ,values=(info[3],info[4],info[5])) #插入資料
                i+=1
        if temp==0:
            showinfo(title='提示', message ="此學期課程沒有此學生的訊息")
            f.close()
            return
        else:
            showinfo(title='提示', message ="已列出表格")
            f.close()
            return
    def spacejudge(self,text):
        spacejudge = 0
        for i in text:
            if not i.isspace():
                spacejudge = 1
                break
        if spacejudge==1:
            return 0
        else:
            return 1


class ListCourseStudentFrame(Frame):
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定義內部變數root
        self.E1 = Entry(self,font=10)
        self.E2 = Entry(self,font=10)
        self.E3 = Entry(self,font=10)
        self.createPage()
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, font=10, text = '學年: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=W)
        Label(self,  font=10,text = '學期: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=W)
        Label(self,  font=10,text = '課程代碼: ').grid(row=3, stick=W, pady=10)
        self.E3.grid(row=3, column=1, stick=W)
        self.tree=ttk.Treeview(self)#表格
        self.tree["columns"]=("代碼","學號","學生姓名")
        self.tree.column("代碼",width=100)   #表示列,不顯示
        self.tree.column("學號",width=100)
        self.tree.column("學生姓名",width=100)  
        self.tree.heading("代碼",text="代碼")  #顯示錶頭
        self.tree.heading("學號",text="學號")
        self.tree.heading("學生姓名",text="學生姓名")
        self.tree.grid(row=4, column=1, stick=W, pady=10)
        Button(self, font=10, text='查詢',command=self.search).grid(row=6, column=1, stick=E, pady=10)
    def search(self):
        x=self.tree.get_children()
        for item in x:
            self.tree.delete(item)#刪除表格內元件
        year = self.E1.get()
        semester = self.E2.get()
        num = self.E3.get()
        if self.spacejudge(year) or self.spacejudge(semester) or self.spacejudge(num):
            showinfo(title='提示', message ="任一輸入不可為空")
        else:
            self.searchInfo(year,semester,num)
    def searchInfo(self,year,semester,num):
        temp=0
        temp2=0
        i=0
        f = open('./課程資訊.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==year and info[1] ==semester and info[2] ==num:
                temp2=1
                classname=info[3]
                f.close()
        if temp2==0:
            showinfo(title='提示', message ="沒有此學期課程訊息")
            f.close()
            return
        else:
            f.close
        f = open('./學生資訊.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==year and info[1] ==semester and info[2] ==num:
                temp=1
                self.tree.insert("",i,text=classname ,values=(info[2],info[3],info[4])) #插入資料
                i+=1
        if temp==0:
            showinfo(title='提示', message ="沒有此學期課程的學生訊息")
            f.close()
            return
        else:
            showinfo(title='提示', message ="已列出表格")
            f.close()
            return
    def spacejudge(self,text):
        spacejudge = 0
        for i in text:
            if not i.isspace():
                spacejudge = 1
                break
        if spacejudge==1:
            return 0
        else:
            return 1
