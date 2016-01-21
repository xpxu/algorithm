#encoding=utf-8
'''
两个数组交换元素，使其和最小。
'''


def switch_list(a,b):

'''
1. a和b数组的大小是无关紧要的。
2. 每一次循环之前，需要保证a和b有序，这样才能保证每次交换是最佳的交换方式
'''
    a.sort()
    b.sort()
    d=abs(sum(a)-sum(b))
    for ii in a:
        for jj in b:
            d_tmp = abs(sum(a)-sum(b)+2*jj-2*ii)
            if (d_tmp<d):
                a.remove(ii)
                a.append(jj)
                b.remove(jj)
                b.append(ii)
                print '数组a中的%d与数组b中的%d交换，'%(ii,jj)
                return switch_list(a,b)
    # 最后一次迭代才会处理下面的两行语句，上层的迭代在前面的return语句就结束了。
    print '交换结束。最后的差值的绝对值为%d'%abs(sum(a)-sum(b))
    return a,b

a=[120, 3, 90, 92, 93]
b=[110, 5, 4, 2, 89, 91]
print switch_list(a, b)