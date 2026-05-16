import csv
with open("data.csv","w",newline="")as file:
    writer=csv.writer(file)
    writer.writerow(["ID","Name","Age"])
    writer.writerow([1,"Alice",20])
    writer.writerow([2,"Bob",21])
    writer.writerow([3,"Charlie",23])
    writer.writerow([4,"David",23])
    writer.writerow([5,"Eva",24])
print("CSV Contents:")
with open("data.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
search_id=input("Enter ID to search:")
with open("data.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        if row[0]==search_id:
            print("reader Found:",row)