# Case Study: Churn Intelligence System
## How Data-Driven Insights Saved $60K+ in Annual Revenue

---

## Executive Summary

**Challenge**: A SaaS startup was losing 28% of new customers within 90 days — 3x industry average.

**Solution**: Built a behavioral early warning system that identifies at-risk users 2-4 weeks before they churn.

**Result**: $10,080 recovered in Year 1, $60K+ projected over 3 years, 303% ROI.

**Timeline**: 6 weeks from analysis to deployment.

---

## The Client

**Company**: TeamFlow (fictitious B2B SaaS startup)
**Industry**: Project Management Software
**Size**: 225 active users, $13,550 MRR
**Problem**: High early-stage churn threatening growth

---

## The Problem

> "We're acquiring users well, but the bucket has holes. We sign up 20 new customers and lose 6 existing ones every month. It's unsustainable."

### Key Metrics (Baseline)

| Metric | Value | Industry Benchmark | Gap |
|--------|-------|-------------------|-----|
| 90-day churn rate | 28% | 5-10% | **3x worse** |
| Onboarding completion | 28% | 50-60% | **50% gap** |
| Feature adoption (3+ features) | 35% | 70%+ | **50% gap** |
| Monthly revenue lost | $5,925 | — | **$71K/year** |

### The Silent Exit Pattern

Through stakeholder interviews and data analysis, we discovered the "silent exit" pattern:

```
Week 1-2:   User signs up, active login
Week 3:     Login frequency drops
Week 4-6:   Complete silence
Week 8-9:   Cancellation email arrives
```

**The problem**: We only learned about churn at Week 8. The signals were there at Week 3.

---

## The Approach

### Phase 1: Discovery (Week 1)

**Activities:**
- Analyzed 300 users × 18 months of behavioral data
- Interviewed 4 stakeholders (CEO, Head of Product, CS Lead, Growth)
- Built 3 detailed user personas with empathy maps
- Mapped current-state onboarding funnel

**Key Findings:**

| Discovery | Impact |
|-----------|--------|
| Users who reach Step 7-8 have **6.5x better retention** | Highest priority: Get users to aha moment |
| 70% of churned users never reached Step 5 | Onboarding is too long |
| Non-collaborators churn **3.6x more** | Social features = retention mechanism |
| No proactive retention system | Flying blind until cancellation |

### Phase 2: Analysis (Week 2)

**SQL Analysis**: Wrote 5 production queries to extract insights

```sql
-- Key Query: Onboarding Funnel Analysis
SELECT
    onboarding_step_reached,
    COUNT(*) AS users_at_step,
    SUM(CASE WHEN churned = 'yes' THEN 1 ELSE 0 END) AS churned_from_step,
    ROUND(100.0 * SUM(CASE WHEN churned = 'yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS churn_rate_pct
FROM users
GROUP BY onboarding_step_reached
ORDER BY onboarding_step_reached;
```

**The 4.6x Insight**:
```
Onboarding Step  | Churn Rate  | Retention Multiple
------------------|-------------|-------------------
Step 1-3 (early)  | 52%         | 1.0x (baseline)
Step 4-6 (middle) | 28%         | 1.9x better
Step 7-8 (aha)    | 8%          | 6.5x better
```

**Data-Driven Hypothesis**: If we can get 20% more users from Step 1-3 → Step 7-8, we reduce churn by 35%.

### Phase 3: Solution Design (Week 3)

**The 5-Signal Churn Risk Model**

| Signal | Weight | Trigger | Rationale |
|--------|--------|---------|-----------|
| Login Frequency | 25 pts | <2 logins in 30 days | Core engagement metric |
| Onboarding Progress | 20 pts | Stuck at Step ≤3 | Never reached aha moment |
| Feature Breadth | 20 pts | Using 1-2 features | Low value realization |
| Collaboration | 20 pts | Never used collab feature | No network effects |
| Inactivity | 15 pts | 7+ days inactive | Disengagement signal |

**Risk Tiers**:
- **Green (0-30)**: Healthy, monitor monthly
- **Amber (31-60)**: At-risk, automated nudge within 48hrs
- **Red (61-100)**: Critical, human outreach within 24hrs

**Proposed Interventions**:

1. **Onboarding Resume Nudge** (Type A)
   - Trigger: Stuck at Step ≤3 for 5+ days
   - Message: "You're 2 steps from unlocking Workflow Automation"
   - CTA: "Continue Setup →"

2. **Feature Discovery Nudge** (Type B)
   - Trigger: Using 1-2 features after 14+ days
   - Message: "Teams like yours use Team Huddles to save 5 hrs/week"
   - CTA: "Show me →"

3. **Re-engagement Nudge** (Type C)
   - Trigger: 7+ days inactive
   - Message: "Hey {name}, here's what's new — pick up where you left off"
   - CTA: "Continue →"

### Phase 4: Build & Validate (Weeks 4-5)

**Built**:
1. ✅ Interactive Streamlit dashboard (live, clickable)
2. ✅ Risk scoring engine (Python, no ML required)
3. ✅ Admin interface for CS team
4. ✅ Nudge delivery system (3 variants)
5. ✅ Performance tracking & analytics

**Validated**:
- Tested on 100 historical users: **78% prediction accuracy**
- A/B tested nudge copy: **32% open rate** (vs. 25% benchmark)
- Piloted with 10 users: **30% converted from Amber → Green**

### Phase 5: Deploy (Week 6)

**Launched**:
- Dashboard live at: `https://churn-intelligence-system.streamlit.app`
- Automated risk scoring: Daily batch job
- Nudge system: Real-time delivery
- Weekly executive digest: Email to CEO/CS/Product

---

## The Results

### 90-Day Outcomes

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| 90-day churn rate | 28% | 20% | **-29% (on track)** |
| Onboarding completion (Step 6+) | 28% | 42% | **+50%** |
| Collaboration adoption (Day 10) | 35% | 48% | **+37%** |
| Amber → Green conversion | N/A | 28% | **New capability** |
| MRR at risk | $14,800 | $9,100 | **-39%** |

### Financial Impact

```
Monthly Revenue Recovered:    $5,800
Annualized (Year 1):          $69,600
Investment (one-time):        $15,000
Net Return (Year 1):          $54,600
ROI:                          303%
Payback Period:               1.5 months
```

### 3-Year Projection

| Year | MRR Recovered | Annual Impact |
|------|---------------|---------------|
| Year 1 | $5,800/mo | $69,600 |
| Year 2 | $7,800/mo | $93,600 (optimized) |
| Year 3 | $10,200/mo | $122,400 (funnel fixed) |
| **Total** | — | **$285,600** |

---

## Stakeholder Quotes

> "For the first time, I wake up Monday morning knowing exactly which accounts need attention. No more reactive firefighting."
> — Customer Success Lead

> "The dashboard paid for itself in 6 weeks. Now I can't imagine running this company without it."
> — CEO / Co-founder

> "We finally have data to back up our product hunches. The onboarding team uses this daily."
> — Head of Product

---

## Lessons Learned

### What Worked

1. **Rule-based > ML**: Simple 5-signal model outperformed complex ML. Faster to build, easier to explain.
2. **Early intervention > Late**: The "rescue window" is Day 7-14. After Day 21, it's too late.
3. **Network effects matter**: Collaboration users churn 3.6x less. Social features = retention.
4. **Executives need one number**: "How much revenue are we losing?" drives action.

### What Didn't Work

1. **Email nudges**: Low open rate (15%). In-product nudges: 32% open rate.
2. **8-step onboarding**: Too long. Simplified to 3 core steps + optional advanced.
3. **Weekly CS meetings**: Too slow. Moved to real-time dashboard alerts.

### What We'd Do Differently

1. **Start with power users**: They're your champions. Give them early access.
2. **A/B test everything**: Copy, timing, channel. Small changes = big impact.
3. **Build for mobile**: 40% of users access via phone. Mobile-first next time.

---

## Replicability Framework

This solution is **industry-agnostic**. Works for:

| Industry | Churn Signal Example |
|----------|---------------------|
| E-commerce | Days since last purchase |
| Healthcare | Missed appointments |
| Education | Course completion rate |
| Finance | Account inactivity |
| Media | Content consumption drop |

**The 5-Signal Framework** adapts to any business with user behavioral data.

---

## Tools & Technologies

| Category | Tool | Why |
|----------|------|-----|
| Data Analysis | SQL | Fast, efficient, universal |
| Data Modeling | Python (Pandas) | Flexible, powerful |
| Visualization | Plotly | Interactive, web-ready |
| Dashboard | Streamlit | No frontend skills needed |
| Design | Figma | Professional wireframes |
| Documentation | Markdown | Version-controlled, clean |

---

## Next Steps

### Immediate (Month 1-3)
- ✅ Optimize nudge copy based on performance data
- ✅ Simplify onboarding to 3 steps
- ✅ Add mobile-responsive nudges
- ✅ Integrate with CRM (Salesforce/HubSpot)

### Medium (Month 4-6)
- 🔄 ML-based churn prediction (Phase 2)
- 🔄 Automated email campaigns
- 🔄 Cohort analysis dashboard
- 🔄 A/B testing framework

### Long-term (Month 7-12)
- 📋 Predictive lead scoring
- 📋 CLV (Customer Lifetime Value) modeling
- 📋 Churn forecast dashboard
- 📋 Advanced cohort analytics

---

## About the Analyst

**[Your Name]** is a Business Analyst specializing in data-driven product decisions and customer retention.

**Expertise**:
- SQL & behavioral analysis
- Stakeholder management & requirements gathering
- End-to-end project ownership
- Executive communication & storytelling

**Contact**:
- LinkedIn: [Your Profile]
- GitHub: [Your Profile]
- Email: [Your Email]

---

## View Live Dashboard

**Interactive Demo**: [https://churn-intelligence-system.streamlit.app](https://churn-intelligence-system.streamlit.app)

**GitHub Repository**: [https://github.com/shru2704/churn-intelligence-system](https://github.com/shru2704/churn-intelligence-system)

---

*"The best time to reduce churn was before users signed up. The second best time is today."*

---

**Project Duration**: 6 weeks
**Team Size**: 1 (Business Analyst)
**Budget**: $15,000 (engineering)
**ROI**: 303% (Year 1), 1,800% (3-year)
