places = {'A':(10, '臺北市'), 'B':(11, '臺中市'), 'C':(12, '基隆市'), 'D':(13, '臺南市'),
          'E':(14, '高雄市'), 'F':(15, '新北市'), 'G':(16, '宜蘭縣'), 'H':(17, '桃園市'),
          'I':(34, '嘉義市'), 'J':(18, '新竹縣'), 'K':(19, '苗栗縣'), 'M':(21, '南投縣'),
          'N':(22, '彰化縣'), 'O':(35, '新竹市'), 'P':(23, '雲林縣'), 'Q':(24, '嘉義縣'),
          'T':(27, '屏東縣'), 'U':(28, '花蓮縣'), 'V':(29, '臺東縣'), 'W':(32, '金門縣'),
          'X':(30, '澎湖縣'), 'Z':(33, '連江縣'),
          'L':(20, '臺中縣'), 'R':(25, '臺南縣'), 'S':(26, '高雄縣'), 'Y':(31, '陽明山')}

weight = [8,7,6,5,4,3,2,1,1]

def p2Sum(num):
    return num // 10 * 1 + num % 10 * 9
def isValidId(pid):
    if pid[0] not in places:
        return False
    if pid[1] != '1' and pid[1] != '2':
        return False
    checkSum = 0
    checkSum = p2Sum(places[pid[0]][0])
    for i in range(1,10):
        checkSum += int(pid[i]) * weight[i-1]
    if checkSum % 10 == 0:
        return True
    else:
        return False
pid = input('輸入身分證字號:')
if isValidId(pid):
    print("正確")
else:
    print("錯誤")
"""
print(278 // 100)
print(278 % 100)
newNUmber = 278 % 100
print(newNUmber // 10)
print(newNUmber % 10)
"""
