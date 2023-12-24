import one_a
import pandas as pd
import math

#assuming population and sample have same variance
def z_test(data, th, tail, z_table_df=pd.read_csv("z_table.csv")):
    sam_mean, sam_stdDev, sam_size = one_a.get_values(data)
    z = z_score(sam_mean, th, sam_stdDev, sam_size)
    p = p_value(z_table_df, z, tail)
    return z, p

def z_score(sam_mean, pop_mean, pop_sd, sam_size):
    z = (sam_mean-pop_mean)/(pop_sd/math.sqrt(sam_size))
    return z

def gene_goodness(z):
    if(z > 0):
        return("Bad gene", 0)
    return("Good gene", 1)

#tail = ["left, right, both"]
def p_value(df, z, tail):
    z = round(z, 2)
    for rowIndex, row in df.iterrows(): #iterate over rows
        if(str(z)[0:len(str(z))-1] == str(row[0])): # str(z)[0:len(str(z))-1] == 
            base = row[0]
            #print(base)
            break
    last = str(z)[-1]
    p_value = row[int(last)+1]
    
    if(tail == "left"):
        p_value = p_value
    elif(tail == "right"):
        p_value = 1-p_value
    else:
        p_value = 2*(1-p_value)
    return p_value

def main():
    list = [5.564134549,5.652057928,4.954057564,4.502248279,4.712804662,4.780296574,4.575680795,3.301847137,5.20017023,5.197178333]
    th = 4
    z, p  = z_test(list, th, tail="right")
    gene, _ = gene_goodness(z)
    print("\n\tz-score: {}\n\tp-value: {}\n\tGene: {}\n".format(z, p, gene))

if __name__ == "__main__": main()