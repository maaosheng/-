
class Page:
    def __init__(self, current_page, per_page, count, show_page):
        try:
            self.current_page = int(current_page)
        except:
            self.current_page = 1
        self.per_page = per_page
        self.count = count
        self.show_page = show_page

    def start(self):
        begin = (self.current_page - 1) * self.per_page
        return begin

    def last(self):
        end = self.current_page * self.per_page
        return end

    def paging(self):
        a, b = divmod(self.count, self.per_page)
        temp_list = []
        if b:
            a += 1
        half = int((self.show_page - 1) // 2)
        if a < self.show_page:
            begin1 = 1
            end1 = a+1
        else:
            if (self.current_page + half) <= self.show_page:
                begin1 = 1
                end1 = self.show_page + 1
            else:
                if (self.current_page + half) >= a:
                    end1 = a + 1
                    begin1 = a - self.show_page + 1
                else:
                    begin1 = self.current_page - half
                    end1 = self.current_page + half + 1

        if self.current_page - 1:
            v = '<li><a  style="display: inline-block;padding: 5px;margin: 5px;color:red" ' \
                'href="/student/asf.html?page=%s">上一页</a></li>' % (self.current_page - 1)
        else:
            v = '<li><a  style="display: inline-block;padding: 5px;margin: 5px;color:red" ' \
                'href="#">上一页</a></li>'
        temp_list.append(v)
        for i in range(begin1, end1):
            if i == self.current_page:
                temp = '<li><a  style="display: inline-block;padding: 5px;margin: 5px;color:red" ' \
                       'href="/student/asf.html?page=%s">%s</a></li>' % (i, i)
            else:
                temp = '<li><a  style="display: inline-block;padding: 5px;margin: 5px" ' \
                       'href="/student/asf.html?page=%s">%s</a></li>' % (i, i)
            temp_list.append(temp)
        if self.current_page < a:
            t = '<li><a  style="display: inline-block;padding: 5px;margin: 5px;color:red" ' \
                'href="/student/asf.html?page=%s">下一页</a></li>' % (self.current_page + 1)
        else:
            t = '<li><a  style="display: inline-block;padding: 5px;margin: 5px;color:red" ' \
                'href="#">下一页</a></li>'
        temp_list.append(t)
        ret = ''.join(temp_list)
        return ret