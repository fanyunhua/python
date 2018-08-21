#coding=utf-8
import re
import requests
url = 'https://www.gushiwen.org/shiwen/'
def get_all_url(url):
    html_text = requests.get(url)
    html_text = html_text.text
    url_text = re.findall('<a href="https://so.gushiwen.org/gushi/(.*?).aspx">(.*?)</a>',html_text)
    #print(url_text)
    #print(html_text)
    return url_text

title_list = [] #获取各个分类链接
name = [] #获取各个分类名称
def get_title(url_list):
    url = []
    u = 'https://so.gushiwen.org/gushi/'
    l = '.aspx'

    for line in url_list:
        #title.append(line[0])
        title_list.append(u+line[0]+l)
        name.append(line[1])
    return url
    #print(url)
    #print(title)
    #print(line[1])
def get_all_url_title():
    temp = []
    u = 'https://so.gushiwen.org/shiwenv_'
    l = '.aspx'
    i = 0

    for line in title_list:
        sb = []
        html_text = requests.get(line)
        html_text = html_text.text
        re_text = re.findall('<span><a href="/shiwenv_(.*?).aspx" target="_blank">',html_text)
        for ll in re_text:
            sb.append(u+ll+l)
        #print(type(re_text))
        temp.insert(i,sb)
        #print(temp)
        i+=1
    return temp
def getall_name_list(li):
    temp = []
    pat = []
    count = 0
    for lp in name:
        pat.append(lp)
        print(pat)
    i = 0
    for line in li:

        path = './' + pat[i] + '.txt'
        f = open(path, 'w+')
        print(path)
        for ie in line:
            count+=1
            name_title = []
            author = []
            content = []
            #print(ie)
            if(ie=='https://so.gushiwen.org/shiwenv_9464a0f0b635.aspx'):
                continue
            if(ie=='https://so.gushiwen.org/shiwenv_d512fc308251.aspx'):
                continue
            html_text = requests.get(ie)
            html_text = html_text.text
            name_title = re.findall('<h1 style=".*?">(.*?)</h1>', html_text)
            author = re.findall('<a href="/authorv.*?.aspx">(.*?)</a>', html_text)
            # content = re.findall('<div .*? class="contson">(.*?)</div>',html_text)
            content = re.findall('<meta name="description" content="(.*?)" />', html_text)
            try:
                f.writelines(''.join(name_title)+'\t'+''.join(author)+'\t'+''.join(content[0]+'\n'))
            except Exception :
                print('一个错误')
            #print(''.join(name_title))
            #print(''.join(content))
            print(count)
            print(ie)
        i+=1
        print(i)
        f.close()
            #name.append(name1)
            #author.append(author1)
            #content.append(content1)

            #print(re_text)
def get_name_url(url):
    url_list_data = []
    u = 'https://so.gushiwen.org/shiwenv_'
    l = '.aspx'
    text = []
    for line in url:
        print(line)
        html_text = requests.get(line)
        html_text = html_text.text
        #print(html_text)
        text.append(re.findall('<span><a href="/shiwenv_(.*?).aspx" target="_blank">.*?</a>',html_text))
    #print(text)
    for line in text:
        for ll in line:
            url_list_data.append(u+ll+l)
        #print(line)
    return url_list_data
    #print(url_list_data)
def get_con(u):
    name = []
    author = []
    content = []
    for line in u:
        html_text = requests.get(line)
        html_text = html_text.text
        name1 = re.findall('<h1 style=".*?">(.*?)</h1>', html_text)
        author1 = re.findall('<a href="/authorv.*?.aspx">(.*?)</a>', html_text)
        # content = re.findall('<div .*? class="contson">(.*?)</div>',html_text)
        content1 = re.findall('<meta name="description" content="(.*?)" />', html_text)
        name.append(name1)
        author.append(author1)
        content.append(content1)
    f = open('./shiwen.txt','w+')
    i = 0
    try:
        for lin in name:
            f.writelines(name[i])
            f.writelines("  ")
            f.writelines(author[i])
            f.writelines("  ")
            f.writelines(content[i])
            f.writelines("\n")
            i += 1
    except Exception:
        print("写入失败")
    f.close()
if __name__ == '__main__':
    allurl = []
    url_list = []
    all_url = []
    allurl = get_all_url(url)
    url_list = get_title(allurl)
    #print(title_list)
    #print(name)
    _all_url_title = get_all_url_title()
    getall_name_list(_all_url_title)
    #all_url = get_name_url(url_list)
    #get_con(all_url)

