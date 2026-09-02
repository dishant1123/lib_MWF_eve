import numpy as np

np.random.seed(2024)   #  seed ----> fix the  array  element. 
n_products = 10

base_price = np.random.randint(
    200, 3000, size=n_products
).astype(float)

cost_price = base_price * np.random.uniform(
    0.4, 0.7, size=n_products
)

units_m1 = np.random.randint(
    50, 500, size=n_products
).astype(float)

units_m2 = np.random.randint(
    50, 500, size=n_products
).astype(float)

units_m3 = np.random.randint(
    50, 500, size=n_products
).astype(float)

# Add missing values
units_m1[[2, 7]] = np.nan
print("Base Prices:", base_price)

# clean :
print("NaN in Month 1:",
      np.isnan(units_m1).sum())

median_m1 = np.nanmedian(units_m1)
units_m1 = np.where(
    np.isnan(units_m1),
    median_m1,
    units_m1
)
print("NaN after imputation:",
      np.isnan(units_m1).sum())

# Clip values at 95th percentile
upper_limit = np.percentile(units_m1, 95)
units_m1 = np.clip(
    units_m1,
    0,
    upper_limit
)

# REVENUE & PROFIT

rev_m1 = base_price * units_m1
rev_m2 = base_price * units_m2
rev_m3 = base_price * units_m3

total_revenue = (
    rev_m1 +
    rev_m2 +
    rev_m3
)
total_units = (
    units_m1 +
    units_m2 +
    units_m3
)

total_cost = cost_price * total_units
profit = total_revenue - total_cost
margin_pct = (
    profit / total_revenue
) * 100

print(
    "Profit Margins %:",
    np.round(margin_pct, 2)
)

# growth :

growth_m2 = (
    (rev_m2 - rev_m1)
    / rev_m1
) * 100

growth_m3 = (
    (rev_m3 - rev_m2)
    / rev_m2
) * 100
print(
    "Top product by revenue:",
    np.argmax(total_revenue)
)
print(
    "Highest margin product:",
    np.argmax(margin_pct)
)
print(
    "Products with >40% margin:",
    np.where(margin_pct > 40)
)
avg_monthly_revenue = np.mean(
    [rev_m1, rev_m2, rev_m3],
    axis=0
)
print(
    "Avg monthly revenue:",
    np.round(avg_monthly_revenue, 2)
)
print(
    "Best growth M2->M3:",
    np.argmax(growth_m3)
)

# summary report :

print("=" * 55)
print("  PRODUCT PERFORMANCE SUMMARY — Q1 2024")
print("=" * 55)
print(
    f"Total portfolio revenue: "
    f"Rs {total_revenue.sum():,.0f}"
)
print(
    f"Average margin: "
    f"{margin_pct.mean():.1f}%"
)
print(
    f"Highest revenue product: "
    f"SKU {np.argmax(total_revenue)+1} — "
    f"Rs {total_revenue.max():,.0f}"
)
print(
    f"Best margin product: "
    f"SKU {np.argmax(margin_pct)+1} — "
    f"{margin_pct.max():.1f}%"
)
print(
    f"Fastest growing in M3: "
    f"SKU {np.argmax(growth_m3)+1} — "
    f"{growth_m3.max():.1f}% growth"
)