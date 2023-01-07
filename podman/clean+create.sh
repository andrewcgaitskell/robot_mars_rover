podman stop container_flask_frontend_1
podman pod stop pod_flask_frontend
podman pod rm pod_flask_frontend
podman rmi image_flask_frontend_1

uid=1000
gid=1000
subuidSize=$(( $(podman info --format "{{ range \
   .Host.IDMappings.UIDMap }}+{{.Size }}{{end }}" ) - 1 ))
subgidSize=$(( $(podman info --format "{{ range \
   .Host.IDMappings.GIDMap }}+{{.Size }}{{end }}" ) - 1 ))

podman pod create \
--name pod_flask_frontend \
--infra-name infra_flask_frontend \
--network bridge \
--uidmap 0:1:$uid \
--uidmap $uid:0:1 \
--uidmap $(($uid+1)):$(($uid+1)):$(($subuidSize-$uid)) \
--gidmap 0:1:$gid \
--gidmap $gid:0:1 \
--gidmap $(($gid+1)):$(($gid+1)):$(($subgidSize-$gid)) \
--publish 5050:5050

podman build -f Dockerfile -t image_python_frontend_1 .

##-v /HOST-DIR:/CONTAINER-DIR

podman run -dt \
--name container_flask_frontend_1 \
--pod pod_flask_frontend \
--user $uid:$gid \
localhost/image_flask_frontend_1:latest
