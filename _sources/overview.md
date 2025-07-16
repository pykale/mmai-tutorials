# Overview

This book presents tutorials on multimodal AI applications using the `PyKale` library.

[//]: # (:::{note})

[//]: # (These resources are currently being developed.)

[//]: # (:::)

The book includes:
- Workshop overview: Learn what the workshop is about and see the schedule.
- Tutorials: Follow hands-on notebooks using multimodal data.
- Applications: Learn how AI can help with brain disorders, cancer, drug interactions, and more.


## What You’ll Need
- A laptop with Wi-Fi capability
- A Google account (https://accounts.google.com/signin) to access and run the tutorials using Google Colab
- A GitHub account (https://github.com/signup) to make contributions and use GitHub Discussions.

## How to Begin
- Start with the Introduction under `Workshop` on the left sidebar.
- Find the tutorial chapters you want to follow under `Tutorials`.
- Follow the tutorials step by step from top to bottom.

## Tips for Attendees
- If you have any question, please ask via [GitHub Discussions](https://github.com/pykale/mmai-tutorials/discussions/new?category=general).
- Use the Search (on the left) to quickly find specific topics.
- If you want to contribute, please read the following section.


## Contributing

### How to Contribute via GitHub

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

### Building the Book Locally

To build the book in development, assuming that the working directory is the project's folder, please call:

```bash
jupyter-book build .
```

### Pre-commit Hooks

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

## Contributors

This workshop is made possible by contributions from:

- **[Shuo Zhou](https://github.com/shuo-zhou)**
- **[Xianyuan Liu](https://github.com/xianyuanliu)**
- **[L. M. Riza Rizky](https://github.com/zaRizk7)**
- **[Mohammod N. I. Suvon](https://github.com/Mdnaimulislam)**
- **[Kelly Ding](https://github.com/kellydingzx)**
- **[Peter Charlton](https://github.com/peterhcharlton)**
- **[Wenrui Fan](https://github.com/orgs/Shef-AIRE/people/wenruifan)**
- **[Sina Tabakhi](https://github.com/SinaTabakhi)**
- **[Jiayang Zhang](https://github.com/jiayang-zhang)**
- **[Haiping Lu](https://github.com/haipinglu)**

<!-- ```{tableofcontents}
``` -->
