# Product Definition: TeamFlow
**SaaS Platform Context for Churn Intelligence System**

---

## Product Overview

**TeamFlow** is a B2B SaaS project management and team collaboration platform for small-to-medium businesses (SMBs) and freelance teams.

### Value Proposition
*"The only project management tool that actually shows your team what to work on next — without endless meetings."*

### Target Market
- **Primary:** SMBs with 5-50 employees
- **Secondary:** Freelance teams and agencies
- **Price Points:** $29/month (Basic), $79/month (Pro), $199/month (Team)

---

## Core Features (7 Features)

| # | Feature Name | Description | Why It Matters |
|---|--------------|-------------|----------------|
| 1 | **Task Boards** | Kanban-style boards with drag-drop cards | Visual workflow management |
| 2 | **Workflow Builder** | Custom automation rules (e.g., "Assign to X when status = Review") | Saves 3+ hours/week on manual coordination |
| 3 | **Team Huddles** (Collaboration Feature) | Async check-ins, @mentions, comment threads | Replaces standup meetings |
| 4 | **File Hub** | Centralized file storage with versioning | Single source of truth |
| 5 | **Time Tracking** | Built-in timer + timesheet reports | Billing and productivity insights |
| 6 | **Analytics Dashboard** | Project progress, team velocity, bottlenecks | Data-driven decisions |
| 7 | **Client Portal** | Branded client access to specific projects | Professional delivery experience |

---

## The "Aha Moment" Definition

### What is the Aha Moment?
**A user completes their first end-to-end workflow automation.**

Specifically: The user creates a custom Workflow Builder rule, assigns it to a task, and watches it automatically move through statuses without manual intervention.

### Why This is the Aha Moment
- Before: User manually assigns, notifies, and updates tasks (takes 5-10 minutes)
- After: Workflow runs automatically (takes 0 seconds)
- **Realization:** "Oh, this software just saved me hours every week. I'm never going back to Trello/Asana."

### When Does It Happen?
- **Day 15-21 average** for users who reach it
- Requires: Task Board + Workflow Builder + at least 1 Team Huddle interaction
- **Only 28% of users reach this moment** (the critical insight)

---

## User Journey Map (Day 0 → Day 90)

### Phase 1: First Login (Day 0)
```
User signs up → Welcome email sent → User logs in
|
→ Onboarding Checklist Shown (8 steps)
```

### Phase 2: Onboarding (Day 0-14)
| Step | Action | Completion Rate |
|------|--------|-----------------|
| Step 1 | Create first project | 100% (forced) |
| Step 2 | Invite team member | 85% |
| Step 3 | Create first task | 72% |
| Step 4 | **Use Team Huddles (@mention)** | 62% ← First "social" feature |
| Step 5 | Set up Workflow Builder rule | 41% ← MAJOR DROP-OFF |
| Step 6 | Assign workflow to task | 33% |
| Step 7 | Complete first automated workflow | 28% ← AHA MOMENT |
| Step 8 | Invite client to portal | 22% |

### Phase 3: Value Discovery (Day 15-30)
- Users who hit Aha Moment (Step 7) → 55% return next week
- Users who don't → 12% return next week
- **4.6x difference in retention**

### Phase 4: Habit Formation (Day 31-90)
- Power Users: Daily logins, 7+ features, invite teammates
- Casual Users: 2-3x weekly logins, 3 features, solo usage
- Churned Users: Activity drops to zero by Day 45

---

## Churn Intelligence Context

### Why Users Churn
| Reason | % of Churned Users | Root Cause |
|--------|-------------------|-------------|
| "Too complex" | 42% | Never reached Aha Moment |
| "Didn't have time to set up" | 28% | Onboarding too long |
| "Team didn't adopt it" | 18% | Collaboration feature never used |
| "Too expensive for value" | 12% | Never experienced time savings |

### The Silent Exit Pattern
```
Day 0-14:   Active login (daily or every 2-3 days)
Day 15-30:  Login frequency drops (every 5-7 days)
Day 31-45:  One final login (often to download data)
Day 45-62:  Complete silence
Day 62+:   Cancellation email arrives
```

**Most founders only see the cancellation on Day 62+. The signals were there all along.**

---

## Pricing & Revenue Model

| Plan | Price | Target User | Features Included |
|------|-------|-------------|-------------------|
| **Basic** | $29/month | Freelancers | Task Boards, File Hub, Time Tracking |
| **Pro** | $79/month | SMB teams | All Basic + Workflow Builder, Team Huddles |
| **Team** | $199/month | Agencies | All Pro + Analytics Dashboard, Client Portal |

### Revenue Distribution (Mock Dataset Assumptions)
- 60% Basic ($29)
- 30% Pro ($79)
- 10% Team ($199)

**Average Revenue Per User (ARPU): $59.50**

---

## Key Metrics for Churn Analysis

| Metric | Current State | Industry Benchmark |
|--------|---------------|-------------------|
| 90-day churn rate | 28% | 5-10% (mature SaaS) |
| Trial-to-paid conversion | 38% | 25-35% |
| Onboarding completion (Step 6+) | 28% | 50-60% |
| Collaboration feature adoption (Day 10) | 35% | 60%+ |
| MRR at risk (monthly) | $14,800 | — |

---

## Assumptions for Dataset Generation

1. **Signup Period:** July 2024 – December 2025 (18 months of user acquisition)
2. **Cohort Size:** ~16-17 new signups per month
3. **Churn Timeline:** Most churns occur between Day 45-90
4. **Seasonality:** Slight dip in December (holidays), spike in January (new year resolutions)
5. **Power User Definition:** 25+ logins in 30 days, 6+ features used
6. **Casual User Definition:** 4-8 logins in 30 days, 2-3 features used
7. **Churned User Definition:** 0-3 logins in 30 days before cancellation

---

*This product definition serves as the source of truth for all data generation, SQL analysis, and artifact creation in the Churn Intelligence System project.*
