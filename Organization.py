# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:46:09 2020

@author: John Meluso
"""
import org_struct as ostr


class Organization(object):
    '''Defines a class Organization which contains an organization network
    structure (a.k.a. an organizational form) populated with agents.'''

    def __init__(self, struct="tree", specs=[4,5]):
        '''
        Creates an instance of class Organization with a specified structure and
        corresponding parameters for that structure. The default is a standard
        tree organizational form.

        Parameters
        ----------
        struct : STRING, optional
            DESCRIPTION. Defines the form or structure of the organization. The
            default is "tree".
        specs : LIST, optional
            DESCRIPTION. Defines the parameters for a specified organizational
            form. The default is [4,5] for a tree structure wherein the zeroth
            entry specifies the tree height and the first entry specifies the
            number of children per node.

        Returns
        -------
        None.

        '''

        # Create network graph of organization
        if struct == "tree":
            self.graph = ostr.clique_tree(specs[0],specs[1])
        else:
            print("Input 'struct' for 'Organization' is not valid.")

        # Create an empty organization
        org = []

        # Create an employee for each node of the organization graph
        for node_ in self.graph:

            #todo - Append agents to organization
            org.append()



    def __repr__(self):
        '''Returns a representation of the organization'''
        return self.__class__.__name__



if __name__ == '__main__':
    o1 = Organization()