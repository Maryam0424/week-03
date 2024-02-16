def record_yield(yields, cow_id, yield_amount, day):
    if cow_id in yields:
        if day in yields[cow_id]:
            yields[cow_id][day].append(yield_amount)
        else:
            yields[cow_id][day] = [yield_amount]
    else:
        yields[cow_id] = {day: [yield_amount]}

def calculate_total_avg(yields):
    totals = {}
    averages = {}
    for cow_id, cow_data in yields.items():
        total_yield = 0
        num_days = len(cow_data)
        for day, day_yield in cow_data.items():
            total_yield += sum(day_yield)
        average_yield = total_yield / num_days
        totals[cow_id] = total_yield
        averages[cow_id] = average_yield
    return totals, averages

def identify_cows(yields):
    best_yield = 0
    best_cow = None
    low_yield_cows = []
    for cow_id, cow_data in yields.items():
        total_yield = sum(sum(day_yield) for day_yield in cow_data.values())
        if total_yield > best_yield:
            best_yield = total_yield
            best_cow = cow_id
        low_days = sum(1 for day_yield in cow_data.values() if sum(day_yield) < 12)
        if low_days >= 4:
            low_yield_cows.append(cow_id)
    return best_cow, low_yield_cows
    
def main():
    yields = {}
    for day in range(1, 8):
        print(f"Day {day}: ")
        num_cows = int(input("Enter the number of cows milked: "))
        for _ in range(num_cows):
            cow_id = input("Enter the 3-digit identity code of the cow: ")
            yield_amount = float(input("Enter the milk yield(liters): "))
            record_yield(yields, cow_id, yield_amount, day)
        
        totals, averages = calculate_total_avg(yields)

        best_cow, low_yield_cow = identify_cows(yields)

        print("\nWeekly Milk Yield Summary: ")
        print("-------------------------------")
        print("Cow ID\tTotal Yield\tAverage Yiled")

        for cow_id in sorted(totals.keys()):
            print(f"{cow_id}\t{totals[cow_id]:.1f}\t\t{averages[cow_id]:.1f}")
        
        print("-------------------------------")
        print(f"Cow with the best yield: {best_cow}")
        print(f"Cows with less than 12 liters for four or more days: {low_yield_cow}")
        for cow_id in low_yield_cow:
            print(cow_id)

main()

