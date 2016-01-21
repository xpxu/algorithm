#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
input:
db/sql/init2.sql;
db/sql/SQLAlchemytest.py;
db/nosql/dump.rdb;
db/nosql/redis/pipeline.py;
db/nosql/redis/basic.py;
db/nosql/redis/socialcircle.py;
re/retest.py;
celerytest/tasks.pyc;
celerytest/test.py;
celerytest/tasks.py;
sorted/sorted_dict.py;
list/classA.py;
webapp/schema.sql;
webapp/fabfile.py;
webapp/conf/supervisor/awesome.conf;
webapp/conf/nginx/awesome;
webapp/conf/README;
webapp/www/urls.py;

output:
(db(nosql(redis(basic.py;,pipeline.py;,socialcircle.py;),
dump.rdb;),sql(SQLAlchemytest.py;,init2.sql;)),
list(classA.py;),celerytest(test.py;,tasks.pyc;,tasks.py;),
re(retest.py;),sorted(sorted_dict.py;),webapp(fabfile.py;,
schema.sql;,www(urls.py;),conf(nginx(awesome;),supervisor(awesome.conf;),README;)))
'''


'''
先构建trie树/字典树, 然后再遍历trie树.
'''

def lists2dictTree(input):
    result = {}
    # 逐行扫描
    for ii in input:
        # 每一行分来成list
        ii_input = ii.split('/')
        # 将每一行都插入到trie树/字典树中
        tmp = result
        for j  in range(len(ii_input)):
            if ii_input[j] not in tmp:
                tmp[ii_input[j]] = {}
            tmp = tmp[ii_input[j]]
    return result


# print 方式
def dictTree2str(input):
    if input == {}:
        return
    i = 0
    for k in input.iterkeys():
        i = i + 1
        print '(',
        print k,
        dictTree2str(input[k])
        if i < len(input):
            print '),',
        else:
            print ')',

# result传递方式
def dictTree2str(input, result):
    if input == {}:
        return
    i = 0
    for k in input.iterkeys():
        i = i + 1
        if i == 1:
            result.append('(')
        result.append(k)
        dictTree2str(input[k], result)
        if i < len(input):
            result.append(',')
        if i == len(input):
            result.append(')')



input = [
    'db/sql/init2.sql;',
    'db/sql/SQLAlchemytest.py;',
    'db/nosql/dump.rdb;',
    'db/nosql/redis/pipeline.py;',
    'db/nosql/redis/basic.py;',
    'db/nosql/redis/socialcircle.py;',
    're/retest.py;',
    'celerytest/tasks.pyc;',
    'celerytest/test.py;',
    'celerytest/tasks.py;',
    'sorted/sorted_dict.py;',
    'list/classA.py;',
    'webapp/schema.sql;',
    'webapp/fabfile.py;',
    'webapp/conf/supervisor/awesome.conf;',
    'webapp/conf/nginx/awesome;',
    'webapp/conf/README;',
    'webapp/www/urls.py;'
    ]

dictTree = lists2dictTree(input)
print dictTree
result = []
dictTree2str(dictTree, result)
print ''.join(result)






