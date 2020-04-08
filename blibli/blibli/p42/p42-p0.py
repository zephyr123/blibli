#coding:utf8
class FileObject:

    def __del__(self,file):
        file.close()

