import re
domainlist=['m.google.com',
'm.docs.google.com',
'www.someisotericdomain.innersite.mall.co.uk',
'www.ouruniversity.department.mit.ac.us',
'www.somestrangeurl.shops.relevantdomain.net',
'www.example.info','https://macxima.medium.com/python-extracting-domain-name-from-urls-using-regular-expressions-7fa2fc13088e']

for l in domainlist:
    res=re.findall(r'(?<=\.)([^.]+)(?:\.(?:co\.uk|ac\.us|[^.]+(?:$|\n)))',l)
    print(l,"|", res[0])
