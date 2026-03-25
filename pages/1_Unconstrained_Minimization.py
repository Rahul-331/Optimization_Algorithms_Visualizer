import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

body {
    background: linear-gradient(135deg, #0a0e27 0%, #1a1a3e 50%, #0f1633 100%);
    background-attachment: fixed;
}

.section-title {
    color: #00ffcc;
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 1.5rem;
    letter-spacing: 0.5px;
    position: relative;
    padding-bottom: 0.8rem;
}

.section-title::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 60px;
    height: 3px;
    background: linear-gradient(90deg, #00ffcc, #00d9ff, transparent);
    border-radius: 2px;
}

.algo-box {
    padding: 1.5rem;
    border-radius: 15px;
    background: rgba(0, 217, 255, 0.08);
    border: 1.5px solid rgba(0, 230, 200, 0.25);
    margin: 1rem 0;
    backdrop-filter: blur(5px);
    transition: all 0.3s ease;
}

.algo-box:hover {
    background: rgba(0, 217, 255, 0.12);
    border-color: rgba(0, 230, 200, 0.4);
}

.algo-box b {
    color: #00ffcc;
    font-weight: 700;
    font-size: 1.05rem;
}

.success-box {
    padding: 1.8rem;
    border-radius: 15px;
    background: linear-gradient(135deg, rgba(0, 100, 80, 0.15) 0%, rgba(0, 150, 120, 0.08) 100%);
    border-left: 5px solid #00e6cc;
    border: 1px solid rgba(0, 230, 200, 0.2);
    color: #b0e0d0;
    font-weight: 500;
    line-height: 1.8;
    box-shadow: 0 8px 32px rgba(0, 230, 200, 0.1);
}

.success-box b {
    color: #00ffcc;
    font-weight: 700;
}

.info-banner {
    padding: 1.5rem;
    border-radius: 15px;
    background: linear-gradient(135deg, rgba(0, 157, 255, 0.1), rgba(0, 230, 200, 0.05));
    border: 1px solid rgba(0, 200, 200, 0.2);
    color: #a0d0e0;
    font-size: 0.95rem;
    backdrop-filter: blur(5px);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="section-title">📉 Gradient Descent Optimizer</p>', unsafe_allow_html=True)

st.markdown("""
<div class="info-banner">
<b>📊 Algorithm:</b> Unconstrained minimization using gradient descent. Adjust learning rate and iterations to observe convergence behavior.
</div>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.header("⚙️ Controls")
lr = st.sidebar.slider("Learning Rate", 0.01, 1.0, 0.1)
start = st.sidebar.slider("Start", -10.0, 10.0, 5.0)
iterations = st.sidebar.slider("Iterations", 10, 100, 30)

def f(x):
    return x**2 + 4*x + 4

if st.button("Run"):

    x_vals = np.linspace(-10, 10, 200)
    y_vals = f(x_vals)

    x_curr = start
    history = [x_curr]

    for _ in range(iterations):
        grad = 2*x_curr + 4
        x_curr -= lr * grad
        history.append(x_curr)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals)
    ax.scatter(history, [f(x) for x in history])
    ax.set_title("Optimization Path")
    ax.grid()

    st.pyplot(fig)

    st.success(f"Minimum at x = {x_curr:.4f}")