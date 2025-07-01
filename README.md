# Multimodal AI tutorials repository

<!-- This repository contains materials and resources for EMBC 2025 Workshop: Open Biomedical Multimodal AI Research – From Pixels to Molecules – 16 July | Copenhagen, Denmark. -->

## Structure

- `tutorials/`: Contains tutorial notebooks and related materials.
- `requirements.txt`: Lists dependencies required for the project.

The structure of each tutorial is as follows:

```text
    ├───tutorial.ipynb
    ├───config.py
    ├───configs
    │   ├───base.yml
    │   ├───**.yml
    ├───model.py
    ├───models
    │   ├───**.pt
    ├───data
    │   ├───**.csv
    │   ├───**.**
    ├───images
    │   ├───**.png
    │   ├───**.jpg
    ├───**.py
```

## How to Contribute

1. Fork the repository.
2. Create a new branch for your tutorial or bug fix:

   ```bash
   git checkout -b my-branch
   ```

3. Make your changes and commit them with clear messages:

   ```bash
   git commit -m "Add function ... to simplify tutorial ... content"
   ```

4. Push your branch to your forked repository:

   ```bash
   git push origin my-tutorial-branch
   ```

5. Open a pull request to the main repository.

Please ensure your contributions adhere to the repository's coding standards and include appropriate documentation.

## Building the Book

To build the book in development, assuming that the working directory is the project's folder, please call:

```bash
jupyter-book build .
```

## Pre-commit Hooks

This repository uses pre-commit hooks to ensure code quality and consistency. To set up pre-commit hooks locally, follow these steps:

1. Install the `pre-commit` package if you haven't already:

   ```bash
   pip install pre-commit
   ```

2. Install the hooks defined in the `.pre-commit-config.yaml` file:

   ```bash
   pre-commit install
   ```

3. Run the hooks manually on all files (optional):

   ```bash
   pre-commit run --all-files
   ```

Pre-commit hooks will now run automatically on every commit to check and format your code.
