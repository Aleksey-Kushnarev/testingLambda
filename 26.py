from functools import reduce

f = open("26.txt")
n, k = map(int, f.readline().split())
a = list(map(lambda x: list(map(int, x.split())), f.readlines()))
a = list(map(lambda x: x if len(x) == 4 else x[:3] + [max(x[3], x[4])], a))
certificate_true = list(filter(lambda x: x[0] == 1, a))
certificate_true_res = sorted(list(map(lambda x: reduce(lambda z, w: z + w, x[1:]), certificate_true)), reverse=True)[k - 1]
certificate_false_res = sorted(list(map(lambda x: sum(x[1:]), a)), reverse=True)[k - 1]
print(str(certificate_true_res) + " С УЧЕТОМ")
print(str(certificate_false_res) + " БЕЗ УЧЕТА")
