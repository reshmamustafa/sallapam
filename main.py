
# -*- coding: utf_8 -*-
from flask import Flask, render_template, request, jsonify
import os
from whoosh.index import create_in
from whoosh.fields import *
import re
from nltk import word_tokenize
from compiler.ast import flatten
from whoosh.qparser import QueryParser # Query parser called
app = Flask(__name__)
schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)# Schema declaration
ix = create_in("index", schema) # Schema definition

@app.route("/")
def hello():
    return render_template('chat1.html')
    
@app.route("/about/")
def abt():
    return render_template('about.html')

@app.route("/ask", methods=['POST'])
def ask():
	message = request.form['messageText'].encode('utf-8').strip()
	pre_index()
	q1 = message.decode('utf-8') # Decode query to use with whoosh query parser
	otp = query_search(q1)
	print otp
	return jsonify({'status':'OK','answer':otp})
def pre_index():
	writer = ix.writer() # Declared writer
	i = 1
	#Stopword list
	st_li=" കാണാന്‍ ‍| നിന്ന് | കുറഞ്ഞ | മുഴുവന് ‍| മുഴുവൻ | കൂടാതെ | ആദ്യം | ഈ | കൂടുതല്‍ | താങ്കള്‍ | എന്നാല് ‍| എന്നാൽ | അതിനു | ശേഷം | ചെയ്യുന്നു | ഇവിടത്തെ | വേണ്ടി | ഏറ്റവും | ഇതില് ‍| ഇതിൽ | വേണ്ടിയും | ആണ് | സ്ഥിതിചെയ്യുന്നു | സ്ഥിതി | സ്ഥിതിചെയ്യുന്ന | ചെയ്യണം | നമ്മുടെ | ഇപ്പോള് ‍| ഇപ്പോൾ | ഒരു | തന്റെ | ചെയ്യുന്ന | എന്ന | ചെയ്യുന്നത് | ഉണ്ട് | മുന്‍പ് | മുമ്പ് | കൂടെ | ചേര്‍ത്തു | ഇപ്രകാരം | എന്നിവയുടെ | കഴിയും | എന്നീ | ഇതാണ് | വളരെ | കാരണം | ഇവിടത്തെ | എപ്പോഴും | കൊണ്ട് | നല്ല | ധാരാളം | എപ്പോഴും | ഇവ | കാരണം | ഇതു | മാത്രമല്ല | മറ്റു | എന്നിവ | കൂടിയാണ് | ഇടയില് ‍| ഇല്ല | എന്നാണ് | എന്നു | കുറച്ച് | അതായത് | എന്തെന്നാല് ‍| എന്തെന്നാൽ | എന്നറിയപ്പെടുന്നു | കിടക്കുന്ന | പോയാല് ‍| പോയാൽ | ഇത് | എല്ലാ | വേണ്ടി | ഇവിടെ | വരുന്നു | പോലുള്ള | വലിയ | പറഞ്ഞ് | ഇതിനെ | കൊടുത്തിട്ടും | എന്ന് | വേണം | ഒരുപോലെ | ഒരു പോലെ | കാര്യമാണ് | കഴിയുന്നു | വളരെ | അധികം | വളരെ അധികം | വളരെയധികം | പോയി | ഉണ്ടാകുന്നുണ്ട് | പക്ഷേ | അതേ | കൊണ്ട് | ഏത് | നിന്നും | എത്താന്‍ | അടുത്ത് | ആയി | എന്നു പറയുന്നു | ഇപ്പോൾ | ഏകദേശം | എന്നുപറയുന്നു | കാണാൻ | ആ | വിവിധ | ഇതിന്റെ | നിന്നു | ഇതിന് | അടുത്ത | അടുത്തുള്ള | പല | പ്രധാന | നിലനിൽക്കുന്ന | നിലനിൽക്കുന്നത് | മുതലായവ | മുതലായവക്ക് | വേണ്ട | പ്രാധാന്യം "
	for line in open('corpus/data'):
	    l1 = line.decode('utf-8') # Decoded line from file to utf-8 format
	    clear = re.sub(st_li, '', line) # Clearing stopwords
	    v1= clear.decode('utf-8')  # Decoded preprocessed text into utf-8 format
	    writer.add_document(title=l1, content=l1) # Title and text is written
	writer.commit() # Writer commit
def jacc_index(a,b):
	c_i = list(set(a).intersection(set(b)))
	c_u = list(set(a).union(set(b)))
	j1 = float(len(c_i)) / float(len(c_u))
	return j1
# Searching
def query_search(qu):
	max=0     
	f1 = open("ndex/in.txt", "w+") # File created for writing search output                  
	mx_sent="നിങ്ങൾ പറയുന്നത് മനസ്സിലായില്ല"
	from whoosh.qparser import QueryParser # Query parser called
	with ix.searcher() as searcher:
	    query = QueryParser("content", ix.schema).parse(qu) # Parsing query
	    results = searcher.search(query) # Parsed output

	    for i in results:
	        for k, v in i.iteritems():
	            a=flatten(word_tokenize(qu))
	            b=word_tokenize(v)
	            j_v=jacc_index(a,b) # Calculating Jaccard index value
	            if (j_v > max):
	                max = j_v
	                mx_sent = v
	                f1.write(qu.encode("utf-8") + "\t")  # Writing query
	                f1.write(v.encode("utf-8"))  # Writing search result in file in.txt
	f1.close()
	print max # Printing the maximum Jaccard index value 
	print mx_sent # Printing the sentence which has maximum matching
	return mx_sent # Returning the output to the function call
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
