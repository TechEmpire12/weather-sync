import pandas as pd
from datetime import datetime

print("--- Testing Aggregation Fix ---")

# 1. Simulate data including a rogue future date (Jan 2026)
dates = [datetime(2025, 12, 15), datetime(2026, 1, 15)]
df = pd.DataFrame({"Daily_Precipitation": [10, 20]}, index=pd.DatetimeIndex(dates))

# 2. Mimic Dashboard Resampling
monthly = df.resample("M").agg({"Daily_Precipitation": "sum"})
print(f"Original Aggregated Index:\n{monthly.index}")

# 3. Create DataFrame for plotting (as in dashboard code)
rain_df = pd.DataFrame({
    "Date": monthly.index,
    "Rainfall": monthly["Daily_Precipitation"].values
})

print(f"\nDataFrame before filtering:\n{rain_df}")

# 4. Apply the Fix
current_time = datetime.now()
print(f"\nFiltering with Current Time: {current_time}")

rain_df_filtered = rain_df[rain_df["Date"] <= current_time]
print(f"\nDataFrame after filtering:\n{rain_df_filtered}")

# 5. Assertion
if len(rain_df_filtered) == 1 and rain_df_filtered.iloc[0]["Date"].year == 2025:
    print("\n✅ PASS: Future date (Jan 2026) was removed.")
else:
    print("\n❌ FAIL: Future date persists or logic error.")
