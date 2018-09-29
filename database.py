import influxdb


def conn(host="les1ie.com", port=8086, user="root", password="fafa", db="cpu"):
    client = influxdb.InfluxDBClient(host=host, port=port, username=user, password=password,database=db)
    return client

def write(conn, data:list):
    conn.write_points(data)

def query(conn, sql):
    result = conn.query(sql)
    return result
