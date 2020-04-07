my_string_list = "four score and seven years ago our fathers brought forth on this continent a new nation".split()
list_len = len(my_string_list)
col_size = int(list_len / 3)
neg_col_size = -1 * col_size
col_1 = my_string_list[: col_size + 1]
col_2 = my_string_list[col_size + 1 : neg_col_size]
col_3 = my_string_list[neg_col_size:]
print(col_1)
print(col_2)
print(col_3)
