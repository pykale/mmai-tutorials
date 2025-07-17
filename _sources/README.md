# Multimodal AI tutorials repository

<!-- This repository contains materials and resources for EMBC 2025 Workshop: Open Biomedical Multimodal AI Research – From Pixels to Molecules – 16 July | Copenhagen, Denmark. -->

This repository contains materials and resources for building the [Jupyter book](https://pykale.github.io/mmai-tutorials/) of the tutorials on multimodal AI applications using [PyKale](https://github.com/pykale/pykale), a Python library of the [PyTorch ecosystem](https://landscape.pytorch.org/?item=training--multimodal--pykale).

## Structure of source code

- [`workshop/`](https://github.com/pykale/mmai-tutorials/tree/main/workshop): Contains information for the EMBC 2025 Workshop.
- [`tutorials/`](https://github.com/pykale/mmai-tutorials/tree/main/tutorials): Contains tutorial notebooks and related materials.
- [`requirements.txt`](https://github.com/pykale/mmai-tutorials/blob/main/requirements.txt): Lists dependencies required for the project.

Each tutorial is organized in a standardized structure as follows:

```text
    ├───tutorial.ipynb
    ├───config.py
    ├───configs
    │   ├───base.yml
    │   ├───**.yml
    ├───model.py
    ├───images
    │   ├───**.png
    │   ├───**.jpg
    ├───helpers
    │   ├───**.py
    ├───extend-reading
    │   ├───**.md
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
   git push origin my-branch
   ```

5. Open a pull request to the main repository.

Please ensure your contributions adhere to the repository's coding standards and include appropriate documentation.

### Building the and preview the book

To build the book locally, you will need to have Jupyter Book and Sphinx Exercise packages installed. If you haven't installed them yet, you can do so using pip:

```bash
pip install jupyter-book==1.0.4.post1
pip install sphinx-exercise==1.0.1
```

To build the book in development, please ensure you are in the root directory of the repository. You can then run the following command:

```bash
jupyter-book build .
```

This will generate the HTML files in the `_build/html` directory. The home page of the book will be available at `_build/html/index.html`, from which you can navigate through the book.

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
