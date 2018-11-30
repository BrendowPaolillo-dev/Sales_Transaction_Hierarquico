import csv
import numpy as np
import scipy.cluster.hierarchy as sch
from scipy.spatial.distance import pdist
from scipy.spatial import distance
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering



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
    """w = []
    j = 0
    for j in range(len(data)):
        i = 0
        w.append([])
        s = 0
        while i < len(data[j]):
            s += data[j][i]
            s += data[j][i+1]
            s += data[j][i+2]
            s += data[j][i+3]
            w[j].append(s)
            s = 0
            i += 4"""

    for j in range(len(data)):
        s = 0
        i = 0
        for i in range(len(data[j])):
            s += data[j][i]
        i = 0
        for i in range(len(data[j])):
            data[j][i] = data[j][i]/s
    #print w
    X = pdist(data, 'euclidean')
    #print distance.euclidean(data[2], data[3])
    #print distance.euclidean(data[2], data[7])
    #print distance.euclidean(data[2], data[17])
    #print distance.euclidean(data[17], data[18])


    #print X
    Z = sch.linkage(X, 'average')
    #print Z
    #c = AgglomerativeClustering(n_clusters=10, affinity='euclidean')
    #print (c.fit_predict(data))
    A = sch.fcluster(Z, t=0.4, criterion='distance')
    print np.sort(A)
    print len(A)
    fig = plt.figure(figsize=(25, 10))
    dn = sch.dendrogram(Z)
    plt.show()

if __name__ =='__main__':
    main()