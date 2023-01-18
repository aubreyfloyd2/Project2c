# Author: Aubrey Floyd
# GitHub username: aubreyfloyd2
# Date: 1/18/2023
# Description: Asks user for a number of cents and outputs how many of each coin
#              would represent that amount with the fewest total number of coins
print("Please enter an amount in cents less than a dollar.")
cents_total = int(input())
Q = cents_total // 25
Q_remainder = cents_total % 25
D = Q_remainder // 10
D_remainder = Q_remainder % 10
N = D_remainder // 5
N_remainder = D_remainder % 5
P = N_remainder // 1
print("Your change will be:")
print("Q:", Q)
print("D:", D)
print("N:", N)
print("P:", P)