import datetime

def log_datetime():
    now = datetime.datetime.now()
    print(f"Script executed at: {now}")

if __name__ == "__main__":
    log_datetime()