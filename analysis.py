import pandas as pd

# Đọc dữ liệu
df = pd.read_csv('dataset.csv')  # hoặc 'vi_misspellings_diverse.csv'

# Thống kê cơ bản
print("Tổng số mẫu:", len(df))
print("Số mẫu không sinh được lỗi (error_type = -1):", (df['error_type'] == -1).sum())

# Thống kê nâng cao
print("Độ dài trung bình câu gốc:", df['original'].str.len().mean())
print("Độ dài trung bình câu lỗi:", df['misspelled'].str.len().mean())

# Nếu muốn nhóm lỗi (ví dụ nhóm âm đầu, âm cuối, dấu, cấu trúc)
error_groups = {
    "Lỗi phụ âm đầu": [1, 2, 3, 4, 5, 6, 13],
    "Lỗi nguyên âm": [1, 7, 8, 10],
    "Lỗi dấu thanh": [1, 7, 8, 11],
    "Lỗi âm cuối": [9, 12],
    "Lỗi hình thái/cấu trúc": [14, 15]
}
for group, types in error_groups.items():
    count = df[df['error_type'].isin(types)].shape[0]
    print(f"{group}: {count} mẫu ({count/len(df)*100:.2f}%)")

    # Tạo bảng thống kê phân phối: Mã lỗi | Loại lỗi | Số lượng mẫu | Tỉ lệ (%)
    error_type_names = {
        -1: "Không sinh lỗi",
        0: "i/y",
        1: "l/n",
        2: "ch/tr",
        3: "s/x",
        4: "r/d/gi",
        5: "c/k",
        6: "o/ô/ơ/u/ư",
        7: "ă/â/a/e/ê",
        8: "u/ư/ô/o",
        9: "p/b",
        10: "dấu câu",
        11: "at/ac, ut/uc, ot/oc, iet/iec",
        12: "ph/v",
        13: "Hoán đổi từ",
        14: "Lặp từ"
    }

    # Đếm số lượng và tỉ lệ
    error_counts = df['error_type'].value_counts().sort_index()
    error_ratios = df['error_type'].value_counts(normalize=True).sort_index() * 100

    # Tạo DataFrame
    table = pd.DataFrame({
        "Mã lỗi": error_counts.index,
        "Loại lỗi": [error_type_names.get(i, "Không rõ") for i in error_counts.index],
        "Số lượng mẫu": error_counts.values,
        "Tỉ lệ (%)": error_ratios.values
    })

    # Định dạng tỉ lệ
    table["Tỉ lệ (%)"] = table["Tỉ lệ (%)"].map(lambda x: f"{x:.2f}")
    print(table)
    # # Đếm số ký tự đã bị làm noise (khác biệt) do lỗi error_type == 8 ở dòng thứ 51 của dataset
    # row_51 = df.iloc[51]
  
    # original = str(row_51['original'])
    # misspelled = str(row_51['misspelled'])
    # # Đếm số ký tự khác biệt giữa original và misspelled
    # # Sử dụng SequenceMatcher để tìm số ký tự bị thay đổi
    # from difflib import SequenceMatcher
    # matcher = SequenceMatcher(None, original, misspelled)
    # noise_chars = 0
    # for tag, i1, i2, j1, j2 in matcher.get_opcodes():
    #     if tag != 'equal':
    #         noise_chars += max(i2 - i1, j2 - j1)
    #     else:
    #         noise_chars += 0
    #         pass
    # print(f"Số ký tự đã làm noise do error_type == 7 ở dòng 51: {noise_chars}")
