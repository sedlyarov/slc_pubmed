from Bio import Entrez

Entrez.email = "mcfrank@stanford.edu"

def get_abstract(pmid):
    handle = Entrez.efetch(db='pubmed', id=pmid, retmode='text', rettype='abstract')
    return handle.read()

def get_record(pmid):
    handle = Entrez.efetch(db='pubmed', id=pmid, retmode='xml')
#    return handle.read()
    return Entrez.read(handle)


def get_links_id(pmid):
	link_list = []
	links = Entrez.elink(dbfrom="pubmed", id=pmid, linkname="pubmed_pubmed")	
	record = Entrez.read(links)
	
	records = record[0][u'LinkSetDb'][0][u'Link']

	for link in records:
		link_list.append(link[u'Id'])

	return link_list

def get_links_term(term):
	links = Entrez.esearch(db="pubmed", retmax = 1, term=term)	
	record = Entrez.read(links)
	link_list = record[u'IdList']

	return link_list


### MAIN -----------------------


for i in get_links_term("SLC1A1[Title/Abstract]"):
	print get_record(i)[].keys()
