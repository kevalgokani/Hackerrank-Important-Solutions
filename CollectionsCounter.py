import collections as cl

def TotalIncome():
    totalMoney = 0
    for i in range(numCust):
        size, price = map(int, input().split())
        if shoes[size]: 
            totalMoney = totalMoney + price
            shoes[size] = shoes[size]-1

    return totalMoney

if __name__ == "__main__":
    numShoes = int(input())
    shoes = cl.Counter(map(int, input().split()))
    numCust = int(input())

    result = int(TotalIncome())
    print(result)
