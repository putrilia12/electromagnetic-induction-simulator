# ⚡ Electromagnetic Induction Simulator

An interactive **Pygame-based simulation of electromagnetic induction** that demonstrates **Faraday’s Law** by allowing users to move a magnet through a coil, adjust coil parameters (such as length, diameter, and number of turns), and observe real-time changes in magnetic field, induced electromotive force, and light bulb intensity

---

## 🎯 Features

* 🧲 Drag-and-drop magnet interaction
* 🔄 Real-time electromagnetic induction simulation
* 💡 Dynamic light bulb response based on induced voltage
* 🌀 Magnetic field visualization (toggleable)
* ⚙️ Adjustable parameters:

  * Magnetic induction
  * Coil length
  * Coil diameter
  * Number of turns
    
* 📊 Real-time parameter display:

  * Number of turns
  * Coil diameter
  * Coil length
  * Magnetic induction
  * Induced electromotive force (automatically calculated)

> Note: All parameters can be adjusted by the user except the induced electromotive force (EMF), which is calculated automatically based on the simulation.

---

## 🧪 Physics Concept

This simulation is based on **Faraday’s Law of Electromagnetic Induction**:

> A changing magnetic flux through a coil induces an electromotive force (EMF).

## 📐 Formulas Used

```text
Faraday's Law:
ε = -N (dΦ/dt)

Magnetic Flux:
Φ = B · A · cos(θ)

For this simulation:
θ = 0°
therefore:
Φ = B · A

Coil Area:
A = πr²

Numerical Approximation:
ε ≈ -N (ΔΦ/Δt)
```

### 🧠 Explanation

* Magnetic flux (Φ) is calculated from the magnetic field (B) and the coil area (A).
* When the magnet moves, the flux changes over time.
* This change generates an induced electromotive force (EMF).
* The EMF value is then used to control the brightness of the light bulb using a sigmoid function for smoother visualization.

---

## 🎮 Controls

### Mouse

* Drag magnet → move magnet through coil

### Keyboard

* **F** → Show/hide magnetic field
* **W / S** → Increase / decrease magnetic induction
* **Arrow Up / Down** → Adjust coil length (diameter)
* **Arrow Left / Right** → Change number of turns

---

## 📸 Preview

### Main Interface

![Main](documentation/1.png)

### Magnetic Field Visualization, Coil Adjustment, Light Bulb Response

![Magnetic Field](documentation/2.png)
![Coil](documentation/3.png)
![Lightbulb](documentation/4.png)

---

## 🗂️ Project Structure

```
electromagnetic-induction-simulator/
│── main.py
│── modules/
│   ├── classes.py
│   └── variables.py
│── pic/
│   ├── magnet.png
│   └── icon.png
│── documentation/
│── README.md
│── .gitignore
```

---

## 🚀 How to Run

1. Clone this repository

```bash
git clone https://github.com/your-username/electromagnetic-induction-simulator.git
```

2. Navigate to project folder

```bash
cd electromagnetic-induction-simulator
```

3. Install dependencies

```bash
pip install pygame
```

4. Run the program

```bash
python main.py
```

---

## 🛠️ Technologies Used

* Python
* Pygame

---

## 👤 Author

Putri Aurelia
🔗 LinkedIn: [https://www.linkedin.com/in/putri-aurelia-728abb342/](https://www.linkedin.com/in/putri-aurelia-728abb342/)

---
