from itertools import permutations
import numpy as np
import pandas as pd


def gene_matrix():
    data = permutations(list("ACGT"))
    combinations = ["".join(item) for item in data]
    matrix = np.array([[np.random.choice(combinations) for n in range(4)] for n in range(10)]).reshape(10,4)
    return matrix


if __name__ == "__main__":
    df = pd.DataFrame(gene_matrix(), columns=["Specimen1",
                                              "Specimen2",
                                              "Specimen3",
                                              "Specimen4"])
    df.index +=1
    print(df)
