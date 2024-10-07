# 引入List類型以便使用
from typing import List

def countLetters(sentence: str) -> List[int]:
    # 創建一個長度為26的列表，對應英文字母a-z，用於儲存每個字母的出現次數
    letterCount: List[int] = [0] * 26
    
# 檢查輸入的句子中的每個字符
    for char in sentence:
        # 檢查字符是否為英文字母
        if char.isalpha():
            # 計算其在字母表中的索引
            index = ord(char) - ord('a')
            letterCount[index] += 1  # 對應字母的計數加一

    return letterCount # 返回包含每個字母計數的列表
pass

#定義一個函數來列印字母計數，列表為參數
def printLetterCount(letterCount: List[int]) -> None:
    
# 檢查字母計數列表，總共26個字母
    for i in range(26):
        # 若該字母的計數大於0，則輸出該字母及其出現的次數
        if letterCount[i] > 0:
            print(f"{chr(i + ord('a'))}: {letterCount[i]}") # 輸出字母出現次數
pass

inputSentence: str = "this is an apple" # 定義句子
letterCount: List[int] = countLetters(inputSentence) # 計算字母出現次數
printLetterCount(letterCount) # 輸出各字母的計數結果