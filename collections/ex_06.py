lst = [3, 6, 7, 4, 0, 2, 12, 54, 10, 11]
#
# maxi = None
# mini = None
#
# for n in lst:
#     if mini == None or n < mini:
#         mini = n
#     if maxi == None or n > maxi:
#         maxi = n
#
# maxx = lst.index(maxi)
# minn = lst.index(mini)
#
# lst[maxx] = mini
# lst[minn] = maxi
# print(lst)
maxi = max(lst)
mini = min(lst)
maxi_spot = lst.index(maxi)
mini_spot = lst.index(mini)

lst[maxi_spot] = mini
lst[mini_spot] = maxi
print(lst)                      #drugi sposób
