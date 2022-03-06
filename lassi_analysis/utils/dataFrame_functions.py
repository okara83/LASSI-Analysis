import pandas
import numpy

def c2d(coordinatesDictionary:dict,timestep,moleculeID):
    return pandas.DataFrame(coordinatesDictionary["structured-data"][timestep][moleculeID]).T

def atom1ToOrigin(atomsdf):
    first_row = atomsdf.iloc[[0]].values[0]
    return atomsdf.apply(lambda row: row - first_row, axis=1)

def node2node_distances_dataframe(atomsdf):
    '''returns N x N dataframe where N=natoms'''
    def node2node_distances(atomsdf:object):
        def distance_generator(atomsdf:object):
            '''lazy distance computation generator'''
            coordinates = atomsdf.values
            for x in coordinates:
                for y in coordinates:
                    yield numpy.linalg.norm(x - y)
            return
        return numpy.triu(numpy.array(list(distance_generator(atomsdf))).reshape(len(atomsdf),len(atomsdf))) #reshape because we return a (len(atomsdf)xlen(atomsdf))x1 array otherwise. So we group len(n) elements at a time
    
    def node_distances_dataframe(atomsdf:object):
        distances_matrix = node2node_distances(atomsdf)
        return pandas.DataFrame(distances_matrix)
        
    return node_distances_dataframe(atomsdf)