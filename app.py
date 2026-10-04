import streamlit as st
import urllib.parse
import os

# -------------------------------------------------------------
# CONFIGURATION & GITHUB RELATIVE PATHS
# -------------------------------------------------------------
WHATSAPP_NUMBER = "919716467561"

# Updated to relative paths for GitHub/Streamlit Cloud Deployment
KVC_PATH = "KVC.png"
QRC_PATH = "QRC.jpeg"
VC_PATH = "visiting card.jpeg"

st.set_page_config(page_title="Kavya International | Premium Printing Solutions", page_icon="🖨️", layout="wide")

# -------------------------------------------------------------
# SESSION STATE INITIALIZATION
# -------------------------------------------------------------
if 'quote_cart' not in st.session_state:
    st.session_state.quote_cart = []
if 'page' not in st.session_state:
    st.session_state.page = "Home & Profile"
if 'lang' not in st.session_state:
    st.session_state.lang = "English"

# -------------------------------------------------------------
# KHAJOORWALA THEME CSS (CREAM BACKGROUND & COMPACT UI)
# -------------------------------------------------------------
st.markdown("""
    <style>
    /* Hide Sidebar completely */
    [data-testid="collapsedControl"], [data-testid="stSidebar"] { display: none !important; }
    
    /* RICH CREAM BACKGROUND */
    .stApp, .main, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .block-container {
        background-color: #FDF9F1 !important;
    }
    
    /* Rounded Symmetrical Buttons */
    div[data-testid="stButton"] > button {
        border-radius: 30px !important;
        font-weight: 700 !important;
        border: 1px solid #CBD5E1 !important;
        transition: all 0.3s ease;
    }
    div[data-testid="stButton"] > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
    }
    
    /* General Styling */
    html, body, [class*="css"] { font-size: 1.05rem; }
    .top-bar-contact { text-align: right; font-size: 1.1rem; color: #0F172A; margin-top: 5px; }
    .top-bar-contact b { color: #0284C7; font-size: 1.4rem; font-weight: 800;}
    
    /* Hero Section */
    .hero-container {
        background: linear-gradient(rgba(15, 23, 42, 0.95), rgba(15, 23, 42, 0.85));
        padding: 25px 30px; border-radius: 12px; color: white; margin-bottom: 25px; 
        text-align: center; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.2);
    }
    .hero-title {font-size: 2.2rem; font-weight: 900; margin-bottom: 8px; line-height: 1.2;}
    .hero-subtitle {font-size: 1.1rem; font-weight: 400; color: #CBD5E1;}
    .section-title {font-size: 1.8rem; font-weight: 800; color: #0F172A; border-bottom: 3px solid #0284C7; padding-bottom: 10px; margin-bottom: 30px; margin-top: 20px;}
    
    /* B2B Product Cards */
    .b2b-card {
        background-color: #FFFFFF !important; 
        padding: 25px; border-radius: 12px; border: 1px solid #E2E8F0;
        box-shadow: 0 4px 15px -3px rgba(0,0,0,0.05); height: 100%; display: flex; flex-direction: column;
    }
    .card-title {font-size: 1.3rem; font-weight: 800; color: #1E293B; margin-bottom: 15px;}
    .trust-badge { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-left: 5px solid #0284C7; padding: 20px; margin-bottom: 25px; border-radius: 8px;}
    </style>
""", unsafe_allow_html=True)

def get_file_bytes(filepath):
    try:
        with open(filepath, "rb") as f: return f.read()
    except FileNotFoundError: return None

def add_to_cart(item_name, size, qty):
    st.session_state.quote_cart.append({"item": item_name, "size": size, "qty": qty})
    st.toast(f"Added {qty}x {item_name} to Cart!", icon="🛒")

# -------------------------------------------------------------
# TOP HEADER 
# -------------------------------------------------------------
top_c1, top_c2, top_c3 = st.columns([1, 2, 1])

with top_c1:
    st.markdown("<p style='font-size:0.9rem; font-weight:700; color:#64748B; margin-bottom:0px;'>Language / भाषा</p>", unsafe_allow_html=True)
    st.session_state.lang = st.selectbox(
        "", 
        ["English", "हिंदी"], 
        index=0 if st.session_state.lang == "English" else 1,
        label_visibility="collapsed"
    )

with top_c2:
    sub1, sub_logo, sub2 = st.columns([1, 2, 1])
    with sub_logo:
        if os.path.exists(KVC_PATH):
            st.image(KVC_PATH, use_container_width=True)
        else:
            st.info("📷 Banner Image Missing")

with top_c3:
    st.markdown("""
        <div class="top-bar-contact">
            Sales & Support<br>
            <b>📞 +91-9716467561</b>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# -------------------------------------------------------------
# MAIN NAVIGATION 
# -------------------------------------------------------------
nav_options = ["Home & Profile", "Premium Blankets", "Other Consumables", "Technical Hub", "Request a Quote", "Contact & Payment"]
nav_options_hi = ["होम", "प्रीमियम ब्लैंकेट्स", "अन्य सामग्री", "तकनीकी सहायता", "कोटेशन प्राप्त करें", "संपर्क विवरण"]

current_options = nav_options if st.session_state.lang == "English" else nav_options_hi

nav_cols = st.columns(6)
for i, col in enumerate(nav_cols):
    with col:
        is_active = (st.session_state.page == nav_options[i])
        if st.button(current_options[i], key=f"nav_{i}", use_container_width=True, type="primary" if is_active else "secondary"):
            st.session_state.page = nav_options[i]
            st.rerun()

st.write("---")

# -------------------------------------------------------------
# PAGE CONTENT RENDERING
# -------------------------------------------------------------
page = st.session_state.page

if page == "Home & Profile":
    if st.session_state.lang == "English":
        st.markdown("""
        <div class="hero-container">
            <div class="hero-title">Genuine Kinyo, Trelleborg & Varn Supply for Delhi NCR Presses.</div>
            <div class="hero-subtitle">World-class offset printing consumables and precision spare parts. Same-day dispatch available.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="hero-container">
            <div class="hero-title">दिल्ली NCR के प्रिंटिंग प्रेस के लिए असली Kinyo, Trelleborg और Varn उत्पाद।</div>
            <div class="hero-subtitle">वर्ल्ड-क्लास ऑफसेट प्रिंटिंग सामग्री और स्पेयर पार्ट्स। सेम-डे डिलीवरी उपलब्ध।</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Authorized Partners</div>', unsafe_allow_html=True)
    logo_cols = st.columns(5)
    
    # Updated to relative paths
    brand_logos = [
        ("kinyo.png", "KINYO"),
        ("trb.png", "TRELLEBORG"),
        ("flint.png", "VARN"),
        ("poly.png", "POLICROM"),
        ("conti.png", "CONTAIR")
    ]
    
    for i, (path, name) in enumerate(brand_logos):
        with logo_cols[i]:
            if os.path.exists(path):
                st.image(path, use_container_width=True)
            else:
                st.markdown(f"<div style='text-align:center; font-weight:800; font-size:1.4rem; color:#475569;'>{name}</div>", unsafe_allow_html=True)
    
    st.write("---")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class="trust-badge">
        <b style='font-size:1.2rem; color:#0F172A;'>Why Kavya International?</b><br><br>
        <ul>
            <li><b>100% Genuine Supply:</b> Authorized distributor certificates available.</li>
            <li><b>Technical Expertise:</b> We help you solve piling and smash issues.</li>
            <li><b>B2B Transparency:</b> GST Invoices and flexible credit terms.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.markdown("""
        <div class="trust-badge">
        <b style='font-size:1.2rem; color:#0F172A;'>Client Testimonials</b><br><br>
        <i>"Kavya International saved our packaging run. We needed custom-cut Kinyo blankets urgently, and Dhirender arranged them the same day. Unmatched service in Naraina."</i><br><br>
        — <b style='color:#0284C7;'>S. Kumar</b>, Production Head (Delhi NCR)
        </div>
        """, unsafe_allow_html=True)

elif page == "Premium Blankets":
    st.markdown('<div class="section-title">Kinyo Premium Offset Blankets</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="b2b-card">', unsafe_allow_html=True)
        if os.path.exists("atlas.jpg"): st.image("atlas.jpg")
        st.markdown('<div class="card-title">Atlas Web AS</div>', unsafe_allow_html=True)
        st.write("**Application:** Web Offset, Newspaper\n\n**Thickness:** 1.95mm / 1.68mm")
        if pdf_bytes := get_file_bytes("Atlas Web AS.pdf"):
            st.download_button("📄 Download Specs", data=pdf_bytes, file_name="Atlas_Web_AS.pdf", mime="application/pdf", key="dl_atlas")
        st.write("---")
        size = st.text_input("Cut Size", placeholder="e.g., 889x1194 mm", key="sz_atlas")
        qty = st.number_input("Qty", min_value=1, key="qt_atlas")
        if st.button("Add to Cart 🛒", key="add_atlas", type="primary", use_container_width=True): add_to_cart("Atlas Web AS", size, qty)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="b2b-card">', unsafe_allow_html=True)
        if os.path.exists("ex6000.jpg"): st.image("ex6000.jpg")
        st.markdown('<div class="card-title">EX6000 (1.95mm)</div>', unsafe_allow_html=True)
        st.write("**Application:** Sheetfed Presses\n\n**Thickness:** 1.93-1.98mm")
        if pdf_bytes := get_file_bytes("EX6000 1.95mm.pdf"):
            st.download_button("📄 Download Specs", data=pdf_bytes, file_name="EX6000_1.95mm.pdf", mime="application/pdf", key="dl_ex")
        st.write("---")
        size = st.text_input("Cut Size", placeholder="Machine Model", key="sz_ex")
        qty = st.number_input("Qty", min_value=1, key="qt_ex")
        if st.button("Add to Cart 🛒", key="add_ex6000", type="primary", use_container_width=True): add_to_cart("EX6000", size, qty)
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="b2b-card">', unsafe_allow_html=True)
        if os.path.exists("mc740.jpg"): st.image("mc740.jpg")
        st.markdown('<div class="card-title">MC740</div>', unsafe_allow_html=True)
        st.write("**Application:** Cardboard / Heavy Stock\n\n**Thickness:** 1.95mm")
        if pdf_bytes := get_file_bytes("MC740.pdf"):
            st.download_button("📄 Download Specs", data=pdf_bytes, file_name="MC740.pdf", mime="application/pdf", key="dl_mc")
        st.write("---")
        size = st.text_input("Cut Size", placeholder="mm", key="sz_mc")
        qty = st.number_input("Qty", min_value=1, key="qt_mc")
        if st.button("Add to Cart 🛒", key="add_mc740", type="primary", use_container_width=True): add_to_cart("MC740", size, qty)
        st.markdown('</div>', unsafe_allow_html=True)

elif page == "Other Consumables":
    st.markdown('<div class="section-title">Press Consumables & Chemicals</div>', unsafe_allow_html=True)
    consumables = [
        {"name": "Contair Rubber Blankets", "desc": "Economy-grade highly durable blankets for standard commercial runs."},
        {"name": "Trelleborg Blankets", "desc": "World-renowned printing blankets known for exceptional dot reproduction."},
        {"name": "Policrom Calibrated Paper", "desc": "Precision calibrated underpacking paper."},
        {"name": "Varn Anti Set-Off Powder", "desc": "Prevents ink offsetting on high-speed runs."}
    ]
    for item in consumables:
        st.markdown('<div class="b2b-card" style="margin-bottom:15px;">', unsafe_allow_html=True)
        col_desc, col_act = st.columns([3, 1.5])
        with col_desc:
            st.markdown(f"<div class='card-title' style='margin-bottom:5px;'>{item['name']}</div>", unsafe_allow_html=True)
            st.write(item['desc'])
        with col_act:
            spec = st.text_input("Grade / Thickness", key=f"spec_{item['name']}")
            qty = st.number_input("Qty", min_value=1, key=f"qty_{item['name']}")
            if st.button("Add to Cart 🛒", key=f"btn_{item['name']}", use_container_width=True, type="primary"): 
                add_to_cart(item['name'], spec, qty)
        st.markdown('</div>', unsafe_allow_html=True)

elif page == "Technical Hub":
    st.markdown('<div class="section-title">Technical Support</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("🛠️ Troubleshooting: Blanket Smashing"): st.write("Utilize blankets with ThermaSphere layers (like Kinyo EX6000).")
        with st.expander("🛠️️ Troubleshooting: Ink Piling"): st.write("Check your dampening solution pH.")
    with col2:
        with st.expander("📖 Best Practices: Underpacking"): st.write("Always use calibrated packing paper (like Policrom).")

elif page == "Request a Quote":
    st.markdown('<div class="section-title">Your Cart & Quotation</div>', unsafe_allow_html=True)
    if not st.session_state.quote_cart:
        st.info("🛒 Your cart is empty. Please add products from the catalog to proceed.")
    else:
        col_cart, col_qr = st.columns([2, 1])
        with col_cart:
            st.write("### Items in Cart")
            items_text = ""
            for item in st.session_state.quote_cart:
                st.markdown(f"- **{item['item']}** | Size: {item['size']} | Qty: {item['qty']}")
                items_text += f"- {item['item']} (Size: {item['size']}, Qty: {item['qty']})\n"
            if st.button("Clear Cart", type="secondary"):
                st.session_state.quote_cart = []
                st.rerun()
                
        with col_qr:
            st.markdown('<div class="trust-badge" style="text-align: center;">', unsafe_allow_html=True)
            st.markdown("<b style='font-size:1.2rem; color:#0F172A;'>Secure Payment</b><br><br>", unsafe_allow_html=True)
            if os.path.exists(QRC_PATH): 
                st.image(QRC_PATH, caption="Scan to Pay via UPI")
            else:
                st.warning("QR code file not found.")
            st.markdown('</div>', unsafe_allow_html=True)
            
        st.write("---")
        with st.form("quote_form"):
            c1, c2, c3 = st.columns(3)
            name = c1.text_input("Name*")
            company = c2.text_input("Press Name*")
            phone = c3.text_input("Mobile No.*")
            c4, c5 = st.columns([2, 1])
            location = c4.text_input("Delivery Location")
            urgency = c5.selectbox("Urgency", ["Standard Delivery", "Urgent / Same-Day"])
            
            if st.form_submit_button("Generate Quote via WhatsApp", type="primary"):
                if name and company and phone:
                    wa_msg = f"*ORDER/QUOTE*\n*Company:* {company}\n*Contact:* {name}\n*Phone:* {phone}\n*Location:* {location}\n*Urgency:* {urgency}\n*Items:*\n{items_text}"
                    st.link_button("📲 Send Order", url=f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(wa_msg)}", type="primary")
                else:
                    st.error("Please fill in Name, Press Name, and Mobile No.")

elif page == "Contact & Payment":
    st.markdown('<div class="section-title">Corporate Office</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="b2b-card">
        <b style='font-size:1.5rem; color:#0F172A;'>KAVYA INTERNATIONAL</b><br>
        <span style='color:#64748B;'>Offset Printing Consumables Supplier</span><br><br>
        <b>Address:</b> 21/27 Naraina Industrial Area Phase-2, New Delhi - 110028<br>
        <b>Mobile:</b> +91-9716467561, +91-8377983811<br>
        <b>Email:</b> kavya.dhiren@gmail.com<br>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        if os.path.exists(VC_PATH): 
            st.image(VC_PATH, caption="Authorized Representative", use_container_width=True)
