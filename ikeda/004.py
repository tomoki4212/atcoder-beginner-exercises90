h, w = map(int, input().split())
long_list = []
h_sum_list = []
w_sum_list = []
sum_list = []
for _ in range(h):
    row = list(map(int, input().split()))
    long_list.append(row)

for a_list in long_list:
    a = sum(a_list)
    h_sum_list.append(a)


for num in range(w):
    w_list = []
    for b_list in long_list:
        w_list.append(b_list[num])
    w_sum_list.append(sum(w_list))

for h_ind in h_sum_list:
    for w_ind in w_sum_list:
        sum_list.append(h_ind+w_ind)

flat_list = [item for sublist in long_list for item in sublist]
answer_list = [a-b for a, b in zip(sum_list, flat_list)]
for i in range(0, len(answer_list), w):
    print(" ".join(map(str, answer_list[i:i + w])))