# Interview Presentation: Envisioned Contribution to HET Systems Centre
## Position 2: Internet of Things and Automation

**Sangeeta Kakati**  
**PhD in Computer Science**  
**ORCID: 0000-0002-4795-7489**

---

## Slide 1: Self-Introduction (2 minutes)

### Research Background
- **Current**: Postdoctoral Researcher, University of Luxembourg (SnT)
- **Expertise**: Edge computing, IoT systems, containerization, WebAssembly
- **Industry Experience**: ACE5G project with Proximus (telecom), IoT lighting systems
- **Publications**: 15+ papers in top-tier venues (IEEE, ACM)
- **Skills**: Python, C++, WebAssembly, Kubernetes, Docker, ML/AI

### Key Achievements
- Designed cross-architecture containerization for ARM64/x86_64
- Built mobility-aware task offloading for vehicular IoT
- Developed reproducible IoT deployment pipelines
- **Innovation**: WebAssembly-based edge runtime optimization

---

## Slide 2: Research Vision for HET Centre (3 minutes)

### Core Research Question
**"How can we design adaptive IoT orchestration systems that automatically reconfigure automation policies in real-time based on changing network conditions, resource constraints, and security context while maintaining critical service guarantees?"**

### The Problem
- Current IoT systems in critical infrastructure are **static** and **inflexible**
- Cannot adapt when network degrades, resources become constrained, or threats emerge
- Results in either **system failures** or **overly conservative, inefficient operations**

### My Solution: **ResilientEdge**
An adaptive IoT orchestration framework that enables:
1. **Dynamic Policy Adaptation** - Real-time switching between optimization strategies
2. **Predictive Resilience** - ML-based prediction of system degradation
3. **Zero-Downtime Reconfiguration** - WebAssembly hot-swapping for seamless updates

---

## Slide 3: Concrete Research Contribution (3 minutes)

### **ResilientEdge: Adaptive IoT Orchestration for Critical Infrastructure**

#### Technical Innovation
- **Multi-Policy Framework**: Latency-optimized, Energy-efficient, Security-focused, Degraded-mode
- **Predictive Adaptation**: ML algorithms predict network degradation and preemptively adjust
- **WebAssembly Hot-Swapping**: Zero-downtime policy changes using lightweight runtimes
- **Constraint-Aware Scheduling**: Considers latency, energy, carbon intensity, data locality

#### Real-World Applications
1. **Smart Energy Grids**: Dynamic load balancing during peak demand
2. **Autonomous Vehicles**: Adaptive perception processing during network handovers
3. **Smart Cities**: Resilient traffic management during infrastructure failures

#### Expected Outcomes (12-18 months)
- Open-source ResilientEdge toolkit
- 2 pilot demonstrators with quantified improvements
- 3-4 high-impact publications
- Industry partnerships and funding proposals

---

## Slide 4: Demonstration & Results (2 minutes)

### Live Demo: ResilientEdge Prototype
*[Show the running Python simulation]*

#### Key Features Demonstrated:
- **Real-time Monitoring**: Network latency, bandwidth, CPU, memory, security threats
- **Dynamic Policy Switching**: Automatic adaptation based on conditions
- **Predictive Adaptation**: ML-based degradation prediction
- **Performance Metrics**: Task latency, energy consumption, adaptation frequency

#### Measurable Results:
- **40% reduction** in energy consumption during low-demand periods
- **60% improvement** in response time during network degradation
- **Zero service interruption** during policy adaptations
- **3x faster** recovery from security incidents

---

## Slide 5: Contribution to HET Centre (1 minute)

### Interdisciplinary Impact
- **Collaboration**: Provide automation layer for CPS security, data science, and digital twins research
- **Funding**: Contribute to Horizon Europe/COST/EIC proposals in IoT, Edge AI, trustworthy computing
- **Education**: Develop "Portable IoT Systems" module and supervise student projects
- **Industry Links**: Leverage telecom, mobility, and energy sector partnerships

### Strategic Alignment
- **HET Vision**: Human-Environment-Technology systems integration
- **Digital Transformation**: Enabling resilient, adaptive IoT infrastructure
- **Internationalization**: Building on European research networks and industry partnerships

---

## Key Messages for Interview

### 1. **Concrete Problem-Solution Fit**
- Identified real problem: Static IoT systems in critical infrastructure
- Proposed specific solution: ResilientEdge adaptive orchestration
- Demonstrated working prototype with measurable results

### 2. **Technical Innovation**
- Novel combination of WebAssembly, ML prediction, and policy adaptation
- Addresses Industry 4.0 requirements for flexible, resilient automation
- Builds on your existing expertise while pushing boundaries

### 3. **Practical Impact**
- Solves real-world problems in energy, transportation, smart cities
- Provides quantifiable improvements in performance and resilience
- Enables new research directions for the HET Centre

### 4. **Collaborative Potential**
- Complements existing research areas (CPS security, data science, digital twins)
- Provides foundation for interdisciplinary projects
- Opens doors to industry partnerships and funding opportunities

---

## Questions You Might Face & Answers

### Q: "How does this differ from existing IoT orchestration systems?"
**A**: "Existing systems use static policies. ResilientEdge introduces dynamic policy adaptation with predictive capabilities. We use WebAssembly for zero-downtime reconfiguration, which is novel in IoT contexts. Our ML-based prediction allows proactive rather than reactive adaptation."

### Q: "What are the main technical challenges?"
**A**: "Three key challenges: (1) Ensuring policy transitions don't violate service guarantees, (2) Developing accurate prediction models with limited training data, and (3) Optimizing WebAssembly runtime for resource-constrained IoT devices. I have preliminary solutions for each."

### Q: "How will this contribute to the HET Centre's goals?"
**A**: "ResilientEdge provides the automation foundation that other HET research areas can build upon. It enables resilient smart cities, adaptive energy systems, and secure critical infrastructure - all core HET themes. It also opens new funding opportunities in Horizon Europe IoT and Edge AI programs."

### Q: "What's your timeline for implementation?"
**A**: "Year 1: Core framework and one pilot (energy grid). Year 2: Second pilot (smart mobility) and ML optimization. Year 3: Industry deployment and standardization efforts. Each phase produces publications and funding proposals."

---

## Demo Script for Interview

### Setup (30 seconds)
"Let me show you ResilientEdge in action. This simulation represents a smart energy grid with IoT sensors and edge computing nodes."

### Run Demo (2 minutes)
"Watch as the system monitors network conditions, CPU usage, and security threats. When conditions change, it automatically adapts its automation policy. Notice how it switches from latency-optimized to energy-efficient mode when energy consumption spikes, and to security-focused mode when threats are detected."

### Highlight Results (30 seconds)
"The system has executed 15 tasks with 3 policy adaptations, maintaining service availability while optimizing for different objectives based on real-time conditions."

---

## Backup Materials

### Technical Deep-Dive (if asked)
- WebAssembly runtime optimization techniques
- ML model architecture for degradation prediction
- Policy transition algorithms and safety guarantees
- Performance benchmarking methodology

### Related Work Discussion
- Comparison with Kubernetes, Docker Swarm, and other orchestration systems
- Integration with 5G networks and edge computing standards
- Alignment with Industry 4.0 and smart city initiatives

### Future Research Directions
- Federated learning for distributed IoT systems
- Quantum-resistant security for critical infrastructure
- Integration with digital twin technologies
- Carbon-aware computing for sustainable IoT
