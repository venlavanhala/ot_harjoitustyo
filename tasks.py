from invoke import task

@task
def start(ctx):
	pass 

@task
def test(ctx):
	ctx.run("pytest src", pty=True)

@task
def coveragereport(ctx):
	ctx.run("coverage run --branch -m pytest", pty=True)
	ctx.run("coverage html", pty=True)

