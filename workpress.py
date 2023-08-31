import os, json, re, pprint

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
        return response
    except:
        pass
    
def workpress():
    for conf in config:
        wp_project = conf['wp_project']
        wp_version = conf['wp_version']
        wp_themes = conf['wp_themes']
        wp_plugins = conf['wp_plugins']
        
        print (f'[!] Start checking project {wp_project}')
        print (f'     [*] Wordpress Version : {str(wp_version)}')
        print (f'     [*] Count Themes      : {len(wp_themes)}')
        print (f'     [*] Count Plugins     : {len(wp_plugins)}')
        
        try:
            print (f'\n     [%] Checking theme vulnerability issue')
            for theme in wp_themes:
                print (f'     [$] Theme Name : {theme}')
                check = requester(theme)
                if '"pageCount":"0"' in check:
                    print (f'     [*] vulnerability issue for theme {theme} not found.\n')
                else:
                    data = json.loads(check)
                    issues = data['pageProps']['pageData']['props']['data']
                    print (f'     [*] found {len(issues)} vulnerability issue for {theme}.')
                    for issue in issues:
                        print(f'        @> {issue["title"]}')
        except:
            print (f'[!] Fail to check project {wp_project}')
            return False
        
        try:
            print (f'\n     [%] Checking plugins vulnerability issue')
            for plugin in wp_plugins:
                print (f'     [$] Plugin Name : {plugin}')
                check = requester(plugin)
                if '"pageCount":"0"' in check:
                    print (f'     [*] vulnerability issue for plugin {plugin} not found.\n')
                else:
                    data = json.loads(check)
                    issues = data['pageProps']['pageData']['props']['data']
                    print (f'     [*] found {len(issues)} vulnerability issue for {plugin}.')
                    for issue in issues:
                        print(f'        @> {issue["title"]}')
        except:
            print (f'[!] Fail to check project {wp_project}')
            return False
        
    
workpress()