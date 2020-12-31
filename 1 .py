class GradeSystemFunctionProfessor(object):#�б¥\��
    def __init__(self, master=None):
        self.root = master #�w�q�����ܼ�root
        self.root.geometry('%dx%d' % (1000, 800))
        self.createPage()  
    def createPage(self):#�D���� 
        self.InputPage = InputFrame(self.root) #�������P������
        self.ProfessorOutputPage = ProfessorOutputFrame(self.root)
        self.ListCoursePage = ListCourseFrame(self.root)
        self.ListCourseStudentPage = ListCourseStudentFrame(self.root)
        self.InputPage.pack() #�w�]���X�{���O"�W�[���Z"������
        self.menu = Menu(self.root)#�Ыص��
        self.menu.add_command(label='�s�W/�ק令�Z', font=10,command = self.InputData)#�W�[�R�O(�ﶵ)   
        self.menu.add_command(label='�C�X�ҵ{���Z',font=10, command = self.ProfessorOutputData)
        self.menu.add_command(label='�C�X�ҵ{�M��',font=10,command = self.ListCourse)
        self.menu.add_command(label='�C�X�ҵ{�ǥ�',font=10,command = self.ListCourseStudent)
        self.menu.add_command(label='�����ϥΪ�',font=10, command = self.ChangeUser)  
        self.root['menu'] = self.menu#������ 
    def InputData(self):
        self.InputPage.pack()#������X�{
        self.ProfessorOutputPage.pack_forget()#���������
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
        self.root = master #�w�q�����ܼ�root
        self.E1 = Entry(self,font=10)
        self.E2 = Entry(self,font=10)
        self.E3 = Entry(self,font=10)
        self.E4 = Entry(self,font=10)
        self.E5 = Entry(self,font=10,show="*")
        self.createPage()
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, font=10, text = '�Ǧ~: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=W)
        Label(self,  font=10,text = '�Ǵ�: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=W)
        Label(self,  font=10,text = '�ҵ{�N�X: ').grid(row=3, stick=W, pady=10)
        self.E3.grid(row=3, column=1, stick=W)
        Label(self,  font=10,text = '�ϥΪ̦W��: ').grid(row=4, stick=W, pady=10)
        self.E4.grid(row=4, column=1, stick=W)
        Label(self,  font=10,text = '�K�X: ').grid(row=5, stick=W, pady=10)
        self.E5.grid(row=5, column=1, stick=W)
        self.tree=ttk.Treeview(self)#���
        self.tree["columns"]=("�Ǹ�","�ǥͩm�W","���Z")
        self.tree.column("�Ǹ�",width=100)#��ܦC,�����
        self.tree.column("�ǥͩm�W",width=100)  
        self.tree.column("���Z",width=100)
        self.tree.heading("�Ǹ�",text="�Ǹ�")#��ܿ��Y
        self.tree.heading("�ǥͩm�W",text="�ǥͩm�W")
        self.tree.heading("���Z",text="���Z")
        self.tree.grid(row=6, column=1, stick=W, pady=10)
        Button(self, font=10, text='�C�X',command=self.search).grid(row=7, column=1, stick=E, pady=10)
    def search(self):
        x=self.tree.get_children()
        for item in x:
            self.tree.delete(item)#�R����椺����
        year = self.E1.get()
        semester = self.E2.get()
        num = self.E3.get()
        username = self.E4.get()
        password = self.E5.get()
        if self.spacejudge(year) or self.spacejudge(semester) or self.spacejudge(num) or self.spacejudge(username) or self.spacejudge(password):
            showinfo(title='����', message ="���@��J���i����")
        else:
            self.searchInfo(year,semester,num,username,password)
    def searchInfo(self,year,semester,num,username,password):
        temp2=0
        f = open('./�ҵ{��T.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==year and info[1] ==semester and info[2] ==num:
                temp2=1
                classname=info[3]
                proname=info[5]
                f.close()
        if temp2==0:
            showinfo(title='����', message ="�S�����Ǵ��ҵ{�T��")
            f.close()
            return
        else:
            f.close
        temp3=0
        f = open('./�b���K�X.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==username and info[1] ==password and info[2] =='2' and info[3]==proname:
                temp3=1
                f.close()
        if temp3==0:
            showinfo(title='���~', message ="�����P�ҵ{�б¤���")
            f.close
            return
        else:
            f.close
        temp=0
        i=0
        f = open('./�ǥ͸�T.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==year and info[1] ==semester and info[2] ==num and info[6]=='1':
                temp=1
                self.tree.insert("",i,text=classname ,values=(info[3],info[4],info[5])) #���J���
                i+=1
        if temp==0:
            showinfo(title='����', message ="���Ǵ��ҵ{�S�����ǥͪ��T��")
            f.close()
            return
        else:
            showinfo(title='����', message ="�w�C�X���")
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
        self.root = master #�w�q�����ܼ�root
        self.E1 = Entry(self,font=10)
        self.E2 = Entry(self,font=10)
        self.E3 = Entry(self,font=10)
        self.createPage()
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, font=10, text = '�Ǧ~: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=W)
        Label(self,  font=10,text = '�Ǵ�: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=W)
        Label(self,  font=10,text = '�ҵ{�N�X: ').grid(row=3, stick=W, pady=10)
        self.E3.grid(row=3, column=1, stick=W)
        self.tree=ttk.Treeview(self)#���
        self.tree["columns"]=("�N�X","�Ǹ�","�ǥͩm�W")
        self.tree.column("�N�X",width=100)   #��ܦC,�����
        self.tree.column("�Ǹ�",width=100)
        self.tree.column("�ǥͩm�W",width=100)  
        self.tree.heading("�N�X",text="�N�X")  #��ܿ��Y
        self.tree.heading("�Ǹ�",text="�Ǹ�")
        self.tree.heading("�ǥͩm�W",text="�ǥͩm�W")
        self.tree.grid(row=4, column=1, stick=W, pady=10)
        Button(self, font=10, text='�d��',command=self.search).grid(row=6, column=1, stick=E, pady=10)
    def search(self):
        x=self.tree.get_children()
        for item in x:
            self.tree.delete(item)#�R����椺����
        year = self.E1.get()
        semester = self.E2.get()
        num = self.E3.get()
        if self.spacejudge(year) or self.spacejudge(semester) or self.spacejudge(num):
            showinfo(title='����', message ="���@��J���i����")
        else:
            self.searchInfo(year,semester,num)
    def searchInfo(self,year,semester,num):
        temp=0
        temp2=0
        i=0
        f = open('./�ҵ{��T.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==year and info[1] ==semester and info[2] ==num:
                temp2=1
                classname=info[3]
                f.close()
        if temp2==0:
            showinfo(title='����', message ="�S�����Ǵ��ҵ{�T��")
            f.close()
            return
        else:
            f.close
        f = open('./�ǥ͸�T.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==year and info[1] ==semester and info[2] ==num:
                temp=1
                self.tree.insert("",i,text=classname ,values=(info[2],info[3],info[4])) #���J���
                i+=1
        if temp==0:
            showinfo(title='����', message ="�S�����Ǵ��ҵ{���ǥͰT��")
            f.close()
            return
        else:
            showinfo(title='����', message ="�w�C�X���")
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