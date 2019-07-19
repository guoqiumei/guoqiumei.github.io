from urllib import request
import xlsxwriter
import pymysql
import re
def kk():
    url='https://appapi.51job.com/api/job/search_job_list.php?postchannel=0000&&keyword=Python%E7%88%AC%E8%99%AB&keywordtype=2&jobarea=030200&searchid=&famoustype=&iswangshen=&pageno=1&pagesize=30&accountid=148506637&key=555a34eb9514e840c6e94439ea810b245d23738a&productname=51job&partner=bf8546f4d567e938ecc9bf7df7890625&uuid=6b5802f1cc42c08ada8cbb6e23085d74&version=863&guid=dfd84c15bc0628a750a17fbd243886fd'
    head={
    'User-Agent':"51job-android-client"

    }
    c=request.Request(url,headers=head)
    a=request.urlopen(c).read().decode()
    print(a)
    pat=re.compile(r"</jobid><jobname><!\[CDATA\[(.*?)\]\]>")
    pat1=re.compile(r"</coid><cddr><!\[CDATA\[(.*?)\]\]>")
    b=pat.findall(a)
    c=pat1.findall(a)
    return c