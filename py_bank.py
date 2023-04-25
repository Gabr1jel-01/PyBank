import sqlite3
from datetime import datetime as dt

from features import (Company,
                      Currency,
                      BankAccount)

#region Kreiranje bankovnog racuna
# account_number = f'BA-{dt.now().year}-{dt.now().month}-{"42".zfill(5)}'

# account_owner = Company(1,
#                         'Firma d.o.o.',
#                         '12345467',
#                         'Ulica i broj',
#                         '10040',
#                         'Dubrava',
#                         'Hrvatska',
#                         'Pero')

# currency = Currency(1, 'EUR', 'EURO')

# bank_account = BankAccount(1, 
#                            account_number,
#                            account_owner,
#                            currency,
#                            10_999.99)

# print(bank_account)
# print(bank_account.currency)

# for transaction in bank_account.transactions:
#     print(transaction)
    
# opening_amount = bank_account.transactions[0].amount
# print(opening_amount)
#endregion


try:
    # 1. korak, otvori konekciju prema bazi
    #db_connection = sqlite3.connect('putanja do foldera u kojem ce se nalaziti baza')
    db_connection = sqlite3.connect('db_data/py_bank.db')
    # 2. korak je kreiranje kursora za kretanje po bazi podataka
    cursor = db_connection.cursor()
    # 3. korak pokreni SQL upit
    #cursor.execute('SQL Query upit za rad s podacima u bazi')
    cursor.execute('SELECT sqlite_version()')
    
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
    
    
    
