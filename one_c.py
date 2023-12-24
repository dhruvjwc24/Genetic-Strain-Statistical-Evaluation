import pandas as pd
from one_b import z_test, gene_goodness
from IPython.display import display

class GeneTest:
    TH = 4
    
    def __init__(self, fname):
        self.fname = fname
        self.df = pd.read_csv(fname)
    def z_test(self):
        z_score, p_value = z_test(self.data, self.TH, tail="right")
        return z_score, p_value
    def readValues(self):
        zScores = []
        pVals = []
        geneGness = []
        for row in self.df.iterrows():
            self.data = row[1].to_list()
            self.data = self.data[1:len(self.data)-3]
            self.z, self.p = self.z_test()
            _, self.gene = gene_goodness(self.z)
            zScores.append(self.z)
            pVals.append(self.p)
            geneGness.append(self.gene)
            #print(self.p, self.z, self.gene)
        self.df["z-score"] = zScores
        self.df["p-val"] = pVals
        self.df["Gene-Gness"] = geneGness
    def display(self):
        display(self.df)

def main():
    fName = "SampleData.csv"
    set = GeneTest(fName)
    set.readValues()
    set.display()

if __name__ == "__main__": main()