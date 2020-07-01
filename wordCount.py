import string

# reference: https://www.itread01.com/content/1516507345.html
def str_count(s):
    count_en = count_dg = count_sp = count_zh = count_pu = 0

    s_len = len(s)
    for c in s:
        # count English letters
        if c in string.ascii_letters:
            count_en += 1
        # count digits
        elif c.isdigit():
            count_dg += 1
        # count spaces
        elif c.isspace():
            count_sp += 1
        # count Chinese characters. Note that Japanese and Korean alphabets is included.
        elif c.isalpha() & (ord(c)>19968) & (ord(c)<65103):
            count_zh += 1
        # count punctuation marks
        elif ord(c)>19968 & ord(c)<65103:
            count_pu += 1



    return {'English letters': count_en, 'Digits': count_dg, 'Spaces': count_sp, 
	'Chinese Characters': count_zh, 'other notations/letters': count_pu}



str_l = "（位元）可縮寫成b（小寫），例如Mb表示Megabit。" # text
count = str_count(str_l)
print(count)