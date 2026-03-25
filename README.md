# 🎯 Optimization Algorithms Visualizer

A professional, interactive Streamlit dashboard showcasing four advanced optimization algorithms with real-time visualizations and parameter controls.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)

---

## 🌐 Live Demo

**Check out the live application:** [https://rahul-algorithm-visualizer.streamlit.app/](https://rahul-algorithm-visualizer.streamlit.app/)

---

## 📋 Overview

This project presents a comprehensive visualization platform for optimization algorithms, designed for students and engineers studying advanced optimization techniques. Each algorithm is implemented with interactive parameter controls and real-time visualizations to understand convergence behavior and algorithm dynamics.

---

## 🧬 Algorithms Implemented

### 1. **Unconstrained Minimization** 📉
Gradient Descent optimizer for single-variable optimization problems.

**Features:**
- Objective function: `f(x) = x² + 4x + 4`
- Real-time optimization path visualization
- Loss convergence tracking
- Parameter controls:
  - Learning rate (0.01 - 1.0)
  - Starting point (-10 to 10)
  - Number of iterations (10 - 200)

**Key Metrics:**
- Final optimized value
- Loss reduction percentage
- Convergence analysis

---

### 2. **Pareto Front** 🎯
Multi-objective optimization for finding non-dominated solutions.

**Features:**
- Two-objective optimization problem
- Decision space and objective space visualization
- Non-dominated solution detection
- Parameter controls:
  - Population size (10 - 100)
  - Generations (10 - 200)
  - Mutation rate (0.01 - 0.5)

**Key Insights:**
- Trade-off analysis between objectives
- Pareto front discovery
- Population distribution

---

### 3. **Genetic Algorithm** 🧬
Evolutionary optimization using genetic operators.

**Features:**
- Population-based stochastic search
- Genetic operators: selection, crossover, mutation
- Convergence tracking
- Parameter controls:
  - Population size (20 - 200)
  - Generations (10 - 300)
  - Mutation rate (0.01 - 0.5)
  - Crossover rate (0.5 - 1.0)

**Key Metrics:**
- Best, average, and worst fitness tracking
- Solution quality progression
- Population diversity analysis

---

### 4. **Simulated Annealing** 🔥
Probabilistic metaheuristic for escaping local minima.

**Features:**
- Temperature-based probability acceptance
- Metropolis criterion implementation
- Acceptance rate monitoring
- Parameter controls:
  - Initial temperature (100 - 1000)
  - Cooling rate (0.90 - 0.99)
  - Iterations per temperature (100 - 1000)
  - Step size (0.1 - 2.0)

**Key Metrics:**
- Cost convergence tracking
- Temperature evolution
- Acceptance rate analysis

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Rahul-331/Optimization_Algorithms_Visualizer.git
cd Optimization_Algorithms_Visualizer
```

2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

### Running the Application

```bash
streamlit run Home.py
```

The application will launch at `http://localhost:8501`

---

## 📁 Project Structure

```
optimization-visualizer/
├── Home.py                              # Main dashboard with tab navigation
├── requirements.txt                     # Python dependencies
├── README.md                            # Project documentation
└── pages/
    ├── 1_Unconstrained_Minimization.py  # Gradient descent implementation
    ├── 2_Pareto_Front.py                # Multi-objective optimization
    ├── 3_Genetic_Algorithm.py           # Evolutionary algorithm
    └── 4_Simulated_Annealing.py         # Temperature-based optimizer
```

---

## 🎨 Features

✨ **Premium User Interface**
- Dark theme with cyan/teal accents
- Glass morphism effects
- Professional typography (Poppins font)
- Responsive layout with sidebar profile

🎛️ **Interactive Controls**
- Real-time parameter adjustment
- Instant visualization updates
- Performance metric tracking
- Algorithm comparison capabilities

📊 **Advanced Visualizations**
- Convergence plots
- Contour maps
- Population distributions
- Multi-objective trade-off analysis

👨‍💻 **Professional Portfolio Design**
- User credentials display
- Expertise showcase
- Tech stack highlights
- Portfolio summary

---

## 📊 Usage Example

### Running Gradient Descent
1. Open the application
2. Navigate to the "Unconstrained Minimization" tab
3. Adjust the learning rate slider (0.01 - 1.0)
4. Set starting point (-10 to 10)
5. Choose number of iterations (10 - 200)
6. View real-time optimization path and loss convergence

### Exploring Pareto Front
1. Go to "Pareto Front" tab
2. Adjust population size and generations
3. View decision space (x, y coordinates)
4. Analyze objective space (f1, f2 values)
5. Identify non-dominated solutions

---

## 📦 Dependencies

- **streamlit** - Web application framework
- **numpy** - Numerical computing
- **matplotlib** - Data visualization

See `requirements.txt` for specific versions.

---

## 🎓 Learning Outcomes

By exploring this visualizer, you'll understand:

✅ Gradient-based optimization methods  
✅ Multi-objective optimization concepts  
✅ Evolutionary algorithm mechanics  
✅ Metaheuristic search strategies  
✅ Convergence behavior analysis  
✅ Parameter sensitivity analysis  
✅ Trade-off analysis in optimization  

---

## 💡 Key Algorithms Overview

| Algorithm | Type | Use Case | Complexity |
|-----------|------|----------|-----------|
| **Gradient Descent** | Deterministic | Single-variable, smooth functions | Low |
| **Pareto Front** | Population-based | Multi-objective problems | High |
| **Genetic Algorithm** | Evolutionary | Non-convex, discrete problems | High |
| **Simulated Annealing** | Probabilistic | Escaping local minima | Medium |

---

## 🔧 Customization

You can easily customize:

1. **Algorithm Parameters** - Modify slider ranges in respective page files
2. **Objective Functions** - Change function definitions in each algorithm
3. **Color Scheme** - Update CSS variables in `Home.py`
4. **Profile Information** - Edit sidebar section in `Home.py`

---

## 📈 Performance Insights

Each algorithm visualization includes:
- **Convergence Analysis** - How quickly the algorithm finds solutions
- **Performance Metrics** - Final values, iterations, error rates
- **Parameter Sensitivity** - Impact of different parameter settings
- **Trade-offs** - Time vs. accuracy, exploration vs. exploitation

---

## 👨‍💻 Author

**Rahul**  
📚 **Institution:** KLH University  
🎓 **Department:** Electronics & Communication Engineering (ECE)  
🔗 **Roll Number:** 2310040040  

**Expertise:**
- Advanced Algorithms & Optimization
- Machine Learning & AI
- Interactive Data Visualization
- Mathematical Modeling

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report issues
- Suggest improvements
- Add new algorithms
- Enhance visualizations

---

## 📞 Support

For questions or suggestions, reach out or create an issue on GitHub.

---

## 🎯 Future Enhancements

- [ ] Constraint handling for optimization
- [ ] Additional algorithms (PSO, Ant Colony, Differential Evolution)
- [ ] Algorithm comparison tools
- [ ] Custom function input
- [ ] Export visualization reports
- [ ] Performance benchmarking suite

---

**Built with ❤️ using Streamlit & Python**
