{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8afae10e",
   "metadata": {},
   "outputs": [],
   "source": [
    "mysql.connector   - caching sha2 password error-  innodb\n",
    "pymysql\n",
    "psychopg2 - postgresql\n",
    "pyodbc- microsoft sql server\n",
    "sqlalchemy  engine"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "41999def",
   "metadata": {},
   "outputs": [],
   "source": [
    "sqlite3      - in memory database\n",
    "sqlitestudio"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9c7abb13",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: mysql.connector in c:\\users\\nehla\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (2.2.9)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 23.2 -> 23.2.1\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "!pip install mysql.connector"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "3d49bf9d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import mysql.connector"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "dd81281b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<mysql.connector.connection_cext.CMySQLConnection object at 0x000002AFFF4654B0>\n"
     ]
    }
   ],
   "source": [
    "con= mysql.connector.connect(\n",
    "    host=\"localhost\",\n",
    "    user=\"root\",\n",
    "    password=\"2594\",\n",
    "    autocommit=True\n",
    "    )\n",
    "print(con)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "8f78d00a",
   "metadata": {},
   "outputs": [],
   "source": [
    "mycursor=con.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "0dd5e688",
   "metadata": {},
   "outputs": [],
   "source": [
    "mycursor.execute(\"CREATE DATABASE SQLPYTHON1\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "b713098d",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('awesome chocolates',)\n",
      "('firstdb',)\n",
      "('freshdb',)\n",
      "('information_schema',)\n",
      "('mv',)\n",
      "('mydb',)\n",
      "('mysql',)\n",
      "('newdb',)\n",
      "('performance_schema',)\n",
      "('pestdatabase',)\n",
      "('pesticide',)\n",
      "('projects_hr',)\n",
      "('sakila',)\n",
      "('sqlpython',)\n",
      "('sys',)\n",
      "('tamilsql',)\n",
      "('world',)\n",
      "('youtubedb',)\n"
     ]
    }
   ],
   "source": [
    "mycursor.execute(\"SHOW DATABASES\")\n",
    "for x in mycursor:\n",
    "    print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "68211751",
   "metadata": {},
   "outputs": [],
   "source": [
    "mycursor.execute(\"USE SQLPYTHON1\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "849ddbb6",
   "metadata": {},
   "outputs": [],
   "source": [
    "mycursor.execute(\"CREATE TABLE stud (sid INT,sname VARCHAR(20),mark INT)\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "21f7f84a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# VARCHAR -  2000 BYTES\n",
    "# VARCHAR2- 4000 BYTES"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "7bb14be2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('stud',)\n"
     ]
    }
   ],
   "source": [
    "mycursor.execute(\"show tables\")\n",
    "for y in mycursor:\n",
    "    print(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "09e41a2c",
   "metadata": {},
   "outputs": [],
   "source": [
    "mycursor.execute(\"insert into stud values(1,'aaa',98),(2,'bbb',88)\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "001662da",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 'aaa', 98)\n",
      "(2, 'bbb', 88)\n",
      "(3, 'ccc', 55)\n",
      "(4, 'ddd', 99)\n",
      "(5, 'gg', 66)\n"
     ]
    }
   ],
   "source": [
    "mycursor.execute(\"Select * from stud\")\n",
    "for y in mycursor:\n",
    "    print(y)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "167fb881",
   "metadata": {},
   "outputs": [],
   "source": [
    "sql=\"insert into stud(sid,sname,mark) values(%s,%s,%s)\"\n",
    "mylist=[\n",
    "    (3,'ccc',55),\n",
    "    (4,'ddd',99),\n",
    "    (5,'gg',66),\n",
    "]\n",
    "mycursor.executemany(sql,mylist)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b4955a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas pd\n",
    "\n",
    "pd.read_csv(r\"Desktop\\employee.csv\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "ad764f70",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3 rows are inserted\n"
     ]
    }
   ],
   "source": [
    "print(mycursor.rowcount, \"rows are inserted\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
