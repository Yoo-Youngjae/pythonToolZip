import pymysql.cursors
import pandas as pd
import datetime


# pymysql 을 이용하기 위한 접근 연결
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

############################################################
try:
    with connection.cursor() as cursor: #pymysql 문법. cursor 가 db 와의 연결점이다.

        res = pd.DataFrame({'A':[],'B':[], 'C':[], 'D' : [], 'E':[],'F':[],'G':[]})

        for i in range(19):
            # 신규 결제 학생수
            sql = '''
            
                        '''
            cursor.execute(sql)
            A = cursor.fetchall()

            sql = '''
                        
                                    '''
            cursor.execute(sql, )
            B = cursor.fetchall()

            sql = '''
            
            '''
            cursor.execute(sql)
            C = cursor.fetchall()

            sql = '''
                     
                        '''
            cursor.execute(sql)
            D = cursor.fetchall()


            row = pd.DataFrame([[A,B,C,D]],
                               columns=['A', 'B', 'C','D'])
            res = pd.concat([res, row])
        res.to_csv("csv/test.csv", mode="w", encoding='EUC-KR')
except Exception as e:
    print(e)
finally:
    connection.close()