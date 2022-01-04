import mysql.connector

connector = mysql.connector.connect(host = "localhost", user = "root", passwd ="root")
cursor = connector.cursor()

cursor.execute("SHOW DATABASES")
db_list = cursor.fetchall()
if not ("student_management_system",) in db_list:
    cursor.execute("CREATE DATABASE student_management_system")

new_connector = mysql.connector.connect(host="localhost", user="root", passwd="root", database="student_management_system")
mycursor = new_connector.cursor()

mycursor.execute("SHOW TABLES")
tb_list = mycursor.fetchall()

if not ("student",) in tb_list:
    mycursor.execute("CREATE TABLE student (stu_id INT PRIMARY KEY AUTO_INCREMENT, stu_name VARCHAR(100), stu_address VARCHAR(500), stu_contact CHAR(10), stu_grade VARCHAR(10), com_maths BOOLEAN, it BOOLEAN, physics BOOLEAN, chemistry BOOLEAN, biology BOOLEAN, english BOOLEAN)")

if not ("lecturer",) in tb_list:
    mycursor.execute("CREATE TABLE lecturer (lecturer_id INT PRIMARY KEY AUTO_INCREMENT, lecturer_name VARCHAR(100), lecturer_address VARCHAR(500), lecturer_contact CHAR(10), lecturer_subject VARCHAR(10), primary_class BOOLEAN, grade_6_8 BOOLEAN, grade_9_11 BOOLEAN, o_level BOOLEAN, a_level BOOLEAN, adult BOOLEAN)")

if not ("lec_sessions",) in tb_list:
    mycursor.execute("CREATE TABLE lec_sessions (lec_id INT PRIMARY KEY AUTO_INCREMENT, lec_subject VARCHAR(20), lec_lesson VARCHAR(200), lec_grade INT, lec_date DATE, lec_time TIME, time_type BOOLEAN, duration INT)")

if not ("payment_details",) in tb_list:
    mycursor.execute("CREATE TABLE payment_details (stu_id INT PRIMARY KEY, year VARCHAR(4), january Date, february Date,march Date,april Date,may Date,june Date,july Date,august Date,september Date,october Date,november Date,december Date")






Students = [['30c4d975-6dc4-11eb-a7d3-1063c8b59945', 'Asiri Silva', 'No. 27/2, Ayuboga Mawatha, Walpola, Ragama', '0112446995', '12', ['Combined Maths', 'Information Technology', 'Biology','Physics'], []], ['a121cd18-6e00-11eb-bcbc-b4a9fc461ec3', 'Kasun Tharaka', 'No. 250, Samagi Road, Walpola', '0721236547', '12', ['Combined Maths', 'Physics', 'Chemistry'], []], ['ca713c7e-6e00-11eb-a99d-b4a9fc461ec3', 'Dasun Chanaka', 'No.215, Wanatha Willuwa, Colombo', '0771122345', '13', ['Combined Maths', 'Information Technology', 'Chemistry'], []], ['05fed0cf-6e01-11eb-9cfe-b4a9fc461ec3', 'Nadun Weerasiri', 'No.54/A, Kandaliyadda Paluwa, Kandana', '0112246357', '12', ['Combined Maths', 'Physics', 'Chemistry', 'Biology'], []], ['45f8ca18-6e01-11eb-8b65-b4a9fc461ec3', 'Adun Perera', 'No. 25, Lakeside, Walpola, Ragama', '0112545697', '13', ['Combined Maths',
'Information Technology', 'Physics'], []], ['d380b4c5-6e01-11eb-8ffb-b4a9fc461ec3', 'Anjana Kalhara', 'No.320, Araliya Road, Gampaha', '0724561254', '12', ['Combined Maths', 'Information Technology', 'Physics'], []]]
Lecturers = [['549f5452-6dfd-11eb-979b-b4a9fc461ec3', 'Dinuka Ganganath', 'No.207, Samagi Mawatha, Walpola, Ragama', '0713313674', 'Physics', ['Advanced Level']], ['886a3e24-6dfd-11eb-a763-b4a9fc461ec3', 'A. W. R. D. Karunarathna', 'No. 15/B, Araliya Uyana, Thewaththa Road, Ragama', '0112245738', 'Biology', ['Grade 6 / 7 / 8', 'Grade 9 / 10 / 11', 'Ordinary Level']], ['d1e6ecca-6dfd-11eb-ba29-b4a9fc461ec3', 'Siril Perera', 'No. 27/C, Kaluwala Junction, Kadawatha', '076412589', 'Mathematics', ['Grade 6 / 7 / 8', 'Grade 9 / 10 / 11', 'Ordinary Level', 'Advanced Level']]]
LectureTimeTable = [['7e6a931d-6e07-11eb-beb8-b4a9fc461ec3', 'Physics', 'Motion', '12', '2021.10.12', '9.00 AM', '2 hours'], ['9ecb3407-6e07-11eb-8d99-b4a9fc461ec3', 'Chemistry', 'Organic Chemistry', '13', '2021.02.24', '9.00 PM', '3 hours'], ['d4425dbd-6e07-11eb-aa4d-b4a9fc461ec3', 'Combined Mathematics', 'Force', '12', '2021.01.31', '10.30 AM', '3 hours']]