import pdfplumber
import os
import pandas as pd
def get_all_pdf_page(file_path,file_name):
    pdf = pdfplumber.open(file_path)
    df_total = pd.DataFrame(columns = range(8))
    p = pdf.pages
    for item in p:
        if item.find_tables():
            table = item.extract_table() #get the table
            df = pd.DataFrame(table)
            result = df_total.append(df)
            temp = result
            df_total = temp
    file_path = 'CN_NEV_Data/' + file_name + ".csv"
    result.to_csv(file_path,encoding='utf_8_sig')

if __name__ == "__main__":
    path = "E:\OneDrive\SW Update\Python_Script\CN_NEV_Data" #文件夹目录
    files= os.listdir(path) #得到文件夹下的所有文件名称
    for file in files:
        suffix = file.split(".")[1]
        file_name = file.split(".")[0]
        if suffix == 'pdf':
            file_path = path + "\\" + file
            #file_path = "CN_NEV_Data/1.pdf"
            get_all_pdf_page(file_path,file_name)



# def get_table_from_pdf(table):
#     table[0] = [x.replace("\n","") for x in table[0]] # remove the \n in the colums
#     columns=table[0]
#     df = pd.dataframe(table[1:], columns) # generage a dataframe
#     oems = list(df.loc[:,table[0][1]])# get the oem namea
#     # full fill the none to the oem names
#     i = 0
#     for name in oems:
#         if name == none:
#             oems[i] = oems[i-1]
#         i +=1
#     df.loc[:,'汽车生产企业名称']=oems # rename the ome list
#     return columns,df
#     print (df)





