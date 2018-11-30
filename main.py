import csv
import numpy as np
import scipy.cluster.hierarchy as sch
from scipy.spatial.distance import pdist
from scipy.spatial import distance
from matplotlib import pyplot as plt

def get_data():
    newfile = open ("noheadertable.txt", "r+")
    aux_list = []
    with open('Sales_Transactions_Dataset_Weekly.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        #print spamreader.shape
        next(spamreader, None)
        for row in spamreader:
            vector =[]
            for j in range (1, 53):
                vector.append(float(row[j]))
            aux_list.append(vector)
    for i in range (len(aux_list)-1):    
        newfile.write(str(aux_list[i]))
    newfile.close()
    return aux_list

def main():
    data = get_data()
    data = np.array(data)

    for j in range(len(data)):
        s = 0
        i = 0
        for i in range(len(data[j])):
            s += data[j][i]
        i = 0
        for i in range(len(data[j])):
            data[j][i] = data[j][i]/s

    X = pdist(data, 'euclidean')
    Z = sch.linkage(X, 'average')
    
    fig = plt.figure(figsize=(25, 10))
    dn = sch.dendrogram(Z)
    plt.show()

if __name__ =='__main__':
    main()