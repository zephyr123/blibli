#coding:utf8
class FileOject:
    '''给文件对象进行包装从而确认在删除时文件流关闭'''
    def __init__(self,filename='sample.txt'):
        #读写模式打开一个文件
        self.new_file = open(filename,'r+')

    def __del__(self):
        self.new_file.close()
        del self.new_file

a = FileOject
