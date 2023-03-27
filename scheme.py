import math
def get_tf_binary(word,index,pos_index_dict,len_docs,individual_tokens):
        return 1
def get_tf_raw_count(word,index,pos_index_dict,len_docs,individual_tokens):
        return len(pos_index_dict[word][2][index])
    
def get_tf_term_frequency(word,index,pos_index_dict,len_docs,individual_tokens):
        num = len(pos_index_dict[word][2][index])*1.0
        den = len_docs[index-1]
        return num/den
    
def get_tf_logNorm(word,index,pos_index_dict,len_docs,individual_tokens):
        return math.log((1+len(pos_index_dict[word][2][index])))
    
def get_tf_logDoubleNorm(word,index,pos_index_dict,len_docs,individual_tokens):
        tokens = individual_tokens[index-1]
        dictionary = {}
        for token in tokens:
            if token not in dictionary:
                dictionary[token] = 1
            else:
                dictionary[token] += 1

        marklist = sorted(dictionary.items(), key=lambda x:x[1])
        sortdict = dict(marklist)
        sortdict = dict(reversed(list(sortdict.items())))
        words = list(sortdict.keys())
        max_tf = sortdict[words[0]]

        return 0.5+0.5*((len(pos_index_dict[word][2][index])*1.0)/max_tf)
        