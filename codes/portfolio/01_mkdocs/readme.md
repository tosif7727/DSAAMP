# Build a portfolio

We will build a portfolio using **MkDocs**, a powerful static site generator tailored for creating project documentation. MkDocs is easy to set up and configure, leveraging Markdown for content creation. It offers a wide range of themes and plugins, enabling you to customize the look and functionality of your documentation site. This makes it an excellent choice for building a professional and visually appealing portfolio.

## 01- install mkdoc
```bash
conda create -n mkdocs python=3.10
conda activate mkdocs
pip install mkdocs
```
## 02- create a new project
```bash
mkdocs new mera_portfolio
cd mera_portfolio
```
## 03- run the server
```bash
mkdocs serve
```
## 04- changing a prot number
```bash
mkdocs serve -a localhost: 1232
```
