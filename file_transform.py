#把pdf转成excel
# 导入所需库
import pdfplumber
import pandas as pd

# 打开PDF文件
pdf = pdfplumber.open("/data/lilumin/cs_fudamental/scf_hw1.pdf") 

# 用于存储所有页面的表格数据
all_tables = []

# 遍历所有页面
for page in pdf.pages:
    table = page.extract_table()
    if table:  # 确保页面有表格
        all_tables.extend(table)  # 合并表格

# 关闭PDF文件
pdf.close()

# 使用 pandas 将数据保存为 Excel
# 将列表转换为 DataFrame
df = pd.DataFrame(all_tables)
df_cleaned = df[df.iloc[:, 0] != '大类名称']
new_header = ['大类名称', '奖项', '作品编号', '作品名称', '学校名称', '作者', '指导教师']
df_cleaned.columns = new_header
# 将结果保存到新 Excel 文件
df_cleaned.to_excel("output.xlsx", index=False)

