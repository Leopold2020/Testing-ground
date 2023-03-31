import smtplib, os, schedule, time
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def send_to_list():
    receipients = ["oliver.stafferod@elev.ga.ntig.se"]
    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        for receipient in receipients:
                connection.sendmail(from_addr=EMAIL,
                to_addrs=receipient,
                msg=f"Subject: Test5 \n\n åäö".encode("utf-8"))   
        connection.close()


if __name__ == "__main__":

    schedule.every(60).seconds.do(send_to_list())

    while True:
        schedule.run_pending()
        time.sleep(1)
