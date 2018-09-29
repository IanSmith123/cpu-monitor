import arrow
from database import conn, write, query
from get_usage import cpu_usage

def generate(obj, value, db):
    j = [
        {
            "measurement": obj,
            "tags": {
                "host": "laptop",
            },
            "time": str(arrow.now()),
            "fields": {
                "value": value
            }
        }
    ]
    return j



def main():
    con = conn()
    while True:
        cpu = cpu_usage()
        write(con, generate("cpu", cpu, "cpu"))
        print(cpu)

main()



