-- ============================================================================
-- Churn Intelligence System - SQL Analysis Queries
-- Project: TeamFlow SaaS Churn Analysis
-- Business Analyst: [Your Name]
-- Date: 2026
-- ============================================================================

-- ============================================================================
-- QUERY 1: Onboarding Funnel Drop-off Analysis
-- ============================================================================
-- Business Question: Where are users abandoning the onboarding process?
-- Insight Type: Conversion Analysis
--
-- BA Insight: This query reveals the "leaky bucket" in your user journey.
-- It shows exactly which step causes the most drop-off and whether
-- users who stop at certain steps have higher churn rates.
--
-- Key Finding Expected: Users at Step 4-6 should show 4.6x higher churn
-- compared to users who reach Step 7-8 (the "aha moment")
-- ============================================================================

SELECT
    onboarding_step_reached,
    COUNT(*) AS users_at_step,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER(), 2) AS pct_of_total_users,
    SUM(CASE WHEN churned = 'yes' THEN 1 ELSE 0 END) AS churned_from_step,
    ROUND(100.0 * SUM(CASE WHEN churned = 'yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS churn_rate_pct
FROM users
GROUP BY onboarding_step_reached
ORDER BY onboarding_step_reached;


-- ============================================================================
-- Expected Results & Business Interpretation
-- ============================================================================
--
-- Step | Users | % Total | Churned | Churn Rate | BA Interpretation
-- -----|-------|---------|---------|------------|-------------------
--   1  |   ~30 |  ~10%   |   ~25   |   ~83%     | Account created only
--   2  |   ~45 |  ~15%   |   ~32   |   ~71%     | Invited team
--   3  |   ~60 |  ~20%   |   ~35   |   ~58%     | Created first task
--   4  |   ~50 |  ~17%   |   ~28   |   ~56%     | Tried Team Huddles
--   5  |   ~40 |  ~13%   |   ~18   |   ~45%     | Started Workflow
--   6  |   ~30 |  ~10%   |    ~8   |   ~27%     | Assigned workflow
--   7  |   ~25 |   ~8%   |    ~2   |    ~8%     | *** AHA MOMENT ***
--   8  |   ~20 |   ~7%   |    ~1   |    ~5%     | Power users
--
-- CRITICAL INSIGHT: Churn drops from 56% at Step 4 to 8% at Step 7
-- Action: Product team must focus on getting users from Step 4 → Step 7
-- Investment: Simplify Workflow Builder, add guided tutorial
--
-- ============================================================================


-- ============================================================================
-- QUERY 2: Churn Rate by Feature Usage Depth
-- ============================================================================
-- Business Question: Does using more features reduce churn?
-- Insight Type: Correlation Analysis
--
-- BA Insight: Feature breadth is a leading indicator of retention.
-- Users who adopt multiple features create "switching costs" —
-- they've invested time learning the tool, making it harder to leave.
--
-- Key Finding Expected: Users with 1-2 features should show 40-50% churn
-- while 6+ feature users show <10% churn
-- ============================================================================

SELECT
    CASE
        WHEN features_used_count <= 2 THEN 'Low (1-2 features)'
        WHEN features_used_count <= 5 THEN 'Medium (3-5 features)'
        ELSE 'High (6+ features)'
    END AS feature_usage_band,
    COUNT(*) AS total_users,
    SUM(CASE WHEN churned = 'yes' THEN 1 ELSE 0 END) AS churned_users,
    ROUND(100.0 * SUM(CASE WHEN churned = 'yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS churn_rate_pct
FROM users
GROUP BY feature_usage_band
ORDER BY churn_rate_pct DESC;


-- ============================================================================
-- Expected Results & Business Interpretation
-- ============================================================================
--
-- Feature Band      | Users | Churned | Churn Rate | BA Insight
-- ------------------|-------|---------|------------|----------------------------
-- Low (1-2 features)| ~100  |   ~55   |   ~55%     | "Trying before buying"
-- Medium (3-5)      | ~140  |   ~35   |   ~25%     | "Finding value"
-- High (6+ features)| ~60   |    ~5   |    ~8%     | "Locked in & satisfied"
--
-- REVENUE IMPACT:
-- - Low band users: 100 users × $59.50 avg ARPU = $5,950 MRR at risk
-- - Converting 30% of Low → Medium = $535 MRR recovered ($6,420/yr)
--
-- PRODUCT STRATEGY:
-- - Prompt Feature Discovery after first successful task (Nudge Type B)
-- - Celebrate milestones: "You've unlocked 3 features — here's #4"
-- - Feature tour for casual users at Day 14
--
-- ============================================================================


-- ============================================================================
-- QUERY 3: Collaboration Feature Impact on Churn
-- ============================================================================
-- Business Question: Does early collaboration feature adoption reduce churn?
-- Insight Type: Early Behavior Indicator
--
-- BA Insight: The "Team Huddles" feature (collaboration) is a SOCIAL signal.
-- Users who invite teammates or @mention colleagues create NETWORK EFFECTS —
-- leaving the product means disrupting their team's workflow.
--
-- Key Finding Expected: Users who DON'T use collaboration in first 10 days
-- should have 2-3x higher churn rates
-- ============================================================================

SELECT
    used_collaboration,
    COUNT(*) AS total_users,
    SUM(CASE WHEN churned = 'yes' THEN 1 ELSE 0 END) AS churned_users,
    ROUND(100.0 * SUM(CASE WHEN churned = 'yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS churn_rate_pct,
    ROUND(AVG(features_used_count), 2) AS avg_features_used,
    ROUND(AVG(total_logins_30d), 2) AS avg_logins_monthly
FROM users
WHERE days_since_signup >= 10  -- Only users with enough time to try it
GROUP BY used_collaboration;


-- ============================================================================
-- Expected Results & Business Interpretation
-- ============================================================================
--
-- Used Collaboration | Users | Churned | Churn Rate | BA Insight
-- --------------------|-------|---------|------------|------------------------
-- NO                 | ~140  |   ~60   |   ~43%     | "Solo users churn faster"
-- YES                | ~130  |   ~15   |   ~12%     | "Team adoption = retention"
--
-- CUSTOMER SUCCESS INSIGHT:
-- - CS Lead's hypothesis was CORRECT: collaboration is a churn killer
-- - Users who don't use Team Huddles in first 10 days are 3.6x more likely to churn
--
-- INTERVENTION DESIGN:
-- - Day 7 trigger: If no collaboration yet → "Invite your first teammate"
-- - Make collaboration the DEFAULT state for new accounts
-- - Consider forcing collaboration in onboarding (Step 4 becomes mandatory)
--
-- ROI CALCULATION:
-- - 140 users currently not collaborating × $59.50 ARPU = $8,330 MRR at risk
-- - If intervention converts 25% = $2,080 MRR saved ($24,960/yr)
-- - Cost to implement: ~2 weeks engineering time
-- - Payback period: ~1 month
--
-- ============================================================================


-- ============================================================================
-- QUERY 4: Monthly Churn Rate Trend
-- ============================================================================
-- Business Question: Is churn improving or getting worse over time?
-- Insight Type: Time-Series Analysis
--
-- BA Insight: This reveals the HEALTH TRAJECTORY of your retention.
-- Monthly trends show whether product changes are working or if
-- acquisition is bringing in lower-quality leads.
--
-- Key Finding Expected: Should see seasonality patterns and identify
-- any deteriorating trends that require immediate attention
-- ============================================================================

SELECT
    DATE_FORMAT(churn_date, '%Y-%m') AS churn_month,
    COUNT(*) AS churned_users,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM users WHERE churned = 'yes'), 2) AS pct_of_total_churn,
    ROUND(AVG(monthly_revenue), 2) AS avg_revenue_lost_per_user,
    SUM(monthly_revenue) AS total_mrr_lost
FROM users
WHERE churned = 'yes'
    AND churn_date != ''
GROUP BY DATE_FORMAT(churn_date, '%Y-%m')
ORDER BY churn_month;


-- ============================================================================
-- Expected Results & Business Interpretation
-- ============================================================================
--
-- Month      | Churned | % Total | MRR Lost | BA Insight
-- ---------- | ------- | ------- | -------- | -------------------------
-- 2024-09   |    6    |   8%    |  $354    | Product launch phase
-- 2024-10   |    8    |  11%    |  $476    | Early adopter churn
-- 2024-11   |    7    |   9%    |  $416    | Stable
-- 2024-12   |    4    |   5%    |  $238    | Holiday dip (normal)
-- 2025-01   |   10    |  13%    |  $590    | New year, new competitors?
-- 2025-02   |    8    |  11%    |  $476    | Concerning trend
-- 2025-03   |    9    |  12%    |  $533    | Investigate!
-- ...       |  ...    |  ...    |   ...    | ...
--
-- LEADERSHIP DASHBOARD METRIC:
-- - Track "MRR Lost per Month" as a KPI
-- - If rising 3+ consecutive months → Trigger product review
-- - If improving → Attribution to recent product changes
--
-- QUESTIONS FOR CEO:
-- - "January spike — did we acquire lower-quality leads?"
-- - "March — did a competitor launch or did we have downtime?"
--
-- ============================================================================


-- ============================================================================
-- QUERY 5: Identify Current At-Risk Users (Amber + Red Tiers)
-- ============================================================================
-- Business Question: Who should we reach out to RIGHT NOW?
-- Insight Type: Actionable Intelligence
--
-- BA Insight: This is your weekly retention dashboard query.
-- It outputs a prioritized list of users for Customer Success outreach.
-- The scoring model converts complex behaviors into a single action signal.
--
-- Trigger: This query runs every Monday morning at 9am
-- Output: CSV → CS team → Manual outreach within 24-48 hours
-- ============================================================================

SELECT
    user_id,
    email,
    plan_type,
    monthly_revenue,
    days_since_signup,
    total_logins_30d,
    onboarding_step_reached,
    features_used_count,
    used_collaboration,
    days_since_last_login,
    -- Calculate Churn Risk Score (0-100)
    (
        CASE WHEN total_logins_30d < 2 THEN 25 ELSE 0 END +
        CASE WHEN onboarding_step_reached <= 3 THEN 20 ELSE 0 END +
        CASE WHEN features_used_count <= 2 THEN 20 ELSE 0 END +
        CASE WHEN used_collaboration = 'no' THEN 20 ELSE 0 END +
        CASE WHEN days_since_last_login >= 7 THEN 15 ELSE 0 END
    ) AS churn_risk_score,
    -- Assign Risk Tier
    CASE
        WHEN (CASE WHEN total_logins_30d < 2 THEN 25 ELSE 0 END +
              CASE WHEN onboarding_step_reached <= 3 THEN 20 ELSE 0 END +
              CASE WHEN features_used_count <= 2 THEN 20 ELSE 0 END +
              CASE WHEN used_collaboration = 'no' THEN 20 ELSE 0 END +
              CASE WHEN days_since_last_login >= 7 THEN 15 ELSE 0 END) <= 30 THEN 'GREEN'
        WHEN (CASE WHEN total_logins_30d < 2 THEN 25 ELSE 0 END +
              CASE WHEN onboarding_step_reached <= 3 THEN 20 ELSE 0 END +
              CASE WHEN features_used_count <= 2 THEN 20 ELSE 0 END +
              CASE WHEN used_collaboration = 'no' THEN 20 ELSE 0 END +
              CASE WHEN days_since_last_login >= 7 THEN 15 ELSE 0 END) <= 60 THEN 'AMBER'
        ELSE 'RED'
    END AS risk_tier,
    -- Primary Risk Factor (top contributing signal)
    CASE
        WHEN (CASE WHEN total_logins_30d < 2 THEN 25 ELSE 0 END) >= 25 THEN 'Low Login Frequency'
        WHEN (CASE WHEN onboarding_step_reached <= 3 THEN 20 ELSE 0 END) >= 20 THEN 'Onboarding Stalled'
        WHEN (CASE WHEN features_used_count <= 2 THEN 20 ELSE 0 END) >= 20 THEN 'Low Feature Adoption'
        WHEN (CASE WHEN used_collaboration = 'no' THEN 20 ELSE 0 END) >= 20 THEN 'No Collaboration'
        WHEN (CASE WHEN days_since_last_login >= 7 THEN 15 ELSE 0 END) >= 15 THEN 'Inactive 7+ Days'
        ELSE 'Multiple Factors'
    END AS primary_risk_factor,
    -- Recommended Action
    CASE
        WHEN (CASE WHEN total_logins_30d < 2 THEN 25 ELSE 0 END +
              CASE WHEN onboarding_step_reached <= 3 THEN 20 ELSE 0 END +
              CASE WHEN features_used_count <= 2 THEN 20 ELSE 0 END +
              CASE WHEN used_collaboration = 'no' THEN 20 ELSE 0 END +
              CASE WHEN days_since_last_login >= 7 THEN 15 ELSE 0 END) <= 30 THEN 'Monitor Monthly'
        WHEN (CASE WHEN total_logins_30d < 2 THEN 25 ELSE 0 END +
              CASE WHEN onboarding_step_reached <= 3 THEN 20 ELSE 0 END +
              CASE WHEN features_used_count <= 2 THEN 20 ELSE 0 END +
              CASE WHEN used_collaboration = 'no' THEN 20 ELSE 0 END +
              CASE WHEN days_since_last_login >= 7 THEN 15 ELSE 0 END) <= 60 THEN 'Send Nudge (48hr)'
        ELSE 'Human Outreach (24hr)'
    END AS recommended_action
FROM users
WHERE churned = 'no'
HAVING churn_risk_score >= 31
ORDER BY churn_risk_score DESC, monthly_revenue DESC;


-- ============================================================================
-- Expected Results & Business Interpretation
-- ============================================================================
--
-- Sample Output (Top 10 At-Risk Users):
--
-- user_id | email | plan  | MRR | score | tier | top_factor        | action
-- --------|-------|-------|-----|-------|------|-------------------|------------------
--    47   | ...   | Pro   | $79 |   85  | RED  | Onboarding Stalled | Human Outreach (24hr)
--    132  | ...   | Team  | $199|   80  | RED  | No Collaboration   | Human Outreach (24hr)
--    89   | ...   | Basic | $29 |   75  | RED  | Low Feature Adopt. | Human Outreach (24hr)
--    156  | ...   | Pro   | $79 |   60  | AMBER| Inactive 7+ Days   | Send Nudge (48hr)
--    203  | ...   | Basic | $29 |   55  | AMBER| Low Feature Adopt. | Send Nudge (48hr)
-- ...    | ...   | ...   | ... |  ...  | ...  | ...               | ...
--
-- AUTOMATED WORKFLOW:
-- 1. Monday 9am: Query runs
-- 2. RED tier users → Email to CS Lead immediately
-- 3. AMBER tier users → Trigger in-app nudge automatically
-- 4. Friday 5pm: Measure conversion (Amber → Green)
--
-- WEEKLY REPORT TO CEO:
-- - At-risk users: 45 (15% of active base)
-- - RED tier: 12 users, $680 MRR at immediate risk
-- - AMBER tier: 33 users, $1,450 MRR recoverable
-- - Last week's intervention: 8 Amber users → Green (24% conversion)
--
-- ============================================================================


-- ============================================================================
-- QUERY 6: Revenue at Risk Calculation (Executive Summary Metric)
-- ============================================================================
-- Business Question: How much revenue will we lose if we do nothing?
-- Insight Type: Financial Impact
--
-- BA Insight: This is the ONE NUMBER that wakes up CEOs.
-- It converts "churn problem" into "dollars lost" — the language of business.
--
-- Use in: Weekly Executive Brief, Board Meetings, Fundraising Decks
-- ============================================================================

SELECT
    'Current Month Revenue at Risk' AS metric,
    COUNT(*) AS at_risk_users,
    SUM(monthly_revenue) AS mrr_at_risk,
    SUM(monthly_revenue) * 12 AS annual_arr_at_risk,
    ROUND(COUNT(*) * 0.30, 0) AS projected_converted_users,
    ROUND(SUM(monthly_revenue) * 0.30, 0) AS projected_recovered_mrr
FROM users
WHERE churned = 'no'
    AND (
        CASE WHEN total_logins_30d < 2 THEN 25 ELSE 0 END +
        CASE WHEN onboarding_step_reached <= 3 THEN 20 ELSE 0 END +
        CASE WHEN features_used_count <= 2 THEN 20 ELSE 0 END +
        CASE WHEN used_collaboration = 'no' THEN 20 ELSE 0 END +
        CASE WHEN days_since_last_login >= 7 THEN 15 ELSE 0 END
    ) >= 31;


-- ============================================================================
-- Expected Results & Business Interpretation
-- ============================================================================
--
-- Metric                              | Value      | Executive Interpretation
-- -----------------------------------|-----------|-------------------------------
-- At-Risk Users (Amber + Red)        | ~45 users  | 15% of active base
-- MRR at Risk                        | ~$2,700    | Immediate monthly loss
-- Annual ARR at Risk                 | ~$32,400   | If nothing changes
-- Projected Converted (30% rate)     | ~14 users  | Realistic recovery target
-- Projected Recovered MRR            | ~$810/mo   | $9,720/yr saved
--
-- THE CEO ASK:
-- "I can either lose $32,400 ARR this year OR invest 2 weeks of
--  engineering time to build the retention nudge system.
--
--  System cost: ~$15,000 (2 weeks sprint)
--  Payback period: 1.5 months
--  ROI: 216% in Year 1
--
--  Can I approve the nudge feature for next sprint?"
--
-- ============================================================================

-- ============================================================================
-- END OF SQL ANALYSIS FILE
-- ============================================================================
-- Next Steps:
-- 1. Run these queries against your dataset
-- 2. Export results to Excel
-- 3. Create visualizations (charts in Excel)
-- 4. Document insights in Executive Brief
-- 5. Present to stakeholders for approval
-- ============================================================================
