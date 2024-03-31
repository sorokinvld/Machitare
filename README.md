<p align="center">
    <img src="./docs/logo.jpeg" alt="Logo" width="300">
</p>

<p align="center">
"Simplicity is the ultimate sophistication." - Leonardo da Vinci
</p>


# Machitare

Machitare is a project exploring what is possible with AI Agents. There are a few areas I intend to explore:

- Recursive breakdown of tasks: Allow agents to recursively breakdown tasks into easier tasks, each layer with its own memory, dynamically resulting in different level of abstraction in task definition and memory
- Real-Time Highly Interactive Agents: Imagine an agent can be interacted with like a person, they can take in new information as they are progressing, or keep working on a task, or even many tasks whilst chatting with the user.
- Video & Audio streaming as the primary communications layer, not text based chat.

I'm starting with the recursive breakdown of tasks and using the GAIA benchmark to see if this approach yields results or not.

## TODO:
- Finish the recursive agent
- Add tools and file processing abilities for the agent 
- Create a simple agent with tool and file processing capabilties
- Benchmark - LLM vs Tools Agent vs Recursive Agent 

----

> This is what I intend this to evolve into:

Machitare is an innovative agent creation framework designed to revolutionize the way agents are built and deployed. With a focus on multi-model support, real-time streaming capabilities, multi-agent architecture, and multi-processor optimization, Machitare aims to provide a powerful and flexible platform for creating intelligent agents.

## Key Features

- **Multi-model by default**: Machitare supports multiple AI models out of the box, allowing developers to leverage the strengths of different models seamlessly.
- **Real-time streaming**: The default operation mode of Machitare is designed for streaming real-time data, enabling agents to process and respond to data in real-time.
- **Multi-agent architecture**: Machitare is built with multi-agent systems in mind, making it easy to create and manage multiple agents working collaboratively.
- **Multi-processor optimization**: The framework is optimized to take advantage of multi-processor systems, ensuring efficient utilization of computational resources.
- **Protobuf communication layer**: Machitare uses Protocol Buffers (protobuf) for efficient and structured communication between agents and other components.
- **Containerization with Docker**: The framework is containerized using Docker, providing portability, scalability, and ease of deployment.

## Design Features and Principles

1. **Modularity and Extensibility**:
   - Machitare follows a modular architecture, allowing developers to easily extend and customize various components of the framework.
   - The framework provides well-defined interfaces and abstractions, enabling seamless integration of new models, algorithms, and functionalities.
   - Machitare encourages the development of reusable and interoperable components, promoting code reusability and maintainability.

2. **Scalability and Performance**:
   - Machitare is designed with scalability in mind, capable of handling large-scale agent deployments and high-throughput data processing.
   - The framework leverages multi-processing capabilities to distribute workload across multiple cores or machines, ensuring optimal performance.
   - Machitare employs efficient communication protocols and data serialization techniques to minimize latency and maximize throughput.

3. **Fault Tolerance and Resilience**:
   - Machitare incorporates fault tolerance mechanisms to ensure the reliability and robustness of agent systems.
   - The framework provides built-in error handling, logging, and monitoring capabilities to detect and recover from failures gracefully.
   - Machitare supports redundancy and failover strategies to maintain system availability and minimize downtime.

4. **Security and Privacy**:
   - Machitare prioritizes the security and privacy of agent systems and the data they process.
   - The framework includes authentication and authorization mechanisms to control access to sensitive resources and functionalities.
   - Machitare employs encryption techniques to protect data in transit and at rest, ensuring the confidentiality and integrity of information.

5. **Ease of Use and Developer Experience**:
   - Machitare provides a user-friendly and intuitive API, making it accessible to developers with varying levels of expertise.
   - The framework offers comprehensive documentation, tutorials, and code examples to facilitate quick onboarding and accelerate development.
   - Machitare integrates with popular development tools and frameworks, enabling seamless integration into existing workflows.

## Getting Started

To get started with Machitare, please refer to the [installation guide](INSTALL.md) and the [documentation](DOCS.md) for detailed instructions on setting up the framework and creating your first agent.

## Contributing

We welcome contributions from the community! If you'd like to contribute to Machitare, please read our [contribution guidelines](CONTRIBUTING.md) and [code of conduct](CODE_OF_CONDUCT.md).

## License

Machitare is released under the [MIT License](LICENSE).