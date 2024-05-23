from openpyxl import workbook
wb = workbook() #새 워크북 생성
ws = wb.active # 현재 활성화된 시트 가져오기
ws.title = "연습시트"  #시트 이름 변경
wb.save("sample.xlsx")  # sample로 이름 저장
wb.close()

