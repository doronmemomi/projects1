import collections

class Dictionary:
    def __init__(self):
        self.dict={}
        
    def __setitem__(self,key,value):
        self.dict[key]=value
        
        
    def sort_by_key(self):
        sorted_dict = dict(sorted(self.dict.items()))
        new_dict=Dictionary()
        new_dict.dict=sorted_dict
        return new_dict
    
    def sort_by_value(self):
        sorted_dict = sorted(self.dict.items(), key=lambda kv: kv[1])
        #sorted_dict=sorted([self.dict(v,k) for (k,v) in self.dict.items()], reverse=False)
        #sorted_dict=sorted(self.dict.iteritems(), key=lambda (k,v): (v,k)):
        new_dict=Dictionary()
        for key,value in sorted_dict:
            new_dict.dict[key]=value;
            
            

        
        #new_dict.dict=sorted_dict
        return new_dict
    
    
    def print(self):
        print(self.dict)