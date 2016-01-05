#!/usr/bin/env python3

import Tree
import DCC

# This script can be used to create an html list and a spreadsheet of documents below the
# specified collection.  The main use of the code is to create CID lists in html and spreadsheet
# from from a set of collections containing CID files


froot = 'Test of CID keyword'
coll = 'Collection-8277'
keyword_filter = 'CID'    # if no keyword set keyword_filter = '' 

# Login to DCC
s = DCC.login(Site = 'Production') 

tr = Tree.return_tree(s, coll, froot)
Tree.xls_tree(s,tr,coll,froot, Keyword = keyword_filter)
Tree.html_tree(s,tr,froot, Keyword = keyword_filter)