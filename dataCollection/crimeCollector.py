import pandas as pd
import time
import concurrent.futures
from sqlalchemy import create_engine
from pandas.io import sql

# Database creds, don't share on public repo
hostname='95.217.156.58'
dbname='crimeStats'
uname='sandwich'
pwd='321#@!IdiotSandwich'
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=uname, pw=pwd))



def get_data(amount):
    j = amount*1000
    print('---------', j)
    df = pd.read_json(
        'https://data.cityofnewyork.us/resource/8h9b-rp9u.json?$offset=%s' % j)
    df.to_sql('crimeTableSegmented', engine, if_exists='append', index=False)
    return df


def main():
    start = time.perf_counter()
    fdb = pd.DataFrame()
    with concurrent.futures.ProcessPoolExecutor() as executor:

        results = [executor.submit(get_data, ij) for ij in range(5012)]

        for f in concurrent.futures.as_completed(results):
            fdb = pd.concat([fdb, f.result()])


    finish = time.perf_counter()
    print('\n\n\n')
    print(f'--------------- {round(finish-start,2)} second(s) ---------------')
    print()

    # This will not work due to coord formatting
    # fdb.to_sql('crimeTable', engine, if_exists='append', index=False)

    # will create ~1.5gb csv
    fdb.to_csv('crimeStats.csv')


if __name__ == '__main__':
    main()