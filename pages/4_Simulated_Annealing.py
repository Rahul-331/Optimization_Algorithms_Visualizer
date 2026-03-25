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

st.markdown('<p class="section-title">🔥 Simulated Annealing Optimizer</p>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.markdown('<div class="algo-box"><b>⚙️ Parameters</b></div>', unsafe_allow_html=True)
    initial_temp = st.slider("Initial Temperature", 100, 1000, 500, key="temp_sa")
    cooling_rate = st.slider("Cooling Rate", 0.90, 0.99, 0.95, key="cool_sa")
    iterations = st.slider("Iterations per Temperature", 100, 1000, 500, key="iter_sa")
    step_size = st.slider("Step Size", 0.1, 2.0, 0.5, key="step_sa")

with col2:
    st.markdown('<div class="algo-box"><b>📊 Config</b></div>', unsafe_allow_html=True)
    st.write(f"**Initial Temperature:** {initial_temp}")
    st.write(f"**Cooling Rate:** {cooling_rate:.4f}")
    st.write(f"**Iterations/Temp:** {iterations}")
    st.write(f"**Step Size:** {step_size:.2f}")

# Objective function (Rastrigin's function for harder problem)
def objective_function(x):
    """Rastrigin function - multiple local minima"""
    n = len(x)
    return 10 * n + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))

if st.button("▶️ Run Simulated Annealing", key="run_sa"):
    with st.spinner("Running Simulated Annealing..."):
        # Initialize
        np.random.seed(42)
        current_solution = np.random.uniform(-5.12, 5.12, 2)
        current_cost = objective_function(current_solution)
        
        best_solution = current_solution.copy()
        best_cost = current_cost
        
        temperature = initial_temp
        cost_history = [current_cost]
        temp_history = [temperature]
        best_history = [best_cost]
        acceptance_history = []
        
        accepted_count = 0
        total_count = 0
        
        while temperature > 1e-3:
            accepted_in_temp = 0
            for iteration in range(iterations):
                # Generate neighbor solution
                neighbor = current_solution + np.random.normal(0, step_size, len(current_solution))
                neighbor = np.clip(neighbor, -5.12, 5.12)
                
                neighbor_cost = objective_function(neighbor)
                delta_cost = neighbor_cost - current_cost
                
                # Acceptance criterion
                if delta_cost < 0 or np.exp(-delta_cost / temperature) > np.random.rand():
                    current_solution = neighbor
                    current_cost = neighbor_cost
                    accepted_in_temp += 1
                    accepted_count += 1
                
                total_count += 1
                
                # Update best
                if current_cost < best_cost:
                    best_solution = current_solution.copy()
                    best_cost = current_cost
                
                cost_history.append(current_cost)
                best_history.append(best_cost)
                temp_history.append(temperature)
            
            acceptance_rate = accepted_in_temp / iterations
            acceptance_history.append(acceptance_rate)
            
            # Cool down
            temperature *= cooling_rate
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig, ax = plt.subplots(figsize=(8, 5), facecolor='#0e1117', edgecolor='#00e6b8')
            ax.plot(cost_history[::10], color='#ff6b6b', linewidth=1.5, alpha=0.7, label='Current Cost')
            ax.plot(best_history[::10], color='#00ffcc', linewidth=2.5, label='Best Cost')
            ax.set_xlabel("Iteration (every 10th)", color="#9ae6b4")
            ax.set_ylabel("Cost", color="#9ae6b4")
            ax.set_title("Simulated Annealing Convergence", color="#00e6b8", fontsize=14, fontweight='bold')
            ax.grid(True, alpha=0.2, color='#00e6b8')
            ax.legend(facecolor='#0b0f15', edgecolor='#00e6b8', labelcolor='#9ae6b4')
            ax.set_facecolor('#0b0f15')
            st.pyplot(fig)
        
        with col2:
            fig2, ax2 = plt.subplots(figsize=(8, 5), facecolor='#0e1117', edgecolor='#00e6b8')
            ax2.plot(acceptance_history, color='#00c6ff', linewidth=2.5, marker='o', markersize=4)
            ax2.set_xlabel("Temperature Step", color="#9ae6b4")
            ax2.set_ylabel("Acceptance Rate", color="#9ae6b4")
            ax2.set_title("Acceptance Rate vs Temperature", color="#00e6b8", fontsize=14, fontweight='bold')
            ax2.grid(True, alpha=0.2, color='#00e6b8')
            ax2.set_facecolor('#0b0f15')
            ax2.set_ylim([0, 1.05])
            st.pyplot(fig2)
        
        st.markdown(f"""
        <div class="success-box">
        <b>✅ Simulated Annealing Complete!</b><br>
        <b>Best Solution:</b> x1={best_solution[0]:.6f}, x2={best_solution[1]:.6f}<br>
        <b>Best Cost:</b> {best_cost:.6f}<br>
        <b>Total Iterations:</b> {total_count}<br>
        <b>Acceptance Rate:</b> {(accepted_count/total_count)*100:.2f}%<br>
        <b>Initial Cost:</b> {cost_history[0]:.6f} → <b>Final Cost:</b> {best_cost:.6f}
        </div>
        """, unsafe_allow_html=True)
