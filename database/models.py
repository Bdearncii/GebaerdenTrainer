from db import connect_db

def add_user(username,email,password):

    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       INSERT INTO users (username, email,password) values (%s,%s,%s)
                       """, (username,email,password))
        conn.commit()

def get_user_by_username(username):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT * FROM users WHERE username = %s""", (username))
        return cursor.fetchone()


def add_progress(user_id, sprache, completion_date):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       INSERT INTO progress (user_id, fach, completion_date) VALUES (%s,%s,%s)"""
                       , (user_id,sprache,completion_date))
        conn.commit()


def get_progress_by_user(user_id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT * FROM progress WHERE user_id = %s"""
                       , (user_id))
        return cursor.fetchall()
    
def add_video(sprache, video_url, video_description): # gebrauch bar?
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       INSERT INTO videos (sprache, video_url, video_description) VALUES (%s,%s,%s)"""
                       , (sprache,video_url,video_description))

def get_video_by_description(video_description): # wörterbuch (description ist das wort wonach wir suchen)
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT * FROM videos WHERE video_description = %s """
                       , (video_description))
        return cursor.fetchall()
