from csv import DictWriter
with open('file.csv','w') as f:
    csv_writer = DictWriter(f,fieldnames=['name','email','phone'])
    csv_writer.writerow({
        'name':'sree',
        'email':'sree@gmial.com',
        'phone':'970865789'
        })
