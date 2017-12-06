
# sisa : Semantic Indexing of Scientific Articles

Keffa is a program in Python for extract semantic fileds from scientific articles in txt format. It uses Python [LSI](https://radimrehurek.com/gensim/models/lsimodel.html) library.

## Installing and requirements

You need Python >= 2.6 or >= 3.3


## How to use

```
The input file should be a text file with one article per line without \n in each article
In the output file you can see the semantic field for each article and their tfidf
you can change the number of topics that you want in output and also the number of semantic fields per line

usage: sifa.py [-h] -i INPUT -o OUTPUT                                                                                                             
sifa is a program for extract semantic fields from french articles. It uses Python TextBlob library.                                                         
optional arguments:                                                                                                                                                         
  -h, --help                       Show this help message and exit                                                                                                                     
  -i INPUT, --input INPUT          Entry text file to index                                                                                                           
  -o OUTPUT, --output OUTPUT       Output file where extracted keywords will be stored
