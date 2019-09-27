class Page:
    def __init__(self,curent_page,per_page,show_page,count):
        try:
            self.curent_page = int(curent_page)
        except:
            self.curent_page = 1
        self.per_page = per_page
        self.show_page = show_page
        self.count = count

    def get_start(self):
        ret = self.curent_page-1
        return ret*self.per_page
    def get_end(self):
        ret = self.curent_page
        return ret*self.per_page

    def Pag(self):
        half = (self.show_page-1)//2
        a,b = divmod(self.count,self.show_page)
        if b:
            a = a + 1
        if a < self.show_page:
            start = 1
            end = a + 1
        else:
            if (self.curent_page+half) <= self.show_page:
                start = 1
                end = self.show_page
            else:
                if (self.curent_page+half)>=a:
                    start = a-self.show_page+1
                    end = a
                else:
                    start = self.curent_page-half
                    end = self.curent_page+half+1
        temp = []
        if self.curent_page-1 and self.curent_page<a:
            ret = "<li><a style='display:inline-block;padding:5px 0'  href='/student/asf.html?page=%s'>上一页</a></li>" %(self.curent_page-1)
        else:
            ret = "<li><a style='display:inline-block;padding:5px 0'  href='#'>上一页</a></li>"

        #---------------------添加返回页面--------------------------

        for info in range(start,end):
            if self.curent_page==info:
                v = "<li><a style='color:red;display:inline-block;padding:5px 0'  href='/student/asf.html?page=%s'>%s</a></li>"%(info,info)
            else:
                v = "<li><a style='display:inline-block;padding:5px 0'  href='/student/asf.html?page=%s'>%s</a><li/>"%(info,info)
            temp.append(v)



        if self.curent_page<a and self.curent_page-1:
            k = "<li><a style='display:inline-block;padding:5px 0'  href='/student/asf.html?page=%s'>下一页</a></li>" % (
                        self.curent_page + 1)
        else:
            k = "<li><a style='display:inline-block;padding:5px 0'  href='#'>下一页</a></li>"

        temp.append(k)

        res = ''.join(temp)
        return res