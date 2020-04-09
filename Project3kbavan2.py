import pandas
import matplotlib.pyplot as plt

fileref = open('SCDB_2019_01_justiceCentered_Citation.csv', encoding="ISO-8859-1")
scdb = pandas.read_csv(fileref)

#scdb2 = pandas.read_csv(fileref)


def project3():
    """This project analyzes the data from the given CSV file and ploting the graphs from the 
    given data. This porject is divided into six parts"""
    
    # part 1
    sub1 = scdb[scdb.term >= 2000]

    # part 2
    fa = plt.figure(figsize=(12, 12))
    sub1.groupby("term")["docketId"].count().plot(kind="bar")
    fa.tight_layout()
    fa.show()
    
    #part3
    
    fb	= plt.figure(figsize=(12,8))
    sub1.groupby(['justice', 'direction'])['caseId'].nunique().plot(kind="bar")
    fb.tight_layout()
    fb.show()
    
    #part 4
    sub2 = scdb[scdb.term >= 2006][scdb.term <= 2018]
    
    #part 5
    fc = plt.figure(figsize=(12,8))
    sub2.groupby('caseDisposition')['term'].count().plot(kind ="bar")
    fc.tight_layout()
    fc.show()
    
    #part 6
    fd = plt.figure(figsize=(12,12))
    sub2.groupby(['justiceName', 'majority'])["caseId"].count().plot(kind ="bar")
    fd.tight_layout()
    fd.show()
    
    
    

project3()

