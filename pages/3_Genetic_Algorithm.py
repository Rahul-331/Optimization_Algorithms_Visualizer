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

st.markdown('<p class="section-title">🧬 Genetic Algorithm Optimizer</p>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.markdown('<div class="algo-box"><b>⚙️ Parameters</b></div>', unsafe_allow_html=True)
    population_size = st.slider("Population Size", 20, 200, 100, key="pop_ga")
    generations = st.slider("Generations", 10, 300, 100, key="gen_ga")
    mutation_rate = st.slider("Mutation Rate", 0.01, 0.5, 0.1, key="mut_ga")
    crossover_rate = st.slider("Crossover Rate", 0.5, 1.0, 0.8, key="cross_ga")

with col2:
    st.markdown('<div class="algo-box"><b>📊 Config</b></div>', unsafe_allow_html=True)
    st.write(f"**Population Size:** {population_size}")
    st.write(f"**Generations:** {generations}")
    st.write(f"**Mutation Rate:** {mutation_rate:.2f}")
    st.write(f"**Crossover Rate:** {crossover_rate:.2f}")

# Objective function (Rastrigin's function - harder optimization problem)
def sphere_function(x):
    return np.sum(x**2)

def fitness(individual):
    """Lower fitness is better (minimization)"""
    return 1 / (1 + sphere_function(individual))

if st.button("▶️ Run Genetic Algorithm", key="run_ga"):
    with st.spinner("Running Genetic Algorithm..."):
        # Initialize population
        np.random.seed(42)
        population = np.random.uniform(-5, 5, (population_size, 2))
        
        best_fitness_history = []
        avg_fitness_history = []
        worst_fitness_history = []
        
        for gen in range(generations):
            # Evaluate fitness
            fitnesses = np.array([fitness(ind) for ind in population])
            
            # Track best, average, worst
            best_fitness_history.append(np.max(fitnesses))
            avg_fitness_history.append(np.mean(fitnesses))
            worst_fitness_history.append(np.min(fitnesses))
            
            # Selection (roulette wheel)
            fitnesses = np.clip(fitnesses, 0, None)
            probabilities = fitnesses / np.sum(fitnesses) if np.sum(fitnesses) > 0 else np.ones(len(fitnesses)) / len(fitnesses)
            selected_indices = np.random.choice(population_size, population_size, p=probabilities)
            
            new_population = []
            
            for i in range(population_size // 2):
                parent1 = population[selected_indices[2*i]].copy()
                parent2 = population[selected_indices[2*i + 1]].copy()
                
                # Crossover
                if np.random.rand() < crossover_rate:
                    alpha = np.random.rand()
                    child1 = alpha * parent1 + (1 - alpha) * parent2
                    child2 = alpha * parent2 + (1 - alpha) * parent1
                else:
                    child1, child2 = parent1.copy(), parent2.copy()
                
                # Mutation
                if np.random.rand() < mutation_rate:
                    child1 += np.random.normal(0, 0.5, child1.shape)
                if np.random.rand() < mutation_rate:
                    child2 += np.random.normal(0, 0.5, child2.shape)
                
                # Clip to bounds
                child1 = np.clip(child1, -5, 5)
                child2 = np.clip(child2, -5, 5)
                
                new_population.extend([child1, child2])
            
            population = np.array(new_population[:population_size])
        
        # Find best solution
        final_fitnesses = np.array([fitness(ind) for ind in population])
        best_idx = np.argmax(final_fitnesses)
        best_solution = population[best_idx]
        best_value = sphere_function(best_solution)
        
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
            # 2D visualization
            fig2, ax2 = plt.subplots(figsize=(8, 5), facecolor='#0e1117', edgecolor='#00e6b8')
            
            # Create mesh for background
            x = np.linspace(-5, 5, 50)
            y = np.linspace(-5, 5, 50)
            X, Y = np.meshgrid(x, y)
            Z = X**2 + Y**2
            
            contour = ax2.contour(X, Y, Z, levels=15, colors='#00c6ff', alpha=0.4, linewidths=0.5)
            ax2.scatter(population[:, 0], population[:, 1], color='#ff6b6b', s=50, alpha=0.6, label='Population')
            ax2.scatter(best_solution[0], best_solution[1], color='#00ffcc', s=200, marker='*', edgecolor='#00e6b8', linewidth=2, label='Best Solution', zorder=5)
            
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
        <b>Best Solution:</b> x1={best_solution[0]:.6f}, x2={best_solution[1]:.6f}<br>
        <b>Best Objective Value:</b> {best_value:.6f}<br>
        <b>Total Generations:</b> {generations}<br>
        <b>Final Best Fitness:</b> {best_fitness_history[-1]:.6f}
        </div>
        """, unsafe_allow_html=True)
