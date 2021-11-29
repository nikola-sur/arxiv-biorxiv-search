import pandas as pd
import datetime
import time
import sys
import string
import gc
import requests
import xml.etree.ElementTree as ET
from urllib.parse import urlencode
from urllib.request import urlopen
from urllib.error import HTTPError

import arxiv_search_function as asf
import biomedrxiv_search_function as bmsf
import datetime

# Notes: 
# - You can include 'cs' in the subjects, but this will increase the number of results.
# - Keywords are searched in the title *and abstract*

records_df = asf.arxivsearch(
	start_date = datetime.date.today() - datetime.timedelta(days=7),
 	end_date = datetime.date.today(), 
	subjects = ['stat', 'math', 'cs'], 
	kwd_req = [], 
	kwd_exc = ['autoencoder'], 
	kwd_one = [['Monte Carlo', 'Markov chain', 'variational inference', 'ergodic', 
	'Gibbs', 'Metropolis', 'Hamiltonian Monte Carlo', 'HMC', 'MCMC', 'SMC', 'PDMP', 'PDMC']], 
	cols = ['id', 'url', 'title', 'categories', 'abstract', 'authors', 'date'],
	export='search_results/',
	max_records=1000)
print(records_df.title)
print(records_df)
