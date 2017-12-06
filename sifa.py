#  -*- coding: utf-8 -*-
from __future__ import unicode_literals
from gensim import corpora, models, similarities
from gensim.models import ldamodel, lsimodel
import codecs
import string
import nltk
import os
import re
import argparse
import sys

# Récupération des arguments
parser=argparse.ArgumentParser(description="Siffa is a program for semantic indexing of French articles. It uses Python LSI library.")
parser.add_argument("-i","--input", help="Entry folder of text files to index",required=True)
parser.add_argument("-o","--output", help="Output folder where the results will be stored",required=True)
args=parser.parse_args()
if args.input == 'None':
    print"Error : Enter input file"
    sys.exit(1)
if not os.path.isfile(args.input):
     print "Error : Input entered is not a file"
     sys.exit(1)
if os.path.exists(args.output):
  print "Error : output file exists in this directory"
  sys.exit(1)
#mon chemin pour les corpus
# fileIN=open('/media/zeynal/Sevil Zeynali/INIST/mesdonnees/LSI_LDA/corpus/corpus_mixe_1_article_1_ligne.txt','r').readlines()
fileIN=open(args.input,"r").readlines()
# fileOut=codecs.open('/media/zeynal/Sevil Zeynali/INIST/mesdonnees/LSI_LDA/resultats/res_corpus_mixe_1_article_1_ligne.txt','w','utf-8')
fileOut= open(args.output,"w")

#ouverture de mon stop liste

stopFile=open(os.getcwd()+'/stop_word.txt','r').readlines()
stop=list()
for i in stopFile:
  i=i.strip()
  stop.append(i)

#appeler le lemmatizer
lemm = nltk.WordNetLemmatizer()
#lemmatizer les mots dans le fichierIN
txt=[[lemm.lemmatize(unicode(word, 'utf-8')) for word in d.lower().split() if (word not in stop and len(word)>3) ] for d in fileIN]
#print type(txt)
#calculer la frequence des mots dans le fichierIN
all_tokens=sum(txt,[])
#print type(all_tokens)
#fire un set de tous les tokens dans le fichierIN qui ont une frequence moin 2
tokens_once=set(word for word in set(all_tokens) if all_tokens.count(word)<2)
#si la freq d'un mot est plus qu'un, pour pas avoir des doublons
texts=[[word for word in text if word not in tokens_once] for text in txt]
#print texts

dictionary=corpora.Dictionary(texts)

corpus=[dictionary.doc2bow(text) for text in texts]
#num_topics ici c'est le nombre de groupe qu'on veut sortir
lsi=lsimodel.LsiModel(corpus,id2word=dictionary,num_topics=20)

if len(fileIN)>1:
  tfidf=models.TfidfModel(corpus)
  doctfidf=tfidf[corpus]
  #num_topics ici c'est le nombre de termes qu'on veut sortir pour chaque groupe
  lsit=lsimodel.LsiModel(doctfidf,id2word=dictionary,num_topics=10)
  
dd=dict()
for i in range(0,lsi.num_topics):
  #print type(lda.print_topic(i))
  fileOut.write(lsi.print_topic(i)+'\n')
  dd[i]=lsi.print_topic(i)



  

