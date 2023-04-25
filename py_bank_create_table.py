import sqlite3


db_path = 'db_data/py_bank.db'
create_table_sql_query = '''
CREATE TABLE IF NOT EXISTS companies(
	id INTEGER PRIMARY KEY
	name TEXT NOT NULL,
	vat_id TEXT NOT NULL,
	street_and_number TEXT NULL,
	postal_code TEXT NULL,
	city TEXT NOT NULL,
	country TEXT NOT NULL,
	contact_person TEXT NULL
);
'''

try:
    
    db_connection = sqlite3.connect(db_path)
    # 2. korak je kreiranje kursora za kretanje po bazi podataka
    cursor = db_connection.cursor()
    # 3. korak pokreni SQL upit
    #cursor.execute('SQL Query upit za rad s podacima u bazi')
    cursor.execute(create_table_sql_query)
    
    # 3.1 korak ako je upit za dohvat podataka (read/select) onda pozovemo fetchall()
    record_set = cursor.fetchall()
    print(record_set)
    
    # 3.2 korak ako je upit za promjenu podataka (insert, update i delete) onda pozovemo commit() 
    #                       ili za snimanje izmjena u bazu 
    #db_connection.commit()
    
    # 4. korak zatvorimo cursor objekt
    cursor.close()

except sqlite3.Error as error:
    print(f'Dogodila se greska u vezi baze: {error}')
except Exception as ex:
    print(f'Dogodila se greska: {ex}')

finally:
    # Finalni korak zatvoriti konekciju prema bazi podataka 
    if db_connection:
        db_connection.close()