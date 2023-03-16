import psycopg2

class Database:
    def __init__(self, host, port, user, password, dbname):
        self.conn = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            dbname=dbname
        )

    def get_channel_ids(self):
        cur = self.conn.cursor()
        cur.execute('SELECT channel_id FROM channels')
        rows = cur.fetchall()
        cur.close()
        return [row[0] for row in rows]

    def close(self):
        self.conn.close()