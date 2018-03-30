import requests
import json
#
# headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#            'accept-encoding': 'json',  # 'gzip, deflate, sdch, br',
#            'upgrade-insecure-requests': '1',
#            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
#            'cookie': '_zap=18524c38-93cc-41ea-a14f-ccc3f622943d; d_c0="AFACkr27QAyPTrAZZ7Vnc_V1qlbFCZK4lEI=|1503282612"; q_c1=3b36829c8f5745c8889443e4e0cfd4ee|1508223078000|1499068468000; capsion_ticket="2|1:0|10:1519352665|14:capsion_ticket|44:MDZiNTg4YzA4YjY1NDVlZDgyYjljZjExOWZjMGMwZTg=|3ced540fc9544a8b96585f1c25aea8e1b78eb4d10dee538be5efebcea2c81613"; r_cap_id="YTE4OGNkZTc5ZjQ4NDZjNWE4YTczMDlkZDRkMjFjMzc=|1519352694|bbd7ddffe62033fc9a1bca9dd1a23ef66751d801"; cap_id="OTYzYzA3NjcyMjBiNDMwMzk0YzNkOGI5YzAzNzcwYjk=|1519352694|38d15bc3378148e0f893a12f929cbe93e9d6b2fc"; l_cap_id="NTIwNmMxOTM0MzNkNDFlYmEwZTZjZTU3OTY1MjNlOWM=|1519352694|8c8798319cba40636e1af98ed1975899f5fd7fff"; z_c0=Mi4xc2dhNUFBQUFBQUFBVUFLU3ZidEFEQmNBQUFCaEFsVk5lOGw4V3dEQWt3YnFCZjJrNEJoUWozS0YtUXU2VWVxYlNR|1519352699|78616cfc83d504de2c3ddb80d675f5be0189b71b; q_c1=3b36829c8f5745c8889443e4e0cfd4ee|1519719287000|1499068468000; __DAYU_PP=Ve36JRFIjjQ6RumMefIn65a59b63c4c2; __utma=51854390.1752076622.1503282613.1521091857.1521107920.19; __utmz=51854390.1521107920.19.15.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/19583984; __utmv=51854390.100-1|2=registration_date=20141230=1^3=entry_date=20141230=1; _xsrf=675a1568-8869-4f62-9105-2db539d6a9bb',
#            'accept-language': 'en-US,en;q=0.8',
#            # 'referer':'https://www.zhihu.com/people/dynames00/followers'
#            }
# re = requests.get(
#     'https://www.zhihu.com/api/v4/members/defaultcao-chaos/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=20&limit=20',
#     headers=headers)
#
# # print re.text
# data = json.loads(re.text)['data']
# #for idata in data:
#     #print idata
