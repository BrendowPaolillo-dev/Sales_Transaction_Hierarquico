import csv

def get_data():
    newfile = open ("noheadertable.txt", "r+")
    aux_list = []
    with open('Sales_Transactions_Dataset_Weekly.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        next(spamreader, None)
        for row in spamreader:
            vector =[]
            for j in range (1, 53):
                vector.append(row[j])
            aux_list.append(vector)
    for i in range (len(aux_list)-1):    
        newfile.write(str(aux_list[i]))
    newfile.close()
    return aux_list

def main():
    data = get_data()
    print data[0]
if __name__ =='__main__':
    main()