# ---------------READ-------------------------------------------
# file1 = open("text_file2.txt", "w")
# file1.write("Hello world")
# file1.close()
# --------------Write--------------------------------------------------
# file1 = open("text_file2.txt", "r")
# print(file1.read())
# file1.close()
# ------------Append-------------------------------------------------
# file1 = open("text_file2.txt", "a")
# file1.write("\n Hello NSTU")
# file1.close()
# --------------Create existing file----------------------------
# file1 = open("text_file2.txt", "x")
# file1.write("Hello world")
# file1.close()
# ---------------Create new file------------------------------------
# file1 = open("text_file3.txt", "x")
# file1.write("Hello world")
# file1.close()
# ----------------read, readline, readlines, printing separately-------------
# file1 = open("text_file3.txt", "r")
# # print(file1.read(15))
# # print(file1.read())
# # print(file1.readline())
# # print(file1.readline())
# # print(file1.readlines())
# all_lines = file1.readlines()
# # for singleLine in all_lines:
#     # print(singleLine)
# print("Total Lines", len(all_lines))
# file1.close()
# ----------------------------------
