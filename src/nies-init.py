from jinja2 import Environment, FileSystemLoader
import typer
import os

app = typer.Typer()


fileLoader = FileSystemLoader("neplatform/templates/")
env = Environment(loader=fileLoader)

TAG = {"main": "stable", "develop": "latest"}
PIPELINE = {"github": "main.yml", "gitlab": ".gitlab-ci.yml"}


@app.command()
def dc(repo=""):
    """
    docker-compose
    """
    rendered = env.get_template("docker-compose.yml").render(
        repo=repo,
    )
    print(rendered)


@app.command()
def am(repo="", branch="develop", hub="github"):
    """
    actions main
    """
    template = PIPELINE[hub]
    rendered = env.get_template(template).render(
        repo=repo,
        branch=branch,
        tag=TAG[branch],
    )
    print(rendered)


@app.command()
def test(name_file="nombre_archivo"):
    a = 'Rscript -e "usethis::use_test('
    b = f"'{name_file}', open = FALSE)"
    os.system(a+b+'"')


if __name__ == "__main__":
    app()
