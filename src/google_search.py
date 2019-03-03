"""
pip install google
"""

from googlesearch import search

# to search
query = input("Enter your search query ::")

for j in search(query, num=10, stop=1, pause=2):
	print(j)
