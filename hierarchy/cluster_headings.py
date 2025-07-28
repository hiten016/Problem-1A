#from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN

def cluster_headings(features):
    #model = AgglomerativeClustering(n_clusters=None, distance_threshold=1.5)
    model = DBSCAN(eps=1.5, min_samples=2)
    return model.fit_predict(features)
