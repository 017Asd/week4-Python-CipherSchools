from csv import DictReader, DictWriter
with open('fiel.csv','r') as f:
    with open('file.csv','w') as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf, fieldnames=['name','email','phone'])
        csv_writer.writeheader()
        for row in csv_reader:
            name, email, phone = row['name'],row['email'],row['phone']
            csv_writer.writerow({
                'name':fname.upper().
            })