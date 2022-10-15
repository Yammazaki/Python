# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'абвну абввот Привет, Слава!'.split()
smb = 'абв'
print(' '.join([word for word in text if smb not in word]))