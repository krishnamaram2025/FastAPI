import mysql.connector
import datetime
import time
import os

def mysql_connect():
    # Establish a connection to the MySQL database
    db_con = mysql.connector.connect(
        host=os.environ['DB_SERVER'],
        user=os.environ['DB_USR'],
        password=os.environ['DB_PWD'],
    )
    return db_con

def insert_skill(skill):
    """
	Method to insert a skill into the database
	"""
    try:
        db_con = mysql_connect()
        # Create a cursor to interact with the database
        db_session = db_con.cursor()      
        insert_query = f"INSERT INTO portfolio.skills (skill_name, stream_name) VALUES ('{skill['skill_name']}','{skill['stream_name']}');"
        res= db_session.execute(insert_query)
        db_con.commit()
        print("res", res)
        return res
			
    except Exception as err:
        print(str(err))
        raise

def get_skills():
    db_con = mysql_connect()
    # Create a cursor to interact with the database
    db_session = db_con.cursor()
    # Execute a SELECT query
    query = f"SELECT * FROM portfolio.skills"
    db_session.execute(query)
    # Fetch all records from the result set
    all_skills = db_session.fetchall()
    skills = []
    for skill in all_skills:
        skill_dict = {
            "skill_name" : skill[0],
            'stream_name': skill[1]      
            }
        skills.append(skill_dict)
    print(skills)
    return skills


def update_skill(skill):
    db_con = mysql_connect()
    # Create a cursor to interact with the database
    db_session = db_con.cursor()
    update_query = f"UPDATE portfolio.skills SET skill_name = '{skill['skill_name']}' WHERE stream_name = '{skill['stream_name']}';"
    print(update_query)
    db_session.execute(update_query)
    db_con.commit()

def delete_skill(skill):
    db_con = mysql_connect()
    # Create a cursor to interact with the database
    db_session = db_con.cursor()
    update_query = f"DELETE FROM portfolio.skills WHERE skill_name = '{skill['skill_name']}';"
    print(update_query)
    db_session.execute(update_query)
    db_con.commit()




