import sqlite3

conn = sqlite3.connect('DB.db')
curs = conn.cursor()
zapr_1 = """CREATE TABLE IF NOT EXISTS INFO_Personal (Name TEXT, SName TEXT, S2Name TEXT, UchStep TEXT, SinDirect TEXT, WorckState TEXT, Depart TEXT, JTitle TEXT, Country TEXT, City TEXT, Adres TEXT, WNumber INT, Email TEXT);"""
zapr_2 = """CREATE TABLE IF NOT EXISTS INFO_UCHASTNIKOV (Type_Man TEXT, Time_send_inv TEXT, Date_get_ans_inv TEXT, Theme_doclad TEXT, Tesis TEXT, Data_join TEXT,NeedGos TEXT, Data_dep TEXT);"""
zapr_3 = """CREATE TABLE IF NOT EXISTS INFO_CONF (ConfName TEXT, Time TEXT,Location TEXT, Organizashn TEXT, Sponsors TEXT, DayCount INT, CountMembers INT, CountSpeckers INT);"""
curs.execute(zapr_1)
curs.execute(zapr_2)
curs.execute(zapr_3)

send_data1 = """INSERT INTO INFO_Personal VALUES ('Alex', 'Yanushkevich', 'Alexeevich', 'Magistr', 'IT', 'Minsk', 'IT', 'Uchitel', 'BY', 'Minsk', 'Minsk/Nemiga/32', '+375299550909',  'lalka417@gmail.com');"""
send_data2 = """INSERT INTO INFO_UCHASTNIKOV VALUES ('Docladchik', '02/02/2020', '06/02/2020', 'Python', 'None', '22/05/2020', 'No', '22/05/2020');"""
send_data3 = """INSERT INTO INFO_CONF VALUES ('IT World', '05/05/2020', 'Minsk', 'Wargaming', 'VkTeam', '1', '500','34');"""
curs.execute(send_data1)
curs.execute(send_data2)
curs.execute(send_data3)
conn.commit()

curs.close()
conn.close()
input()