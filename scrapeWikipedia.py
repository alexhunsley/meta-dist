# scrapeWikipedia.py
#

import wikipediaapi

def print_categorymembers(categorymembers, level=0, max_level=2):
	print("got catmembers: ", categorymembers)
	for c in categorymembers.values():
	    print("%s: %s (ns: %d)" % ("*" * (level + 1), c.title, c.ns))
	    if c.ns == wikipediaapi.Namespace.CATEGORY and level <= max_level:
	        print_categorymembers(c.categorymembers, level + 1)


wiki_wiki = wikipediaapi.Wikipedia('en')

distsPage = wiki_wiki.page("Category:Continuous Distributions")
print("Category members: %s" % distsPage.title)
print()

print_categorymembers(distsPage.categorymembers)
