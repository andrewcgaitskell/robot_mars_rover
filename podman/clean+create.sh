podman stop container_flask_frontend_1
podman pod stop pod_flask_frontend
podman pod rm pod_flask_frontend
podman rmi image_python_frontend_1

uid=1000
gid=1000
subuidSize=$(( $(podman info --format "{{ range \
   .Host.IDMappings.UIDMap }}+{{.Size }}{{end }}" ) - 1 ))
subgidSize=$(( $(podman info --format "{{ range \
   .Host.IDMappings.GIDMap }}+{{.Size }}{{end }}" ) - 1 ))

podman build -f Dockerfile -t image_python_frontend_1 .

##-v /HOST-DIR:/CONTAINER-DIR

podman run -dt \
--name container_flask_frontend_1 \
--user $uid:$gid\
--publish 5000:5000  \
localhost/image_python_frontend_1:latest
