import pandas as pd

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv('sample_data.csv')

# 1. Kiểm tra các thông tin cơ bản về dữ liệu
print(df.info())  # Kiểm tra kiểu dữ liệu và số lượng giá trị không rỗng

# 2. Kiểm tra các giá trị thiếu
print(df.isnull().sum())  # Kiểm tra số lượng giá trị thiếu trong từng cột

# 3. Loại bỏ các dòng có giá trị thiếu (nếu cần)
df_cleaned = df.dropna()  # Loại bỏ dòng có giá trị thiếu
# Hoặc, thay thế giá trị thiếu bằng giá trị trung bình (hoặc giá trị khác)
# df['column_name'] = df['column_name'].fillna(df['column_name'].mean())

# 4. Loại bỏ các giá trị trùng lặp
df_cleaned = df_cleaned.drop_duplicates()  # Loại bỏ dòng trùng lặp

# 5. Kiểm tra kiểu dữ liệu của các cột và chuyển đổi nếu cần
df_cleaned['column_name'] = pd.to_numeric(df_cleaned['column_name'], errors='coerce')  # Chuyển đổi kiểu dữ liệu

# 6. Loại bỏ các dòng có giá trị không hợp lệ (ví dụ: giá trị âm cho cột tuổi)
df_cleaned = df_cleaned[df_cleaned['age'] >= 0]  # Lọc ra các dòng có giá trị hợp lệ

# 7. Kiểm tra lại dữ liệu sau khi làm sạch
print(df_cleaned.head())  # In ra 5 dòng đầu tiên sau khi làm sạch

# 8. Lưu lại dữ liệu đã được làm sạch
df_cleaned.to_csv('cleaned_sample_data.csv', index=False)

#thay doi dulieu
