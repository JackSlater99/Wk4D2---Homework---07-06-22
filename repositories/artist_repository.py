from db.run_sql import run_sql
from models.artist import Artist

def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for result in results:
        artist = Artist(result['first_name'], result['last_name'], result['id'])
        artists.append(artist)
    return artists

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    if result is not None:
        artist = Artist(result['first_name'], result['last_name'], result['id'])
    return artist

def save(artist):
    sql = "INSERT INTO artists (first_name, last_name) VALUES (%s, %s) RETURNING id"
    values = [artist.first_name, artist.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']                                                                                   #THIS LINE???
    artist.id = id
    return artist

def update(artist):
    sql = "UPDATE artists SET (first_name, last_name) VALUES (%s, %s) WHERE id = %s"
    values = [artist.first_name, artist.last_name, artist.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)