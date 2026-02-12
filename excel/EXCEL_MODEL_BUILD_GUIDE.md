# Excel Churn Scoring Model — Complete Build Guide
## Churn Intelligence System

This guide provides step-by-step instructions to build the complete 4-tab Excel workbook for the Churn Intelligence System.

---

## Workbook Structure Overview

```
Churn_Intelligence_Model.xlsx
│
├── Tab 1: Raw Data         [Import CSV]
├── Tab 2: Score Calculator  [Auto-calculates risk scores]
├── Tab 3: Retention Dashboard [Visualizations]
└── Tab 4: Intervention Tracker  [Manual tracking log]
```

---

## TAB 1: Raw Data

### Setup Instructions

1. **Open Excel** → Create new workbook
2. **Rename Sheet1** → "Raw Data"
3. **Import the CSV**: Data → From Text/CSV → Select `churn_intelligence_dataset.csv`
4. **Load to**: Table in existing worksheet

### Column Reference (for formulas)

| Column | Letter | Field Name | Description |
|--------|--------|------------|-------------|
| A | user_id | Unique identifier |
| B | email | User email |
| C | signup_date | Date user signed up |
| D | plan_type | Basic/Pro/Team |
| E | monthly_revenue | Monthly MRR |
| F | churned | yes/no |
| G | churn_date | Date of churn |
| H | last_login_date | Most recent login |
| I | days_since_last_login | Days inactive |
| J | total_logins_30d | Logins in last 30 days |
| K | features_used_count | Number of features used |
| L | onboarding_step_reached | 1-8 |
| M | used_collaboration | yes/no |
| N | support_tickets_raised | Count of tickets |
| O | days_since_signup | Days since signup |

### Create Named Range

1. Select all data (A1:O301)
2. Formulas → Define Name → `UserData`
3. This makes formulas cleaner across tabs

---

## TAB 2: Score Calculator

### Create New Sheet

1. **+** button → New Sheet
2. Rename → "Score Calculator"

### Column Structure

| Column | Letter | Header | Formula |
|--------|--------|--------|---------|
| A | user_id | =Raw Data!A |
| B | plan_type | =Raw Data!D |
| C | monthly_revenue | =Raw Data!E |
| D | total_logins_30d | =Raw Data!J |
| E | onboarding_step | =Raw Data!L |
| F | features_used | =Raw Data!K |
| G | used_collaboration | =Raw Data!M |
| H | days_inactive | =Raw Data!I |
| I | **Login Score** | `=IF(D2<2,25,0)` |
| J | **Onboarding Score** | `=IF(E2<=3,20,0)` |
| K | **Feature Score** | `=IF(F2<=2,20,0)` |
| L | **Collaboration Score** | `=IF(G2="no",20,0)` |
| M | **Inactivity Score** | `=IF(H2>=7,15,0)` |
| N | **TOTAL RISK SCORE** | `=SUM(I2:M2)` |
| O | **RISK TIER** | `=IF(N2<=30,"Green",IF(N2<=60,"Amber","Red"))` |
| P | **Primary Risk Factor** | *(see formula below)* |
| Q | **Recommended Action** | *(see formula below)* |

### Row 2 Formulas (Copy Down to Row 301)

**Cell I2 - Login Score:**
```excel
=IF(D2<2,25,0)
```
*Interpretation: Less than 2 logins in 30 days = high risk signal (+25 points)*

**Cell J2 - Onboarding Score:**
```excel
=IF(E2<=3,20,0)
```
*Interpretation: Stuck at Step 3 or below = high risk (+20 points)*

**Cell K2 - Feature Score:**
```excel
=IF(F2<=2,20,0)
```
*Interpretation: Only 1-2 features used = low engagement (+20 points)*

**Cell L2 - Collaboration Score:**
```excel
=IF(G2="no",20,0)
```
*Interpretation: Never used collaboration = no network effect (+20 points)*

**Cell M2 - Inactivity Score:**
```excel
=IF(H2>=7,15,0)
```
*Interpretation: Inactive 7+ days = disengaging (+15 points)*

**Cell N2 - Total Risk Score:**
```excel
=SUM(I2:M2)
```
*Range: 0-100 points*

**Cell O2 - Risk Tier:**
```excel
=IF(N2<=30,"Green",IF(N2<=60,"Amber","Red"))
```
*Classification based on score thresholds*

**Cell P2 - Primary Risk Factor:**
```excel
=IF(I2=25,"Low Login Frequency",
IF(J2=20,"Onboarding Stalled",
IF(K2=20,"Low Feature Adoption",
IF(L2=20,"No Collaboration",
IF(M2=15,"Inactive 7+ Days","Multiple Factors")))))
```
*Identifies the single biggest churn driver*

**Cell Q2 - Recommended Action:**
```excel
=IF(O2="Green","Monitor Monthly",
IF(O2="Amber","Send Nudge (48hr)","Human Outreach (24hr)"))
```
*Actionable next step based on tier*

---

### Conditional Formatting (Visual Indicators)

**Apply to Column O (Risk Tier):**

1. Select O2:O301
2. Home → Conditional Formatting → New Rule
3. "Format only cells that contain"
4. **Green Rule**: Cell Value = "Green" → Green fill, dark green text
5. **Amber Rule**: Cell Value = "Amber" → Yellow fill, dark brown text
6. **Red Rule**: Cell Value = "Red" → Red fill, white text

**Apply to Column N (Risk Score):**

1. Select N2:N301
2. Conditional Formatting → Color Scale
3. 3-Color Scale: Green (0) → Yellow (50) → Red (100)

**Apply to Columns I-M (Signal Scores):**

1. Select I2:M301
2. Conditional Formatting → Data Bars
3. Show value + bar (makes signals visually pop)

---

## TAB 3: Retention Dashboard

### Create New Sheet

1. **+** button → New Sheet
2. Rename → "Retention Dashboard"

---

### Chart 1: Risk Tier Distribution (Donut Chart)

**Data Table (Cells A2:B4):**

```
        | Users | % Total
--------|-------|--------
Green   | 165   | 73%
Amber   | 45    | 20%
Red     | 15    | 7%
```

**Formulas:**
```excel
B2: =COUNTIF('Score Calculator'!O:O,"Green")
B3: =COUNTIF('Score Calculator'!O:O,"Amber")
B4: =COUNTIF('Score Calculator'!O:O,"Red")

C2: =B2/SUM($B$2:$B$4)
C3: =B3/SUM($B$2:$B$4)
C4: =B4/SUM($B$2:$B$4)
```

**Create Chart:**
1. Select A1:B4
2. Insert → Chart → Doughnut
3. Style: Add data labels, show percentages
4. Title: "Current User Risk Distribution"

**Executive Insight:**
> "73% of users are healthy (Green), 20% need intervention (Amber), 7% require immediate action (Red)."

---

### Chart 2: Onboarding Funnel Drop-off (Bar Chart)

**Data Table (Cells E2:F8):**

```
Step | Users | Churn Rate
-----|-------|------------
1    | 30    | 83%
2    | 45    | 71%
3    | 60    | 58%
4    | 50    | 56%
5    | 40    | 45%
6    | 30    | 27%
7    | 25    | 8%
8    | 20    | 5%
```

**Formulas:**
```excel
F3: =COUNTIF('Raw Data'!L:L,E3)
G3: =SUMIFS('Raw Data'!F:F,'Raw Data'!L:L,E3,'Raw Data'!F:F,"yes")/F3
```
*(Copy down for all steps)*

**Create Chart:**
1. Select E1:G8
2. Insert → Chart → Clustered Column
3. Secondary axis for Churn Rate (line overlay)
4. Title: "Onboarding Funnel: Drop-off by Step"

**Executive Insight:**
> "Users who reach Step 7-8 have 6.5x better retention than those who stop at Step 1-3. Product priority: Simplify path to Step 7."

---

### Chart 3: Feature Usage vs. Churn Rate (Scatter/Combo)

**Data Table (Cells E12:F14):**

```
Feature Usage | Users | Churn Rate
-------------|-------|------------
Low (1-2)    | 100   | 55%
Medium (3-5) | 140   | 25%
High (6+)    | 60    | 8%
```

**Formulas:**
```excel
E13: =COUNTIF('Raw Data'!K:K,"<=2")
E14: =COUNTIFS('Raw Data'!K:K,">=3",'Raw Data'!K:K,"<=5")
E15: =COUNTIF('Raw Data'!K:K,">=6")

F13: =SUMIFS('Raw Data'!F:F,'Raw Data'!K:K,"<=2",'Raw Data'!F:F,"yes")/E13
... (similar for others)
```

**Create Chart:**
1. Insert → Chart → Combo Chart
2. Users: Column chart
3. Churn Rate: Line with markers on secondary axis
4. Title: "Feature Breadth Impact on Retention"

**Executive Insight:**
> "High feature adopters (6+) have 7x lower churn than low adopters. Intervention: Feature discovery nudges at Day 14."

---

### Chart 4: Monthly Churn Trend (Line Chart)

**Data Table (Cells I2:J13):**

```
Month    | Churned Users | MRR Lost
---------|---------------|----------
2024-08  | 4             | $236
2024-09  | 6             | $354
2024-10  | 8             | $476
2024-11  | 7             | $416
2024-12  | 4             | $238
2025-01  | 10            | $590
2025-02  | 8             | $476
2025-03  | 9             | $533
```

**Formula:**
```excel
I3: =TEXT('Raw Data'!G2,"YYYY-MM")
J3: =COUNTIFS('Raw Data'!G:G,">=2024-08-01",'Raw Data'!G:G,"<=2024-08-31")
K3: =SUMIFS('Raw Data'!E:E,'Raw Data'!G:G,">=2024-08-01",'Raw Data'!G:G,"<=2024-08-31")
```

**Create Chart:**
1. Select I1:K10
2. Insert → Chart → Line with Markers
3. Dual series: Churned Users + MRR Lost
4. Title: "Monthly Churn Trend (6 Months)"

**Executive Insight:**
> "Churn spiked in January (+150% vs Dec). Investigation needed: Did competitor launch? Did we have downtime?"

---

### Dashboard Header Section

**Cells A1:D2 — Key Metrics:**

```
+------------------+------------------+------------------+------------------+
| Active Users     | At-Risk Users    | MRR at Risk      | Projected Savings|
| 225              | 45 (20%)         | $2,700/mo        | $810/mo         |
+------------------+------------------+------------------+------------------+
```

**Formulas:**
```excel
B1: =COUNTIF('Raw Data'!F:F,"no")
B2: =COUNTIF('Score Calculator'!O:O,"Amber")+COUNTIF('Score Calculator'!O:O,"Red")
C2: =SUMIFS('Raw Data'!E:E,'Score Calculator'!O:O,"Amber")+SUMIFS('Raw Data'!E:E,'Score Calculator'!O:O,"Red")
D2: =C2*0.30
```

**Apply formatting:**
- B1: Large font, green
- B2: Large font, amber if >30, red if >50
- C2: Currency format, red
- D2: Currency format, green (this is recoverable!)

---

## TAB 4: Intervention Tracker

### Create New Sheet

1. **+** button → New Sheet
2. Rename → "Intervention Tracker"

### Column Structure

| Column | Header | Type | Notes |
|--------|--------|------|-------|
| A | user_id | Lookup | VLOOKUP from Score Calculator |
| B | email | Lookup | VLOOKUP from Raw Data |
| C | plan_type | Lookup | Shows user's plan (prioritization) |
| D | risk_tier | Lookup | Green/Amber/Red |
| E | risk_score | Lookup | 0-100 score |
| F | primary_risk_factor | Lookup | Main churn signal |
| G | nudge_type | Dropdown | A=Onboarding, B=Feature, C=Re-engagement |
| H | date_sent | Date | When nudge was delivered |
| I | date_opened | Date | When user clicked (if tracked) |
| J | date_responded | Date | When user took action |
| K | status | Dropdown | Sent→Opened→Responded→Converted/Churned |
| L | notes | Text | CS team notes |

### Data Validation (Dropdowns)

**Column G - Nudge Type:**
1. Select G2:G301
2. Data → Data Validation → List
3. Source: `Onboarding Resume,Feature Discovery,Re-engagement`
4. Input Message: "Select nudge type"

**Column K - Status:**
1. Select K2:K301
2. Data → Data Validation → List
3. Source: `Sent,Opened,Responded,Converted,Churned`
4. Input Message: "Current status"

### Initial Data Load (Import At-Risk Users)

**Cell A2 Formula (copy down):**
```excel
=IF('Score Calculator'!O2="Green","",IF('Score Calculator'!O2="Amber",'Score Calculator'!A2,IF('Score Calculator'!O2="Red",'Score Calculator'!A2,"")))
```

**Cell B2 Formula:**
```excel
=IFERROR(VLOOKUP(A2,'Raw Data'!A:B,2,FALSE),"")

**Cell C2 Formula:**
```excel
=IFERROR(VLOOKUP(A2,'Score Calculator'!A:B,2,FALSE),"")
```

**Cell D2 Formula:**
```excel
=IFERROR(VLOOKUP(A2,'Score Calculator'!A:O,15,FALSE),"")
```

**Cell E2 Formula:**
```excel
=IFERROR(VLOOKUP(A2,'Score Calculator'!A:N,14,FALSE),"")
```

**Cell F2 Formula:**
```excel
=IFERROR(VLOOKUP(A2,'Score Calculator'!A:P,16,FALSE),"")
```

### Weekly Summary Table

**Cells N1:P7 — Intervention Performance:**

```
Metric | This Week | This Month
-------|-----------|------------
Nudges Sent | 12 | 45
Opened | 8 | 32
Responded | 5 | 18
Converted | 3 | 12
Churned | 1 | 3
Conversion Rate | 25% | 27%
MRR Recovered | $59 | $237
```

**Formulas:**
```excel
O2: =COUNTA(H:H)-1  // Nudges sent
O3: =COUNTA(I:I)-1  // Opened
O4: =COUNTA(J:J)-1  // Responded
O5: =COUNTIF(K:K,"Converted")
O6: =COUNTIF(K:K,"Churned")
O7: =O5/(O5+O6)  // Conversion rate
O8: =SUMIFS(C:C,K:K,"Converted")  // MRR recovered
```

---

## Conditional Formatting (Advanced)

### Color-Coded Status Column

**Column K (Status):**

1. Select K2:K301
2. Conditional Formatting → Highlight Cells Rules → Equal to
3. **Sent**: Yellow background
4. **Opened**: Light orange
5. **Responded**: Light blue
6. **Converted**: Green background
5. **Churned**: Red background

### Risk Score Heat Map

**Column E (Risk Score):**

1. Select E2:E301
2. Conditional Formatting → Color Scale
3. 2-color: White (0) → Red (100)

---

## Dashboard Print Layout (for Executive Brief)

### Page Setup

1. Page Layout → Size → Letter
2. Orientation: Landscape
3. Margins: Narrow (0.5")
4. Set Print Area: A1:L40 (dashboard area)
5. Insert → Header → "Churn Intelligence Dashboard — Week of [Date]"
6. Insert → Footer → "Confidential — TeamFlow Internal"

---

## Pivot Table Alternative (for Advanced Users)

### Create Pivot from Raw Data

1. Select Raw Data tab → Insert → PivotTable
2. Place in new worksheet "Pivot Analysis"
3. **Rows**: plan_type
4. **Values**: Count of user_id, Sum of monthly_revenue
5. **Filters**: churned, used_collaboration

### Pivot 2: Risk Tier by Plan

1. Rows: plan_type
2. Columns: risk_tier (from Score Calculator)
3. Values: Count of user_id

This shows which plans have higher churn risk (e.g., "Basic users skew Amber/Red")

---

## Export Instructions

### Saving as Template (for reuse)

1. File → Save As → Excel Template (.xltx)
2. Name: `Churn_Intelligence_Template.xltx`
3. This allows monthly refresh with new data

### Exporting Dashboard for Slides

1. Select charts on Retention Dashboard
2. Copy → Paste Special → Picture (Enhanced Metafile)
3. Insert into PowerPoint/Keynote
4. Resize for presentation

---

## Testing Your Model

### Validation Checklist

- [ ] All 300 users imported (COUNTA in Raw Data = 300)
- [ ] 75 churned users (COUNTIF churned="yes" = 75)
- [ ] Risk scores range 0-100 (MAX score = 100, MIN = 0)
- [ ] 50-60% Green, 20-30% Amber, 10-20% Red (check distribution)
- [ ] No #REF or #N/A errors in any tab
- [ ] Charts auto-update when raw data changes
- [ ] Conditional formatting applies correctly

### Sample Validation Checks

**Test 1: Verify Churned User Has High Score**
1. Find a user with churned="yes" in Raw Data
2. Check their Score Calculator row
3. Expected: Score should be 61-100 (Red tier)

**Test 2: Verify Power User Has Low Score**
1. Find user with 25+ logins, 6+ features, collaboration=yes
2. Check their Score Calculator row
3. Expected: Score should be 0-30 (Green tier)

**Test 3: Test Intervention Tracker**
1. Manually add "Converted" status to row 2
2. Check weekly summary — O5 (Converted) should increment
3. MRR Recovered should increase by that user's monthly_revenue

---

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| #REF errors | Column letters don't match | Check formula references match actual column positions |
| Charts not updating | Data range fixed | Change chart data range to Table (dynamic) |
| Conditional formatting not applying | Rules conflict | Clear all rules, reapply in correct order |
| VLOOKUP returning #N/A | user_id not found | Check for leading/trailing spaces in IDs |
| Percentage showing as decimal | Cell format | Format cells as Percentage with 1 decimal |

---

## Next Steps After Building

1. **Weekly Refresh**: Replace Raw Data with latest export
2. **Monday Dashboard**: Review Retention Dashboard tab
3. **Tuesday Actions**: Export Red/Amber users → Assign to CS team
4. **Friday Review**: Update Intervention Tracker with results
5. **Monthly Report**: Copy charts to Executive Brief

---

*Excel Model Complete!*
*Next: Figma Wireframes → BRD → Executive Brief*
