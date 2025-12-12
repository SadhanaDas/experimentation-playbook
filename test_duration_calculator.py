def test_duration_calculator(sample_size_per_group, groups, daily_traffic):
    
    total_required_sample = sample_size_per_group * groups
    days_needed = total_required_sample / daily_traffic

    print(f"Total Sample Required: {total_required_sample}")
    print(f"Daily Eligible Traffic: {daily_traffic}")
    print(f"Estimated Duration: {round(days_needed, 2)} days")

    return round(days_needed, 2)
