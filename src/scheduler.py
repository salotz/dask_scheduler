"""Start up a SLURM scheduler process that you can connect to."""
import time

import click

from dask_jobqueue import SLURMCluster

@click.group()
def cli():
    pass

@cli.command()
@click.option('--account', default='dicksonlab')
@click.option('--cores', default=1)
@click.option('--walltime', default="00:30:00")
@click.option('--memory', default='4 GB')
@click.option('--processes', default=1)
@click.option('--interface', default='ib0')
@click.option('--local-dir', default='/mnt/local')
@click.option('--scheduler-port', default=0)
@click.option('--dash-port', default=0)
@click.option('--num-workers', default=-1)
@click.option('--adapt-min', default=1)
@click.option('--adapt-max', default=5)
def slurm(account, cores, walltime, memory, processes, interface, local_dir,
                          scheduler_port, dash_port,
                          num_workers, adapt_min, adapt_max):

    # choose either adaptive mode or fixed number of walkers mode (you
    # can always connect to and scale manually without adapt mode),
    # but adapt mode is the default since it is the most no nonsense
    # DWIM approach
    adapt_mode = True
    if num_workers > -1:
        adapt_mode = False

    local_cluster_kwargs = {'scheduler_port' : scheduler_port,
                            'dashboard_address' : ':{}'.format(dash_port)}

    cluster = SLURMCluster(project=account,
                           cores=cores,
                           walltime=walltime,
                           memory=memory,
                           processes=processes,
                           interface=interface,
                           **local_cluster_kwargs)
    with cluster:

        click.echo("Scheduler address: {}".format(cluster.scheduler_address))
        click.echo("Dashboard port: {}".format(cluster.dashboard_link))

        if adapt_mode:
            cluster.adapt(minimum=adapt_min, maximum=adapt_max)
        else:
            cluster.scale(num_workers)



        # loop forever to block
        while True:
            # sleep so we avoid evaluating the loop to frequently
            time.sleep(2)




if __name__ == "__main__":


    cli()
