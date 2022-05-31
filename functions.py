from db_creds import *
import mysql.connector as mysql

"""Database"""
MYSQL_USER =  'root' #USER-NAME
MYSQL_PASS =  'Kirgizistan993' #MYSQL_PASS
MYSQL_DATABASE = 'dbforusers'#DATABASE_NAME

mydb = mysql.connect(user=MYSQL_USER,passwd=MYSQL_PASS,database=MYSQL_DATABASE, host='127.0.0.1')

c = mydb.cursor(dictionary=True)

def search_students_for_help(email):
    # mydb = mysql.connect(
	# 		host = "127.0.0.1", 
	# 		user = "root",
	# 		passwd = "Kirgizistan993",
	# 		database = "dbforusers",
    #         )


    c = mydb.cursor(dictionary=True)
    
    vc_query = f"select NeedCourse_1, NeedCourse_2 from courses where email = '{email}'"
    c.execute(vc_query)
    vc_records =  c.fetchone() 
    print(vc_records)
    mydb.commit()

    NeedCourses = list(vc_records.values())    
    # print(NeedCourses)

    entries = []
    for course in NeedCourses:
        # print(course)
        c = mydb.cursor(dictionary=True)
        vc_query = f"SELECT * FROM courses WHERE '{course}' IN(CanCourse_1, CanCourse_2, CanCourse_3);"
        c.execute(vc_query)
        vc_records =  c.fetchall()
        # print(vc_records)
        # if vc_records not in entries:
        # if not any(d['Email'] == email for d in vc_records):
        entries.extend(vc_records)
        # entries.append(vc_records)
        mydb.commit()
    # print("\n")
    # print(entries)
    # print("\n")
    
    entries = [dict(t) for t in {tuple(d.items()) for d in entries}] #source:https://stackoverflow.com/a/9427216/12804377
    # print(entries)
    # remove own entry
    for user in entries:
        if user['Email'] == email:
            entries.remove(user)
            break
    # Get name of those email addresses
    for user in entries:
        c = mydb.cursor(dictionary=True)
        query = f"SELECT StudentName FROM students WHERE email = '{user['Email']}'"
        c.execute(query)
        result =  c.fetchall()
        print(result)
        if len(result) > 0:
            user['Name'] = result[0]['StudentName'].strip()
        else:
            user['Name'] = user['Email']
        mydb.commit()

    return entries
    

# if __name__ == "_main_":
#     print(search_students_for_help("sallydarwish77@student.bth.se"))
