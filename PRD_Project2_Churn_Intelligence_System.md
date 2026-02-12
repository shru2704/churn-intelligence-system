# PRD: Churn Intelligence System — BA-Driven Early Warning Framework for SaaS Startups
**Document Type:** Product Requirements Document (PRD)  
**Prepared by:** Shruti, Business Analyst  
**Version:** 1.0  
**Date:** February 2026  
**Domain:** SaaS Startup — Product & Revenue Retention

---

## 1. Project Overview

### 1.1 Background
Early-stage SaaS startups live and die by retention. Yet most founding teams only discover a user has churned after they've already cancelled — when it's too late to intervene. The signals were always there: declining login frequency, unused features, unanswered in-app prompts. No one was watching.

This project builds a BA-driven churn early warning framework from scratch — combining behavioral data analysis, stakeholder pain mapping, and a product fix roadmap that a founding team can understand, afford, and act on. No data science team required.

### 1.2 Problem Statement
> *"Early-stage SaaS startups lose 20–30% of their paying users within the first 90 days — not because the product is bad, but because no one is watching the right signals. This project builds a BA-driven churn early warning framework from scratch, combining behavioral data analysis, stakeholder pain mapping, and a product fix roadmap — the kind of work a founding team would actually pay for."*

### 1.3 Project Goals
- Identify the behavioral signals that predict churn 2–4 weeks before it happens
- Build a simple, non-technical churn scoring model any founder can maintain in Excel
- Map the onboarding funnel drop-off points using SQL analysis
- Design a product intervention (in-app retention nudge) using Figma wireframes
- Deliver a one-page Executive Brief that drives a real product decision

---

## 2. Scope

### 2.1 In Scope
- Mock dataset of 300 users (active, at-risk, and churned) with behavioral attributes
- User persona development (3 personas: Power User, Casual User, Churned User)
- Empathy mapping from simulated stakeholder interviews
- SQL queries to analyze onboarding funnel drop-offs and usage patterns
- Excel-based churn scoring model with risk tiering (Green / Amber / Red)
- Figma wireframe of in-app retention nudge (smart tooltip intervention)
- One-page Executive Brief with 3 prioritized recommendations
- BRD for the in-app retention nudge feature

### 2.2 Out of Scope
- Machine learning or predictive modeling
- CRM integration or live data pipeline
- Email campaign design or execution
- Engineering sprint planning

---

## 3. User Persona Development

Build 3 detailed personas based on behavioral research. Each persona should feel like a real person, not a template.

### Persona 1 — The Power User (Maya, 31, Product Manager at a 20-person startup)
- Logs in daily, uses 7+ features, invites teammates
- Pays monthly, has been active for 6+ months
- Pain point: Wants deeper analytics and API access
- Churn risk: LOW — but at risk if a competitor offers better integrations
- What keeps her: Efficiency, depth, team collaboration features

### Persona 2 — The Casual User (Rohan, 27, Freelance Designer)
- Logs in 2–3x per week, uses 3 core features only
- Signed up after a free trial, paying monthly
- Pain point: Finds advanced features confusing, onboarding felt overwhelming
- Churn risk: MEDIUM — likely to churn at next billing cycle if not re-engaged
- What keeps him: Simplicity, visual output quality, price

### Persona 3 — The Churned User (Priya, 34, Operations Manager at an SME)
- Logged in frequently for first 2 weeks, then activity dropped to zero by Day 45
- Never completed onboarding checklist, never used core "aha feature"
- Cancelled on Day 62 — cited "too complex" in exit survey
- Pain point: Never reached the value moment — product didn't guide her there
- What she needed: A guided onboarding path, human check-in at Day 14

---

## 4. Stakeholder Map & Discovery

| Stakeholder | Role | Key Question |
|---|---|---|
| Co-founder / CEO | Strategy & revenue | "How much is churn actually costing us per month?" |
| Head of Product | Feature prioritization | "Which features do churned users never reach?" |
| Customer Success Lead | User relationships | "What are users saying before they leave?" |
| Growth / Marketing | Acquisition & retention overlap | "Are we attracting the wrong users?" |

### 4.1 Simulated Stakeholder Interview Findings

**CEO:** Knows churn is a problem but has no visibility into *when* a user is about to leave. Currently reacts after cancellation. Wants a "dashboard I can check every Monday morning."

**Head of Product:** Suspects the onboarding checklist (currently 8 steps) is too long. Has no data to confirm. Believes the "aha moment" (first successful workflow completion) happens too late in the journey — usually after Day 21, by which time 30% of users have already lost interest.

**Customer Success Lead:** Has been doing manual check-ins via email for high-value accounts only. Has a gut feeling that users who don't use the collaboration feature in the first 10 days almost always churn. No data to back this up — yet.

**Growth Lead:** Conversion from free trial to paid is strong (38%), but 90-day retention of newly converted users is only 71%. Suspects the product experience, not the acquisition channel, is the problem.

---

## 5. Current State Analysis (As-Is)

### 5.1 Onboarding Funnel (Current)
```
User Signs Up (Day 0)
      ↓
Welcome Email Sent
      ↓
User Logs In for First Time (Day 0–3) — 85% completion
      ↓
Onboarding Checklist Shown (8 steps)
      ↓
Step 1–3 Completed — 72% of users
      ↓
Step 4–6 Completed — 41% of users  ← MAJOR DROP-OFF
      ↓
Step 7–8 Completed ("Aha Moment") — 28% of users
      ↓
Returns next week — 55% of users who hit aha moment
                    12% of users who did not
```

### 5.2 Key Insight from Funnel
Users who do NOT complete onboarding Steps 4–6 (which include the core "aha" feature) are **4.6x more likely to churn within 90 days.** This is the single most important finding in the project.

### 5.3 Current Churn Signals (Not Being Tracked)
- Login frequency drop (from daily → weekly → gone)
- Feature usage narrowing (from 5+ features → 1–2 features)
- Onboarding checklist abandonment (stopped at step 3 or 4)
- Support ticket absence (at-risk users stop asking for help — they just leave)
- Collaboration feature non-use in first 10 days

---

## 6. Churn Scoring Model Design

### 6.1 Churn Risk Score — 5 Behavioral Signals

Build this as an Excel model. Each signal contributes points to a risk score. Higher score = higher churn risk.

| Signal | Condition | Points Added |
|---|---|---|
| Login Frequency | Less than 2 logins in last 14 days | +25 |
| Onboarding Progress | Stuck at Step 3 or below | +20 |
| Feature Breadth | Using only 1–2 features | +20 |
| Collaboration Feature | Never used in first 10 days | +20 |
| Days Since Last Activity | 7+ days of inactivity | +15 |

**Risk Tiers:**
- 🟢 **Green (0–30 points):** Healthy — monitor monthly
- 🟡 **Amber (31–60 points):** At-Risk — trigger retention nudge within 48 hours
- 🔴 **Red (61–100 points):** High Risk — human outreach required within 24 hours

### 6.2 Model Output
The Excel model should output:
- A risk score per user
- A risk tier (Green / Amber / Red)
- The top contributing signal for each at-risk user
- A weekly summary tab showing: total users per tier, trend over 4 weeks, projected churn if no action taken

---

## 7. SQL Analysis Queries

Run the following queries against the mock user behavioral dataset.

### Mock Dataset Schema
```sql
CREATE TABLE users (
  user_id INT,
  signup_date DATE,
  plan_type VARCHAR(20),  -- 'monthly' or 'annual'
  churned BOOLEAN,
  churn_date DATE,
  last_login DATE,
  total_logins_30d INT,
  features_used_count INT,
  onboarding_step_reached INT,  -- 1 to 8
  used_collaboration BOOLEAN,
  support_tickets_raised INT,
  days_since_signup INT
);
```

**Query 1 — Onboarding Funnel Drop-off Analysis:**
```sql
SELECT 
  onboarding_step_reached,
  COUNT(*) AS users_at_step,
  ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS pct_of_total,
  SUM(CASE WHEN churned = TRUE THEN 1 ELSE 0 END) AS churned_from_step,
  ROUND(100.0 * SUM(CASE WHEN churned = TRUE THEN 1 ELSE 0 END) / COUNT(*), 2) AS churn_rate_pct
FROM users
GROUP BY onboarding_step_reached
ORDER BY onboarding_step_reached;
```

**Query 2 — Churn Rate by Feature Usage Depth:**
```sql
SELECT 
  CASE 
    WHEN features_used_count <= 2 THEN 'Low (1-2 features)'
    WHEN features_used_count <= 5 THEN 'Medium (3-5 features)'
    ELSE 'High (6+ features)'
  END AS feature_usage_band,
  COUNT(*) AS total_users,
  SUM(CASE WHEN churned = TRUE THEN 1 ELSE 0 END) AS churned,
  ROUND(100.0 * SUM(CASE WHEN churned = TRUE THEN 1 ELSE 0 END) / COUNT(*), 2) AS churn_rate_pct
FROM users
GROUP BY feature_usage_band
ORDER BY churn_rate_pct DESC;
```

**Query 3 — Collaboration Feature Impact on Churn:**
```sql
SELECT 
  used_collaboration,
  COUNT(*) AS total_users,
  SUM(CASE WHEN churned = TRUE THEN 1 ELSE 0 END) AS churned,
  ROUND(100.0 * SUM(CASE WHEN churned = TRUE THEN 1 ELSE 0 END) / COUNT(*), 2) AS churn_rate_pct
FROM users
WHERE days_since_signup <= 10
GROUP BY used_collaboration;
```

**Query 4 — Monthly Churn Rate Trend:**
```sql
SELECT 
  DATE_FORMAT(churn_date, '%Y-%m') AS churn_month,
  COUNT(*) AS churned_users,
  ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM users WHERE churned = TRUE), 2) AS pct_of_total_churn
FROM users
WHERE churned = TRUE
GROUP BY churn_month
ORDER BY churn_month;
```

**Query 5 — Identify Current At-Risk Users (Amber + Red):**
```sql
SELECT 
  user_id,
  days_since_signup,
  total_logins_30d,
  onboarding_step_reached,
  features_used_count,
  used_collaboration,
  DATEDIFF(CURDATE(), last_login) AS days_inactive,
  -- Calculate risk score
  (CASE WHEN total_logins_30d < 2 THEN 25 ELSE 0 END +
   CASE WHEN onboarding_step_reached <= 3 THEN 20 ELSE 0 END +
   CASE WHEN features_used_count <= 2 THEN 20 ELSE 0 END +
   CASE WHEN used_collaboration = FALSE THEN 20 ELSE 0 END +
   CASE WHEN DATEDIFF(CURDATE(), last_login) >= 7 THEN 15 ELSE 0 END) AS churn_risk_score
FROM users
WHERE churned = FALSE
HAVING churn_risk_score >= 31
ORDER BY churn_risk_score DESC;
```

---

## 8. Proposed Solution — In-App Retention Nudge

### 8.1 Concept
A smart tooltip system that detects churn signals and intervenes before the user disengages. The nudge is triggered automatically when a user's churn score enters the Amber zone.

### 8.2 Nudge Types (3 variants)

**Nudge Type A — Onboarding Resume Prompt**
- Trigger: User stuck at Step 3 or below for 5+ days
- Message: "You're 2 steps away from unlocking [core feature]. Most users who complete this save 3 hours/week."
- CTA: "Continue Setup →"

**Nudge Type B — Feature Discovery Prompt**
- Trigger: User using only 1–2 features after 14+ days
- Message: "Teams like yours use [unused feature] to [specific benefit]. Want a 2-minute walkthrough?"
- CTA: "Show me →"

**Nudge Type C — Re-engagement Prompt**
- Trigger: 7+ days of inactivity
- Message: "Hey [name], it's been a week. Here's what's new — and a shortcut to where you left off."
- CTA: "Pick up where I left off →"

### 8.3 Figma Wireframe Screens to Design

**Screen 1:** Dashboard view — user sees a subtle banner nudge (not a modal popup)
- Top of screen, dismissible
- Icon + short message + CTA button

**Screen 2:** Onboarding checklist page — resume prompt overlay
- Progress bar showing current step
- "You're almost there" message with benefit statement
- Large CTA button

**Screen 3:** Admin view — Retention Dashboard
- Churn risk distribution pie chart (Green / Amber / Red)
- List of top 10 at-risk users with risk score and top signal
- Nudge delivery log (sent / opened / converted)
- Weekly retention trend line chart

---

## 9. Detailed Deliverables & Artifact Instructions

### 9.1 Deliverable 1: Mock Dataset (CSV)
Generate a CSV file with 300 rows representing users.

**Required columns:**
```
user_id, signup_date, plan_type, churned (yes/no), churn_date, 
last_login_date, total_logins_30d, features_used_count, 
onboarding_step_reached (1-8), used_collaboration (yes/no), 
support_tickets_raised, days_since_signup, monthly_revenue
```

**Data distribution rules:**
- 25% of users churned (75 users)
- Of churned users: 70% never reached onboarding Step 6 or beyond
- Of churned users: 80% never used the collaboration feature
- Monthly revenue per user: $29 (basic), $79 (pro), $199 (team)
- Date range: July 2024 – December 2025

### 9.2 Deliverable 2: Excel Churn Scoring Model
Build an Excel workbook with 4 tabs:

**Tab 1 — User Data:** Paste the mock CSV here

**Tab 2 — Churn Score Calculator:**
- Formula columns for each of the 5 risk signals
- Auto-calculated total risk score
- Conditional formatting: Green / Amber / Red tiers
- Top signal column (shows which factor contributes most)

**Tab 3 — Retention Dashboard:**
- Tier distribution chart (donut chart: Green / Amber / Red)
- Onboarding funnel visualization (bar chart showing drop-off by step)
- Feature usage vs. churn rate chart
- Monthly churn trend line

**Tab 4 — Intervention Tracker:**
- Log of at-risk users with assigned nudge type
- Status column: Nudge Sent / Responded / Converted / Churned
- Monthly conversion rate from at-risk → retained

### 9.3 Deliverable 3: Empathy Map (Document)
Create a 3-section empathy map (one per persona) covering:
- What they Say about the product
- What they Think but don't say
- What they Do (behavioral patterns)
- What they Feel during key moments
- Pain points and gains

### 9.4 Deliverable 4: Figma Wireframes
Design low-fidelity wireframes for:
- 3 nudge variants (as described in Section 8.2)
- Admin retention dashboard (as described in Section 8.3)
- Mobile-responsive nudge for app users

### 9.5 Deliverable 5: Business Requirements Document (BRD)
Full BRD for the In-App Retention Nudge System.

**Required sections:**
- Executive Summary
- Business Objectives and Success Metrics
- Functional Requirements (FR-001 through FR-010 minimum)
- Non-Functional Requirements
- User Stories (minimum 6) with Acceptance Criteria
- Process Flow: Nudge Trigger Logic
- Assumptions, Dependencies, and Constraints
- Out of Scope items

**Required User Stories:**
1. As an at-risk user, I want a contextual prompt at the right moment so that I rediscover value without feeling spammed
2. As a power user, I do NOT want nudges so that my workflow is uninterrupted (negative story — important for scope)
3. As a product manager, I want to see which nudge type converts best so that I can invest in the highest-ROI intervention
4. As a co-founder, I want a weekly digest of at-risk users so that I can personally reach out to high-value accounts
5. As a customer success lead, I want to override the nudge system manually so that I can customize outreach for enterprise accounts
6. As an end user, I want to dismiss a nudge without penalty so that I don't feel pressured

### 9.6 Deliverable 6: One-Page Executive Brief
A crisp, founder-ready summary document.

**Structure:**
- **The Problem:** 3 bullet stats from the data (churn rate, cost per churned user, % who never hit aha moment)
- **The Root Cause:** Single clear sentence — "Users are churning because they never reach the aha moment, and we have no system to catch them before they leave."
- **The Opportunity:** Monthly revenue at risk + monthly revenue recoverable if 30% of Amber-tier users are converted
- **The Recommendation:** 3 actions ranked by effort vs. impact (a 2x2 matrix)
- **The Ask:** Specific decision required from the CEO (approve nudge feature for next sprint)

---

## 10. Success Metrics & KPIs

| KPI | Current (Baseline) | Target (3 months) | Target (6 months) |
|---|---|---|---|
| 90-day churn rate | 28% | 20% | 15% |
| Onboarding completion rate (Step 6+) | 28% | 50% | 65% |
| Collaboration feature adoption (Day 10) | 35% | 55% | 70% |
| Amber-tier users converted to Green | Not tracked | 25% | 40% |
| Monthly Recurring Revenue at risk | $14,800 | $9,000 | $5,500 |

---

## 11. Timeline & Milestones

| Phase | Activity | Duration |
|---|---|---|
| Research | Persona development, empathy mapping, stakeholder interviews | Week 1 |
| Data Work | Mock dataset creation, SQL queries, pattern identification | Week 2 |
| Modeling | Excel churn scoring model, retention dashboard | Week 3 |
| Design | Figma wireframes for nudge system and admin dashboard | Week 4 |
| Documentation | BRD, Executive Brief, process flow diagrams | Week 5 |
| Review | Stakeholder walkthrough, final iteration | Week 6 |

---

## 12. Assumptions & Constraints

**Assumptions:**
- SaaS product is B2B, targeting SMEs and freelancers
- Monthly subscription model ($29 / $79 / $199 tiers)
- Team size is 8–12 people (no dedicated data analyst)
- The founding team can commit 1 sprint (2 weeks) to build the nudge feature

**Constraints:**
- No access to live data — all analysis on mock dataset
- Nudge system must be buildable without a data science team
- Executive Brief must fit on a single page — startup context demands brevity
- Figma wireframes are concept-level only, not a developer handoff spec

---

## 13. Tools Used

| Tool | Purpose |
|---|---|
| Excel | Churn scoring model, retention dashboard, intervention tracker |
| SQL (MySQL syntax) | Behavioral pattern analysis, at-risk user identification |
| Figma | Nudge wireframes, admin dashboard design |
| Word / Google Docs | BRD, Executive Brief, empathy maps |
| Draw.io / Lucidchart | Onboarding funnel visualization, nudge trigger flow |

---

## 14. Instructions for Claude (Build Prompt)

When using this PRD to build project artifacts, instruct Claude as follows:

> "You are helping me build a Business Analyst portfolio project called the Churn Intelligence System. Using the PRD provided, please build the following artifacts one at a time:
> 1. First, generate the mock CSV dataset (300 rows) based on Section 9.1 specifications — make the data feel realistic with proper distributions
> 2. Then write all 5 SQL queries from Section 7 with comments explaining the business insight each query reveals
> 3. Then build the Excel workbook (4 tabs) as described in Section 9.2 — include formulas, conditional formatting, and charts
> 4. Then write the full BRD document as described in Section 9.5, including all 6 user stories with detailed acceptance criteria
> 5. Finally, write the One-Page Executive Brief from Section 9.6 — make it punchy, data-driven, and startup-friendly
> Use real startup language throughout. Include specific numbers. The goal is a portfolio project that makes a startup interviewer think: 'This person actually understands our problems.'"

---

*End of PRD — Project 2*
