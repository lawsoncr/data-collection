# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 21:58:57 2021

@author: claws
"""

import pandas as pd
def main():
    personData = pd.read_csv('basic_person.csv')
    studentData = pd.read_csv('person_detail_f.csv')
    mapData = pd.read_csv('student_detail_v.csv')
    
    personData = pd.DataFrame(personData)
    studentData = pd.DataFrame(studentData)
    mapData = pd.DataFrame(mapData)
    
    mapData = mapData.groupby('student_id_new')
    mapData = mapData.max().reset_index()
    df = mapData.merge(personData, on='acct_id_new')
    df = df.merge(studentData, on='person_detail_id_new')
    df = df.to_csv('joined.csv', index=False)
    
if __name__ == '__main__':
    main()
