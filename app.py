import streamlit as st
import pandas as pd

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

# 4. Timeline
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
