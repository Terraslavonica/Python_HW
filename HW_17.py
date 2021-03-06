import sqlite3
import pandas as pd
import csv

# Task 1. Прочитайте о следующих командах и попробуйте их - UPDATE, DELETE, CASCADE
# Create connection
connection = sqlite3.connect('learners.db')

connection.execute('PRAGMA foreign_keys = ON')

connection.execute('DROP TABLE IF EXISTS courses')
connection.execute('DROP TABLE IF EXISTS learners')
connection.execute('DROP TABLE IF EXISTS attendance')

connection.execute('PRAGMA foreign_keys = ON')
connection.execute('''CREATE TABLE IF NOT EXISTS learners (
        learner_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        sex INTEGER,
        UNIQUE (first_name, last_name, sex)              
        )''')

connection.execute('''CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY,
    course TEXT UNIQUE,
    prep TEXT
    )''')

connection.execute('''CREATE TABLE IF NOT EXISTS attendance (
    attendance_id INTEGER PRIMARY KEY,
    course_id INTEGER REFERENCES courses (course_id) ON UPDATE CASCADE ON DELETE CASCADE, 
    learner_id INTEGER REFERENCES learners (learner_id) ON UPDATE CASCADE ON DELETE CASCADE
    )''')  # тут отличие от следующего варианта

query = '''INSERT INTO learners (first_name, last_name, sex) VALUES (?, ?, ?)'''

learners = [('Dima', 'Biba', 0), ('Shamil', 'Urazbakhtin', 0), ('Loli', 'Alekseeva', 1),
            ('Katya', 'Yakovleva', 1), ('Olya', 'Mazur', 1), ('Masha', 'Volkova', 1)]
connection.executemany(query, learners)

query2 = "INSERT INTO courses (course, prep) VALUES (?, ?)"
connection.executemany(query2, (['python', 'Sasha'], ['prak', 'Nadya'], ['ML', 'Lavrentiy'], ['NGS', 'Ura']))

query3 = "INSERT INTO attendance (course_id, learner_id) VALUES (?, ?)"
connection.executemany(query3, ([1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 1], [2, 3], [2, 4], [2, 3],
                                [3, 1], [3, 3], [3, 4], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6]))


query4 = '''SELECT * FROM attendance
    JOIN learners on attendance.learner_id = learners.learner_id
    JOIN courses on courses.course_id = attendance.course_id'''

res = connection.execute(query4)

print(res.fetchall())

for row in res.fetchall():
    print(row)

update_query = '''UPDATE learners SET last_name = "Superman" where learner_id = 1'''  # заменим фамилию одному из студентов
connection.execute(update_query)

update_query_many = """UPDATE courses SET course = ? where course_id = ?"""
records = [('python-2', 1), ('prak-2', 2)]  # продолжающиеся курсы приобретают 2 в названии
connection.executemany(update_query_many, records)

update_query_prep = """UPDATE courses SET prep = 'Misha' where course_id = 2"""
connection.execute(update_query_prep)

delete_query = """DELETE from learners where learner_id = 6"""  # Маша ушла)
connection.execute(delete_query)

connection.execute('UPDATE learners SET learner_id = 100 WHERE first_name = "Dima"')

connection.commit()
connection.close()

# Task 1. Прочитайте о следующих командах и попробуйте их - UPDATE, DELETE, CASCADE.
# Аналогичный вариант немного с другим оформлением ключей, тоже работает.
# Create connection
connection = sqlite3.connect('learners.db')

connection.execute('PRAGMA foreign_keys = ON')

connection.execute('''CREATE TABLE IF NOT EXISTS learners (
        learner_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        sex INTEGER,
        UNIQUE (first_name, last_name, sex)              
        )''')

connection.execute('''CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY,
    course TEXT UNIQUE,
    prep TEXT
    )''')

connection.execute('''CREATE TABLE IF NOT EXISTS attendance (
    attendance_id INTEGER PRIMARY KEY,
    course_id INTEGER,
    learner_id INTEGER,
    FOREIGN KEY (course_id) REFERENCES courses (course_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (learner_id) REFERENCES learners (learner_id) ON UPDATE CASCADE ON DELETE CASCADE
    )''')

query = '''INSERT INTO learners (first_name, last_name, sex) VALUES (?, ?, ?)'''

learners = [('Dima', 'Biba', 0), ('Shamil', 'Urazbakhtin', 0), ('Loli', 'Alekseeva', 1),
            ('Katya', 'Yakovleva', 1), ('Olya', 'Mazur', 1), ('Masha', 'Volkova', 1)]
connection.executemany(query, learners)

query2 = "INSERT INTO courses (course, prep) VALUES (?, ?)"
connection.executemany(query2, (['python', 'Sasha'], ['prak', 'Nadya'], ['ML', 'Lavrentiy'], ['NGS', 'Ura']))

query3 = "INSERT INTO attendance (course_id, learner_id) VALUES (?, ?)"
connection.executemany(query3, (
[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 1], [2, 3], [2, 4], [2, 3], [3, 1], [3, 3], [3, 4],
[4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6]))

# connection.execute('DROP TABLE IF EXISTS courses')
# connection.execute('DROP TABLE IF EXISTS learners')
# connection.execute('DROP TABLE IF EXISTS attendance')

query4 = '''SELECT * FROM attendance
    JOIN learners on attendance.learner_id = learners.learner_id
    JOIN courses on courses.course_id = attendance.course_id'''

res = connection.execute(query4)

print(res.fetchall())

for row in res.fetchall():
    print(row)

cursor = connection.cursor()

update_query = '''UPDATE learners SET last_name = "Superman" where learner_id = 1'''  # заменим фамилию одному из студентов
cursor.execute(update_query)

update_query_many = """UPDATE courses SET course = ? where course_id = ?"""
records = [('python-2', 1), ('prak-2', 2)]  # продолжающиеся курсы приобретают 2 в названии
cursor.executemany(update_query_many, records)

update_query_prep = """UPDATE courses SET prep = 'Misha' where course_id = 2"""
cursor.execute(update_query_prep)

delete_query = """DELETE from learners where learner_id = 6"""  # Маша ушла)
cursor.execute(delete_query)

cursor.execute('UPDATE learners SET learner_id = 100 WHERE first_name = "Dima"')

cursor.close()

connection.commit()
connection.close()



# Task 2. Пришло время сделать свою БД! Подумайте как организовать базу, создайте её и заполните
# данными через питон на основе своих данных или воспользуйтесь учебными

# Create connaction
connection = sqlite3.connect('chipseq.db')

connection.execute('PRAGMA foreign_keys = ON')

# First table, metadata about animal
connection.execute('DROP TABLE IF EXISTS metadata')
connection.execute('''CREATE TABLE IF NOT EXISTS metadata (
        metadata_id INTEGER PRIMARY KEY,
        dna_chip_id TEXT UNIQUE,
        breed TEXT,
        sex TEXT
        )''')

# Second table, SNPs data
connection.execute('''CREATE TABLE IF NOT EXISTS genstudio (
        genstudio_id INTEGER PRIMARY KEY,
        SNP_Name TEXT,
        SNP_Index INTEGER,
        SNP_Aux INTEGER,
        Sample_ID TEXT,
        SNP TEXT,
        Allele1_Top TEXT,
        Allele2_Top TEXT,
        Allele1_Forward TEXT,
        Allele2_Forward TEXT,
        Allele1_AB TEXT,
        Allele2_AB TEXT,
        Chr TEXT,
        Position TEXT,
        GC_Score REAL,
        GT_Score REAL,
        Theta REAL,
        R REAL,
        B_Allele_Freq REAL,
        Log_R_Ratio REAL,
        FOREIGN KEY (Sample_ID) REFERENCES metadata (dna_chip_id)
        )''')

# Fill the tables
# # Способ 0
# metadata = pd.read_csv('genotyping_data/metadata.csv', sep = ',', index_col=0)
# metadata.head(10)
#
# query = "INSERT INTO metadata (dna_chip_id, breed, sex) VALUES (?, ?, ?)"
#
# for index, data in metadata.iterrows():
#     mydata = list(data)
#     connection.execute(query, mydata)

# # Способ 1, работает, но считывает русские буквы с искажением, с кодировкой не справилась, 'dialect' не помогает
# with open('genotyping_data/metadata.csv','r') as metadata: # `with` statement available in 2.5+
#     # csv.DictReader uses first line in file for column headings by default
#     dr = csv.DictReader(metadata) # comma is default delimiter
#     to_db = [(i['dna_chip_id'], i['breed'], i['sex']) for i in dr]

# Способ 2. Работает, но не быстрее Способа 0
query = "INSERT INTO metadata (dna_chip_id, breed, sex) VALUES (?, ?, ?)"
df = pd.read_csv('genotyping_data/metadata.csv', sep=',', index_col=0)
to_db = [(i['dna_chip_id'], i['breed'], i['sex']) for j, i in df.iterrows()]
connection.executemany(query, to_db)

# # Способ 3. Вопреки заверениям с форумов, не заработал
# df = pd.read_csv('genotyping_data/metadata.csv', sep=',', index_col=0)
# df.to_sql('metadata', 'connection', if_exists='append', index=False)

# Способ 0
# genstudio = pd.read_csv('genotyping_data/genstudio.csv', sep=',', index_col=0)
# genstudio.head(10)
# genstudio.dtypes
# genstudio['Chr'].tail(40)
#
# query2 = '''INSERT INTO genstudio (SNP_Name, SNP_Index, SNP_Aux, Sample_ID, SNP, Allele1_Top, Allele2_Top,
#          Allele1_Forward, Allele2_Forward, Allele1_AB, Allele2_AB, Chr, Position, GC_Score, GT_Score,
#          Theta, R, B_Allele_Freq, Log_R_Ratio) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
#
# for index, data in genstudio.iterrows():
#     mydata = list(data)
#     connection.execute(query2, mydata)

# Способ 1.
query2 = '''INSERT INTO genstudio (SNP_Name, SNP_Index, SNP_Aux, Sample_ID, SNP, Allele1_Top, Allele2_Top,
         Allele1_Forward, Allele2_Forward, Allele1_AB, Allele2_AB, Chr, Position, GC_Score, GT_Score,
         Theta, R, B_Allele_Freq, Log_R_Ratio) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
df = pd.read_csv('genotyping_data/genstudio.csv', sep=',', index_col=0, chunksize=10000)
for chunk in df:
    to_db = [(i['SNP Name'], i['SNP Index'], i['SNP Aux'], i['Sample ID'], i['SNP'], i['Allele1 - Top'], i['Allele2 - Top'],
          i['Allele1 - Forward'], i['Allele2 - Forward'], i['Allele1 - AB'], i['Allele2 - AB'], i['Chr'], i['Position'],
          i['GC Score'], i['GT Score'], i['Theta'], i['R'], i['B Allele Freq'], i['Log R Ratio']) for k, i in chunk.iterrows()]
    connection.executemany(query2, to_db)
# Этот способ так же не дает преимущества в производительности. Способ 0 (выше) отработал гораздо быстрее!
# Не знаю, короче, какой способ ты тимел в виду в комментариях в чате

connection.commit()
connection.close()