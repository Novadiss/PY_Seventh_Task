with open('1.txt', 'r', encoding='utf-8') as f:
    file_1_count = f.read()
    file_1_len = len(file_1_count.split('\n'))
    file_1_name = '1.txt'

with open('2.txt', 'r', encoding='utf-8') as f:
    file_2_count = f.read()
    file_2_len = len(file_2_count.split('\n'))
    file_2_name = '2.txt'

with open('3.txt', 'r', encoding='utf-8') as f:
    file_3_count = f.read()
    file_3_len = len(file_3_count.split('\n'))
    file_3_name = '3.txt'

with open('4.txt', 'w') as f:
    if file_1_len < file_2_len and file_2_len < file_3_len:
        f.write(f'1.txt\n{file_1_len}\n{file_1_count}\n')
        f.write(f'2.txt\n{file_2_len}\n{file_2_count}\n')
        f.write(f'3.txt\n{file_3_len}\n{file_3_count}\n')
    elif file_1_len < file_3_len and file_3_len < file_2_len:
        f.write(f'1.txt\n{file_1_len}\n{file_1_count}\n')
        f.write(f'3.txt\n{file_3_len}\n{file_3_count}\n')
        f.write(f'2.txt\n{file_2_len}\n{file_2_count}\n')
    elif file_2_len < file_1_len and file_1_len < file_3_len:
        f.write(f'2.txt\n{file_2_len}\n{file_2_count}\n')
        f.write(f'1.txt\n{file_1_len}\n{file_1_count}\n')
        f.write(f'3.txt\n{file_3_len}\n{file_3_count}\n')
    elif file_2_len < file_3_len and file_3_len < file_1_len:
        f.write(f'2.txt\n{file_2_len}\n{file_2_count}\n')
        f.write(f'3.txt\n{file_3_len}\n{file_3_count}\n')
        f.write(f'1.txt\n{file_1_len}\n{file_1_count}\n')
    elif file_3_len < file_1_len and file_1_len < file_2_len:
        f.write(f'3.txt\n{file_3_len}\n{file_3_count}\n')
        f.write(f'1.txt\n{file_1_len}\n{file_1_count}\n')
        f.write(f'2.txt\n{file_2_len}\n{file_2_count}\n')
    elif file_3_len < file_2_len and file_2_len < file_1_len:
        f.write(f'3.txt\n{file_3_len}\n{file_3_count}\n')
        f.write(f'2.txt\n{file_2_len}\n{file_2_count}\n')
        f.write(f'1.txt\n{file_1_len}\n{file_1_count}\n')

with open('4.txt', 'r') as f:
    print(f.read())