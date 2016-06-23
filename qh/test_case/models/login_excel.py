#coding=utf-8
import xlrd

class LoginExcel(object):
    #获取一个工作表
    def open_excel(self, file):
        try:
            data = xlrd.open_workbook(file) #打开Excel文件读取数据
            return data
        except Exception as e:
            print(str(e))
    
    #根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
    def  excel_table_byname(self,file, colnameindex, by_name):
        data = self.open_excel(file)
        table = data.sheet_by_name(by_name) #通过名称获取工作表
        nrows = table.nrows #行数
        ncols = table.ncols #列数
        colnames =  table.row_values(colnameindex) #某一行数据 ，userlogin.xlsx标题的内容
        list =[]
        #读取每行的数据，遍历放入list中
        for rownum in range(1,nrows):
            row = table.row_values(rownum)
            if row:
                app = {}
                for i in range(len(colnames)):
                    app[colnames[i]] = row[i]
                list.append(app)
        return list 


if __name__ == '__main__':
    login_excel = LoginExcel()
    list = login_excel.excel_table_byname(file=r'F:\\workspace\\qh\\data\\userlogin.xlsx', 
                                      colnameindex=0, 
                                      by_name='userlogin')
    for i in range(len(list)):
        print('===================username')
        print(list[i]['username'])
        print('===================password')
        print(list[i]['password'])
#     for row in list:
#         print(row)
    