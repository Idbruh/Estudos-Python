# def solution(N):
#     bin_rep = str(bin(N))[2:]
#     bin_gap = False
#     bin_max = 0
#     bin_counter = 0
#     for symbol in bin_rep:
#         if symbol == '1':
#             if bin_max < bin_counter:
#                 bin_max = bin_counter
#             bin_gap = True
#             bin_counter = 0
#         elif bin_gap:
#             bin_counter += 1
#     return bin_max
#
#
# print(solution(2000))



def solution(N):
  return len(
      max (
          bin(N)[2:].strip('0').strip('1').split('1'))
  )
# O(N)


print(solution(1041))