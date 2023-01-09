from csv import writer

with open('file.csv','w') as f:
    csv_writer=  writer(f) 
    csv_writer.writerow(['name','email'])

    csv_writer.writerows(['name','email'])