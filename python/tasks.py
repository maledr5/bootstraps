from invoke import task

@task
def push(ctx):
	ctx.run("git push && git push heroku")
