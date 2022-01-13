import os
import pandas as pd

files = os.listdir('data/')
df_list = []
all_students_list = []
for file in files:
    path = 'data/'
    path += file
    if path.split('.')[-1] == 'csv':
        print(path)
        df = pd.read_csv(path, encoding='utf-16')
        # print(df.head())
        df_list.append(df)

    elif path.split('.')[-1] == 'xls':
        print(path)
        with open(path, 'rb') as file:
            df = pd.read_excel(file)
            print(df.head())
            all_students_list.append(df)

all_students = pd.concat(all_students_list, ignore_index=True, sort=False)

all_mails = all_students['Institute Email'].to_list()

lesser_attendy_list = []
for mail in all_mails:
    count = 0
    for df in df_list:
        my_list = df['MAIL_ID'].apply(lambda x:x.upper()).to_list()
        if mail in my_list:
            count += 1

    all_students.loc[all_students['Institute Email'] == mail, "Attendance"] = count
    if count < 5:
        lesser_attendy_list.append(all_students.loc[all_students['Institute Email'] == mail])
        print()

lesser_attendy_df = pd.concat(lesser_attendy_list, ignore_index=True, sort=False)
for val in lesser_attendy_df['Email'].values:
    print(val)
# lesser_attendy_df[['Name', 'Roll No', 'Attendance', 'Email', 'Institute Email']].to_csv('lesser_attende.csv')
# all_students.to_csv('all_students_report.csv')
