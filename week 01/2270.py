import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
disk_number_arr = []
for i in arr:
    disk_number_arr.append(list(map(int, input().split())))