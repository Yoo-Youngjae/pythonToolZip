import pymysql.cursors
import pandas as pd

## mysql connection 정보 입력
hostname = '127.0.0.1'
port = 3306
username = 'root'
password = 'myPassWord'
defaultSchema = ''
##########################

connection = pymysql.connect(host=hostname,
                             port=port,
                             user=username,
                             password=password,
                             db=defaultSchema,
                             charset='utf8')
try:
    with connection.cursor() as cursor:
        # 아래에 sql 문을 복붙 하세요.
        sql = '''
                    SELECT pid, name, type, price, bookedAidCount from performances
                    ;
                 '''
        # sql 문을 실행
        cursor.execute(sql)
        # sql 문 실행 결과를 받아오기.
        rows = cursor.fetchall()
        df = pd.DataFrame(rows)
        print(df)
except Exception as e:
    # 에러 발생시 에러코드가 아래를 통해 출력됩니다.
    print(e)
finally:
    # 프로그램이 종료될 때 connection 을 닫아 줍니다.
    connection.close()