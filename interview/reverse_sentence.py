'''
input: the sky is blue
output: blue is sky the

'''

def reverse_sentence(s):
    work_list = s.split(' ')
    work_list.reverse()
    print (' ').join(work_list)

if __name__ == "__main__":
    sentence = "the sky is blue"
    reverse_sentence(sentence)



