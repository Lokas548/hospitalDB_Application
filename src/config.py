import pyodbc

def connectDB():
    connectionString = (
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=KOMPUTER;'
        r'DATABASE=Больница;'
        r'Trusted_Connection=yes;')

    connect = pyodbc.connect(connectionString)
    if(connect):
        print("success")
    else:
        print("no connection")
    return connect

connection = connectDB()
cursor = connection.cursor()

def findEmployee(data):
    if(data[0] == "id_сотрудника"):
        SQLQUERRY = f"""SELECT *
        FROM Сотрудник
        WHERE {data[0]} = {data[1]}"""
        rows = connection.cursor().execute(SQLQUERRY).fetchall()
    elif (data[0] == "НаименованиеОтделение"):
        SQLQUERRY = f"""SELECT *
                FROM Сотрудник
                WHERE id_отделения = (SELECT id_отделения
                FROM Отделение
                WHERE Отделение.Наименование = N'{data[1]}')"""
        rows = connection.cursor().execute(SQLQUERRY).fetchall()
    elif(data[0] == "НаименованиеДолжность"):
        SQLQUERRY = f"""SELECT *
        FROM Сотрудник
        WHERE id_должности = (SELECT id_должности
        FROM Должность
        WHERE Должность.Наименование = N'{data[1]}')"""
        rows = connection.cursor().execute(SQLQUERRY).fetchall()
    elif(data[0] == "Наименование"):
        SQLQUERRY = f"""SELECT *
            FROM Сотрудник
            WHERE {data[0]} = {data[1]}"""
        rows = connection.cursor().execute(SQLQUERRY).fetchall()
    elif (data[0] == "ФИО"):
        SQLQUERRY = f"""SELECT *
                FROM Сотрудник
                WHERE Фамилия = N'{data[1]}' and Имя = N'{data[2]}' and Отчество = N'{data[3]}'"""
        rows = connection.cursor().execute(SQLQUERRY).fetchall()
    if(data[0] == "*"):
        SQLQUERRY = f"""SELECT *
        FROM Сотрудник"""
        rows = connection.cursor().execute(SQLQUERRY).fetchall()
    return rows

def findEmployeeColumns():
    list = []
    for row in cursor.columns(table='Сотрудник'):
        list.append(row.column_name)

    return list

def findPatient(data):
    if(data[0] == "id_пациента"):
        SQLQUERRY = f"""SELECT *
        FROM Пациент
        WHERE {data[0]} = {data[1]}"""
        rows = connection.cursor().execute(SQLQUERRY).fetchall()
    elif (data[0] == "ФИО"):
        SQLQUERRY = f"""SELECT *
                FROM Пациент
                WHERE Фамилия = N'{data[1]}' and Имя = N'{data[2]}' and Отчество = N'{data[3]}'"""
        rows = connection.cursor().execute(SQLQUERRY).fetchall()
    elif (data[0] == "Номер_полиса"):
        SQLQUERRY = f"""SELECT *
            FROM Пациент
            WHERE {data[0]} = '{data[1]}'"""
        rows = connection.cursor().execute(SQLQUERRY).fetchall()
    if (data[0] == "*"):
        SQLQUERRY = f"""SELECT *
            FROM Пациент"""
        rows = connection.cursor().execute(SQLQUERRY).fetchall()
    return rows

def findPatientColumns():
    list = []
    for row in cursor.columns(table='Пациент'):
        list.append(row.column_name)

    return list

def findScheudleColumns():
    list = []
    for row in cursor.columns(table='Прием'):
        list.append(row.column_name)

    return list

def getScheudle(data):
    SQLQUERRY = f"""SELECT *
                   FROM Прием
                   WHERE Прием.id_сотрудника = (SELECT id_сотрудника
							FROM Сотрудник
							WHERE Фамилия = N'{data[0]}' AND Имя = N'{data[1]}' AND Отчество = N'{data[2]}')
	AND id_пациента IS NULL
    """
    rows = connection.cursor().execute(SQLQUERRY).fetchall()
    return rows

def insertAppoint(data,id):
    SQLQUERRY = f"""execute [Записать_на_прием] {id},{data[0]},{data[1]},{data[2]}"""
    append = connection.cursor().execute(SQLQUERRY)
    connection.commit()
    return append

def insertEmployee(data):
    SQLQUERRY = f'''execute [Добавить_сотрудника] {data[0]},{data[1]},{data[2]},{data[3]},{data[4]},
    {data[5]},{data[6]},{data[7]},{data[8]},{data[9]}'''
    append = connection.cursor().execute(SQLQUERRY)
    connection.commit()
    return append

def insertPatient(data):
    SQLQUERRY = f'''execute [Добавить_пациента] {data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]},{data[7]}'''
    append = connection.cursor().execute(SQLQUERRY)
    connection.commit()
    return append

def patientHistory(id):
    SQLQUERRY = f'''SELECT * FROM [История_болезней] ({id})'''
    rows = connection.cursor().execute(SQLQUERRY).fetchall()
    return rows

def patientSickDays(id):
    SQLQUERRY = f'''SELECT * FROM [Больничные_Пациента]({id})'''
    rows = connection.cursor().execute(SQLQUERRY).fetchall()
    return rows



