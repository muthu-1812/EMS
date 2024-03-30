import os
import pickle

from Company import Company


def init_company():
    if os.path.isfile('data.pickle'):
        with open('data.pickle', 'rb') as f:
            return pickle.load(f)
    else:
        return Company("ABC_COMPANY")


def save_data_to_pickle(company):
    with open('data.pickle', 'wb') as f:
        pickle.dump(company, f)
