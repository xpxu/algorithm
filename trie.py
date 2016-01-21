#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
通过trie树构建正则表达式
'''

class Trie(object):

    def __init__(self):
        self.trie={}

    def add(self,word):
        tree=self.trie
        for c in word:
            if c not in tree:
                tree[c]={}
            tree=tree[c]
        tree['']=None
        print self.trie

    @staticmethod
    def _preg(tree):
        sp,vt,vn='',[],[]
        for x in tree:
            if tree[x]:
                s=Trie._preg(tree[x])
                if s:
                    vn.append(x+s)
                else:
                    vt.append(x)
            else:
                sp='?'
        vt=''.join(vt)
        if len(vt)>1:
            vt='['+vt+']'
        if vn:
            if vt:
                vn.append(vt)
            if len(vn)>1:
                vn='(?:'+'|'.join(vn)+')'
            else:
                vn=vn[0]
                if sp and len(vn)>1:
                    vn='(?:'+vn+')'
            return vn+sp
        elif vt:
            return vt+sp
        return ''

    def regex(self):
        return Trie._preg(self.trie)

if __name__=='__main__':
    tr=Trie()
    for w in ['foobar','foobah','fooxar','foozap','fooza']:
        tr.add(w)
    print tr.regex()