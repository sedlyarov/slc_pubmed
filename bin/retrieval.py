from Bio import Entrez
import pprint
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def search(query):
    Entrez.email = 'sedlyarov@gmail.com'
    handle = Entrez.esearch(db='pubmed', 
                            sort='relevance', 
                            retmax='10000',
                            retmode='xml', 
                            term=query)
    results = Entrez.read(handle)
    return results


def fetch_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = 'your.email@example.com'
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results = Entrez.read(handle)
    return results




f = open('slc1a1_title_abstract.txt',"w")
results = search('SLC1A1[Title/Abstract]')
id_list = results['IdList']
papers = fetch_details(id_list)
for i, paper in enumerate(papers):
#        print("%d) %s" % (i+1, paper['MedlineCitation']['Article']['ArticleTitle']))
#		print paper['MedlineCitation']['Article']['Abstract']['AbstractText'][0]
        f.write(paper['MedlineCitation']['Article']['ArticleTitle'])
        try:
            f.write("\n".join(paper['MedlineCitation']['Article']['Abstract']['AbstractText']))
        except:
            pass

    print "Discovered %d papers" % len(papers) 

    f.close()
    # Pretty print the first paper in full to observe its structure
    #import json
    #print(json.dumps(papers[0], indent=2, separators=(',', ':')))


