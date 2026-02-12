# Business Requirements Document (BRD)
## In-App Retention Nudge System

---

| Document Information | Details |
|---------------------|---------|
| **Project Name** | Churn Intelligence System |
| **Document Title** | In-App Retention Nudge System — BRD |
| **Version** | 1.0 |
| **Date** | February 2026 |
| **Author** | Business Analyst |
| **Status** | Draft — Ready for Stakeholder Review |
| **Document Owner** | Product Team |
| **Target Audience** | Engineering, Product, Customer Success, Executive Team |

---

## Document Revision History

| Version | Date | Author | Changes Made |
|---------|------|--------|--------------|
| 1.0 | Feb 2026 | Business Analyst | Initial BRD creation |
| | | | |

---

## 1. Executive Summary

### 1.1 Business Problem

TeamFlow currently loses **28% of paying users within the first 90 days**. The majority of this churn is preventable:

- **42% of churned users** cite "too complex" as their reason for leaving
- **70% of churned users** never completed onboarding beyond Step 5
- **80% of churned users** never used the collaboration feature

The root cause is clear: **Users are churning because they never reach the "aha moment," and we have no system to catch them before they leave.**

### 1.2 Proposed Solution

Build an **In-App Retention Nudge System** that:
1. Identifies at-risk users based on behavioral signals (login frequency, onboarding progress, feature usage)
2. Automatically delivers contextual nudges at the right moment
3. Enables Customer Success team to prioritize high-value human outreach
4. Provides real-time visibility into retention health via admin dashboard

### 1.3 Business Impact

| Metric | Current State | Target (3 Months) | Target (6 Months) |
|--------|--------------|-------------------|-------------------|
| 90-day churn rate | 28% | 20% | 15% |
| Onboarding completion (Step 6+) | 28% | 50% | 65% |
| Collaboration adoption (Day 10) | 35% | 55% | 70% |
| MRR at risk | $14,800 | $9,000 | $5,500 |
| **Revenue Recovered** | — | **$5,800/mo** | **$9,300/mo** |

**ROI**: $15,000 engineering investment → $69,600 annual revenue recovered = **364% ROI in Year 1**

### 1.4 Scope Overview

**In Scope:**
- Behavioral scoring engine (5-signal risk model)
- 3 automated nudge variants (Onboarding Resume, Feature Discovery, Re-engagement)
- Admin retention dashboard for CS team
- Nudge delivery tracking and conversion analytics
- Dismissal preferences (respect user choice)

**Out of Scope:**
- Machine learning / predictive modeling
- Email campaign automation
- CRM integrations (Salesforce, HubSpot)
- Mobile app updates (Phase 2)

---

## 2. Business Objectives

### 2.1 Primary Objectives (SMART Goals)

| ID | Objective | Success Metric | Target | Measurement Method |
|----|-----------|----------------|--------|-------------------|
| BO-1 | Reduce 90-day churn rate | Churn rate % | ≤20% in 90 days | SQL query on users table |
| BO-2 | Increase onboarding completion | Step 6+ completion % | ≥50% in 90 days | Funnel analysis query |
| BO-3 | Recover at-risk users | Amber → Green conversion % | ≥25% in 90 days | Intervention tracker |
| BO-4 | Reduce MRR at risk | Monthly MRR at risk | ≤$9,000 in 90 days | Risk score aggregation |
| BO-5 | Enable CS team efficiency | Response time to Red-tier | ≤24 hours | Intervention tracker |

### 2.2 Secondary Objectives

| ID | Objective | Description |
|----|-----------|-------------|
| BO-6 | Improve user sentiment | Reduce "too complex" complaints in exit surveys by 50% |
| BO-7 | Increase feature adoption | Average features per user from 3.2 to 4.5 |
| BO-8 | Validate signals | Confirm 5-signal model predicts churn with ≥80% accuracy |

---

## 3. Functional Requirements

### 3.1 Risk Scoring Engine

| ID | Requirement | Description | Priority |
|----|-------------|-------------|----------|
| **FR-001** | Calculate Churn Risk Score | System shall calculate a risk score (0-100) for each active user based on 5 behavioral signals | P0 |
| **FR-001.1** | Login Frequency Signal | Add 25 points if user has <2 logins in last 30 days | P0 |
| **FR-001.2** | Onboarding Progress Signal | Add 20 points if user is stuck at Step 3 or below | P0 |
| **FR-001.3** | Feature Breadth Signal | Add 20 points if user is using only 1-2 features | P0 |
| **FR-001.4** | Collaboration Signal | Add 20 points if user has never used collaboration feature in first 10 days | P0 |
| **FR-001.5** | Inactivity Signal | Add 15 points if user has been inactive for 7+ days | P0 |
| **FR-002** | Classify Risk Tier | System shall classify users into tiers based on score: Green (0-30), Amber (31-60), Red (61-100) | P0 |
| **FR-003** | Identify Primary Risk Factor | System shall identify the single highest-contributing signal for each at-risk user | P1 |
| **FR-004** | Recalculate Scores Daily | Risk scores shall be recalculated once every 24 hours for all active users | P0 |
| **FR-005** | Exclude Power Users | System shall exclude users from nudge targeting if they meet ALL criteria: 25+ logins/month, 6+ features, collaboration=yes | P1 |

### 3.2 Nudge Delivery System

| ID | Requirement | Description | Priority |
|----|-------------|-------------|----------|
| **FR-006** | Trigger Nudge on Tier Change | System shall automatically trigger appropriate nudge when user's risk tier changes from Green to Amber or Red | P0 |
| **FR-006.1** | Nudge Type A — Onboarding Resume | Deliver onboarding resume nudge when user stuck at Step ≤3 for 5+ days | P0 |
| **FR-006.2** | Nudge Type B — Feature Discovery | Deliver feature discovery nudge when user using 1-2 features for 14+ days | P0 |
| **FR-006.3** | Nudge Type C — Re-engagement | Deliver re-engagement nudge when user inactive for 7+ days | P0 |
| **FR-007** | Respect User Dismissal Preferences | System shall not show same nudge type to same user for 30 days after dismissal | P0 |
| **FR-008** | Limit Nudge Frequency | System shall not show more than 1 nudge per user per 7-day period | P0 |
| **FR-009** | Never Nudge Power Users | System shall never display nudges to users classified as Green tier | P0 |
| **FR-010** | Track Nudge Delivery | System shall log all nudge events: user_id, nudge_type, timestamp, status (sent/opened/responded) | P0 |

### 3.3 Admin Dashboard

| ID | Requirement | Description | Priority |
|----|-------------|-------------|----------|
| **FR-011** | Display Risk Tier Distribution | Dashboard shall show donut chart of Green/Amber/Red user counts | P0 |
| **FR-012** | List At-Risk Users | Dashboard shall list all Amber and Red users sorted by risk score (descending), then by revenue (descending) | P0 |
| **FR-013** | Show User Risk Details | Dashboard shall display per-user: risk score, tier, primary risk factor, recommended action | P0 |
| **FR-014** | Display Nudge Performance Metrics | Dashboard shall show: nudges sent, open rate, response rate, conversion rate | P0 |
| **FR-015** | Show MRR at Risk | Dashboard shall calculate and display monthly recurring revenue for all Amber + Red users | P0 |
| **FR-016** | Filter and Sort | Dashboard shall allow filtering by: risk tier, plan type, date range; sorting by: score, revenue, date | P1 |
| **FR-017** | Export User List | Dashboard shall allow export of at-risk user list to CSV format | P1 |
| **FR-018** | Manual Intervention Log | Dashboard shall allow CS team to log manual outreach actions and status updates | P1 |

### 3.4 Data & Integration

| ID | Requirement | Description | Priority |
|----|-------------|-------------|----------|
| **FR-019** | User Behavior Data Access | System shall read user data from `users` table: login counts, onboarding progress, feature usage flags | P0 |
| **FR-020** | Write Nudge Events | System shall write nudge delivery events to `nudge_events` table | P0 |
| **FR-021** | Update User Scores | System shall write calculated risk scores to `user_risk_scores` table daily | P0 |
| **FR-022** | Real-Time Risk Lookup | Admin dashboard shall query risk scores from `user_risk_scores` table with <500ms response time | P0 |

---

## 4. Non-Functional Requirements

### 4.1 Performance

| ID | Requirement | Description | Priority |
|----|-------------|-------------|----------|
| **NFR-001** | Score Calculation Time | Daily batch job for 300 users must complete within 5 minutes | P0 |
| **NFR-002** | Dashboard Load Time | Admin dashboard must load within 2 seconds on standard connection | P0 |
| **NFR-003** | Nudge Display Latency | Nudges must display within 500ms of page load for targeted users | P0 |
| **NFR-004** | API Response Time | Risk score lookup API must respond within 500ms for single user query | P1 |

### 4.2 Usability

| ID | Requirement | Description | Priority |
|----|-------------|-------------|----------|
| **NFR-005** | Non-Intrusive Design | Nudges must be dismissible, non-modal (except onboarding resume), and not block core workflows | P0 |
| **NFR-006** | Clear CTAs | All nudges must have single, clear call-to-action button | P0 |
| **NFR-007** | Mobile Responsive | Nudges and dashboard must be fully functional on mobile devices (≥375px width) | P0 |
| **NFR-008** | Accessibility | Nudges must meet WCAG 2.1 AA standards: keyboard navigation, screen reader support, color contrast | P1 |

### 4.3 Reliability

| ID | Requirement | Description | Priority |
|----|-------------|-------------|----------|
| **NFR-009** | Uptime | Nudge delivery system must maintain 99.5% uptime during business hours | P0 |
| **NFR-010** | Data Accuracy | Risk scores must be 100% accurate based on defined calculation rules | P0 |
| **NFR-011** | No Duplicate Nudges | System shall never deliver duplicate nudge type to same user within 30-day exclusion period | P0 |

### 4.4 Security

| ID | Requirement | Description | Priority |
|----|-------------|-------------|----------|
| **NFR-012** | Access Control | Admin dashboard shall be accessible only to users with `admin` or `customer_success` role | P0 |
| **NFR-013** | Data Privacy | Nudge events shall not contain PII beyond user_id | P0 |
| **NFR-014** | Audit Logging | All admin dashboard actions (user views, exports, interventions) must be logged with timestamp and actor | P1 |

### 4.5 Scalability

| ID | Requirement | Description | Priority |
|----|-------------|-------------|----------|
| **NFR-015** | User Base Growth | System must support 10x user growth (300 → 3,000 users) without architecture changes | P1 |
| **NFR-016** | Nudge Volume | System must support delivery of up to 1,000 nudges per day | P1 |

---

## 5. User Stories

### User Story 1: At-Risk User — Contextual Nudge

**As an** at-risk user (Rohan, casual freelancer),
**I want** a contextual prompt at the right moment,
**So that** I can rediscover product value without feeling spammed.

**Acceptance Criteria:**
- [ ] System detects user is stuck at Step 3 for 5+ days
- [ ] Nudge displays on next login after trigger condition is met
- [ ] Nudge is contextual (references user's name, current step, and next action)
- [ ] Nudge is dismissible with single click
- [ ] After dismissal, same nudge type does not reappear for 30 days
- [ ] Nudge copy is clear, concise (<20 words), and action-oriented
- [ ] CTA button navigates directly to relevant feature/page

**Definition of Done:**
- Nudge designed, implemented, and tested
- Dismissal preference stored in database
- A/B test variant created (optional enhancement)

---

### User Story 2: Power User — No Nudges (Negative Story)

**As a** power user (Maya, daily active, 7 features),
**I do NOT want** retention nudges,
**So that** my workflow is uninterrupted and I'm not annoyed.

**Acceptance Criteria:**
- [ ] System classifies user as Green tier (score ≤30)
- [ ] NO nudges of any type are displayed to Green-tier users
- [ ] User never sees "You're almost there!" or "It's been a while" messages
- [ ] User can still access help content if they choose (not nudged)
- [ ] If user's behavior changes and score increases to Amber, THEN nudges may appear

**Definition of Done:**
- Power user exclusion logic implemented
- Tested with power user test accounts
- Dashboard verifies no nudge events for Green-tier users

---

### User Story 3: Product Manager — Nudge Performance Analytics

**As a** Product Manager,
**I want** to see which nudge type converts best,
**So that** I can invest in the highest-ROI intervention.

**Acceptance Criteria:**
- [ ] Dashboard displays nudge performance metrics by type:
  - Nudges sent (count)
  - Open rate (%)
  - Response rate (%)
  - Conversion rate (% — Amber → Green within 30 days)
- [ ] Metrics are filterable by date range (this week, this month, last 90 days)
- [ ] Metrics are exportable to CSV
- [ ] Dashboard shows trend line for conversion rate over time
- [ ] Comparison view allows comparing Nudge Type A vs Type B vs Type C

**Definition of Done:**
- Nudge events table populated with delivery/open/response data
- Dashboard aggregates and displays metrics correctly
- Tested with sample data

---

### User Story 4: Co-founder — Weekly At-Risk User Digest

**As a** Co-founder / CEO,
**I want** a weekly digest of at-risk users,
**So that** I can personally reach out to high-value accounts in danger of churning.

**Acceptance Criteria:**
- [ ] System generates weekly email report every Monday at 9am
- [ ] Report includes:
  - Top 10 at-risk users (Red tier)
  - Each user's: email, plan, monthly revenue, risk score, primary risk factor
  - Total MRR at risk
  - Previous week's intervention outcomes
- [ ] Report is sent to configured email list (CEO, Head of Product, CS Lead)
- [ ] Report is actionable: includes "Recommended Action" for each user
- [ ] Optional: Report available as in-app notification for admins

**Definition of Done:**
- Weekly email job scheduled and tested
- Report template designed and approved
- Admin preferences page allows email list configuration

---

### User Story 5: Customer Success Lead — Manual Override

**As a** Customer Success Lead,
**I want** to override the automated nudge system manually,
**So that** I can customize outreach for enterprise accounts or special cases.

**Acceptance Criteria:**
- [ ] Admin dashboard allows CS team to:
  - Manually assign specific nudge type to user (override automatic trigger)
  - Schedule nudge for future date/time
  - Cancel pending nudge
  - Log "Human Outreach Completed" status
- [ ] Manual overrides take precedence over automated triggers
- [ ] Override actions are logged in audit trail
- [ ] Dashboard displays "Auto" vs "Manual" flag for nudge source

**Definition of Done:**
- Manual intervention UI implemented in dashboard
- Database schema supports manual scheduling
- Tested with manual override scenarios

---

### User Story 6: End User — Dismiss Without Penalty

**As an** end user,
**I want** to dismiss a nudge without penalty,
**So that** I don't feel pressured or annoyed by the product.

**Acceptance Criteria:**
- [ ] All nudges have visible dismiss button (× icon or "Dismiss" text)
- [ ] Dismissing a nudge does NOT:
  - Increase risk score
  - Trigger follow-up email
  - Affect product functionality
  - Show "Are you sure?" confirmation (no friction)
- [ ] Dismissal preference is stored for 30 days
- [ ] After 30 days, same nudge type may appear again (but not guaranteed)
- [ ] User can re-enable nudges via Settings page (optional enhancement)

**Definition of Done:**
- Dismissal action implemented across all nudge types
- Dismissal preference stored with 30-day TTL
- Tested: dismiss → wait 31 days → login → verify nudge can reappear

---

## 6. Process Flows

### 6.1 Nudge Trigger Logic Flow

```
START: Daily Score Calculation Job (runs 2am daily)
  │
  ├─ For each active user (churned = 'no'):
  │   │
  │   ├─ Calculate risk score (5 signals)
  │   ├─ Determine risk tier (Green/Amber/Red)
  │   ├─ Store in user_risk_scores table
  │   └─ Compare to previous tier
  │       │
  │       ├─ IF tier changed to Amber OR Red:
  │       │   │
  │       │   ├─ Check nudge history (last 30 days)
  │       │   ├─ IF same nudge type sent in last 30 days:
  │       │   │   └─ SKIP (respect exclusion period)
  │       │   │
  │       │   └─ ELSE (no recent nudge):
  │       │       │
  │       │       ├─ Determine nudge type:
  │       │       │   ├─ IF onboarding_step <= 3:
  │       │       │   │   └─ Nudge Type A (Onboarding Resume)
  │       │       │   ├─ ELIF features_used <= 2 AND days_since_signup >= 14:
  │       │       │   │   └─ Nudge Type B (Feature Discovery)
  │       │       │   └─ ELSE:
  │       │       │       └─ Nudge Type C (Re-engagement)
  │       │       │
  │       │       ├─ Create nudge event (status = 'pending')
  │       │       └─ Schedule for next user login
  │       │
  │       └─ ELSE (tier unchanged or Green):
  │           └─ No action
  │
  └─ END: Wait 24 hours until next run

USER LOGIN EVENT (real-time)
  │
  ├─ Check for pending nudges for this user
  ├─ IF pending nudge exists:
  │   ├─ Display nudge in UI
  │   ├─ Update nudge event status = 'sent'
  │   └─ Start tracking open/response
  │
  └─ ELSE:
      └─ No nudge displayed
```

### 6.2 Admin Dashboard User Journey

```
CS Lead Logs In → Access Admin Dashboard
  │
  ├─ View: Risk Tier Distribution (donut chart)
  ├─ View: Top At-Risk Users (sorted table)
  │
  ├─ FOR each Red-tier user:
  │   ├─ Review primary risk factor
  │   ├─ Review monthly revenue (prioritize high-value)
  │   ├─ Click "Outreach" action
  │   ├─ Log intervention type (email, call, in-app)
  │   └─ Set follow-up reminder (7 days)
  │
  ├─ FOR each Amber-tier user:
  │   ├─ Verify automatic nudge was sent
  │   ├─ Monitor for response (wait 7 days)
  │   └─ IF no response → Escalate to manual outreach
  │
  ├─ Weekly Review (every Friday):
  │   ├─ Export conversion metrics
  │   ├─ Identify underperforming nudges
  │   └─ A/B test new copy if conversion < 20%
  │
  └─ Monthly Review (last day of month):
      ├─ Calculate MRR recovered (converted users × revenue)
      ├─ Compare to previous month
      └─ Report to executive team
```

### 6.3 Data Flow Diagram

```
[users table] ← (existing data source)
    │
    │ Daily batch job reads:
    │ - total_logins_30d
    │ - onboarding_step_reached
    │ - features_used_count
    │ - used_collaboration
    │ - days_since_last_login
    │
    ▼
[Risk Score Calculator] (NEW component)
    │
    │ Calculates:
    │ - risk_score (0-100)
    │ - risk_tier (Green/Amber/Red)
    │ - primary_risk_factor
    │
    ├─→ [user_risk_scores table] (NEW table)
    │       │
    │       └─ Queried by: Admin Dashboard
    │
    └─→ [Nudge Trigger Engine] (NEW component)
            │
            │ Checks:
            │ - Tier change (Green → Amber/Red)
            │ - Nudge history (30-day exclusion)
            │ - User eligibility (not power user)
            │
            └─→ [nudge_events table] (NEW table)
                    │
                    │ Stores:
                    │ - user_id
                    │ - nudge_type
                    │ - status (pending/sent/opened/responded/converted)
                    │ - sent_at
                    │ - opened_at
                    │ - responded_at
                    │
                    ├─→ [Frontend Nudge Display] (NEW UI)
                    │       │
                    │       └─ Displays nudge to user on login
                    │
                    └─→ [Admin Dashboard] (NEW UI)
                            │
                            └─ Shows: Nudge performance metrics
```

---

## 7. Data Model

### 7.1 New Tables

#### Table: `user_risk_scores`

| Column | Type | Description | Notes |
|--------|------|-------------|-------|
| `id` | INT | Primary key | Auto-increment |
| `user_id` | INT | Foreign key to users table | |
| `risk_score` | INT | Calculated score (0-100) | |
| `risk_tier` | VARCHAR(10) | Green/Amber/Red | |
| `primary_risk_factor` | VARCHAR(50) | Highest contributing signal | e.g., "Onboarding Stalled" |
| `score_calculated_at` | TIMESTAMP | When score was last calculated | |
| `previous_tier` | VARCHAR(10) | Previous tier (for change detection) | |
| `created_at` | TIMESTAMP | Row creation timestamp | |
| `updated_at` | TIMESTAMP | Row last update timestamp | |

**Indexes:**
- Primary key: `id`
- Unique index: `user_id`
- Index for queries: `risk_tier`, `risk_score` (DESC)

---

#### Table: `nudge_events`

| Column | Type | Description | Notes |
|--------|------|-------------|-------|
| `id` | INT | Primary key | Auto-increment |
| `user_id` | INT | Foreign key to users table | |
| `nudge_type` | VARCHAR(50) | Type of nudge | Onboarding Resume, Feature Discovery, Re-engagement |
| `trigger_reason` | VARCHAR(100) | Why nudge was triggered | e.g., "Tier change Green→Amber" |
| `status` | VARCHAR(20) | Current state | pending, sent, opened, responded, converted, dismissed |
| `is_manual` | BOOLEAN | Was this manually scheduled? | Default: FALSE |
| `scheduled_for` | TIMESTAMP | When to send nudge | For manual scheduling |
| `sent_at` | TIMESTAMP | When nudge was displayed | NULL until sent |
| `opened_at` | TIMESTAMP | When user clicked/viewed nudge | NULL until opened |
| `responded_at` | TIMESTAMP | When user took CTA action | NULL until response |
| `converted_at` | TIMESTAMP | When user moved to Green tier | NULL until conversion |
| `dismissed_at` | TIMESTAMP | When user dismissed nudge | NULL until dismissed |
| `created_by` | INT | Admin user ID (if manual) | NULL for automatic |
| `created_at` | TIMESTAMP | Row creation timestamp | |
| `updated_at` | TIMESTAMP | Row last update timestamp | |

**Indexes:**
- Primary key: `id`
- Index for queries: `user_id`, `status`, `sent_at`
- Composite index: `(user_id, status, sent_at)`

---

#### Table: `intervention_logs` (Optional Enhancement)

| Column | Type | Description | Notes |
|--------|------|-------------|-------|
| `id` | INT | Primary key | |
| `user_id` | INT | Foreign key to users table | |
| `intervention_type` | VARCHAR(50) | Type of outreach | Email, Phone, In-app, Video call |
| `performed_by` | INT | Admin/CS user ID | Foreign key to users table |
| `notes` | TEXT | Free-form notes | |
| `follow_up_date` | DATE | When to check back | Optional |
| `outcome` | VARCHAR(50) | Result | Converted, Still at-risk, Churned |
| `created_at` | TIMESTAMP | Timestamp | |

---

### 7.2 Modified Tables

#### Table: `users` (existing — no changes required)

This table already contains all required fields for risk calculation:
- `total_logins_30d`
- `onboarding_step_reached`
- `features_used_count`
- `used_collaboration`
- `days_since_last_login`
- `monthly_revenue`

No schema changes required.

---

## 8. Assumptions

### 8.1 Business Assumptions

| ID | Assumption | Impact if False |
|----|------------|----------------|
| A-1 | 5-signal risk model accurately predicts churn with ≥70% accuracy | May need to add/remove signals after validation |
| A-2 | Users will respond positively to contextual nudges (≥20% open rate) | Nudge fatigue may require frequency adjustments |
| A-3 | 30-day nudge exclusion period prevents user annoyance | Users may still perceive nudges as spam |
| A-4 | Engineering team can deliver within 2-week sprint | Timeline may extend; business case may weaken |
| A-5 | Churn is primarily due to lack of product understanding, not product fit | Solution will not work if product-market fit issue |

### 8.2 Technical Assumptions

| ID | Assumption | Impact if False |
|----|------------|----------------|
| A-6 | Users table data is accurate and up-to-date | Risk scores will be incorrect |
| A-7 | Frontend can support real-time nudge display (not page refresh required) | Nudges may appear delayed, reducing effectiveness |
| A-8 | Admin dashboard queries execute in <2 seconds for 300-user dataset | User experience may be unacceptable; pagination required |
| A-9 | Daily batch job can complete within 5 minutes for 300 users | May need to optimize or increase job frequency |
| A-10 | No existing nudge system conflicts with this implementation | May cause duplicate nudges or race conditions |

### 8.3 Data Assumptions

| ID | Assumption | Impact if False |
|----|------------|----------------|
| A-11 | `last_login_date` is updated correctly on every user session | Inactivity signal will be inaccurate |
| A-12 | `onboarding_step_reached` reflects highest step completed | Onboarding signal will be inaccurate |
| A-13 | `used_collaboration` flag is set when user performs any collaboration action | Collaboration signal will miss users |
| A-14 | User activity data is available within 24 hours of action | Risk scores will be stale |

---

## 9. Dependencies

### 9.1 Internal Dependencies

| Dependency | Owner | Required By | Status |
|------------|-------|-------------|--------|
| Product approval of nudge copy | Product Manager | Sprint Start | Pending |
| UI design approval | Designer | Sprint Start | Pending |
| `users` table access | Engineering | Day 1 | Available |
| Frontend dev capacity | Engineering Lead | Sprint Start | Available |
| QA testing resources | QA Lead | Week 2 | Available |

### 9.2 External Dependencies

| Dependency | Owner | Required By | Status |
|------------|-------|-------------|--------|
| Email service for weekly digest (optional) | DevOps | Week 2 | Available (SendGrid/Mailgun) |
| Analytics dashboard platform (optional) | Data Team | Month 2 | Not required for MVP |

### 9.3 Blocking Dependencies

- **None identified** — all requirements can be met with existing infrastructure

---

## 10. Constraints

### 10.1 Technical Constraints

| ID | Constraint | Description |
|----|------------|-------------|
| C-1 | No machine learning | Risk scoring must use rule-based logic only |
| C-2 | Single database | No additional database infrastructure |
| C-3 | Batch processing only | Real-time score calculation not available |
| C-4 | No CRM integration | Manual export required for Salesforce/HubSpot sync |

### 10.2 Business Constraints

| ID | Constraint | Description |
|----|------------|-------------|
| C-5 | Sprint timeline | Feature must be delivered in 2-week sprint |
| C-6 | No additional hiring | Must be built by existing team |
| C-7 | Budget cap | Engineering investment ≤$15,000 (approximately 80 hours) |
| C-8 | CEO approval required | Feature cannot launch without executive sign-off |

### 10.3 User Experience Constraints

| ID | Constraint | Description |
|----|------------|-------------|
| C-9 | Non-modal only | Nudges must NOT block user workflows (except onboarding resume) |
| C-10 | Single CTA | Each nudge may have only one primary action button |
| C-11 | Character limits | Nudge copy ≤140 characters (to prevent TL;DR) |

---

## 11. Out of Scope Items

The following are explicitly **OUT OF SCOPE** for Phase 1:

| Item | Reason | Future Phase |
|------|--------|--------------|
| Machine learning churn prediction | Requires data science team; MVP uses rule-based scoring | Phase 3 |
| Email campaign automation | Not in current tech stack; requires ESP integration | Phase 2 |
| Mobile app nudges | Mobile app updates require separate release | Phase 2 |
| Slack/Teams integration for admin alerts | Not prioritized for MVP | Phase 2 |
| A/B testing framework | Manual variant switching for MVP | Phase 2 |
| Internationalization | Nudges in English only for MVP | Phase 3 |
| Advanced analytics (cohort analysis) | Excel-based analysis for MVP | Phase 2 |
| Self-serve nudge customization | Admin-managed only for MVP | Phase 3 |

---

## 12. Risk Register

| ID | Risk | Probability | Impact | Mitigation Strategy | Owner |
|----|------|-------------|--------|-------------------|--------|
| R-1 | Nudge open rate < 15% | Medium | High | A/B test copy variants; adjust frequency | Product Manager |
| R-2 | Power users complain about nudges | Low | Medium | Strict Green-tier exclusion; no false positives | Engineering |
| R-3 | Risk scores don't predict churn accurately | Medium | High | Validate with historical data; iterate signals | Business Analyst |
| R-4 | Engineering overruns 2-week sprint | Medium | Medium | Reduce scope to Type A nudges only; defer dashboard | Engineering Lead |
| R-5 | Users dismiss all nudges (nudge blindness) | Medium | High | Implement 30-day exclusion; limit frequency | Product Manager |
| R-6 | Data quality issues in users table | Low | High | Data validation checks before rollout | Engineering |
| R-7 | CEO doesn't approve feature | Low | Critical | Strong business case; pilot with small cohort | Business Analyst |
| R-8 | Competitor launches similar feature | Low | Medium | Accelerate timeline; emphasize differentiation | Product Manager |

---

## 13. Success Criteria

### 13.1 Go-Live Criteria (MVP)

The feature is considered "live" when ALL of the following are met:

- [ ] All P0 functional requirements implemented and tested
- [ ] Risk score calculation accuracy validated against 100 historical users
- [ ] Nudge display tested across 3 user types (Power, Casual, Churned)
- [ ] Admin dashboard loads in <2 seconds with test data
- [ ] Dismissal preference storage verified (30-day exclusion)
- [ ] UAT signed off by Product Manager and CS Lead
- [ ] CEO approval obtained for production deployment

### 13.2 Post-Launch Success Metrics (90 Days)

| Metric | Baseline | Target (90 days) | Stretch (180 days) |
|--------|----------|------------------|-------------------|
| 90-day churn rate | 28% | ≤20% | ≤15% |
| Nudge open rate | — | ≥30% | ≥40% |
| Amber → Green conversion | — | ≥25% | ≥40% |
| MRR recovered | — | ≥$5,800/mo | ≥$9,300/mo |
| CS response time (Red tier) | — | ≤24 hours | ≤12 hours |
| User sentiment (exit surveys) | 42% "too complex" | ≤25% | ≤15% |

---

## 14. Appendix

### 14.1 Glossary

| Term | Definition |
|------|------------|
| **Aha Moment** | The point at which a user first realizes the core value of the product; for TeamFlow, this is completing the first automated workflow |
| **Amber Tier** | Medium-risk users (score 31-60); require automated nudge within 48 hours |
| **Churn** | User cancels subscription or stops paying |
| **Green Tier** | Low-risk users (score 0-30); healthy, monitor monthly |
| **MRR** | Monthly Recurring Revenue |
| **Nudge** | A contextual, non-intrusive prompt designed to guide user behavior |
| **Red Tier** | High-risk users (score 61-100); require human outreach within 24 hours |
| **Retention** | The opposite of churn; users who continue paying |
| **Risk Score** | A 0-100 point score indicating likelihood of churn; higher = riskier |

### 14.2 Reference Documents

| Document | Location | Owner |
|----------|----------|-------|
| PRD: Churn Intelligence System | `/PRD_Project2_Churn_Intelligence_System.md` | Business Analyst |
| Product Definition: TeamFlow | `/01_Product_Definition.md` | Business Analyst |
| SQL Analysis Queries | `/sql/01_onboarding_funnel_analysis.sql` | Business Analyst |
| User Personas & Empathy Maps | `/docs/02_User_Personas_Empathy_Maps.md` | Business Analyst |
| Excel Model Build Guide | `/excel/EXCEL_MODEL_BUILD_GUIDE.md` | Business Analyst |
| Figma Wireframe Specs | `/figma/FIGMA_WIREFRAME_SPECIFICATIONS.md` | Business Analyst |

### 14.3 Approval Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Product Manager | _______________ | ___________ | ___ |
| Engineering Lead | _______________ | ___________ | ___ |
| Customer Success Lead | _______________ | ___________ | ___ |
| CEO / Co-founder | _______________ | ___________ | ___ |
| Business Analyst | _______________ | ___________ | ___ |

---

**Document End**

*Next: Executive Brief → Final Portfolio Assembly*
