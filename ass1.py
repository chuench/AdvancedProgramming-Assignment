import csv
import smtplib

# Read the Vaccination.csv file
filename = 'Vaccination.csv'
with open(filename, 'r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]

# Save the data in a newly created csv file named NewCSVdataFile.csv
new_filename = 'NewCSVdataFile.csv'
with open(new_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Send an email notification when the process is done
sender = "mingchuen07@gmail.com"
receiver = "xiaoming1xf@outlook.com"
message = f"Subject: Succesfull copying data from {filename} to {new_filename}\n\nData copy task has been completed successfully."

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender, "xkucdofapzqtrlye")
    smtp.sendmail(sender, receiver, message)
