import pandas as pd

def c2d(coordinatesDictionary:dict,timestep,moleculeID):
    return pd.DataFrame(coordinatesDictionary["structured-data"][timestep][moleculeID]).T

def atom1ToOrigin(atomsdf):
    first_row = atomsdf.iloc[[0]].values[0]
    return atomsdf.apply(lambda row: row - first_row, axis=1)