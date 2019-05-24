# _*_ coding:utf-8 _*_
__author__ = "Ink.white"

import re
import urllib.request


'''
https://video.coral.qq.com/varticle/3753518160/comment/v2?callback=_varticle3753518160commentv2&orinum=10&oriorder=o&pageflag=1&cursor=6507261712650141754&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=1555322886422
https://video.coral.qq.com/varticle/3753518160/comment/v2?callback=_varticle3753518160commentv2&orinum=10&oriorder=o&pageflag=1&cursor=6507463116999636007&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=1555322886423
https://video.coral.qq.com/varticle/3753518160/comment/v2?callback=_varticle3753518160commentv2&orinum=10&oriorder=o&pageflag=1&cursor=6507549963949946654&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=1555322886424
https://video.coral.qq.com/varticle/3753518160/comment/v2?callback=_varticle3753518160commentv2&orinum=10&oriorder=o&pageflag=1&cursor=6507887290740096334&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=1555322886425
https://video.coral.qq.com/varticle/3740715815/comment/v2?callback=_varticle3740715815commentv2&orinum=10&oriorder=o&pageflag=1&cursor=6506525073530698409&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=1555324767851
https://video.coral.qq.com/varticle/3740715815/comment/v2?callback=_varticle3740715815commentv2&orinum=10&oriorder=o&pageflag=1&cursor=6506537459810241802&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=1555324767852
https://video.coral.qq.com/varticle/3740715815/comment/v2?callback=_varticle3740715815commentv2&orinum=10&oriorder=o&pageflag=1&cursor=6506511941513000437&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=1555324767853
'''

url = input("请输入需要爬取的js_addr:")
data = urllib.request.urlopen(url).read().decode('utf-8','ignore')
# "content":"\u7236\u6bcd\u6c38\u8fdc\u4e0d\u4f1a\u77e5\u9053\u81ea\u5df1\u504f\u5fc3\uff0c\u800c\u4e14\u6c38\u8fdc\u4e0d\u4f1a\u627f\u8ba4",
re_content = re.compile('"content":"(.*?)"').findall(data)
for i in range(0,len(re_content)):
    thisdata = re_content[i]
    print(thisdata)
    print(type(thisdata))
    print(u"{abc}".format(abc=thisdata))
    break
print('当前的数据长度条数为:',len(re_content))
