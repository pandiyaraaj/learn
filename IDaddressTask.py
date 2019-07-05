# Getting input from the user
ip = input("Enter an ID address: ")

# Assignging dummy values
len_seg = 0
# num_seg = ""
seg_num = 1

for i in range(0, len(ip)):
    if ip[i] in '1234567890':
        len_seg += 1
    elif ip[i] not in '1234567890' and len_seg != 0:
        print("length of segment {} is {}".format(seg_num, len_seg))
        seg_num += 1
        # num_seg = num_seg + str(len_seg)
        len_seg = 0
if len_seg != 0:
    print("length of segment {} is {}".format(seg_num, len_seg))
    seg_num += 1
    # num_seg = num_seg + str(len_seg)

# Total segments
# final = len(num_seg)
print("\nTotal number of segment is {}".format(seg_num -1))
