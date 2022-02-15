import sqlite3
import random
conn=sqlite3.connect('table111')
cursor=conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS table111(id INTEGER PRIMARY KEY AUTOINCREMENT, Qwestion Text, answer_1 Text,answer_2 Text,answer_3 Text) ''')

# a=random.randint(0,9)
# b=random.randint(0,9)
l = [('Что такое питон?', 'язык программирования ', 'лекарство', 'животное'),
     ('Что такое list?', 'список ', 'множество', 'словарь'),
     ('Что такое range?', 'функция ', 'итератор', 'генератор')]
cursor.executemany('''INSERT INTO table111(Qwestion,answer_1,answer_2,answer_3) VALUES (?,?,?,?)''', l)
# conn.commit()
cursor.execute('''SELECT id FROM table111''')
k = cursor.fetchall()
r = random.choice(k)
print(*r)  # * используется для распаковки элемента из кортежа

cursor.execute('''SELECT Qwestion,answer_1,answer_2,answer_3 FROM table111 WHERE id=?''', (r))
oo = cursor.fetchall()
print(oo)
#conn.commit()
# cursor.execute('''SELECT col1,col2 FROM table1''')
# k=cursor.fetchall()
# print('Заполненная таблица')
# for i in k:
#    print(*i)
# cursor.execute('''SELECT avg(col1),avg(col2) FROM table1''')
# average_col=cursor.fetchall()
# #print(average_col)
# for i in average_col:
#    sum_duple=sum(i)
#    average_result=sum(i)/len(i)
# print('Среднее арифмитическое всех значений из колонки один и два ',average_result)
# if average_result>len(k):
#    cursor.execute('''DELETE FROM table1 WHERE id=4''')
#    cursor.execute('''SELECT col1,col2 FROM table1''')
#    k1 = cursor.fetchall()
#    print('Таблица после удаления четвертой записи ')
#    for i in k1:
#       print(*i)


