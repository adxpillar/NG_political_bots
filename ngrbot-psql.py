import psycopg2-binary 
import os
from dotenv import load_dotenv

load_dotenv()

localhost = os.getenv('LOCAL_HOST')
database =  os.getenv('DATABASE') 
port = os.getenv('PORT')
user = os.getenv('USER')
password = os.getenv('PASSWORD')



conn = psycopg2.connect(host=localhost,database=database,port=port,user=user,password=password)
cur = conn.cursor()

# # Table creation
# commands = (# Table 1
#             '''
#             Create Table TwitterUser(User_Id BIGINT PRIMARY KEY, User_Name TEXT);
#             ''',
#             # Table 2
#             '''Create Table TwitterTweet(Tweet_Id BIGINT PRIMARY KEY,
#                                          User_Id BIGINT,
#                                          Tweet TEXT,
#                                          Retweet_Count INT,
#                                          CONSTRAINT fk_user
#                                              FOREIGN KEY(User_Id)
#                                                  REFERENCES TwitterUser(User_Id));''',
#             # Table 3
#             '''Create Table TwitterEntity(Id SERIAL PRIMARY KEY,
#                                          Tweet_Id BIGINT,
#                                          Hashtag TEXT,
#                                          CONSTRAINT fk_user
#                                              FOREIGN KEY(Tweet_Id)
#                                                  REFERENCES TwitterTweet(Tweet_Id));''')

for command in commands:
    # create tables 
    cur.execute(command)

conn.commit()
cur.close()
conn.close()