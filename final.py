import pickle 
import numpy as np
import pandas as pd
class transaction:
    
    def __init__(self,amount,category):
        self.amount = amount
        self.category = category
# ['misc', 'grocery', 'entertainment', 'gas_transport', 'shopping',
# 'food_dining', 'personal_care', 'health_fitness', 'travel',
# 'kids_pets', 'home']
account_to_db = {
    "23456789012": "./datasets/mockData.csv"
}

account_cluster_to_forest = {
    1: "./models/amount_cluster_segment0isolationForest.pkl",
    0: "./models/amount_cluster_segment1isolationForest.pkl"
}

misc_cluster_to_forest={

0: "./models/amount_by_misc/segment_1_iForest.pkl",
1: "./models/amount_by_misc/segment_0_iForest.pkl",
2: "./models/amount_by_misc/segment_2_iForest.pkl"
}

food_dining_cluster_to_forest={

    0:'./models/amount_by_food_dining/segment_1_iForest.pkl',
    1:'./models/amount_by_food_dining/segment_0_iForest.pkl'
}

travel_cluster_to_forest={

    0: './models/amount_by_travel/segment_0_iForest.pkl',
    1: './models/amount_by_travel/segment_1_iForest.pkl'
}

shopping_cluster_to_forest={

    0:'./models/amount_by_shopping/segment_1_iForest.pkl',
    1: './models/amount_by_shopping/segment_0_iForest.pkl'
}

grocery_cluster_to_forest={

0: "./models/amount_by_grocery/segment_1_iForest.pkl",
1: "./models/amount_by_grocery/segment_2_iForest.pkl",
2: "./models/amount_by_grocery/segment_0_iForest.pkl"
}

d = {
    "misc":misc_cluster_to_forest,
    "food_dining":food_dining_cluster_to_forest,
    "travel":travel_cluster_to_forest,
    "shopping":shopping_cluster_to_forest,
    "grocery":grocery_cluster_to_forest
}
t1 = transaction(54,"food_dining")
def get_db(acc_no):

    return pd.read_csv(account_to_db[acc_no])

def get_amount_cluster(db):

    with open("./models/amount_clusters.pkl","rb") as f:
        model = pickle.load(f)

    return model.predict([[np.log(db["Amount"].mean())]])[0]

def get_amount_anomalous_score(db,curr_amount):

    cluster = get_amount_cluster(db)

    with open(account_cluster_to_forest[cluster],"rb") as f:
        model = pickle.load(f)

    return model.score_samples([[np.log(curr_amount)]])[0]

def get_category_anomalous_score(db,category,curr_amount):

    try:
        with open(f"./models/amount_by_{category}/clusters.pkl","rb") as f:
            model = pickle.load(f)

        cluster = model.predict([[np.log(db["Amount"].mean())]])[0]

        # print(cluster)

        # print(d[category][cluster])

        with open(d[category][cluster],"rb") as f:
            model = pickle.load(f)

        return model.score_samples([[np.log(curr_amount)]])[0]
    
    except:
        
        with open(f"./models/amount_by_{category}/iForest.pkl","rb") as f:
            model = pickle.load(f)

        return model.score_samples([[np.log(curr_amount)]])[0]

