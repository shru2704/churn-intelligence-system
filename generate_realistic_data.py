#!/usr/bin/env python3
"""
Enhanced Dataset Generator - More Realistic Patterns
Generates realistic user behavioral data with seasonal patterns,
power law distributions, and cohort-based behaviors
"""

import csv
import random
import math
from datetime import datetime, timedelta
from collections import defaultdict

# Configuration
TOTAL_USERS = 300
START_DATE = datetime(2024, 7, 1)
END_DATE = datetime(2025, 12, 31)

# Pricing
PLANS = {'Basic': 29, 'Pro': 79, 'Team': 199}

# Names
FIRST_NAMES = [
    'James', 'Mary', 'Robert', 'Patricia', 'John', 'Jennifer', 'Michael', 'Linda',
    'David', 'Elizabeth', 'William', 'Barbara', 'Richard', 'Susan', 'Joseph', 'Jessica',
    'Rahul', 'Priya', 'Arjun', 'Ananya', 'Rohan', 'Kavya', 'Aarav', 'Diya',
    'Maya', 'Aditya', 'Kabir', 'Ishita', 'Vihaan', 'Anika', 'Ayush', 'Riya',
    'Chen', 'Wei', 'Yuki', 'Hiroshi', 'Mei', 'Jin', 'Akira', 'Yuna'
]

LAST_NAMES = [
    'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis',
    'Patel', 'Sharma', 'Singh', 'Kumar', 'Gupta', 'Verma', 'Reddy', 'Chopra',
    'Chen', 'Wang', 'Li', 'Zhang', 'Liu', 'Tanaka', 'Sato', 'Yamamoto'
]

def get_seasonal_factor(date):
    """Returns seasonal multiplier (0.8 to 1.2) for signup patterns"""
    month = date.month
    # Lower activity in December (holidays), spike in January
    if month == 12:
        return 0.7
    elif month == 1:
        return 1.3
    elif month in [6, 7]:  # Summer dip
        return 0.85
    else:
        return 1.0

def power_law_distribution(alpha=2.5):
    """Generate power-law distributed number (realistic for user activity)"""
    # Pure Python implementation of Pareto distribution
    u = 1.0 - random.random()
    return (1.0 / (u ** (1.0 / alpha))) * 5

def select_plan_with_upgrade_path():
    """Select plan with realistic upgrade patterns"""
    # Most start on Basic, some upgrade over time
    initial_choice = random.choices(
        ['Basic', 'Pro', 'Team'],
        weights=[0.75, 0.20, 0.05],
        k=1
    )[0]

    return initial_choice, PLANS[initial_choice]

def generate_cohort_behavior(days_since_signup):
    """Generate behavior based on user's cohort (when they signed up)"""
    # Early adopters (first 3 months) more engaged
    # Later users more casual
    if days_since_signup > 400:  # Early adopters
        base_engagement = 1.3
    elif days_since_signup > 200:  # Middle cohort
        base_engagement = 1.0
    else:  # Recent users
        base_engagement = 0.85

    return base_engagement

def generate_user_behavior(user_type, days_since_signup, base_engagement):
    """Generate realistic behavioral patterns"""

    if user_type == 'power':
        # Power users: Logins follow power law with high base
        logins_30d = int(min(45, power_law_distribution(2.0) * base_engagement))
        features = random.randint(5, 7)
        onboarding = random.randint(6, 8)
        collab = random.random() < 0.90

    elif user_type == 'casual':
        # Casual users: Moderate, consistent usage
        logins_30d = random.randint(4, 14)
        features = random.randint(2, 4)
        onboarding = random.randint(3, 5)
        collab = random.random() < 0.45

    elif user_type == 'at_risk':
        # At-risk users: Declining engagement
        logins_30d = random.randint(0, 6)
        features = random.randint(1, 3)
        onboarding = random.randint(1, 4)
        collab = random.random() < 0.25

    else:  # churned
        # Churned users: Very low engagement before leaving
        logins_30d = random.randint(0, 4)
        features = random.randint(1, 2)
        onboarding = random.randint(1, 4)
        collab = random.random() < 0.15

    # Adjust for cohort behavior
    logins_30d = int(logins_30d * base_engagement)
    logins_30d = max(0, min(50, logins_30d))

    return {
        'total_logins_30d': logins_30d,
        'features_used_count': features,
        'onboarding_step_reached': onboarding,
        'used_collaboration': collab
    }

def generate_support_tickets(user_type, days_active):
    """Generate realistic support ticket patterns"""
    if user_type == 'power':
        # Power users request features, not problems
        return random.choices([0, 1, 2], weights=[0.50, 0.35, 0.15])[0]
    elif user_type == 'churned':
        # Churned users often don't complain, they just leave
        return random.choices([0, 1], weights=[0.75, 0.25])[0]
    else:
        return random.choices([0, 1, 2], weights=[0.60, 0.30, 0.10])[0]

def generate_user(user_id, user_type):
    """Generate a single realistic user record"""

    # Signup with seasonal pattern
    days_into_period = random.randint(0, (END_DATE - START_DATE).days)

    # Apply seasonal weighting
    attempts = 0
    while True:
        test_date = START_DATE + timedelta(days=days_into_period)
        seasonal_factor = get_seasonal_factor(test_date)
        if random.random() < seasonal_factor or attempts > 10:
            signup_date = test_date
            break
        attempts += 1
        days_into_period = random.randint(0, (END_DATE - START_DATE).days)

    # Plan selection with upgrade path
    plan_type, monthly_revenue = select_plan_with_upgrade_path()

    # Determine if churned based on user type
    is_churned = user_type == 'churned'

    # Calculate days since signup
    if is_churned:
        # Churn happens between Day 30-90 typically
        days_active = random.randint(30, 90)
        churn_date = signup_date + timedelta(days=days_active)
        days_since_signup = days_active
    else:
        days_since_signup = (END_DATE - signup_date).days
        churn_date = ''

    # Cohort behavior modifier
    base_engagement = generate_cohort_behavior(days_since_signup)

    # Generate behavior
    behavior = generate_user_behavior(user_type, days_since_signup, base_engagement)

    # Last login calculation
    if is_churned:
        days_inactive = random.randint(14, 90)
        last_login = churn_date - timedelta(days=random.randint(0, 7))
    else:
        if user_type == 'power':
            days_inactive = random.randint(0, 3)
        elif user_type == 'casual':
            days_inactive = random.randint(0, 7)
        else:  # at_risk
            days_inactive = random.randint(7, 21)
        last_login = END_DATE - timedelta(days=days_inactive)

    # Support tickets
    support_tickets = generate_support_tickets(user_type, days_since_signup)

    # Generate email
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    email = f"{first_name.lower()}.{last_name.lower()}{random.randint(1, 999)}@example.com"

    return {
        'user_id': user_id,
        'email': email,
        'signup_date': signup_date.strftime('%Y-%m-%d'),
        'plan_type': plan_type,
        'monthly_revenue': monthly_revenue,
        'churned': 'yes' if is_churned else 'no',
        'churn_date': churn_date.strftime('%Y-%m-%d') if is_churned else '',
        'last_login_date': last_login.strftime('%Y-%m-%d'),
        'days_since_last_login': days_inactive,
        'total_logins_30d': behavior['total_logins_30d'],
        'features_used_count': behavior['features_used_count'],
        'onboarding_step_reached': behavior['onboarding_step_reached'],
        'used_collaboration': 'yes' if behavior['used_collaboration'] else 'no',
        'support_tickets_raised': support_tickets,
        'days_since_signup': days_since_signup
    }

def main():
    print("Generating Enhanced Realistic Dataset...")
    print(f"   Total users: {TOTAL_USERS}")

    users = []

    # Generate users by type with realistic distribution
    user_types = []

    # Churned users (25%)
    user_types.extend(['churned'] * 75)

    # Power users (20% of active = 15% of total)
    user_types.extend(['power'] * 45)

    # Casual users (45% of active = 34% of total)
    user_types.extend(['casual'] * 100)

    # At-risk users (35% of active = 26% of total)
    user_types.extend(['at_risk'] * 80)

    # Verify distribution
    print(f"\nUser Distribution:")
    print(f"   Churned: {len([t for t in user_types if t == 'churned'])} ({len([t for t in user_types if t == 'churned'])/len(user_types)*100:.1f}%)")
    print(f"   Power: {len([t for t in user_types if t == 'power'])} ({len([t for t in user_types if t == 'power'])/len(user_types)*100:.1f}%)")
    print(f"   Casual: {len([t for t in user_types if t == 'casual'])} ({len([t for t in user_types if t == 'casual'])/len(user_types)*100:.1f}%)")
    print(f"   At-risk: {len([t for t in user_types if t == 'at_risk'])} ({len([t for t in user_types if t == 'at_risk'])/len(user_types)*100:.1f}%)")

    # Generate users
    print(f"\nGenerating user records...")
    for i, user_type in enumerate(user_types, 1):
        if i % 50 == 0:
            print(f"   Progress: {i}/{len(user_types)}")
        users.append(generate_user(i, user_type))

    # Shuffle to mix users
    random.shuffle(users)

    # Write to CSV
    output_file = 'data/churn_intelligence_dataset.csv'
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'user_id', 'email', 'signup_date', 'plan_type', 'monthly_revenue',
            'churned', 'churn_date', 'last_login_date', 'days_since_last_login',
            'total_logins_30d', 'features_used_count', 'onboarding_step_reached',
            'used_collaboration', 'support_tickets_raised', 'days_since_signup'
        ])
        writer.writeheader()
        writer.writerows(users)

    print(f"\n[OK] Dataset generated: {output_file}")

    # Print statistics
    print(f"\nDataset Statistics:")

    active_users = [u for u in users if u['churned'] == 'no']
    churned_users = [u for u in users if u['churned'] == 'yes']

    print(f"\nUser Status:")
    print(f"   Active Users: {len(active_users)} ({len(active_users)/len(users)*100:.1f}%)")
    print(f"   Churned Users: {len(churned_users)} ({len(churned_users)/len(users)*100:.1f}%)")

    # Calculate at-risk users
    at_risk = 0
    for user in active_users:
        score = 0
        if user['total_logins_30d'] < 2:
            score += 25
        if user['onboarding_step_reached'] <= 3:
            score += 20
        if user['features_used_count'] <= 2:
            score += 20
        if user['used_collaboration'] == 'no':
            score += 20
        if user['days_since_last_login'] >= 7:
            score += 15

        if score >= 31:
            at_risk += 1

    print(f"   At-Risk Users: {at_risk} ({at_risk/len(active_users)*100:.1f}% of active)")

    # Revenue
    active_mrr = sum(u['monthly_revenue'] for u in active_users)
    churned_mrr = sum(u['monthly_revenue'] for u in churned_users)

    print(f"\nRevenue:")
    print(f"   Active MRR: ${active_mrr:,.2f}")
    print(f"   Churned MRR: ${churned_mrr:,.2f}")
    print(f"   Total MRR: ${active_mrr + churned_mrr:,.2f}")

    # Login distribution (power law check)
    logins = [u['total_logins_30d'] for u in active_users]
    logins_sorted = sorted(logins)
    print(f"\nLogin Distribution (Active Users):")
    print(f"   Min: {min(logins)}")
    print(f"   Max: {max(logins)}")
    print(f"   Median: {logins_sorted[len(logins)//2]:.1f}")
    print(f"   Mean: {sum(logins)/len(logins):.1f}")

    print(f"\n[OK] Dataset complete! Ready for dashboard.")

if __name__ == '__main__':
    main()
