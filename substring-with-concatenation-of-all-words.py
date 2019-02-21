# coding=utf-8 
# @Time :2019/2/21 14:35

class Solution:
    def split(self,string,width):
        result=[]
        i=0 
        length=len(string)
        while i<=length-width:
            result.append(string[i:i+width])
            i=i+width
        return result
        
    def findSubstring(self, s: 'str', words: 'List[str]') -> 'List[int]':
        result = []
        words_count = len(words)
        if words_count>0:
            length_word = len(words[0])
        else:
            length_word = 0
        i=0 
        length_s = len(s)
        if length_s==0 or words_count==0:
            return []
        while i <= length_s-length_word*words_count:#利用while循环，实现对s遍历            
            string_list = self.split(s[i:i+length_word*words_count],length_word)#将s从i开始切分出一个长度和words中所有单词加在一起长度相同的一个子串，并将这个子串切开，放在string_list中            
            string_list.sort()#由于words中的单词并不是排好序的，所以这里需要调用两个sort函数，将这两个列表排序，这样才能够判断他们是否相等。            
            words.sort()            
            if  string_list == words:#如果不是排好序的列表，即使里面的元素都相等，但是顺序不等的话，也是不会相等的。             
                result.append(i)            
            i = i + 1        
        return result
