import csv
import sqlite3


def statistic():
    connect = sqlite3.connect("database.db")
    cursor = connect.cursor()
    cursor.execute(
        'create table if not exists Datas(country TEXT, dates DATE, total INTEGER, new INTEGER, death INTEGER, newdeath INTEGER )')
    cursor.execute(
        'create table if not exists Countries(country TEXT, dates DATE, total INTEGER, new INTEGER, death INTEGER, newdeath INTEGER )')
    cursor.execute(
        'create table if not exists Numbers(num INTEGER )')
    check = []
    searchingCursor = connect.execute(
        'select * from Datas limit 1;')
    searching = searchingCursor.fetchall()
    for set in searching:
        check.append(set)

    if not check:
        cursor = connect.cursor()
        cursor.execute('drop table if exists Datas')
        cursor.execute('create table if not exists Datas(country TEXT, dates DATE, total INTEGER, new INTEGER, death INTEGER, newdeath INTEGER )')

        dataList = csv.reader(open("covid.csv", "r"))
        for set in dataList:
            if set[0] == "iso_code":
                pass
            else:
                database = [set[2], set[3], set[4], set[5], set[6], set[7]]
                cursor.execute(
                    "INSERT INTO Datas(country, dates, total, new, death, newdeath) VALUES (?,?,?,?,?,?);", database)
                connect.commit()
    else:
        pass

    check2 = []
    searchingCursor = connect.execute(
        'select * from Countries limit 1;')
    searching2 = searchingCursor.fetchall()
    for set in searching2:
        check2.append(set)
    if not check2:
        cursor = connect.cursor()
        cursor.execute('drop table if exists Countries')
        cursor.execute('create table if not exists Countries(country TEXT PRIMARY KEY, population INTEGER, popdense FLOAT, life FLOAT)')
        dataList = csv.reader(open("covid.csv", "r"))
        CountryList = []
        for set in dataList:
            if set[0] == "iso_code":
                pass
            else:
                if set[2] in CountryList:
                    pass
                else:
                    database = [set[2], set[20], set[21], set[33]]
                    CountryList.append(set[2])
                    cursor.execute(
                        "INSERT INTO Countries(country, population, popdense, life) VALUES (?,?,?,?);", database)
                    connect.commit()
    else:
        pass
