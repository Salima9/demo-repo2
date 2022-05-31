import mysql.connector as mysql
"""Database"""
MYSQL_USER =  'root' #USER-NAME
MYSQL_PASS =  'Kirgizistan993' #MYSQL_PASS
MYSQL_DATABASE = 'dbforusers'#DATABASE_NAME

mydb = mysql.connect(user=MYSQL_USER,passwd=MYSQL_PASS,database=MYSQL_DATABASE, host='127.0.0.1')

c = mydb.cursor(dictionary=True)

# def search_student(search_name):
#         """Kollar om namnet som söks finns i databasen. Om den finns så returneras namnet"""
#         student_name = f"select StudentName from students where left (StudentName, 1) = '{search_name[0]}' order by StudentName"
#         c.execute(student_name)
#         result_names = c.fetchall()
#         #print(result_names)
#         mydb.commit()
#         new_name_lst =list(map(lambda d: d['StudentName'], result_names))
#         #print(new_name_lst)
#         if search_name in new_name_lst: 
            
#             return search_name
#         else: 
#             return new_name_lst

        

# print(search_student("sh"))
        

# def get_search_student_courses(student_name):
#     """"Kollar om namnet som söks finns i databasen. Om den finns så returneras lista av kurser"""
#     student_name_2 = search_student(student_name)
#     #print(search_lst[0])
#     #if str(student_name) == str(search_lst[0]): 
#     for name in (len(student_name_2)): 
#         print(name)
#         search_email = f"select Email from students where StudentName = '{name}'"
#         c.execute(search_email)
#         search_email_1 = c.fetchall()
#         print(search_email_1)
#         mydb.commit()
#         student_email = list(map(lambda d: d['Email'], search_email_1))

#         for email in range(len(student_email)):

#             courses = f"select CanCourse_1, CanCourse_2, CanCourse_3, NeedCourse_1, NeedCourse_2 from courses where Email = '{email}'"
#             c.execute(courses)
#             result = c.fetchall()
#             mydb.commit()
#             can_course_lst = list(map(lambda d: d['CanCourse_1', 'CanCourse_2', 'CanCourse_3', 'NeedCourse_1', 'NeedCourse_2'], result))
#             return can_course_lst

# print(get_search_student_courses("ha"))


# class SearchPopupMenu(): 
#     """Search Box popar ut där man kan skriva in namn på den studenten man söker. Om namnet finns i databasen, en profil sida på den personen visas upp."""
#     def __init__(self, **kwargs):
#         super(SearchPopupMenu, self).__init__(**kwargs)


#     # title = 'Search by name'
#     # text_button_ok = 'Search'
#     # def __init__(self):
#     #     super().__init__()
#         # self.size_hint = [0.9, 0.3]
#         # self.events_callback = self.callback
    
#     # def on_touch_down(self, touch):
#     #     super().open()
#     #     self.focus = True
#     #     FocusBehavior.ignored_touch.append(touch)

#     # def callback(self, *args):
#     #     search_name = self.text_field.text
#     #     self.search_student(search_name)
    
#     def search_student(self, search_name):
#         """Kollar om namnet som söks finns i databasen. Om den finns så returneras namnet"""
#         student_name = f"select StudentName from students where StudentName = '{search_name}'"
#         c.execute(student_name)
#         result = c.fetchone()
#         print(result)
#         mydb.commit()

#         student_name_1 = list(result.values())
#         student_name_2 = student_name_1[0]
#         print(student_name_1)
#         if str(search_name.upper()) == str(student_name_2.upper()): 
#             return student_name_2
#         else:
#             print("error")
#             #här kan göra såm som kollar om första bokstaven finns i databasen

        

#     def get_search_student_courses(self, student_name):
#         """"Kollar om namnet som söks finns i databasen. Om den finns så returneras lista av kurser"""
#         student_name_2 = self.search_student(student_name)
#         #print(search_lst[0])
#         #if str(student_name) == str(search_lst[0]): 
#         if str(student_name_2.upper()) == str(student_name.upper()):
#             search_email = f"select Email from students where StudentName = '{student_name}'"
#             c.execute(search_email)
#             search_email_1 = c.fetchone()
#             #print(result)
#             mydb.commit()
#             student_email = list(search_email_1.values())
#             student_email_1 = student_email[0]

#             courses = f"select CanCourse_1, CanCourse_2, CanCourse_3, NeedCourse_1, NeedCourse_2 from courses where Email = '{student_email_1}'"
#             c.execute(courses)
#             result = c.fetchone()
#             mydb.commit()
#             can_course_lst = list(result.values())
#             return can_course_lst

def search_student(search_name):
        """Kollar om namnet som söks finns i databasen. Om den finns så returneras namnet"""

        student_name = f"select StudentName from students where StudentName = '{search_name}'"
        c.execute(student_name)
        result_search_name = c.fetchone()
        print(result_search_name)
        mydb.commit()
        student_name_1 = list(result_search_name.values())
        student_name_2 = student_name_1[0]
        print(student_name_1)
        if str(search_name.upper()) == str(student_name_2.upper()): 
            return student_name_2
        else:
            print("error")
            #här kan göra såm som kollar om första bokstaven finns i databasen
        
print(search_student("sali"))

# class Search: 
#     def __init__(self, search_word):
#         self.search_word = search_word


# #SALIMAS
#     def check_name(self, search_word):
#         """Kollar om namnet som söks finns i databasen. Om den finns så returneras namnet"""
#         student_name = f"select StudentName from students where StudentName = '{search_word}'"
#         c.execute(student_name)
#         result = c.fetchall()
#         print(result)
#         mydb.commit()
#         student_name_1 = list(map(lambda d: d['StudentName'], result))

#         #print(student_name_1)

#         student_name_2 = student_name_1[0]
#         if str(search_word.upper()) == str(student_name_2.upper()): 
            
#             return student_name_2 
#         else:
#             self.check_courses(search_word)

# #FATIMES
#     # def check_name(self, search_word):
#     #     """Kollar om namnet som söks finns i databasen. Om den finns så returneras namnet"""
#     #     student_name = f"select StudentName from students where StudentName = '{search_word}'"
#     #     c.execute(student_name)
#     #     result = c.fetchall()
#     #     print(result)
#     #     mydb.commit()
#     #     student_name_1 = list(map(lambda d: d['StudentName'], result))

#         #print(student_name_1)

#         student_name_2 = student_name_1[0]
#         if str(search_word.upper()) == str(student_name_2.upper()): 
            
#             return student_name_2 
#         else:
#             self.check_courses(search_word)

    
#     def check_courses(self, search_word):
#         """"Kollar om namnet som söks finns i databasen. Om den finns så returneras lista av kurser"""
        
#         search_email = f"select Email from students where CanCourse_1 = '{search_word}' or CanCourse_2 = '{search_word}' or CanCourse_3   = '{search_word}'"
        
#         c.execute(search_email)
#         search_email_1 = c.fetchall()
#         mydb.commit()
#         student_email = list(map(lambda d: d['Email'], search_email_1))
#         #student_email_2 = student_email[0]

#         print(student_email)

#         # courses = f"select StudentName from students where Email = '{student_email_2}'"
#         # c.execute(courses)
#         # result = c.fetchone()
#         # mydb.commit()
#         # can_course_lst = list(result.values())
#         return student_email  


# search = Search("matte")

# print(search.check_name("matte"))



