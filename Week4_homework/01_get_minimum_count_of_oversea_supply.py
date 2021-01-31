# Q. 라면 공장에서는 하루에 밀가루를 1톤씩 사용합니다.
# 원래 밀가루를 공급받던 공장의 고장으로 앞으로 k일 이후에야 밀가루를 공급받을 수 있기 때문에 해외 공장에서 밀가루를 수입해야 합니다.
#
# 해외 공장에서는 향후 밀가루를 공급할 수 있는 날짜와 수량을 알려주었고,
# 라면 공장에서는 운송비를 줄이기 위해 최소한의 횟수로 밀가루를 공급받고 싶습니다.
#
# 현재 공장에 남아있는 밀가루 수량 stock, 밀가루 공급 일정(dates)과 해당 시점에 공급 가능한 밀가루 수량(supplies),
# 원래 공장으로부터 공급받을 수 있는 시점 k가 주어질 때,
# 밀가루가 떨어지지 않고 공장을 운영하기 위해서 최소한 몇 번 해외 공장으로부터 밀가루를 공급받아야 하는지를 반환 하시오.
#
# dates[i]에는 i번째 공급 가능일이 들어있으며, supplies[i]에는 dates[i] 날짜에 공급 가능한 밀가루 수량이 들어 있습니다.


import heapq

ramen_stock = 4  # 밀가루 수량
supply_dates = [4, 10, 15]  # 밀가루 공급 일정
supply_supplies = [20, 5, 10]  # 공급 가능한 밀가루 수량
supply_recover_k = 30  # 원래 공장으로부터 공급 받을수 있는 시점


# 1. 4일동안은 있는거로 사용가능
# 2. 26일 정도를 공급 일정에서 공급받아 사용해야함
# 3. 운송비를 줄이기위해 최소한 휫수로 밀가루 공급 받아야함 <-- 최소값
# 4. 총 필요 톤수 26톤 4 일 20톤 , 15일에 10톤 두번받으면됨

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0  # 공급받는 횟수를 받기 위한 변수
    current_day_index = 0  # 오늘이 몇일인지 알아야 가져올지 말지 결정할수있기때문
    max_heap = []  # 공급량이 떨어지지 않는 한에서 , 최대값을 받기위한 heap 선언
    while stock < k: # stock이 공급받을수있는 시점보다 크면 안되기때문에 그 전까지 반복

        for date_index in range(current_day_index, len(dates)):
            if dates[date_index] <= stock:  #
                heapq.heappush(max_heap, -supply_supplies[date_index])
            else:
                current_day_index = date_index
                break

        answer += 1
        stock += -heapq.heappop(max_heap)

    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
