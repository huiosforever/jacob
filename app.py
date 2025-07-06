import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="VC Crypto Deal Analyzer", layout="wide")

st.title("🪙 VC Crypto Deal Analyzer (Bay Street Framework)")

# 1. Executive Summary
st.header("1. Executive Summary")
st.markdown("""
- **Sector**: DeFi  
- **Thesis**: A decentralized derivatives platform with strong token utility and emissions control.  
- **Key Risks**: Token unlocks begin in 3 months; smart contracts unaudited.  
- **Exit Pathways**: CEX listing (Binance), DEX liquidity mining, potential acquisition by Layer 2 protocol.  
""")

# 2. Document Checklist
st.header("2. Document Checklist")
checklist_data = {
    "Section": [
        "Pitch Deck", "Tokenomics Sheet", "Smart Contract Audit",
        "Team & Bios", "Market & Strategy", "Legal Structure (SAFT)", "Custom Requests"
    ],
    "Status": ["✅", "✅", "❌", "✅", "✅", "❌", "⏳"]
}
st.dataframe(pd.DataFrame(checklist_data))

# 3. Quantamental Metrics
st.header("3. Quantamental Metrics")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Private Token Deal")
    st.metric("Token IRR", "27.5%")
    st.metric("FDV", "$150M")
    st.metric("Bay Score", "82")
    st.markdown("- AHA (Holder Alignment): 30\n- LSD (Liquidity/Security Design): 32\n- FX Drag: +20")

with col2:
    st.subheader("Public Comps")
    st.markdown("""
    - **Comps**: $GMX, $DYDX, $INJ  
    - **Median EV/Revenue**: 9.8x  
    - **30D Volatility**: 44%
    """)

# 4. Diligence Timeline
st.header("4. Diligence Timeline")
timeline = [
    ("Week 1", "Whitepaper + Token Model Review"),
    ("Week 2", "Dev Activity + Ecosystem Fit"),
    ("Week 3", "Legal/SAFT Review"),
    ("Week 4", "IC Memo + Token Listing Readiness")
]
st.table(pd.DataFrame(timeline, columns=["Week", "Milestone"]))

# 5. Summary
st.header("5. Summary")
st.success("This protocol demonstrates strong emissions control and ecosystem fit but requires further review of its audit and unlock schedule.")

# 6. Charts & Visualizations
st.header("6. Charts & Visualizations")

chart_titles = [
    "Token Price Simulation", "Treasury Balance Over Time", "Dev Activity Heatmap", "User Growth Curve",
    "FDV vs TVL", "Token Supply Inflation", "Top Holder Concentration", "DEX vs CEX Volume",
    "Protocol Revenue YoY", "Staking Participation Rate", "Bridge Usage", "Chain Gas Fees (last 30d)",
    "Validator Count Over Time", "Security Incidents Timeline", "Public Comps Performance"
]

for i, title in enumerate(chart_titles):
    st.subheader(f"Chart {i+1}: {title}")
    # Generate fake data
    df = pd.DataFrame({
        "x": np.linspace(1, 100, 100),
        "value": np.random.normal(loc=100, scale=10, size=100).cumsum()
    })
    st.line_chart(df.set_index("x"))
    st.divider()
