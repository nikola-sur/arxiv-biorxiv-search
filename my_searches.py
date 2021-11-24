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

records_df = asf.arxivsearch(
	start_date = datetime.date.today() - datetime.timedelta(days=7),
 	end_date = datetime.date.today(), 
	subjects = ['cs', 'stat', 'math'], 
	kwd_req = [], 
	kwd_exc = [], 
	kwd_one = [['parallel'], ['Bayes'], ['sample'], ['sampler'], ['sampling'], ['Monte'], 
    ['Markov'], ['tempering'], ['tempered'], ['variational'], ['scalable'], ['ergodic'], ['Gibbs'], ['Metropolis'], 
    ['Hamiltonian'], ['MCMC']], 
	cols = ['id', 'url', 'title', 'categories', 'abstract', 'authors', 'date'])
print(records_df.title)


