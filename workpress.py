import os, json, re, pprint

issues = []

try:
    import cloudscraper
    scraper = cloudscraper.create_scraper()
except:
    print ('[!] Module cloudscraper not installed.')
    print ('[!] Tips : $ pip install cloudscraper')
    
try:
    projects = open('workpress.json')
    config = json.load(projects)
except:
    print ('[!] File projects.json not found.')


def regexer(data):
    try:
        re.findall(r'')
    except:pass
    
def requester(query):
    try:
        response = scraper.get('https://wpscan.com/_next/data/yGhSKJB8dSeuEsH5fOGT9/search.json?text='+ query).text
        data = json.loads(response)
        print (data)
        return response
    except:
        pass
    
# def scanall():
#     for conf in config:
#         wp_project = conf['wp_project']
#         wp_version = conf['wp_version']
        
#         print (f'[>] Start checking project {wp_project}')
#         try:
#             print (f'     [*] Wordpress Version : {str(wp_version)}')
#             # checkVersion = requester('Wordpress '+ str(wp_version))
#             checkVersion = requester('Wordpress')
#             if '"pageCount":"0"' in checkVersion:
#                 print (f'     [*] vulnerability issue for Wordpress {str(wp_version)} not found.')
#             else:
#                 print (f'     [*] found vulnerability issue for Wordpress {str(wp_version)}.')
#         except:
#             print (f'[!] Fail to check project {wp_project}')
#             return False
        
    
# scanall()

requester('wordpress')