import joblib

def load_classifier():
    return joblib.load('model/heading_classifier.pkl')

# hierarchy/semantic_graph.py
import networkx as nx

def build_heading_graph(headings):
    G = nx.DiGraph()
    for i, h in enumerate(headings[:-1]):
        G.add_edge(h['text'], headings[i+1]['text'])
    return G
