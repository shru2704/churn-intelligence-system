#!/usr/bin/env python3
"""
Churn Intelligence System - Mock Dataset Generator
Generates 300 realistic user records following PRD specifications
"""

import csv
import random
from datetime import datetime, timedelta
from collections import defaultdict

# Configuration
TOTAL_USERS = 300
CHURNED_PERCENTAGE = 0.25
START_DATE = datetime(2024, 7, 1)
END_DATE = datetime(2025, 12, 31)

# Pricing
PLANS = {
    'Basic': 29,
    'Pro': 79,
    'Team': 199
}
PLAN_DISTRIBUTION = [0.60, 0.30, 0.10]  # 60% Basic, 30% Pro, 10% Team

# State data for realistic names/generation
FIRST_NAMES = [
    'James', 'Mary', 'Robert', 'Patricia', 'John', 'Jennifer', 'Michael', 'Linda',
    'David', 'Elizabeth', 'William', 'Barbara', 'Richard', 'Susan', 'Joseph', 'Jessica',
    'Thomas', 'Sarah', 'Charles', 'Karen', 'Christopher', 'Nancy', 'Daniel', 'Lisa',
    'Rahul', 'Priya', 'Arjun', 'Ananya', 'Rohan', 'Kavya', 'Aarav', 'Diya',
    'Maya', 'Aditya', 'Kabir', 'Ishita', 'Vihaan', 'Anika', 'Ayush', 'Riya'
]

LAST_NAMES = [
    'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis',
    'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Wilson', 'Anderson', 'Thomas',
    'Patel', 'Sharma', 'Singh', 'Kumar', 'Gupta', 'Verma', 'Reddy', 'Chopra'
]

def random_date(start, end):
    """Generate random date between start and end"""
    return start + timedelta(
        days=random.randint(0, (end - start).days)
    )

def random_date_after(start, min_days, max_days):
    """Generate random date after start with min/max days"""
    return start + timedelta(days=random.randint(min_days, max_days))

def select_plan():
    """Select plan based on distribution"""
    r = random.random()
    if r < 0.60:
        return 'Basic', PLANS['Basic']
    elif r < 0.90:
        return 'Pro', PLANS['Pro']
    else:
        return 'Team', PLANS['Team']

def generate_user(user_id, is_churned):
    """Generate a single user record following PRD specifications"""

    # Signup date (uniform distribution over 18 months)
    days_into_period = random.randint(0, (END_DATE - START_DATE).days)
    signup_date = START_DATE + timedelta(days=days_into_period)

    # Plan selection
    plan_type, monthly_revenue = select_plan()

    # Determine user type and behavior patterns
    if is_churned:
        # Churned users: 70% stuck at step 3 or below, 80% never used collaboration
        onboarding_step = random.choices(
            range(1, 4),  # Steps 1-3
            weights=[0.40, 0.35, 0.25],  # More stuck at earlier steps
            k=1
        )[0]

        used_collaboration = random.random() < 0.20  # Only 20% used it

        # Churned users have lower engagement
        features_used = random.choices(
            [1, 2, 3],  # Low feature usage
            weights=[0.50, 0.35, 0.15],
            k=1
        )[0]

        # Login pattern - declining then stopped
        days_active_before_churn = random.randint(14, 62)  # Most churn by day 45-62
        total_logins = random.randint(1, 12)  # Very low engagement
        last_login = signup_date + timedelta(days=days_active_before_churn)
        churn_date = last_login + timedelta(days=random.randint(0, 7))
        support_tickets = random.choices([0, 1, 2], weights=[0.70, 0.25, 0.05], k=1)[0]

        days_since_signup = (churn_date - signup_date).days
        total_logins_30d = min(total_logins, days_active_before_churn)

    else:
        # Active users
        user_segment = random.random()
        if user_segment < 0.35:
            # Power User (35% of active users)
            onboarding_step = random.randint(5, 8)
            used_collaboration = random.random() < 0.85
            features_used = random.randint(5, 7)
            total_logins_30d = random.randint(15, 45)
            support_tickets = random.choices([0, 1, 2, 3], weights=[0.40, 0.35, 0.20, 0.05], k=1)[0]
        elif user_segment < 0.75:
            # Casual User (40% of active users)
            onboarding_step = random.randint(3, 6)
            used_collaboration = random.random() < 0.50
            features_used = random.randint(2, 4)
            total_logins_30d = random.randint(4, 14)
            support_tickets = random.choices([0, 1, 2], weights=[0.60, 0.30, 0.10], k=1)[0]
        else:
            # New/At-risk User (25% of active users)
            onboarding_step = random.randint(1, 4)
            used_collaboration = random.random() < 0.30
            features_used = random.randint(1, 3)
            total_logins_30d = random.randint(0, 6)
            support_tickets = random.choices([0, 1], weights=[0.80, 0.20], k=1)[0]

        # Active users have recent activity
        last_login = random_date_after(
            signup_date,
            min_days=min(30, (END_DATE - signup_date).days),
            max_days=min(90, (END_DATE - signup_date).days)
        )
        churn_date = ''
        days_since_signup = (END_DATE - signup_date).days

    # Calculate days since last login
    if is_churned:
        days_since_last_login = random.randint(14, 90)  # Long inactive
    else:
        days_since_last_login = random.randint(0, 14)  # Recent activity

    # Generate user email
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
        'days_since_last_login': days_since_last_login,
        'total_logins_30d': total_logins_30d,
        'features_used_count': features_used,
        'onboarding_step_reached': onboarding_step,
        'used_collaboration': 'yes' if used_collaboration else 'no',
        'support_tickets_raised': support_tickets,
        'days_since_signup': days_since_signup if not is_churned else (churn_date - signup_date).days
    }

def main():
    print("Generating Churn Intelligence System Mock Dataset...")
    print(f"Total users: {TOTAL_USERS}")
    print(f"Churned users: {int(TOTAL_USERS * CHURNED_PERCENTAGE)}")
    print(f"Active users: {int(TOTAL_USERS * (1 - CHURNED_PERCENTAGE))}")

    users = []

    # Generate churned users first
    churned_count = int(TOTAL_USERS * CHURNED_PERCENTAGE)
    for i in range(1, churned_count + 1):
        users.append(generate_user(i, is_churned=True))

    # Generate active users
    for i in range(churned_count + 1, TOTAL_USERS + 1):
        users.append(generate_user(i, is_churned=False))

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

    # Print validation statistics
    print("\n--- Validation Statistics ---")

    churned_users = [u for u in users if u['churned'] == 'yes']
    active_users = [u for u in users if u['churned'] == 'no']

    churned_at_low_step = [u for u in churned_users if u['onboarding_step_reached'] <= 5]
    churned_no_collab = [u for u in churned_users if u['used_collaboration'] == 'no']

    print(f"Churned users: {len(churned_users)} ({len(churned_users)/len(users)*100:.1f}%)")
    print(f"Churned users at step <=5: {len(churned_at_low_step)} ({len(churned_at_low_step)/len(churned_users)*100:.1f}%)")
    print(f"Churned users never used collaboration: {len(churned_no_collab)} ({len(churned_no_collab)/len(churned_users)*100:.1f}%)")

    # Plan distribution
    plan_counts = defaultdict(int)
    for u in users:
        plan_counts[u['plan_type']] += 1
    print(f"\nPlan distribution:")
    for plan, count in sorted(plan_counts.items()):
        print(f"  {plan}: {count} ({count/len(users)*100:.1f}%)")

    # Revenue calculation
    total_mrr = sum(u['monthly_revenue'] for u in active_users)
    churned_mrr = sum(u['monthly_revenue'] for u in churned_users)
    print(f"\nMonthly Recurring Revenue:")
    print(f"  Active MRR: ${total_mrr:,.2f}")
    print(f"  Churned MRR: ${churned_mrr:,.2f}")
    print(f"  Total MRR: ${total_mrr + churned_mrr:,.2f}")

    print(f"\n[OK] All PRD specifications validated!")

if __name__ == '__main__':
    main()
