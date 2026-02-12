# Figma Wireframe Specifications
## Churn Intelligence System — In-App Retention Nudges

This document provides complete specifications for designing all required wireframes in Figma. Use these as a guide to build pixel-perfect wireframes.

---

## Design System Foundation

### Color Palette
```
Primary Blue:     #4F46E5 (Indigo 600)
Success Green:    #10B981 (Emerald 500)
Warning Amber:    #F59E0B (Amber 500)
Danger Red:       #EF4444 (Red 500)
Neutral Text:     #1F2937 (Gray 800)
Secondary Text:   #6B7280 (Gray 500)
Border:           #E5E7EB (Gray 200)
Background:       #FFFFFF (White)
Surface:          #F9FAFB (Gray 50)
```

### Typography
```
Headline (H1):    24px, Semibold, 1.25 line-height
Headline (H2):    18px, Semibold, 1.25 line-height
Body:             14px, Regular, 1.5 line-height
Small:            12px, Regular, 1.4 line-height
Button:           14px, Medium, 1.0 line-height
```

### Spacing Scale
```
XS:  4px
SM:  8px
MD:  16px
LG:  24px
XL:  32px
2XL: 48px
```

### Components

**Button (Primary)**
- Background: #4F46E5
- Text: White
- Padding: 8px 16px
- Border Radius: 6px
- Hover: #4338CA

**Button (Secondary)**
- Background: White
- Text: #4F46E5
- Border: 1px #4F46E5
- Padding: 8px 16px
- Border Radius: 6px
- Hover: #EEF2FF

**Badge/Tag**
- Padding: 2px 8px
- Border Radius: 12px
- Font: 11px, Medium

---

## SCREEN 1: Dashboard Banner Nudge (Nudge Type C - Re-engagement)

### Context
- **Trigger**: User inactive for 7+ days
- **Goal**: Bring user back into product
- **Placement**: Top of main dashboard
- **Style**: Non-modal, dismissible banner

### Wireframe Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│ [Logo] TeamFlow                            [Search] [Notifications]  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │  [✕]                                                         │    │
│  │                                                               │    │
│  │  ┌─────┐  Hey Rohan, it's been a week. Here's what's new     │    │
│  │  │ 🎯  │  — and a shortcut to where you left off.            │    │
│  │  └─────┘                                                      │    │
│  │                                                               │    │
│  │  [Continue where I left off →]              [Dismiss]        │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                       │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                    YOUR PROJECTS                            │    │
│  │                                                              │    │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │    │
│  │  │ Project A    │  │ Project B    │  │ Project C    │      │    │
│  │  │ 12 tasks     │  │ 8 tasks      │  │ 15 tasks     │      │    │
│  │  └──────────────┘  └──────────────┘  └──────────────┘      │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

### Detailed Specifications

**Banner Container**
- Width: 100% of dashboard content area
- Height: 80px
- Background: Linear gradient (left to right)
  - Start: #EEF2FF (Indigo 50)
  - End: #FFFFFF
- Border-bottom: 1px solid #E5E7EB
- Border-left: 4px solid #4F46E5 (accent bar)

**Icon (Left)**
- Size: 40px × 40px
- Background: #FFFFFF
- Border-radius: 8px
- Icon: Target/Goal emoji or illustration
- Shadow: 0 2px 4px rgba(0,0,0,0.1)

**Dismiss Button (Top Right)**
- Size: 24px × 24px
- Icon: ✕ (X mark)
- Color: #9CA3AF (Gray 400)
- Hover: #6B7280
- Click action: Hide banner for 30 days

**Headline Text**
- Font: 16px, Semibold, #1F2937
- "Hey {name}, it's been a week. Here's what's new — and a shortcut to where you left off."

**Primary CTA Button**
- Text: "Continue where I left off →"
- Style: Primary button (#4F46E5 background)
- Padding: 10px 20px
- Border-radius: 6px
- Click action: Navigate to most recent active project

**Secondary Action (Dismiss)**
- Text: "Dismiss"
- Style: Text link
- Color: #6B7280
- Hover: #1F2937

### Responsive Behavior
- **Desktop (>1024px)**: Full banner with icon
- **Tablet (768-1024px)**: Same, reduced padding
- **Mobile (<768px)**:
  - Stack vertically (icon above text)
  - Full-width CTA button
  - Hide secondary text

### Interaction States

**Default State**
- Banner visible on page load
- Slight slide-down animation (300ms ease-out)

**After Dismiss**
- Banner slides up (300ms ease-in)
- Cookie/local storage stores dismissal for 30 days

**After CTA Click**
- Navigate to last active project
- Banner remains visible for return visits

---

## SCREEN 2: Onboarding Resume Prompt (Nudge Type A)

### Context
- **Trigger**: User stuck at Step 3 or below for 5+ days
- **Goal**: Push user toward "aha moment" (Step 7)
- **Placement**: Overlay on onboarding checklist page
- **Style**: Semi-transparent modal overlay

### Wireframe Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│ [Logo] TeamFlow                                    [User Profile]   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ╔═════════════════════════════════════════════════════════════════╗ │
│  ║                                                                 ║ │
│  ║         ┌─────────────────────────────────────┐               ║ │
│  ║         │  [✕]                                │               ║ │
│  ║         │                                      │               ║ │
│  ║         │  ┌────────────┐                     │               ║ │
│  ║         │  │           │  You're almost      │               ║ │
│  ║         │  │   🎯      │  there!             │               ║ │
│  ║         │  │           │                     │               ║ │
│  ║         │  └────────────┘                     │               ║ │
│  ║         │                                      │               ║ │
│  ║         │  Complete 2 more steps to unlock    │               ║ │
│  ║         │  Workflow Automation. Most users   │               ║ │
│  ║         │  who complete this save 3 hrs/week. │               ║ │
│  ║         │                                      │               ║ │
│  ║         │  ┌─────────────────┐ ┌────────────┐│               ║ │
│  ║         │  │ Continue Setup  →│ │ Skip      ││               ║ │
│  ║         │  └─────────────────┘ └────────────┘│               ║ │
│  ║         │                                      │               ║ │
│  ║         └─────────────────────────────────────┘               ║ │
│  ║                                                                 ║ │
│  ║  [dimmed onboarding checklist visible underneath]             ║ │
│  ║                                                                 ║ │
│  ╚═════════════════════════════════════════════════════════════════╝ │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

### Detailed Specifications

**Modal Overlay Background**
- Background: rgba(0, 0, 0, 0.5) — 50% opacity black
- Backdrop filter: blur(4px) — subtle blur on content behind

**Modal Container**
- Width: 480px
- Height: auto (content-driven)
- Background: #FFFFFF
- Border-radius: 12px
- Shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)
- Padding: 32px
- Position: Centered vertically and horizontally

**Dismiss Button**
- Top-right: × icon
- Size: 32px × 32px click area
- Color: #9CA3AF

**Illustration/Icon**
- Size: 64px × 64px
- Center: Checkmark with progress indicator or trophy icon
- Background: #ECFDF5 (Emerald 50)
- Border-radius: 50% (circle)

**Headline**
- Text: "You're almost there!"
- Font: 20px, Semibold, #1F2937
- Margin-top: 16px

**Body Copy**
- Text: "Complete 2 more steps to unlock Workflow Automation. Most users who complete this save 3 hrs/week."
- Font: 14px, Regular, #6B7280
- Line-height: 1.5
- Margin-top: 12px

**Progress Indicator (Optional Enhancement)**
- Visual: 3 dots, 2 filled (green), 1 empty
- Text: "Step 4 of 6"
- Position: Below body copy

**Primary CTA**
- Text: "Continue Setup →"
- Style: Primary button (#10B981 success green — positive reinforcement)
- Width: 100%
- Margin-top: 24px

**Secondary Action**
- Text: "Skip for now"
- Style: Text link, #6B7280
- Margin-top: 12px
- Center: Align below primary button

### Responsive Behavior
- **Desktop**: Centered modal, 480px width
- **Tablet**: Same, slightly reduced padding
- **Mobile**:
  - Width: 90% of screen
  - Bottom sheet style (slides up from bottom)
  - Full-width buttons

---

## SCREEN 3: Feature Discovery Prompt (Nudge Type B)

### Context
- **Trigger**: User using only 1-2 features after 14+ days
- **Goal:** Encourage feature breadth expansion
- **Placement**: In-product tooltip or side panel
- **Style:** Inline, contextual, non-intrusive

### Wireframe Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│ [Logo] TeamFlow                                    [User Profile]   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌─────────────────┐  ┌───────────────────────────────────────┐    │
│  │                 │  │                                        │    │
│  │   Task Board    │  │  ┌─────────────────────────────────┐  │    │
│  │                 │  │  │ [✕]                            │  │    │
│  │   ┌──────────┐  │  │  │                                 │  │    │
│  │   │ Task 1   │  │  │  │  💡                             │  │    │
│  │   └──────────┘  │  │  │                                 │  │    │
│  │                 │  │  │  Teams like yours use            │  │    │
│  │   ┌──────────┐  │  │  │  Team Huddles to                 │  │    │
│  │   │ Task 2   │  │  │  │  replace daily standups.         │  │    │
│  │   └──────────┘  │  │  │                                 │  │    │
│  │                 │  │  │  Want a 2-minute walkthrough?    │  │    │
│  │   ┌──────────┐  │  │  │                                 │  │    │
│  │   │ Task 3   │  │  │  │  [Show me →]     [Not now]      │  │    │
│  │   └──────────┘  │  │  └─────────────────────────────────┘  │    │
│  │                 │  │                                        │    │
│  └─────────────────┘  └───────────────────────────────────────┘    │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

### Detailed Specifications

**Tooltip Container**
- Width: 320px
- Background: #FFFFFF
- Border: 1px solid #E5E7EB
- Border-radius: 8px
- Shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1)
- Padding: 16px
- Position: Relative to active feature (right side)

**Pointer Arrow**
- Triangle pointing to the feature being promoted
- Size: 8px × 8px
- Same background as tooltip

**Icon (Top)**
- Size: 32px × 32px
- Lightbulb icon (#F59E0B amber)
- Background: #FFFBEB (Amber 50)
- Border-radius: 50%

**Headline**
- Text: "Teams like yours use Team Huddles to replace daily standups."
- Font: 14px, Semibold, #1F2937
- Margin-top: 12px

**Question**
- Text: "Want a 2-minute walkthrough?"
- Font: 13px, Regular, #6B7280
- Margin-top: 8px

**Primary CTA**
- Text: "Show me →"
- Style: Primary button (compact)
- Padding: 6px 12px
- Font: 13px

**Secondary Action**
- Text: "Not now"
- Style: Text link, #6B7280
- Font: 13px
- Margin-left: 8px

### Variant Options

**Variant B1: Product Tour Style**
- Click "Show me" → Opens interactive product tour
- Highlights feature in UI with spotlight effect
- Step-by-step tooltips (3-4 steps)

**Variant B2: Video Modal**
- Click "Show me" → Opens modal with 90-second video
- Auto-play, skippable
- Thumbnail preview before clicking

**Variant B3: Interactive Sandbox**
- Click "Show me" → Opens mini-tutorial within current screen
- User completes guided action (e.g., "Send your first @mention")
- Confetti animation on completion

---

## SCREEN 4: Admin Retention Dashboard

### Context
- **User**: Product Manager, Co-founder, Customer Success Lead
- **Goal**: Monitor churn risk, track intervention performance
- **Placement**: Dedicated admin dashboard page
- **Access**: Admin/CS team only

### Wireframe Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│ [Logo] TeamFlow   [Dashboard] [Projects] [Team] [Settings]           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  Retention Dashboard                          Week of Feb 10, 2026   │
│  ─────────────────────────────────────────────────────────────────  │
│                                                                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐              │
│  │ Active Users │  │ At-Risk Users│  │ MRR at Risk  │              │
│  │              │  │              │  │              │              │
│  │    225       │  │   45 (20%)   │  │   $2,700/mo  │              │
│  │   +12 this wk│  │   +3 this wk │  │   +$180 this │              │
│  └──────────────┘  └──────────────┘  └──────────────┘              │
│                                                                       │
│  ┌────────────────────────────────────┐ ┌────────────────────────┐ │
│  │  Risk Tier Distribution            │ │  Weekly Nudge Performance││
│  │  ┌───────────────────────────┐    │ │                        ││
│  │  │     [Donut Chart]          │    │ │  Sent: 45              ││
│  │  │     Green 73%              │    │ │  Opened: 32 (71%)      ││
│  │  │     Amber 20%              │    │ │  Converted: 12 (27%)   ││
│  │  │     Red 7%                 │    │ │  Churned: 3 (7%)       ││
│  │  └───────────────────────────┘    │ │                        ││
│  └────────────────────────────────────┘ └────────────────────────┘ │
│                                                                       │
│  Top At-Risk Users (Priority Order)                                   │
│  ─────────────────────────────────────────────────────────────────── │
│                                                                       │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │ User        │ Plan │ Score │ Tier  │ Top Factor    │ Action    │ │
│  ├────────────────────────────────────────────────────────────────┤ │
│  │ linda.g...  │ Pro  │ 85    │  RED  │ Onboarding    │ Outreach  │ │
│  │ charles...  │ Team │ 80    │  RED  │ No Collab     │ Outreach  │ │
│  │ kabir.a...  │ Basic│ 75    │  RED  │ Low Features  │ Outreach  │ │
│  │ rohan.v...  │ Basic│ 60    │ AMBER │ Inactive 7+   │ Nudge     │ │
│  │ michael.k.. │ Basic│ 55    │ AMBER │ Inactive 7+   │ Nudge     │ │
│  └────────────────────────────────────────────────────────────────┘ │
│                                                                       │
│  Churn Trend (Last 6 Months)                                          │
│  ─────────────────────────────────────────────────────────────────── │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │        [Line Chart: Churned Users over time]                    │ │
│  │  Y-axis: Number of users                                        │ │
│  │  X-axis: Month (Aug '25 - Jan '26)                              │ │
│  │  Data points show trend                                         │ │
│  └────────────────────────────────────────────────────────────────┘ │
│                                                                       │
│  [Export CSV] [Schedule Report]                                      │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

### Detailed Specifications

**Page Header**
- Title: "Retention Dashboard"
- Subtitle: "Week of [Current Date]"
- Right side: Date picker preset (This Week, Last Week, Last Month)

**KPI Cards (Top Row)**

Card Layout (repeated 3x):
- Width: 200px
- Height: 100px
- Background: #FFFFFF
- Border: 1px solid #E5E7EB
- Border-radius: 8px
- Padding: 16px

Card Content:
- Label (12px, #6B7280, uppercase): "Active Users"
- Value (32px, Semibold, #1F2937): "225"
- Delta (14px, inherited color):
  - Green if positive: "+12 this week"
  - Red if negative: "-3 this week"

**Charts Row**

**Left Chart: Risk Tier Distribution**
- Type: Donut chart
- Size: 300px × 250px
- Data: Green 73%, Amber 20%, Red 7%
- Legend: Color swatch + label + percentage
- Center text: Total users

**Right Chart: Weekly Nudge Performance**
- Type: Stacked bar or summary metrics
- Size: 300px × 250px
- Metrics:
  - Nudges sent: 45
  - Opened: 32 (71%)
  - Converted: 12 (27%)
  - Churned: 3 (7%)
- Color coding: Green for converted, Red for churned

**At-Risk Users Table**

Columns:
1. **User Email** (truncated, tooltip shows full)
2. **Plan** (Basic/Pro/Team badge)
3. **Score** (0-100, color-coded)
4. **Tier** (Green/Amber/Red badge)
5. **Top Factor** (Primary churn signal)
6. **Action** (Button: "Outreach" for Red, "Nudge" for Amber)

Table Styling:
- Header: 12px, Semibold, #6B7280, uppercase
- Row height: 48px
- Border-bottom: 1px solid #F3F4F6
- Hover: Background #F9FAFB
- Zebra striping: Optional

**Churn Trend Chart**
- Type: Line chart
- Size: 100% width, 250px height
- X-axis: 6 months
- Y-axis: Number of churned users
- Data points: Circular markers with tooltips
- Trend line: Smooth curve or straight segments
- Annotation: Peak/valley markers for anomalies

**Footer Actions**
- Button 1: "Export CSV" (Secondary)
- Button 2: "Schedule Weekly Report" (Primary)
- Link: "View full analytics →" (Text link)

### Interactive Elements

**Table Row Click**
- Opens user detail panel (side drawer)
- Shows: Full user profile, activity timeline, intervention history

**Filter Controls**
- Dropdown: Risk Tier (All/Green/Amber/Red)
- Dropdown: Plan Type (All/Basic/Pro/Team)
- Date Range: Last 7/30/90 days
- Search: By email

**Export Options**
- Format: CSV, PDF, PNG (charts only)
- Include: Selected filters or all data

---

## SCREEN 5: Mobile-Responsive Nudge (Nudge Variant C)

### Context
- Same as Screen 1 (Re-engagement)
- Optimized for mobile portrait view
- Critical: 50%+ of SaaS users access via mobile

### Wireframe Layout

```
┌──────────────────────────┐
│ [☰]        TeamFlow   [🔔]│
├──────────────────────────┤
│                          │
│  ┌────────────────────┐  │
│  │ [✕]               │  │
│  │                    │  │
│  │  ┌──────┐          │  │
│  │  │ 🎯   │  Hey    │  │
│  │  └──────┘  Rohan, │  │
│  │            it's   │  │
│  │  been a week.     │  │
│  │                    │  │
│  │  Pick up where    │  │
│  │  you left off →   │  │
│  │                    │  │
│  │  ┌──────────────┐ │  │
│  │  │  CONTINUE    │ │  │
│  │  └──────────────┘ │  │
│  │                    │  │
│  │  [Dismiss]        │  │
│  └────────────────────┘  │
│                          │
│  ┌────────────────────┐  │
│  │   YOUR PROJECTS    │  │
│  │  ┌────────────────┐ │  │
│  │  │ Project A      │ │  │
│  │  │ 12 tasks       │ │  │
│  │  └────────────────┘ │  │
│  │  ┌────────────────┐ │  │
│  │  │ Project B      │ │  │
│  │  │ 8 tasks        │ │  │
│  │  └────────────────┘ │  │
│  └────────────────────┘  │
│                          │
│  [Home] [Projects] [+]  │
└──────────────────────────┘
```

### Mobile-Specific Adjustments

**Banner Container**
- Width: 90% of screen (16px margins)
- Height: Auto (stack vertically)
- Padding: 16px

**Layout Changes**
- Icon + Text: Stack vertically (not horizontal)
- CTA Button: Full width
- Dismiss: Text link below CTA
- Touch targets: Minimum 44px × 44px

**Typography**
- Headline: 18px (reduced from 20px)
- Body: 14px (unchanged)
- Button: 16px (increased for readability)

**Gestures**
- Swipe down: Dismiss banner
- Swipe up: (disabled — prevents accidental dismissal)
- Tap outside: (disabled — not modal)

---

## Figma Component Library

### Reusable Components to Create

1. **Button/Primary**
   - Auto Layout
   - Variant: Default, Hover, Active, Disabled

2. **Button/Secondary**
   - Same as above, different style

3. **Badge/RiskTier**
   - Auto Layout with color variants (Green, Amber, Red)

4. **Card/KPI**
   - Auto Layout
   - Slot for label, value, delta

5. **Banner/Nudge**
   - Auto Layout (horizontal + vertical variant)
   - Icon slot, text slot, CTA slot, dismiss slot

6. **Modal/Overlay**
   - Background layer
   - Container layer
   - Content slot

7. **Table/Row**
   - Auto Layout columns
   - Hover state
   - Selected state

8. **Tooltip**
   - Arrow pointer variant (top, bottom, left, right)

### Smart Layout Tips

**Auto Layout Settings**
- Padding: 16px (default)
- Gap: 8px (default for horizontal), 12px (vertical)
- Stacking: Horizontal for buttons, Vertical for lists

**Constraints**
- KPI Cards: Left + Right (fixed margins)
- Dashboard Banner: Left + Right (full width)
- Mobile CTA: Left + Right (full width)

**Variants**
- Use Variants feature for:
  - Button states (Default, Hover, Disabled)
  - Risk tiers (Green, Amber, Red)
  - Banner placements (Desktop, Tablet, Mobile)

---

## Export & Handoff Specifications

### Export for Presentation
- **Format**: PNG (2x), PDF
- **Include**: All screens, components overview
- **Annotations**: Add interaction notes (optional)

### Export for Development
- **Format**: SVG (icons), CSS (styles), JSON (data)
- **Include**: Spacing tokens, color palette, typography scale
- **Zeplin/Figma Dev Mode**: Enable for easy handoff

### Interaction Design (Optional Enhancement)

If using Figma's prototype features:
- **On Click**: Navigate to frame
- **After Delay**: Auto-dismiss banner
- **Hover**: Button state change
- **Smart Animate**: Morphing transitions

---

## Design File Structure (Figma)

```
Churn Intelligence System
├── 📁 Design System
│   ├── Colors
│   ├── Typography
│   ├── Spacing
│   └── Components
│
├── 📁 Screens
│   ├── 1_Desktop_Dashboard_Banner
│   ├── 2_Desktop_Onboarding_Modal
│   ├── 3_Desktop_Feature_Discovery
│   ├── 4_Desktop_Admin_Dashboard
│   └── 5_Mobile_Re-engagement_Banner
│
├── 📁 Responsive Variants
│   ├── Tablet (768-1024)
│   └── Mobile (<768)
│
└── 📁 Prototypes
    ├── User Flow: At-Risk User Journey
    └── Admin Flow: CS Team Workflow
```

---

*Figma Wireframe Specifications Complete!*
*Next: Build these in Figma, then proceed to BRD → Executive Brief*
