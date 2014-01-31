import subprocess
import os.path
from celery import shared_task
from time import sleep
from tempfile import mkdtemp
from shutil import copyfile, rmtree
import logging

from django.conf import settings
from .models import Job, Result
from .parser import parse_sea_output


@shared_task()
def run_simple_calculation(job_id):
    job = Job.objects.get(pk=job_id)
    with open(job.structure.name, 'r') as f:
        lines = f.readlines()
        num_lines = len(lines)
    sleep(30.) # seconds
    job.status = Job.STATUS.done
    job.save()
    return num_lines

@shared_task()
def run_sea_calculation(job_id):
    job = Job.objects.get(pk=job_id)
    temp_dir = mkdtemp()
    temp_path = os.path.join(temp_dir, 'struct')
    temp_struct_path = temp_path + '.gro'
    temp_topo_path = temp_path + '.top'
    copyfile(job.structure.path, temp_struct_path)
    copyfile(job.topology.path, temp_topo_path)
    solvate_cmd = os.path.join(settings.SEA_HOME, "bin", "solvate")
    input_path = temp_path
    arg_list = [solvate_cmd, "-s", input_path, "-i", str(job.iterations)]
    logging.info( "%s" % ' '.join(arg_list))
    try:
        output_str = subprocess.check_output(arg_list, stderr=subprocess.STDOUT)
        output = parse_sea_output(output_str)
        create_result_obj(job, output)
        status = Job.STATUS.done
    except subprocess.CalledProcessError, e:
        output_str = "There was an error:\n%s" % e.output
        output_str += "return code: %s\n" % e.returncode
        status = Job.STATUS.error

    sleep(10.) # seconds
    job.status = status
    job.save()
    rmtree(temp_dir)
    return "%s\n%s" % (status, output_str)

def create_result_obj(job, output):
    r = Result.objects.create(job=job, **output)
    return
