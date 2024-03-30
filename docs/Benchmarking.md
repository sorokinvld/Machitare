# BENCHMARKING.md

## The Importance of Benchmarking

Benchmarking is a crucial aspect of evaluating the performance and capabilities of any agent creation framework. It allows us to assess how well our agents perform compared to other state-of-the-art systems and identify areas for improvement. By setting clear benchmarks and measuring our progress against them, we can ensure that Machitare remains at the forefront of agent development.

## GAIA Benchmark

As a first step in testing the capabilities of our agents, we have chosen to use the GAIA benchmark. GAIA, which stands for General AI Assistants, is a benchmark that aims to evaluate the fundamental abilities of AI systems in real-world scenarios.

### About GAIA

GAIA proposes a set of questions that require a combination of reasoning, multi-modality handling, web browsing, and tool-use proficiency. These questions are designed to be conceptually simple for humans but challenging for even the most advanced AI systems.

The benchmark has shown that human respondents achieve an impressive 92% accuracy, while state-of-the-art language models like GPT-4, even when equipped with plugins, only manage to achieve 15% accuracy. This significant performance gap highlights the need for more robust and versatile AI systems that can exhibit human-like reasoning and problem-solving abilities.

### GAIA's Methodology

GAIA's methodology departs from the current trend in AI benchmarks, which often focus on tasks that are increasingly difficult for humans. Instead, GAIA posits that the advent of Artificial General Intelligence (AGI) depends on a system's ability to exhibit similar robustness as the average human on these real-world questions.

The benchmark consists of 466 carefully crafted questions and their corresponding answers. While the questions are publicly available, the answers to 300 of them are retained to power a leaderboard, which can be accessed at [https://huggingface.co/spaces/gaia-benchmark/leaderboard](https://huggingface.co/spaces/gaia-benchmark/leaderboard).

### Machitare and GAIA

By using the GAIA benchmark as a starting point, we aim to evaluate the performance of Machitare's agents in real-world scenarios. This will help us identify strengths and weaknesses in our framework and guide our development efforts towards creating more capable and robust agents.

We will regularly run our agents through the GAIA benchmark and track their progress on the leaderboard. This will not only allow us to compare our performance against other AI systems but also provide valuable insights into areas where we can improve our agents' abilities.

## Future Benchmarking Efforts

While the GAIA benchmark serves as an excellent starting point, we recognize the need to expand our benchmarking efforts to cover a wider range of tasks and domains. As Machitare evolves, we will continue to explore and incorporate additional benchmarks that align with our goals and help us push the boundaries of agent development.

By maintaining a strong focus on benchmarking and continuous improvement, we aim to make Machitare the go-to framework for creating highly capable and versatile agents that can tackle real-world challenges with human-like proficiency.

## Running the basic benchmark

# Running the basic benchmark

To run the basic benchmark, follow these steps:

1. Download the GAIA data: 
    - Visit [https://huggingface.co/spaces/gaia-benchmark/datasets](https://huggingface.co/spaces/gaia-benchmark/datasets)
    - Download the necessary dataset files and save them to a local directory.

2. Open a terminal and navigate to the directory where Machitare is installed.

3. Run the benchmark script using Poetry:
    ```bash
    poetry run python machitare/bench.py --data-dir /path/to/gaia/data
    ```
    Replace `/path/to/gaia/data` with the actual path to the directory where you saved the GAIA dataset files.

4. The benchmark will start running and display the progress and results in the terminal.

Note: Make sure you have Poetry installed and the necessary dependencies for Machitare are installed in the virtual environment.

After running the benchmark, you can analyze the results and evaluate the performance of Machitare's agents in real-world scenarios.

# File types in the GAIA Benchmark:

- .MOV
- .csv
- .docx
- .jpg
- .json
- .jsonld
- .m4a
- .mp3
- .pdb
- .pdf
- .png
- .pptx
- .py
- .txt
- .xlsx
- .xml
- .zip