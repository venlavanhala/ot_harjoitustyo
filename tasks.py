from invoke import task

@task
def start(ctx):
	pass 

@task
def test(ctx):
	ctx.run("pytest src", pty=True)

@task
def coveragereport(ctx):
	ctx.run("coverage run --branch -m pytest src", pty=True)
	ctx.run("coverage html", pty=True)

@task
def lint(ctx):
	ctx.run("pylint src", pty=True)
