cost = int(input())
retail_price = int(input())
N = int(input()) # 單日需求量 D
quantity_order = int(input()) # 訂貨量 q
prob_list = list() # 購買機率

# cost = 2
# retail_price = 10
# N = 8 # 單日需求量 D
# quantity_order = 2 # 訂貨量 q
# prob_list = [0.06, 0.15, 0.22, 0.22, 0.17, 0.10, 0.05, 0.02, 0.01] # 購買機率


prob_sum = 0

for i in range(N + 1):
    prob = float(input())
    if prob > 0 and prob < 1:
        prob_list.append(prob)
    prob_sum += prob
print("Correct") if prob_sum == 1 else print("Error")

max_q = 0
profit = 0
profit_max = 0
for i in range(quantity_order):
    profit = 0
    prob_list_sum = 0
    for j in range(N):
        if j <= i:
            profit += (retail_price * j - cost * quantity_order) * prob_list[j]
            prob_list_sum += prob_list[j]
        else:
            profit += (retail_price - cost) * quantity_order * (1 - prob_list_sum) 
            break
        
print(profit)
print(int(profit))
