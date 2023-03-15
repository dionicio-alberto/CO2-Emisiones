import pandas as pd
import matplotlib.pyplot as plt
import package.functionss as fss
 
data = pd.read_csv("package\co2_emissions_kt_by_country.csv",index_col=0)

if __name__ == "__main__":
    fss.que_ver(data)

