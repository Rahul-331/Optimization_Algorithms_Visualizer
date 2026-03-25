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

st.markdown('<p class="section-title">🎯 Multi-Objective Optimization - Pareto Front</p>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.markdown('<div class="algo-box"><b>⚙️ Parameters</b></div>', unsafe_allow_html=True)
    population_size = st.slider("Population Size", 10, 100, 50, key="pop_pareto")
    generations = st.slider("Generations", 10, 200, 50, key="gen_pareto")
    mutation_rate = st.slider("Mutation Rate", 0.01, 0.5, 0.1, key="mut_pareto")

with col2:
    st.markdown('<div class="algo-box"><b>📊 Config</b></div>', unsafe_allow_html=True)
    st.write(f"**Population Size:** {population_size}")
    st.write(f"**Generations:** {generations}")
    st.write(f"**Mutation Rate:** {mutation_rate:.2f}")

# Multi-objective functions
def objective1(x, y):
    return (x - 1) ** 2 + (y - 1) ** 2

def objective2(x, y):
    return (x + 1) ** 2 + (y + 1) ** 2

def is_dominated(point, population):
    """Check if a point is dominated by any point in the population"""
    for other in population:
        if all(objective_i(other) <= objective_i(point) for objective_i in [objective1, objective2]):
            if any(objective_i(other) < objective_i(point) for objective_i in [objective1, objective2]):
                return True
    return False

if st.button("▶️ Run Multi-Objective Optimization", key="run_pareto"):
    with st.spinner("Computing Pareto Front..."):
        # Initialize population
        np.random.seed(42)
        population = np.random.uniform(-5, 5, (population_size, 2))
        
        pareto_fronts = []
        
        for gen in range(generations):
            # Calculate objectives
            f1_vals = np.array([objective1(ind[0], ind[1]) for ind in population])
            f2_vals = np.array([objective2(ind[0], ind[1]) for ind in population])
            
            # Find non-dominated solutions
            pareto_front = []
            for i, individual in enumerate(population):
                point = individual
                dominated = False
                for j, other in enumerate(population):
                    if i != j:
                        if f1_vals[j] <= f1_vals[i] and f2_vals[j] <= f2_vals[i]:
                            if f1_vals[j] < f1_vals[i] or f2_vals[j] < f2_vals[i]:
                                dominated = True
                                break
                if not dominated:
                    pareto_front.append((point, f1_vals[i], f2_vals[i]))
            
            pareto_fronts.append(pareto_front)
            
            # Selection and mutation
            selected = np.random.choice(len(population), population_size // 2, replace=True)
            offspring = population[selected].copy()
            offspring += np.random.normal(0, mutation_rate, offspring.shape)
            offspring = np.clip(offspring, -5, 5)
            
            population = np.vstack([population, offspring])
            population = population[:population_size]
        
        # Final Pareto front
        final_pareto = pareto_fronts[-1] if pareto_fronts else []
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig, ax = plt.subplots(figsize=(8, 6), facecolor='#0e1117', edgecolor='#00e6b8')
            
            if final_pareto:
                points = np.array([p[0] for p in final_pareto])
                ax.scatter(points[:, 0], points[:, 1], color='#00ffcc', s=100, alpha=0.8, label='Pareto Front', edgecolor='#00c6ff', linewidth=2)
            
            ax.scatter(population[:, 0], population[:, 1], color='#ff6b6b', s=30, alpha=0.3, label='Population')
            
            ax.set_xlabel("X", color="#9ae6b4")
            ax.set_ylabel("Y", color="#9ae6b4")
            ax.set_title("Pareto Front in Decision Space", color="#00e6b8", fontsize=14, fontweight='bold')
            ax.grid(True, alpha=0.2, color='#00e6b8')
            ax.legend(facecolor='#0b0f15', edgecolor='#00e6b8', labelcolor='#9ae6b4')
            ax.set_facecolor('#0b0f15')
            st.pyplot(fig)
        
        with col2:
            fig2, ax2 = plt.subplots(figsize=(8, 6), facecolor='#0e1117', edgecolor='#00e6b8')
            
            if final_pareto:
                f1_pareto = [p[1] for p in final_pareto]
                f2_pareto = [p[2] for p in final_pareto]
                ax2.scatter(f1_pareto, f2_pareto, color='#00ffcc', s=100, alpha=0.8, label='Pareto Front', edgecolor='#00c6ff', linewidth=2)
                ax2.plot(f1_pareto, f2_pareto, color='#ff6b6b', alpha=0.3, linewidth=1)
            
            ax2.set_xlabel("Objective 1", color="#9ae6b4")
            ax2.set_ylabel("Objective 2", color="#9ae6b4")
            ax2.set_title("Pareto Front in Objective Space", color="#00e6b8", fontsize=14, fontweight='bold')
            ax2.grid(True, alpha=0.2, color='#00e6b8')
            ax2.legend(facecolor='#0b0f15', edgecolor='#00e6b8', labelcolor='#9ae6b4')
            ax2.set_facecolor('#0b0f15')
            st.pyplot(fig2)
        
        st.markdown(f"""
        <div class="success-box">
        <b>✅ Pareto Optimization Complete!</b><br>
        <b>Final Pareto Front Size:</b> {len(final_pareto)}<br>
        <b>Total Generations:</b> {generations}<br>
        <b>Population Size:</b> {population_size}<br>
        <b>Solutions Count:</b> {len(pareto_fronts[-1]) if pareto_fronts else 0}
        </div>
        """, unsafe_allow_html=True)
