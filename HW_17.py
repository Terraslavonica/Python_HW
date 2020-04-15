import sqlite3
import pandas as pd
import os


# Task 1. Прочитайте о следующих командах и попробуйте их - UPDATE, DELETE, CASCADE
# не опняла, что значит попробовать? На табличке какой-нибудь?

# Task 2. Пришло время сделать свою БД! Подумайте как организовать базу, создайте её и заполните
# данными через питон на основе своих данных или воспользуйтесь учебными

# Create connaction
connection = sqlite3.connect('chipseq.db')

# First table, metadata about animal
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
metadata = pd.read_csv('genotyping_data/metadata.csv', sep = ',', index_col=0)
metadata.head(10)

query = "INSERT INTO metadata (dna_chip_id, breed, sex) VALUES (?, ?, ?)"

for index, data in metadata.iterrows():
    mydata = list(data)
    connection.execute(query, mydata)

genstudio = pd.read_csv('genotyping_data/genstudio.csv', sep = ',', index_col=0)
genstudio.head(10)
genstudio.dtypes
genstudio['Chr'].tail(40)

query2 = '''INSERT INTO genstudio (SNP_Name, SNP_Index, SNP_Aux, Sample_ID, SNP, Allele1_Top, Allele2_Top,
         Allele1_Forward, Allele2_Forward, Allele1_AB, Allele2_AB, Chr, Position, GC_Score, GT_Score,
         Theta, R, B_Allele_Freq, Log_R_Ratio) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

for index, data in genstudio.iterrows():
    mydata = list(data)
    connection.execute(query2, mydata)

connection.commit()
connection.close()
