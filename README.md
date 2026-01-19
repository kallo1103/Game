# Game Project

This is a Unity game project.

## Getting Started

### Prerequisites

* Unity Hub
* Unity Editor (Version recommended: Check `ProjectSettings/ProjectVersion.txt`)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/kallo1103/Game.git
    ```

2. Open Unity Hub.
3. Click "Add" -> "Add project from disk".
4. Select the cloned project folder.
5. Open the project in Unity.

## Structure

* `Assets/`: Contains all game assets (Scripts, Scenes, textures, etc.).
* `Packages/`: Dependency definitions.
* `ProjectSettings/`: Unity project settings.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/amazing-feature`).
3. Commit your changes (`git commit -m 'Add some amazing feature'`).
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a Pull Request.

## Performance Testing (JMeter)

We have conducted performance testing for the chosen web application (`https://messenger-fe-eight.vercel.app`) using Apache JMeter.

### Summary

* **Tool**: Apache JMeter 5.6.3
* **Test Date**: 2026-01-19
* **Scenarios**:
  1. Basic Load (10 users)
  2. Heavy Load (50 users)
  3. Stress Test (20 users @ 60s)
* **Results**: The system handled up to 50 concurrent users with **0% error rate** and an average response time of **~300-500ms**.

For detailed test plans, configurations, and analysis, please refer to the [JMeter Report](jmeter/readme.md).

**Artifacts:**

* Test Plan: `jmeter/performance_test.jmx`
* Raw Results: `jmeter/results.csv`
* Summary Report: `jmeter/readme.md`
* HTML Dashboard: `jmeter/dashboard/index.html`
