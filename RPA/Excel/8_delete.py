from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

ws.delete_rows(8) #8번 쨰 줄에 있는 7번 학생 삭제
ws.delete_rows(8,3) #8번 쨰 줄부터 3줄 삭제
ws.delete_cols(2) #2번쨰 열 b부터 삭제
ws.delete_cols(2,2) #2번쨰 열 b부터 2개 삭제




wb.save("sample_delete_row.xlsx")

