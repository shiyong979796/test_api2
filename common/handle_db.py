import pymysql


class HandleDb:
    def __init__(self, hos, port, database, user, pwd):
        self.connect = pymysql.connect(user=user, password=pwd, database=database, port=port)
        self.cur = self.connect.cursor(pymysql.cursors.DictCursor)

    def get_fetch_one(self, sql):
        self.cur.execute(sql)
        self.cur.fetchone()

    def get_fetchall(self, sq):
        self.cur.execute(sq)
        return self.cur.fetchall()

    def get_fetchone(self, sq):
        self.cur.execute(sq)
        return self.cur.fetchone()

    def count_line(self, sq):
        count = self.cur.execute(sq)
        return count

    def commit(self):
        self.connect.commit()

    def close_db(self):
        self.connect.close()
