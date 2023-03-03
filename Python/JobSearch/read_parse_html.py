def get_urls_srch_kwd_in_text(url='', srcTag='a', srchLst=[], topX=0, cntntFrmt='lxml'):
    """
    Fn: Returns a list hyperlinks where text in anchor tag meets the given search criteria. 
    url: http[s] url to be requested, requires password-less connection 
    srcTag: optional, default is 'a' for anchor tag; pass the html tag to be searched 
    topX: optional, default=null; used for returning top X urls eg. top 3 urls from the search 
    cntntFrmt is optional; is BeautifulSoup requests content format
    """
    #libraries
    import requests
    from bs4 import BeautifulSoup as BS

    #declaration
    ret_kwd_href_list = []
    defaultUrl = 'https://www.google.com/search?q='
    url = (defaultUrl if url =='' else url)+('+'.join([itm for itm in srchLst]))    
    print(url)
    url_request = requests.get(url)
    url_content = BS(url_request.content, cntntFrmt)
    anchor_tags = url_content.find_all(srcTag)

    for anchor_tag in anchor_tags:
        anchor_tag_text=anchor_tag.text.lower().strip()
        anchor_tag_href=anchor_tag.get("href")
        anchor_tag_href_lst = [anchor_tag_href for eachitem in srchLst if (anchor_tag_text.find(eachitem) != -1)] 
        #->Code to be modified to making anchor_tag_href_lst list unique 
        #and appending relative path results (./xxxxx/xxxx) to generate URLs instead of ignoreing them
        if len(anchor_tag_href_lst)>0 and "http" in anchor_tag_href_lst[0]:
            ret_kwd_href_list.append(anchor_tag_href_lst[0])
        if topX!=0 and len(ret_kwd_href_list)>=topX: break
    
    return ret_kwd_href_list
    #return ret_kwd_href_list[:topX] if (topX>0 and topX<len(ret_kwd_href_list)) else ret_kwd_href_list[:len(ret_kwd_href_list)]


def find_JobsAtTopAustinCompanies():
    #search_list=['jobs','hiring','career','data','science','scientist']
    search_list=['query','careers','data','scientist']
    url = "https://www.builtinaustin.com/2018/06/28/austin-companies-hiring-july-2018"
    s = get_urls_srch_kwd_in_text(anchor_tags, search_list)
    s=set(s)    
    print(s)    

def get_urls_srch_kwd_in_href(anchor_tags):
    kwd_href_list = []
    #search_list=['jobs','hiring','career','data','science','scientist']
    search_list=['search','jobs']
    for anchor_tag in anchor_tags:
        anchor_tag_href=anchor_tag.get("href")
        print(anchor_tag_href)
        print(type(anchor_tag_href))
        x = [anchor_tag_href for eachitem in search_list if (anchor_tag_href.find(eachitem) != -1)] 
        if len(x)>0 and "https" in x[0]:
            kwd_href_list.append(x[0]) 
    return kwd_href_list 

#"https://github.com/sibujoseph"
#"https://github.com/sibujoseph/Python-Projects/"
#"https://github.com/search?q="

#get_urls_srch_kwd_in_text(srchLst=['scikit-learn','project'])
get_urls_srch_kwd_in_text(srchLst=['india+today','trending','news','india'], topX=5)
