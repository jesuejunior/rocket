#!/bin/python

import subprocess
import sys
import json


def split_output(orig_list):
    return [i.strip() for i in orig_list.split("\n") if i.strip()]


def safe_run_script(command, *args, **kwargs):
    #print "Running: {}".format(command)
    s = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = s.communicate()[0]
    return output


used_images = split_output(safe_run_script("grep 'image:' {0}".format(sys.argv[1]) + " | sort -u | grep -v '^#' | awk -F ':' '{print $2}'"))

current_images = split_output(safe_run_script("docker images | tail -n +2 | awk '{print $1}' | sort"))

current_images_set = set(current_images)
used_images_set = set(used_images)

to_delete = current_images_set.difference(used_images_set)

all_containers = split_output(safe_run_script("docker ps -a -q"))


image_ids_to_delete = []
for image in to_delete:
    if image != "<none>":
        image_data = json.loads(safe_run_script("docker inspect {0}".format(image)))
        image_ids_to_delete.append(image_data[0]['Id'][:12])

# Adiciona os IDs de todas as imagens untagged
image_ids_to_delete.extend(split_output(safe_run_script("docker images | grep '<none>' | awk '{print $3}'")))

container_ids_to_remove = []
for container in all_containers:
    from_image = safe_run_script("docker inspect {0}".format(container))
    from_image_json = json.loads(from_image)
    image_id = from_image_json[0]['Image'][:12]
    if image_id in image_ids_to_delete:
        container_ids_to_remove.append(container)


print "Removing containers:"
print container_ids_to_remove

print "Removing images:"
print image_ids_to_delete


for container in container_ids_to_remove:
    safe_run_script("docker stop {0}".format(container))
    safe_run_script("docker rm {0}".format(container))

for image in image_ids_to_delete:
    safe_run_script("docker rmi '{0}'".format(image))

safe_run_script("docker images | grep '<none>' | awk '{print $3}' | xargs -n1 docker rmi")
