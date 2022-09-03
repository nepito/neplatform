from jinja2 import Environment, FileSystemLoader

import typer

app = typer.Typer()


fileLoader = FileSystemLoader("neplatform/templates/")
env = Environment(loader=fileLoader)


@app.command()
def dc(repo=""):
    rendered = env.get_template("docker-compose.yml").render(
        repo=repo,
    )
    print(rendered)


if __name__ == "__main__":
    app()
