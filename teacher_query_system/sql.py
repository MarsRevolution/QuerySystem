import csv
import sqlite3

# 连接到SQLite数据库
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# 创建表（如果表已存在，此步骤可以省略）
cursor.execute('''
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY,
    department TEXT,
    name TEXT,
    title TEXT,
    photo TEXT
)
''')

# 读取CSV文件并插入到数据库
with open('infos.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute('''
        INSERT INTO teachers (department, name, title, photo) VALUES (?, ?, ?, ?)
        ''', (row['Department'], row['Name'], row['Title'], row['Photo']))

# 提交事务
conn.commit()

# 关闭数据库连接
conn.close()

