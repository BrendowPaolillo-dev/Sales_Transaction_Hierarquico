import csv
import numpy as np
import scipy.cluster.hierarchy as sch
from scipy.spatial.distance import pdist
from matplotlib import pyplot as plt

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
    data = np.array(data)
    print data
    X = pdist(data, 'euclidean')
    print X
    Z = sch.linkage(X, 'single')
    print Z
    fig = plt.figure(figsize=(25, 10))
    dn = sch.dendrogram(Z)
    plt.show()
    
if __name__ =='__main__':
    main()