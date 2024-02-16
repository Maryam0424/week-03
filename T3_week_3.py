from T1_week_3 import calculate_total_avg

def identify_cows(yields):
    best_yield = 0
    best_cow = None
    low_yield_cows = []

    cow_totals = {cow_id: sum(sum(day_yield) for day_yield in cow_data.values()) for cow_id, cow_data in yields.items()}
    
    for cow_id, cow_data in yields.items():
        total_yield = cow_totals[cow_id]

        if total_yield > best_yield:
            best_yield = total_yield
            best_cow = cow_id

        num_days = len(cow_data)
        average_yield = total_yield / num_days
        
        if average_yield < 12:
            low_yield_cows.append(cow_id)
            
    return best_cow, low_yield_cows

def main():
    yields = {
        '001': {1: [12, 13], 2: [14, 15], 3: [16, 17], 4: [18, 19], 5: [20, 21], 6: [22, 23], 7: [24, 25]},
        '002': {1: [11, 12], 2: [13, 14], 3: [15, 16], 4: [17, 18], 5: [19, 20], 6: [21, 22], 7: [23, 24]}}
    
    totals, _ = calculate_total_avg(yields)

    best_cow, low_yield_cows = identify_cows(yields)

    print("Most Priductive Cow: ")
    print(f"Indetify Code Number: {best_cow}")
    print(f"Weekly Yield: {sum(sum(day_yield) for day_yield in yields[best_cow].values())} liters")

    print("\nCows with Low Volume of Milk: ")
    for cow_id in low_yield_cows:
        print(f"Identity Code Number: {cow_id}")
        print(f"Weekly Yield: {sum(sum(day_yield) for day_yield in yields[cow_id].values())} liters")

main()