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

def insert_team(team):
    """
	Method to insert a team into the database
	"""
    try:
        db_con = mysql_connect()
        # Create a cursor to interact with the database
        db_session = db_con.cursor()      
        insert_query = f"INSERT INTO hackathon.teams (team_name, member1, member2, member3) VALUES ('{team['team_name']}','{team['member1']}','{team['member2']}', '{team['member3']}');"
        res= db_session.execute(insert_query)
        db_con.commit()
        print("res", res)
        return res
			
    except Exception as err:
        print(str(err))
        raise

def get_teams():
    db_con = mysql_connect()
    # Create a cursor to interact with the database
    db_session = db_con.cursor()
    # Execute a SELECT query
    query = f"SELECT * FROM hackathon.teams"
    db_session.execute(query)
    # Fetch all records from the result set
    all_teams = db_session.fetchall()
    teams = []
    for team in all_teams:
        team_dict = {
            "team_name" : team[0],
            'member1': team[1],
            'member2': team[2],
            'member3': team[3]        
            }
        teams.append(team_dict)
    print(teams)
    return teams


def update_team(team):
    db_con = mysql_connect()
    # Create a cursor to interact with the database
    db_session = db_con.cursor()
    update_query = f"UPDATE hackathon.teams SET member1 = '{team['member1']}' WHERE team_name = '{team['team_name']}';"
    print(update_query)
    db_session.execute(update_query)
    db_con.commit()

def delete_team(team):
    db_con = mysql_connect()
    # Create a cursor to interact with the database
    db_session = db_con.cursor()
    update_query = f"DELETE FROM hackathon.teams WHERE team_name = '{team['team_name']}';"
    print(update_query)
    db_session.execute(update_query)
    db_con.commit()




