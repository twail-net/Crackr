from nltk.tag.stanford import StanfordPOSTagger
import textprocess as tp
import os, time

#Wraps the part of speech taggin functionality within this file

try:
    pwd = os.path.dirname(os.path.realpath(__file__))
    print pwd
except:
    print 'Something screwed up, using os.getcwd() instead'
    pwd = os.getcwd()
    
print "POSTagger Loaded"
post = StanfordPOSTagger(pwd+'/stanford-postagger/models/english-bidirectional-distsim.tagger',
                         pwd+"/stanford-postagger/stanford-postagger.jar", java_options="-mx3000m")

def tag(text):
    text = tp.preprocess(text)
    #print text
    t1 = time.time()
    outlist = post.tag(text.split())
    t2 = time.time()
    print "POS Tagging complete. Time taken: ", t2-t1, " seconds"
    return outlist
