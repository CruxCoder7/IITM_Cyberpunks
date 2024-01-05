import numpy as np
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-mpnet-base-v2')

transaction_labels = {
    'misc': ['various', 'miscellaneous', 'other'],
    'grocery': ['food', 'supermarket', 'groceries'],
    'entertainment': ['movies', 'music', 'fun'],
    'gas_transport': ['fuel', 'transportation', 'gas'],
    'shopping': ['retail', 'stores', 'mall'],
    'food_dining': ['restaurants', 'dining', 'eating out'],
    'personal_care': ['self-care', 'grooming', 'hygiene'],
    'health_fitness': ['wellness', 'exercise', 'fitness'],
    'travel': ['journey', 'trip', 'vacation'],
    'kids_pets': ['children', 'family', 'pets'],
    'home': ['household', 'residence', 'dwelling']
}


def get_category(text):
    text_embeddings = model.encode([text])
    
    ground_headings = list(transaction_labels.keys())
    ground_label = list(i + " " + " ".join(transaction_labels[i]) for i in transaction_labels)
    ground_label_embeddings = model.encode(ground_label)
    
    matrix = euclidean_distances(text_embeddings, ground_label_embeddings)
    euclidean_distances_res = np.array([ground_headings[i] for i in matrix.argmin(axis = 1)])
    
    return euclidean_distances_res[0]

def get_embeddings(list_of_text): # Input Should be list of Words
    embeddings = model.encode(list_of_text)
    return embeddings