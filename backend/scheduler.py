from datetime import datetime, timedelta

def create_schedule(dates, user_data):
    schedule = {}
    
    # Defaults if student doesn't provide input
    wakeup = int(user_data.get("wakeup", 8))     # e.g., 8 AM
    sleep = int(user_data.get("sleep", 23))      # e.g., 11 PM
    
    for i in range(120):  # Approximate length of a semester: 4 months
        current_day = datetime.today() + timedelta(days=i)
        date_str = current_day.strftime('%Y-%m-%d')

        daily_plan = []

        # Add standard meal times
        daily_plan.append("🍳 Breakfast – 8:00 AM")
        daily_plan.append("🥗 Lunch – 12:00 PM")
        daily_plan.append("🍽️ Dinner – 6:00 PM")

        # Add 2 study sessions per day
        study_start = wakeup + 2  # Give time after waking
        daily_plan.append(f"📚 Study Session 1 – {study_start}:00")
        daily_plan.append(f"📚 Study Session 2 – {study_start + 2}:00")

        # Add a rest/fun block
        daily_plan.append("🎉 Free Time – 9:00 PM")

        # Add to main schedule
        schedule[date_str] = daily_plan

    return schedule
