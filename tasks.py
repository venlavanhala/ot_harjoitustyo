from invoke import task
import sys
pty=sys.platform != "win32"

@task
def start(ctx):
	ctx.run("python3 src/program.py", pty=pty)

@task
def test(ctx):
	ctx.run("pytest src", pty=pty)

@task
def build(ctx):
	ctx.run("python3 src/initialize.py", pty=pty)

@task
def coveragereport(ctx):
	ctx.run("coverage run --branch -m pytest src", pty=pty)
	ctx.run("coverage html", pty=pty)

@task
def lint(ctx):
	ctx.run("pylint src", pty=pty)

