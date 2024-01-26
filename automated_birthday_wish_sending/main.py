import pandas
import datetime as dt
import smtplib
PLACEHOLDER="[NAME]"
import os,random
#reading birthday csv file#########
def read_csv():
     try:
        birthday_data=pandas.read_csv("birthdays.csv")

     except FileNotFoundError:
         print("file not availabe")

     else:
        birthday_data_dict=birthday_data.to_dict(orient="records")
        #print(birthday_data_dict)
        now_day=dt.datetime.now()
        #print(now_day)
        weekday=now_day.day
        month=now_day.month

        directory="letter_templates"
        file_name=random.choice(os.listdir(directory))
        count=0
        #print(birthday_data_dict)
        for item in birthday_data_dict:

           if weekday==item["day-33-API_learning"] and month==item["month"]:

             try:
                with open(f"letter_templates/{file_name}",'r') as file1:
                  letter_content=file1.read()
                  #print(letter_content)
                  stripped_name = item["name"].strip()
                  #print(stripped_name)
                  new_name = letter_content.replace(PLACEHOLDER,stripped_name)

             except FileNotFoundError:
                 print("File not found")

             # mail sending process#
             else:
                 my_email = "swarasadvelkar@gmail.com"


                 receiver = item["email"]
                 password = "duhc gzio bilf olvr"
                 with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                      # transport layer security  encryption  of data is done here#
                      connection.starttls()
                      connection.login(user=my_email, password=password)
                      connection.sendmail(from_addr=my_email, to_addrs=receiver,
                                          msg=f"Subject:Happy Birthday!\n\n{new_name}")
           else:
                print("no ones birthday today")

read_csv()





















