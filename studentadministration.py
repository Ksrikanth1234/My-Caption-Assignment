import csv
def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer= csv.writer(csv_file)

        if csv_file.tell()==0:
            writer.writerow(["name","age","mobile","E-mail"])

        writer.writerow(info_list)

if __name__=='__main__':
    condition=True
    student_num=1

    while condition:
        student_info=input("Enter student #{} details(name,age,mobile,e-mail):".format(student_num))
        student_list=student_info.split(' ')
        print("\nName:{}\nAge:{}\nMobile:{}\nE-mail:{}".format(student_list[0],student_list[1],student_list[2],student_list[3]))

        check=input("Is entered details correct?(yes/no):")

        if check=="yes":
             write_into_csv(student_list)
             student_num+=1

             condition_check=input("Enter (yes/no) if you want to enter another student info:")
             if condition_check=="yes":
                 condition=True
             elif condition_check=="no":
                 condition=False
        elif check=="no":
                 print("re-enter details!!\n"
