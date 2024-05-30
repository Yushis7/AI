from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

#행8번 위치 새 줄 넣기
# ws.insert_row(8)

#8번 행 새 줄 5번 넣기
ws.insert_row(8,5)

#b번쨰 열이 생성
ws.insert_cols(2)

wb.save("sample_insert_rows.xlsx")

