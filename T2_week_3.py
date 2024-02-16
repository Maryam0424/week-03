from T1_week_3 import calculate_total_avg

def calculate_total_weekly_volume(yields):
    total_volume = sum(sum(sum(day_yield) for day_yield in cow_data.values()) for cow_data in yields.values())
    return round(total_volume)

def calculate_average_yield_per_cow(totals):
    num_cows = len(totals)
    total_yield = sum(totals.values())
    if num_cows != 0:
        average_yield = total_yield /num_cows
    else:
        average_yield = total_yield / num_cows
    return round(average_yield)

def main():
    yields = {'001': {1: [12, 13], 2: [14, 15], 3: [16, 17], 4: [18, 19], 5: [20, 21], 6: [22, 23], 7: [24, 25]},
        '002': {1: [11, 12], 2: [13, 14], 3: [15, 16], 4: [17, 18], 5: [19, 20], 6: [21, 22], 7: [23, 24]}}
    
    total_weekly_volume = calculate_total_weekly_volume(yields)
    totals, _ = calculate_total_avg(yields)
    average_yield_per_cow = calculate_average_yield_per_cow(totals)

    print("Total Weeekly Volume of Milk for the Herd (liters): ", total_weekly_volume)
    print("Average Yield per cow in a week (lietrs): ", average_yield_per_cow)

main()