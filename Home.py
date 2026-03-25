import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Optimization Portfolio", layout="wide", initial_sidebar_state="expanded")

# ----------- SIDEBAR PROFILE -----------
with st.sidebar:
    st.markdown("## 👨‍💻 RAHUL")
    st.markdown("**Optimization Engineer**")
    st.divider()
    
    st.markdown("### Profile")
    st.write("**🎓 Roll Number:** 2310040040")
    st.write("**🏢 Institution:** KLH University")
    st.write("**📚 Department:** ECE (Electronics & Communication)")
    
    st.divider()
    st.markdown("### Expertise")
    st.write("• Advanced Algorithms")
    st.write("• Optimization Techniques")
    st.write("• Machine Learning & AI")
    
    st.divider()
    st.markdown("### Tech Stack")
    col1, col2 = st.columns(2)
    with col1:
        st.write("🐍 Python")
        st.write("🧮 NumPy")
    with col2:
        st.write("🤖 ML")
        st.write("⚡ Optimization")
    
    st.divider()
    st.markdown("### Portfolio")
    st.write("📈 4 Advanced Algorithms")
    st.write("🎯 Real-time Visualizations")
    st.write("⚡ Interactive Dashboard")
    
    st.markdown("---")
    st.markdown("""
    <p style="color: #707080; font-size: 0.8rem; text-align: center; margin-top: 1rem;">
    Built with <span style="color: #ff6b6b;">💡</span> for Advanced Optimization
    </p>
    """, unsafe_allow_html=True)

# ----------- CUSTOM CSS -----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

body {
    background: linear-gradient(135deg, #0a0e27 0%, #1a1a3e 50%, #0f1633 100%);
    background-attachment: fixed;
    color: #e0e0e0;
}

.title {
    font-size: 3.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #00d9ff 0%, #00ffcc 40%, #00f9a0 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-shadow: 0 0 30px rgba(0, 217, 255, 0.3);
    letter-spacing: -1px;
    margin-bottom: 0.5rem;
    font-family: 'Poppins', sans-serif;
}

.subtitle {
    color: #00e6cc;
    font-size: 1.3rem;
    font-weight: 300;
    letter-spacing: 1px;
    margin-bottom: 2rem;
    opacity: 0.95;
}

.card {
    padding: 2rem;
    border-radius: 20px;
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(0, 230, 200, 0.15);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    position: relative;
    overflow: hidden;
}

.card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0, 230, 200, 0.4), transparent);
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 50px rgba(0, 217, 255, 0.25);
    border-color: rgba(0, 230, 200, 0.3);
    background: rgba(255, 255, 255, 0.08);
}

.card h3 {
    color: #00ffcc;
    font-size: 1.4rem;
    font-weight: 700;
    margin-bottom: 0.8rem;
    letter-spacing: 0.5px;
}

.card p {
    color: #b0b0b0;
    font-size: 1rem;
    line-height: 1.6;
    margin-bottom: 1rem;
}

.card ul {
    list-style: none;
    padding: 0;
}

.card li {
    padding: 0.5rem 0;
    color: #a0a0a0;
    margin-left: 1.5rem;
    position: relative;
}

.card li::before {
    content: '▹';
    position: absolute;
    left: 0;
    color: #00e6cc;
    font-weight: 700;
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

.slider-label {
    color: #00e6cc;
    font-weight: 600;
    font-size: 0.95rem;
    letter-spacing: 0.5px;
}

.stSlider [data-testid="stSliderTickBarMax"] {
    color: #00d9ff;
}

.divider {
    height: 2px;
    background: linear-gradient(90deg, transparent, rgba(0, 230, 200, 0.3), transparent);
    margin: 2rem 0;
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

.footer {
    text-align: center;
    color: #707080;
    font-size: 0.85rem;
    letter-spacing: 0.5px;
    margin-top: 3rem;
    padding-top: 2rem;
    border-top: 1px solid rgba(0, 230, 200, 0.1);
}
</style>
""", unsafe_allow_html=True)

# ----------- HEADER -----------
st.markdown('<div style="margin-bottom: 0.5rem;"><p class="title">🚀 Optimization Portfolio</p></div>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Advanced Algorithm Visualizer & Performance Analyzer</p>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Create tabs for different optimization methods
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏠 Home", 
    "📉 Unconstrained Minimization", 
    "🎯 Pareto Front",
    "🧬 Genetic Algorithm",
    "🔥 Simulated Annealing"
])

# ----------- HOME TAB -----------
with tab1:
    st.markdown('<p class="section-title">✨ Welcome to Optimization Lab</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-banner" style="margin-bottom: 2rem;">
    <b style="color: #00ffcc;">⚡ Interactive Optimization Toolkit</b><br>
    Explore advanced algorithms for single and multi-objective optimization problems. Each module provides intuitive parameters, real-time visualizations, and performance metrics.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("""
        <div class="card">
        <h3>📉 Gradient-Based Methods</h3>
        <p>Master classical optimization using calculus and gradient descent approaches.</p>
        <ul>
            <li><strong>Unconstrained Minimization</strong> - Gradient descent with dynamic learning rates</li>
            <li><strong>Critical Point Analysis</strong> - Identify minima, maxima, and saddle points</li>
            <li><strong>Convergence Visualization</strong> - Track optimization paths in real-time</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
        <h3>🧬 Metaheuristic Algorithms</h3>
        <p>Advanced nature-inspired and probabilistic optimization techniques for complex problems.</p>
        <ul>
            <li><strong>Genetic Algorithms</strong> - Population-based evolutionary search</li>
            <li><strong>Simulated Annealing</strong> - Escape local minima with temperature dynamics</li>
            <li><strong>Pareto Optimization</strong> - Handle multi-objective trade-offs</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    st.markdown('<p class="section-title">🎯 Algorithm Overview</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="medium")
    
    with col1:
        st.markdown("""
        <div class="algo-box" style="text-align: center; height: 100%;">
        <div style="font-size: 2.5rem; margin-bottom: 0.8rem;">📉</div>
        <b style="font-size: 1.1rem;">Unconstrained</b><br>
        <span style="color: #808080; font-size: 0.85rem;">Find minima using gradients</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="algo-box" style="text-align: center; height: 100%;">
        <div style="font-size: 2.5rem; margin-bottom: 0.8rem;">🎯</div>
        <b style="font-size: 1.1rem;">Pareto Front</b><br>
        <span style="color: #808080; font-size: 0.85rem;">Multi-objective optimization</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="algo-box" style="text-align: center; height: 100%;">
        <div style="font-size: 2.5rem; margin-bottom: 0.8rem;">🧬</div>
        <b style="font-size: 1.1rem;">Genetic / SA</b><br>
        <span style="color: #808080; font-size: 0.85rem;">Evolutionary & annealing</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-banner" style="margin-top: 2rem;">
    <b style="color: #00ffcc;">💡 Pro Tip:</b> Select any algorithm tab above to configure parameters and run visualizations. Each algorithm displays real-time convergence plots and performance metrics.
    </div>
    """, unsafe_allow_html=True)

# ----------- UNCONSTRAINED MINIMIZATION TAB -----------
with tab2:
    st.markdown('<p class="section-title">📉 Gradient Descent Optimizer</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-banner">
    <b>📊 Algorithm:</b> Unconstrained minimization using gradient descent. Adjust learning rate and iterations to observe convergence behavior.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
        st.markdown('<div class="algo-box"><b>⚙️ Configuration</b></div>', unsafe_allow_html=True)
        lr = st.slider("Learning Rate", 0.01, 1.0, 0.1, key="lr_unconstrained", help="Controls the step size during optimization")
        start = st.slider("Start Point", -10.0, 10.0, 5.0, key="start_unconstrained", help="Initial point for optimizer")
        iterations = st.slider("Iterations", 10, 200, 50, key="iter_unconstrained", help="Number of optimization steps")
        
    with col2:
        st.markdown('<div class="algo-box"><b>📋 Current Settings</b></div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div style="padding: 0.5rem; color: #a0a0a0; font-size: 0.9rem; line-height: 1.8;">
        <span style="color: #00ffcc;"><b>Learning Rate:</b></span> {lr}<br>
        <span style="color: #00ffcc;"><b>Starting Point:</b></span> {start:.2f}<br>
        <span style="color: #00ffcc;"><b>Max Iterations:</b></span> {iterations}
        </div>
        """, unsafe_allow_html=True)
    
    # Define objective function
    def f_unconstrained(x):
        return x**2 + 4*x + 4
    
    def f_prime(x):
        return 2*x + 4
    
    if st.button("▶️ Run Optimization", key="run_unconstrained"):
        with st.spinner("Computing optimization path..."):
            x_vals = np.linspace(-10, 10, 200)
            y_vals = f_unconstrained(x_vals)
            
            x_curr = start
            history = [x_curr]
            loss_history = [f_unconstrained(x_curr)]
            
            for _ in range(iterations):
                grad = f_prime(x_curr)
                x_curr -= lr * grad
                history.append(x_curr)
                loss_history.append(f_unconstrained(x_curr))
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig, ax = plt.subplots(figsize=(8, 5), facecolor='#0a0e27', edgecolor='#00e6b8')
                ax.plot(x_vals, y_vals, color='#00d9ff', linewidth=3, label='f(x) = x² + 4x + 4')
                ax.scatter(history, loss_history, color='#00ffcc', s=80, alpha=0.85, label='Optimization Path', edgecolors='#00d9ff', linewidth=1.5)
                ax.plot(history, loss_history, color='#ff6b6b', alpha=0.4, linewidth=2)
                ax.set_xlabel("x", color="#00e6cc", fontsize=11, fontweight='600')
                ax.set_ylabel("f(x)", color="#00e6cc", fontsize=11, fontweight='600')
                ax.set_title("Optimization Path", color="#00ffcc", fontsize=13, fontweight='bold')
                ax.grid(True, alpha=0.15, color='#00e6b8', linestyle='--', linewidth=0.5)
                ax.legend(facecolor='#1a1a3e', edgecolor='#00e6cc', labelcolor='#b0e0d0', loc='upper right', framealpha=0.95)
                ax.set_facecolor('#1a1a3e')
                for spine in ax.spines.values():
                    spine.set_edgecolor('#00e6cc')
                    spine.set_alpha(0.3)
                st.pyplot(fig)
            
            with col2:
                fig2, ax2 = plt.subplots(figsize=(8, 5), facecolor='#0a0e27', edgecolor='#00e6b8')
                ax2.plot(np.arange(len(loss_history)), loss_history, color='#ff6b6b', linewidth=3, marker='o', markersize=5, label='Loss Trend')
                ax2.fill_between(np.arange(len(loss_history)), loss_history, alpha=0.2, color='#ff6b6b')
                ax2.set_xlabel("Iteration", color="#00e6cc", fontsize=11, fontweight='600')
                ax2.set_ylabel("Loss", color="#00e6cc", fontsize=11, fontweight='600')
                ax2.set_title("Loss Over Iterations", color="#00ffcc", fontsize=13, fontweight='bold')
                ax2.grid(True, alpha=0.15, color='#00e6b8', linestyle='--', linewidth=0.5)
                ax2.legend(facecolor='#1a1a3e', edgecolor='#00e6cc', labelcolor='#b0e0d0', framealpha=0.95)
                ax2.set_facecolor('#1a1a3e')
                for spine in ax2.spines.values():
                    spine.set_edgecolor('#00e6cc')
                    spine.set_alpha(0.3)
                st.pyplot(fig2)
            
            st.markdown(f"""
            <div class="success-box">
            <b>✅ Optimization Complete!</b><br>
            <b>Final x:</b> {x_curr:.6f}<br>
            <b>Final Loss:</b> {loss_history[-1]:.6f}<br>
            <b>Total Iterations:</b> {len(history)-1}<br>
            <b>Loss Reduction:</b> {((loss_history[0] - loss_history[-1]) / loss_history[0] * 100):.2f}%
            </div>
            """, unsafe_allow_html=True)

# ----------- PARETO FRONT TAB -----------
with tab3:
    st.markdown('<p class="section-title">🎯 Multi-Objective Pareto Optimizer</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-banner">
    <b>📊 Algorithm:</b> Evolutionary multi-objective optimization. Find trade-off solutions between conflicting objectives using mutation and selection.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
        st.markdown('<div class="algo-box"><b>⚙️ Configuration</b></div>', unsafe_allow_html=True)
        population_size = st.slider("Population Size", 10, 100, 50, key="pop_pareto", help="Number of candidate solutions")
        generations = st.slider("Generations", 10, 200, 50, key="gen_pareto", help="Evolution iterations")
        mutation_rate = st.slider("Mutation Rate", 0.01, 0.5, 0.1, key="mut_pareto", help="Genetic mutation probability")
    
    with col2:
        st.markdown('<div class="algo-box"><b>📋 Current Settings</b></div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div style="padding: 0.5rem; color: #a0a0a0; font-size: 0.9rem; line-height: 1.8;">
        <span style="color: #00ffcc;"><b>Population:</b></span> {population_size} solutions<br>
        <span style="color: #00ffcc;"><b>Generations:</b></span> {generations}<br>
        <span style="color: #00ffcc;"><b>Mutation Rate:</b></span> {mutation_rate:.2f}
        </div>
        """, unsafe_allow_html=True)
    
    def objective1(x, y):
        return (x - 1) ** 2 + (y - 1) ** 2
    
    def objective2(x, y):
        return (x + 1) ** 2 + (y + 1) ** 2
    
    if st.button("▶️ Run Multi-Objective Optimization", key="run_pareto"):
        with st.spinner("Computing Pareto Front..."):
            np.random.seed(42)
            population = np.random.uniform(-5, 5, (population_size, 2))
            
            pareto_fronts = []
            
            for gen in range(generations):
                f1_vals = np.array([objective1(ind[0], ind[1]) for ind in population])
                f2_vals = np.array([objective2(ind[0], ind[1]) for ind in population])
                
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
                
                selected = np.random.choice(len(population), population_size // 2, replace=True)
                offspring = population[selected].copy()
                offspring += np.random.normal(0, mutation_rate, offspring.shape)
                offspring = np.clip(offspring, -5, 5)
                
                population = np.vstack([population, offspring])
                population = population[:population_size]
            
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
            <b>Population Size:</b> {population_size}
            </div>
            """, unsafe_allow_html=True)

# ----------- GENETIC ALGORITHM TAB -----------
with tab4:
    st.markdown('<p class="section-title">🧬 Genetic Algorithm Optimizer</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-banner">
    <b>📊 Algorithm:</b> Population-based evolutionary search with selection, crossover, and mutation operators.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
        st.markdown('<div class="algo-box"><b>⚙️ Configuration</b></div>', unsafe_allow_html=True)
        population_size_ga = st.slider("Population Size", 20, 200, 100, key="pop_ga", help="Number of individuals in population")
        generations_ga = st.slider("Generations", 10, 300, 100, key="gen_ga", help="Evolution cycles")
        mutation_rate_ga = st.slider("Mutation Rate", 0.01, 0.5, 0.1, key="mut_ga", help="Genetic mutation probability")
        crossover_rate_ga = st.slider("Crossover Rate", 0.5, 1.0, 0.8, key="cross_ga", help="Genetic recombination probability")
    
    with col2:
        st.markdown('<div class="algo-box"><b>📋 Current Settings</b></div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div style="padding: 0.5rem; color: #a0a0a0; font-size: 0.9rem; line-height: 1.8;">
        <span style="color: #00ffcc;"><b>Population:</b></span> {population_size_ga} individuals<br>
        <span style="color: #00ffcc;"><b>Generations:</b></span> {generations_ga}<br>
        <span style="color: #00ffcc;"><b>Mutation Rate:</b></span> {mutation_rate_ga:.2f}<br>
        <span style="color: #00ffcc;"><b>Crossover Rate:</b></span> {crossover_rate_ga:.2f}
        </div>
        """, unsafe_allow_html=True)
    
    def sphere_function(x):
        return np.sum(x**2)
    
    def fitness_ga(individual):
        return 1 / (1 + sphere_function(individual))
    
    if st.button("▶️ Run Genetic Algorithm", key="run_ga"):
        with st.spinner("Running Genetic Algorithm..."):
            np.random.seed(42)
            population_ga = np.random.uniform(-5, 5, (population_size_ga, 2))
            
            best_fitness_history = []
            avg_fitness_history = []
            worst_fitness_history = []
            
            for gen in range(generations_ga):
                fitnesses = np.array([fitness_ga(ind) for ind in population_ga])
                
                best_fitness_history.append(np.max(fitnesses))
                avg_fitness_history.append(np.mean(fitnesses))
                worst_fitness_history.append(np.min(fitnesses))
                
                fitnesses = np.clip(fitnesses, 0, None)
                probabilities = fitnesses / np.sum(fitnesses) if np.sum(fitnesses) > 0 else np.ones(len(fitnesses)) / len(fitnesses)
                selected_indices = np.random.choice(population_size_ga, population_size_ga, p=probabilities)
                
                new_population = []
                
                for i in range(population_size_ga // 2):
                    parent1 = population_ga[selected_indices[2*i]].copy()
                    parent2 = population_ga[selected_indices[2*i + 1]].copy()
                    
                    if np.random.rand() < crossover_rate_ga:
                        alpha = np.random.rand()
                        child1 = alpha * parent1 + (1 - alpha) * parent2
                        child2 = alpha * parent2 + (1 - alpha) * parent1
                    else:
                        child1, child2 = parent1.copy(), parent2.copy()
                    
                    if np.random.rand() < mutation_rate_ga:
                        child1 += np.random.normal(0, 0.5, child1.shape)
                    if np.random.rand() < mutation_rate_ga:
                        child2 += np.random.normal(0, 0.5, child2.shape)
                    
                    child1 = np.clip(child1, -5, 5)
                    child2 = np.clip(child2, -5, 5)
                    
                    new_population.extend([child1, child2])
                
                population_ga = np.array(new_population[:population_size_ga])
            
            final_fitnesses = np.array([fitness_ga(ind) for ind in population_ga])
            best_idx = np.argmax(final_fitnesses)
            best_solution_ga = population_ga[best_idx]
            best_value_ga = sphere_function(best_solution_ga)
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig, ax = plt.subplots(figsize=(8, 5), facecolor='#0e1117', edgecolor='#00e6b8')
                ax.plot(best_fitness_history, color='#00ffcc', linewidth=2.5, label='Best Fitness')
                ax.fill_between(range(len(avg_fitness_history)), worst_fitness_history, best_fitness_history, alpha=0.3, color='#00c6ff', label='Fitness Range')
                ax.plot(avg_fitness_history, color='#ff6b6b', linewidth=2, linestyle='--', label='Average Fitness')
                ax.set_xlabel("Generation", color="#9ae6b4")
                ax.set_ylabel("Fitness", color="#9ae6b4")
                ax.set_title("Genetic Algorithm Convergence", color="#00e6b8", fontsize=14, fontweight='bold')
                ax.grid(True, alpha=0.2, color='#00e6b8')
                ax.legend(facecolor='#0b0f15', edgecolor='#00e6b8', labelcolor='#9ae6b4')
                ax.set_facecolor('#0b0f15')
                st.pyplot(fig)
            
            with col2:
                fig2, ax2 = plt.subplots(figsize=(8, 5), facecolor='#0e1117', edgecolor='#00e6b8')
                
                x = np.linspace(-5, 5, 50)
                y = np.linspace(-5, 5, 50)
                X, Y = np.meshgrid(x, y)
                Z = X**2 + Y**2
                
                contour = ax2.contour(X, Y, Z, levels=15, colors='#00c6ff', alpha=0.4, linewidths=0.5)
                ax2.scatter(population_ga[:, 0], population_ga[:, 1], color='#ff6b6b', s=50, alpha=0.6, label='Population')
                ax2.scatter(best_solution_ga[0], best_solution_ga[1], color='#00ffcc', s=200, marker='*', edgecolor='#00e6b8', linewidth=2, label='Best Solution', zorder=5)
                
                ax2.set_xlabel("X1", color="#9ae6b4")
                ax2.set_ylabel("X2", color="#9ae6b4")
                ax2.set_title("Final Population Distribution", color="#00e6b8", fontsize=14, fontweight='bold')
                ax2.grid(True, alpha=0.2, color='#00e6b8')
                ax2.legend(facecolor='#0b0f15', edgecolor='#00e6b8', labelcolor='#9ae6b4')
                ax2.set_facecolor('#0b0f15')
                st.pyplot(fig2)
            
            st.markdown(f"""
            <div class="success-box">
            <b>✅ Genetic Algorithm Complete!</b><br>
            <b>Best Solution:</b> x1={best_solution_ga[0]:.6f}, x2={best_solution_ga[1]:.6f}<br>
            <b>Best Objective Value:</b> {best_value_ga:.6f}<br>
            <b>Total Generations:</b> {generations_ga}<br>
            <b>Final Best Fitness:</b> {best_fitness_history[-1]:.6f}
            </div>
            """, unsafe_allow_html=True)

# ----------- SIMULATED ANNEALING TAB -----------
with tab5:
    st.markdown('<p class="section-title">🔥 Simulated Annealing Metaheuristic</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-banner">
    <b>📊 Algorithm:</b> Probabilistic optimization inspired by metal annealing. Accepts worse solutions with decreasing probability to escape local minima.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
        st.markdown('<div class="algo-box"><b>⚙️ Configuration</b></div>', unsafe_allow_html=True)
        initial_temp = st.slider("Initial Temperature", 100, 1000, 500, key="temp_sa", help="Starting probability for worse solutions")
        cooling_rate = st.slider("Cooling Rate", 0.90, 0.99, 0.95, key="cool_sa", help="Temperature reduction factor")
        iterations_sa = st.slider("Iterations per Temperature", 100, 1000, 500, key="iter_sa", help="Steps at each temperature level")
        step_size = st.slider("Step Size", 0.1, 2.0, 0.5, key="step_sa", help="Solution perturbation magnitude")
    
    with col2:
        st.markdown('<div class="algo-box"><b>📋 Current Settings</b></div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div style="padding: 0.5rem; color: #a0a0a0; font-size: 0.9rem; line-height: 1.8;">
        <span style="color: #00ffcc;"><b>Initial Temp:</b></span> {initial_temp}°<br>
        <span style="color: #00ffcc;"><b>Cooling Rate:</b></span> {cooling_rate:.4f}<br>
        <span style="color: #00ffcc;"><b>Iterations/Temp:</b></span> {iterations_sa}<br>
        <span style="color: #00ffcc;"><b>Step Size:</b></span> {step_size:.2f}
        </div>
        """, unsafe_allow_html=True)
    
    def objective_function_sa(x):
        n = len(x)
        return 10 * n + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))
    
    if st.button("▶️ Run Simulated Annealing", key="run_sa"):
        with st.spinner("Running Simulated Annealing..."):
            np.random.seed(42)
            current_solution = np.random.uniform(-5.12, 5.12, 2)
            current_cost = objective_function_sa(current_solution)
            
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
                for iteration in range(iterations_sa):
                    neighbor = current_solution + np.random.normal(0, step_size, len(current_solution))
                    neighbor = np.clip(neighbor, -5.12, 5.12)
                    
                    neighbor_cost = objective_function_sa(neighbor)
                    delta_cost = neighbor_cost - current_cost
                    
                    if delta_cost < 0 or np.exp(-delta_cost / temperature) > np.random.rand():
                        current_solution = neighbor
                        current_cost = neighbor_cost
                        accepted_in_temp += 1
                        accepted_count += 1
                    
                    total_count += 1
                    
                    if current_cost < best_cost:
                        best_solution = current_solution.copy()
                        best_cost = current_cost
                    
                    cost_history.append(current_cost)
                    best_history.append(best_cost)
                    temp_history.append(temperature)
                
                acceptance_rate = accepted_in_temp / iterations_sa
                acceptance_history.append(acceptance_rate)
                
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
            <b>Acceptance Rate:</b> {(accepted_count/total_count)*100:.2f}%
            </div>
            """, unsafe_allow_html=True)

st.write("---")
st.markdown("""
<div class="footer">
👨‍💻 <b>Optimization Lab</b> | Advanced Algorithm Visualizer<br>
<span style="font-size: 0.8rem; color: #606070;">Built with Streamlit • Powered by NumPy & Matplotlib</span>
</div>
""", unsafe_allow_html=True)