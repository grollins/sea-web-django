import subprocess
import os.path
from celery import shared_task
from tempfile import mkdtemp
from shutil import copyfile, rmtree
import logging
from django.conf import settings

from .models import Job, Result
from .parser import parse_sea_output

@shared_task()
def run_sea_calculation(job_id):
    # Move user-submitted files to temporary directory for calculation
    job = Job.objects.get(pk=job_id)
    temp_dir = mkdtemp()
    temp_path = os.path.join(temp_dir, 'struct')
    temp_struct_path = temp_path + '.gro'
    temp_topo_path = temp_path + '.top'
    copyfile(job.structure.path, temp_struct_path)
    copyfile(job.topology.path, temp_topo_path)
    job.structure_filename = os.path.basename(job.structure.path)
    job.topology_filename = os.path.basename(job.topology.path)
    solvate_cmd = os.path.join(settings.SEA_HOME, "bin", "solvate")
    input_path = temp_path

    # Create list of solvate arguments
    arg_list = [solvate_cmd, "-s", input_path, "-i", str(job.iterations),
                "-d", str(job.surface_detail)]
    if job.calculation_type == job.CALC_TYPE.dipole:
        pass
    elif job.calculation_type == job.CALC_TYPE.quadrupole:
        arg_list.append("-q")
    else:
        logging.error("Unexpected calculation type %s" % \
                     (str(job.calculation_type)))
    logging.info( "%s" % ' '.join(arg_list))

    # Run calculation
    try:
        output_str = subprocess.check_output(arg_list, stderr=subprocess.STDOUT)
        output = parse_sea_output(output_str)
        create_result_obj(job, output)
        status = Job.STATUS.done
    except subprocess.CalledProcessError, e:
        output_str = "There was an error:\n%s" % e.output
        output_str += "return code: %s\n" % e.returncode
        status = Job.STATUS.error

    # Delete temporary files, user-submitted files, and save job
    job.status = status
    job.save()
    rmtree(temp_dir)
    job.structure.delete()
    job.topology.delete()
    return "%s\n%s" % (status, output_str)

def create_result_obj(job, output):
    r = Result.objects.create(job=job, **output)
    return
