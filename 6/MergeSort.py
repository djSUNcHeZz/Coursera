#супер быстрая Сортировка по методу двух указателей двух неубывающих списков O(NlogN)
def merge(A, B):
	C = []
	i, j = 0, 0
	while i < len(A) and j < len(B):
		if A[i] < B[j]:
			C.append(A[i])
			i += 1
		else:
			C.append(B[j])
			j += 1
	C += A[i:] + B[j:]
	return C


'''
текст к задаче
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
print(*merge(A, B))
далее текст не из задачи
'''


def merge_sort(A):
	return merge(merge_sort(A[:len(A) // 2]),
														merge_sort(A[len(A) // 2:])) if len(A) > 1 else A


A = [int(i) for i in input().split()]
print(*merge_sort(A))

