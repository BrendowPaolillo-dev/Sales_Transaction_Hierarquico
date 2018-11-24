import csv
if __name__ =='__main__':
    with open('Sales_Transactions_Dataset_Weekly.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            print ', '.join(row)